/**
 * Zustand store: the single source of truth for the UI.
 *
 * Holds: the challenge list, the current challenge id, a
 * display-only copy of the player's source, the run arguments
 * (n, seed), the last run result, and progress.
 *
 * The v0.9.0 pivot removed:
 *   - The per-step trace + step player (the player debugs in
 *     VSCode; the trace is no longer shipped by the server).
 *   - The in-app debug surface (debug session state, breakpoints,
 *     pop-out debug window).
 *   - The AI report tab + Ollama hint endpoint.
 *   - The editor (Monaco) + editor pop-out window.
 *
 * What stays:
 *   - Challenge selection (left rail, current detail).
 *   - Source-of-truth model: ``source`` is a display-only
 *     copy of ``solutions/<id>.py`` on disk. The ``run()``
 *     action re-reads the file from disk before sending it to
 *     the server, so VSCode edits are picked up automatically.
 *   - Run args (n, seed, mode).
 *   - The last run result + the verdict.
 *   - Progress (per-challenge best ops, completed list).
 *
 * Components subscribe to slices so a Run doesn't re-render
 * the challenge list (and vice versa).
 */
import { create } from 'zustand';

import type {
  ChallengeDetail,
  ChallengeSummary,
  ProgressOut,
  RunResponse,
} from '../types/api';
import * as challengesApi from '../api/challenges';
import * as runApi from '../api/run';
import * as progressApi from '../api/progress';
import * as solutionsApi from '../api/solutions';


export type RunMode = 'practice' | 'real_test';


export interface AppState {
  // Challenge selection
  challenges: ChallengeSummary[];
  currentDetail: ChallengeDetail | null;

  // Display-only copy of solutions/<id>.py. The run() action
  // re-reads the file from disk before sending it to the server,
  // so VSCode edits are always picked up. The zustand copy is
  // updated after Run (and on challenge select) so the UI
  // always shows what's on disk.
  source: string;

  // Run args
  n: number;
  seed: number | null;
  /** Practice = the user picks n + seed (default). Real-test = the
   *  server picks a "reasonable" n and a random seed; the UI
   *  disables the n / seed inputs and shows the actual values the
   *  server used once the run completes. */
  mode: RunMode;

  // Last run
  isRunning: boolean;
  runResult: RunResponse | null;
  error: string | null;

  // Progress
  progress: ProgressOut | null;

  // --- Actions ---
  loadChallenges(): Promise<void>;
  selectChallenge(id: string): Promise<void>;
  setSource(s: string): void;
  setN(n: number): void;
  setSeed(s: number | null): void;
  setMode(m: RunMode): void;
  run(): Promise<void>;
  reset(): void;
  loadProgress(): Promise<void>;
  markDone(): Promise<void>;
  /**
   * Force a re-read of ``solutions/<id>.py`` from disk. Used by
   * the AppShell on a "Reload from disk" button (the user
   * clicked it after editing in VSCode). The file-on-disk model
   * means a regular Run also picks up the latest content — this
   * is just an explicit refresh for the display copy.
   */
  refreshSourceFromDisk(): Promise<void>;
}


/**
 * Module-scope ref-sentinel: kept for the broadcastSync
 * integration (the main window and any future detached
 * surfaces may still need to suppress echo broadcasts).
 * Currently a no-op because there are no detached windows —
 * the v0.9.0 pivot removed the editor pop-out + the
 * debug pop-out + the detached-pane host.
 */
export const applyingRemoteRef = { current: false };


export const useAppStore = create<AppState>((set, get) => ({
  challenges: [],
  currentDetail: null,
  source: '',
  n: 16,
  seed: 1,
  mode: 'practice',
  isRunning: false,
  runResult: null,
  error: null,
  progress: null,

  async loadChallenges() {
    const list = await challengesApi.listChallenges();
    set({ challenges: list });
  },

  async selectChallenge(id: string) {
    set({
      isRunning: true,
      error: null,
      runResult: null,
    });
    try {
      const detail = await challengesApi.getChallenge(id);
      // Load the player's saved source from disk, or fall back
      // to the starter. The file is the source of truth — the
      // user edits it in VSCode, the run action reads it from
      // disk, and the cOde(n) UI shows a display copy.
      let source = detail.starter_source;
      try {
        const saved = await solutionsApi.getSolution(id);
        if (saved.exists && saved.source) {
          source = saved.source;
        }
      } catch {
        // ignore — use starter
      }
      set({
        currentDetail: detail,
        source,
        n: Math.min(16, detail.max_n),
        seed: 1,
      });
    } catch (e) {
      set({ error: (e as Error).message });
    } finally {
      set({ isRunning: false });
    }
  },

  setSource(s: string) {
    // Display-only: when the user runs, the server reads the
    // file from disk; this set is just so the UI can show
    // what's in the (in-memory) copy. In normal use the
    // source is reloaded from disk on challenge select and
    // after each run.
    set({ source: s });
  },
  setN(n: number) {
    set({ n });
  },
  setSeed(s: number | null) {
    set({ seed: s });
  },

  setMode(m: RunMode) {
    set({ mode: m });
  },

  async run() {
    const { currentDetail, n, seed, mode } = get();
    if (!currentDetail) return;
    set({ isRunning: true, error: null });
    try {
      // File on disk is the source of truth. Re-read before
      // every run so VSCode edits are picked up automatically —
      // no need for an explicit "Save" button.
      let source: string;
      try {
        const saved = await solutionsApi.getSolution(currentDetail.id);
        source = saved.exists && saved.source
          ? saved.source
          : currentDetail.starter_source;
      } catch {
        source = currentDetail.starter_source;
      }
      const result = await runApi.runChallenge({
        challengeId: currentDetail.id,
        source,
        n,
        seed,
        mode,
      });
      // After a real-test run, sync the UI n/seed to what the
      // server actually used (it ignored our values).
      const updates: Partial<AppState> = {
        runResult: result,
        source,
      };
      if (mode === 'real_test') {
        updates.n = result.n;
        updates.seed = result.seed;
      }
      set(updates);
      // Side-effect: persist progress if it passed.
      if (result.passed) {
        try {
          await progressApi.markChallengeDone(
            currentDetail.id,
            result.user_ast_ops ?? 0,
            result.actual_complexity,
          );
          await get().loadProgress();
        } catch {
          // progress save is best-effort
        }
      }
    } catch (e) {
      set({ error: (e as Error).message });
    } finally {
      set({ isRunning: false });
    }
  },

  reset() {
    set({ runResult: null, error: null });
  },

  async loadProgress() {
    try {
      const p = await progressApi.getProgress();
      set({ progress: p });
    } catch {
      // ignore
    }
  },

  async markDone() {
    const { runResult, currentDetail } = get();
    if (!runResult || !currentDetail) return;
    try {
      await progressApi.markChallengeDone(
        currentDetail.id,
        runResult.user_ast_ops ?? 0,
        runResult.actual_complexity,
      );
      await get().loadProgress();
    } catch {
      // ignore
    }
  },

  async refreshSourceFromDisk() {
    const { currentDetail } = get();
    if (!currentDetail) return;
    try {
      const saved = await solutionsApi.getSolution(currentDetail.id);
      if (saved.exists) {
        set({ source: saved.source });
      }
    } catch {
      // ignore
    }
  },
}));
