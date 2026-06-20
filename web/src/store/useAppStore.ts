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
import type { OpenInVSCodeResult } from '../types/electron';
import * as challengesApi from '../api/challenges';
import * as runApi from '../api/run';
import * as progressApi from '../api/progress';
import * as solutionsApi from '../api/solutions';
import * as vscodeApi from '../api/vscode';


// Re-export so the inline ``import('...')`` in the action
// signature resolves to a named type, not a dynamic one.
export type { ChallengeDetail } from '../types/api';


/** Normalise the IPC result across main-process versions.
 *  Old versions return a plain boolean. New versions return
 *  ``{ ok, filePath?, error? }``. The boolean case gets
 *  upgraded to the object shape so callers don't need to
 *  special-case it. */
function normaliseOpenResult(
  raw: unknown,
): OpenInVSCodeResult {
  if (typeof raw === 'boolean') {
    return raw
      ? { ok: true }
      : { ok: false, error: 'VSCode did not respond. Is it installed?' };
  }
  if (raw && typeof raw === 'object' && 'ok' in raw) {
    return raw as OpenInVSCodeResult;
  }
  return { ok: false, error: 'Unexpected response from the desktop app.' };
}


/** Tiny re-export of the vscode API so the action can call
 *  ``writeActiveChallengeFor(id)`` without a separate import
 *  inside the store closure. The exported ``vscode`` API
 *  uses ``apiPost`` which uses ``fetch``; the store
 *  doesn't need anything fancier. */
const writeActiveChallengeFor = vscodeApi.writeActiveChallenge;


export type RunMode = 'practice' | 'real_test';


export interface AppState {
  theme: 'light' | 'dark';
  toggleTheme: () => void;

  language: 'en' | 'de';
  setLanguage: (lang: 'en' | 'de') => void;

  baseFontSize: number;
  increaseFontSize: () => void;
  decreaseFontSize: () => void;

  // Challenge selection
  challenges: ChallengeSummary[];
  currentDetail: ChallengeDetail | null;
  openChallengeIds: string[];

  // Display-only copy of solutions/<id>.py. The run() action
  // re-reads the file from disk before sending it to the server,
  // so VSCode edits are always picked up. The zustand copy is
  // updated after Run (and on challenge select) so the UI
  // always shows what's on disk.
  source: string;
  activeVersion: number;
  versions: number[];
  versionNames: Record<number, string>;
  modifiedVersions: number[];

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
  closeChallenge(id: string): void;
  setSource(s: string): void;
  saveSource(s: string): Promise<void>;
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

  switchVersion(version: number): Promise<void>;
  renameVersion(version: number, name: string): Promise<void>;
  resetVersion(version: number): Promise<void>;

  // --- Open-in-VSCode state (shared between TransportBar + VSCodeTab) ---
  /** True while a click is being processed. */
  vscodeOpening: boolean;
  /** Last error from the most recent open attempt, or null. */
  vscodeLastError: string | null;
  /** The absolute file path the most recent successful open targeted. */
  vscodeLastOpenedPath: string | null;
  /** Click handler — the handoff-file write + on-demand starter
   *  creation + IPC call, all in one. Defined here (not as a
   *  component hook) so the TransportBar's button and the
   *  VSCodeTab's big button share the same loading + error
   *  state. Returns a normalised result for callers that want
   *  to chain. */
  openInVSCode: (detail: import('../types/api').ChallengeDetail | null)
    => Promise<import('../types/electron').OpenInVSCodeResult>;
  /** Manually clear the error (e.g. when the user opens the
   *  VSCodeTab after seeing a stale error in the transport bar). */
  clearVSCodeError: () => void;
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
  theme: (localStorage.getItem('coden-theme') as 'dark' | 'light') || 'dark',
  toggleTheme: () => set((state) => {
    const next = state.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('coden-theme', next);
    return { theme: next };
  }),

  language: (localStorage.getItem('coden-language') as 'en' | 'de') || 'en',
  setLanguage: (lang) => set(() => {
    localStorage.setItem('coden-language', lang);
    return { language: lang };
  }),

  baseFontSize: Number(localStorage.getItem('coden-font-size')) || 16,
  increaseFontSize: () => set((state) => {
    const next = Math.min(24, state.baseFontSize + 2);
    localStorage.setItem('coden-font-size', next.toString());
    return { baseFontSize: next };
  }),
  decreaseFontSize: () => set((state) => {
    const next = Math.max(12, state.baseFontSize - 2);
    localStorage.setItem('coden-font-size', next.toString());
    return { baseFontSize: next };
  }),

  challenges: [],
  currentDetail: null,
  openChallengeIds: [],
  source: '',
  activeVersion: 1,
  versions: [],
  versionNames: {},
  modifiedVersions: [],
  n: 16,
  seed: 1,
  mode: 'practice',
  isRunning: false,
  runResult: null,
  error: null,
  progress: null,

  vscodeOpening: false,
  vscodeLastError: null,
  vscodeLastOpenedPath: null,

  async loadChallenges() {
    const list = await challengesApi.listChallenges();
    set({ challenges: list });
  },

  async selectChallenge(id: string) {
    const { openChallengeIds } = get();
    const isNew = !openChallengeIds.includes(id);

    set({
      isRunning: true,
      error: null,
      runResult: null,
      openChallengeIds: isNew ? [...openChallengeIds, id] : openChallengeIds,
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
        if (saved && saved.source) {
          source = saved.source;
        }
        set({ 
          activeVersion: saved?.active_version ?? 1, 
          versions: saved?.versions ?? [],
          versionNames: saved?.version_names ?? {},
          modifiedVersions: saved?.modified_versions ?? []
        });
      } catch {
        // ignore — use starter
        set({ activeVersion: 1, versions: [], versionNames: {}, modifiedVersions: [] });
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

  closeChallenge(id: string) {
    const { openChallengeIds, currentDetail } = get();
    const newOpen = openChallengeIds.filter((cid) => cid !== id);
    set({ openChallengeIds: newOpen });

    // If we closed the active tab, switch to another one (or null)
    if (currentDetail?.id === id) {
      if (newOpen.length > 0) {
        // Switch to the last opened tab
        get().selectChallenge(newOpen[newOpen.length - 1]!);
      } else {
        set({ currentDetail: null, source: '', runResult: null, error: null });
      }
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
  async saveSource(s: string) {
    const { currentDetail } = get();
    if (!currentDetail) return;
    try {
      // Optimistic update
      set({ source: s });
      await solutionsApi.putSolution(currentDetail.id, s);
    } catch (e) {
      console.error('Failed to save source:', e);
    }
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
        source = saved && saved.source ? saved.source : currentDetail.starter_source;
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
      if (saved && saved.source) {
        set({ 
          source: saved.source, 
          activeVersion: saved.active_version, 
          versions: saved.versions,
          versionNames: saved.version_names,
          modifiedVersions: saved.modified_versions
        });
      }
    } catch {
      // ignore
    }
  },

  async openInVSCode(detail) {
    if (!detail) {
      const error = 'Pick a challenge first.';
      set({ vscodeLastError: error });
      return { ok: false, error };
    }
    set({ vscodeOpening: true, vscodeLastError: null });
    try {
      // 1. Write the handoff file so the F5 launch config
      //    defaults to this challenge.
      try {
        await writeActiveChallengeFor(detail.id);
      } catch {
        // best-effort
      }
      // 2. Make sure the solution file exists. The player
      //    might be opening this challenge in VSCode for the
      //    first time — the file might be missing. Create
      //    it from the starter template if so.
      try {
        const existing = await solutionsApi.getSolution(detail.id);
        if (!existing || !existing.source) {
          try {
            await solutionsApi.putSolution(detail.id, detail.starter_source);
          } catch {
            // best-effort; main process will surface
            // "file not found" if the write didn't go through
          }
        }
      } catch {
        // best-effort
      }
      // 3. Hand off to the main process.
      const api = window.electronAPI;
      if (!api?.openInVSCode) {
        const error =
          'The cOde(n) desktop app is not running. Launch the ' +
          'packaged app (or `npm start` in electron/ after a build) ' +
          'so the Electron main process can resolve the file path.';
        set({ vscodeLastError: error });
        return { ok: false, error };
      }
      const result = normaliseOpenResult(await api.openInVSCode(detail.id));
      if (!result.ok) {
        set({
          vscodeLastError:
            result.error ??
            'Could not open the file in VSCode. Is VSCode installed?',
        });
      } else if (result.filePath) {
        set({ vscodeLastOpenedPath: result.filePath, vscodeLastError: null });
      } else {
        set({ vscodeLastError: null });
      }
      return result;
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      set({ vscodeLastError: message });
      return { ok: false, error: message };
    } finally {
      set({ vscodeOpening: false });
    }
  },

  clearVSCodeError() {
    set({ vscodeLastError: null });
  },

  async switchVersion(version: number) {
    const { currentDetail } = get();
    if (!currentDetail) return;
    try {
      const res = await solutionsApi.switchVersion(currentDetail.id, version);
      set({ source: res.source, activeVersion: res.active_version, versions: res.versions, versionNames: res.version_names, modifiedVersions: res.modified_versions });
    } catch (e) {
      console.error(e);
    }
  },

  async renameVersion(version: number, name: string) {
    const { currentDetail } = get();
    if (!currentDetail) return;
    try {
      const res = await solutionsApi.renameVersion(currentDetail.id, version, name);
      set({ source: res.source, activeVersion: res.active_version, versions: res.versions, versionNames: res.version_names, modifiedVersions: res.modified_versions });
    } catch (e) {
      console.error(e);
    }
  },

  async resetVersion(version: number) {
    const { currentDetail } = get();
    if (!currentDetail) return;
    try {
      const res = await solutionsApi.resetVersion(currentDetail.id, version);
      set({ source: res.source, activeVersion: res.active_version, versions: res.versions, versionNames: res.version_names, modifiedVersions: res.modified_versions });
    } catch (e) {
      console.error(e);
    }
  },
}));
