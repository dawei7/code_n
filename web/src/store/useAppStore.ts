/**
 * Zustand store: the single source of truth for the UI.
 *
 * Holds: the challenge list, the current challenge id, the editor
 * source, the run arguments (n, seed), the last run result, the
 * step-player state (frame index, play/pause, speed), and progress.
 *
 * Components subscribe to slices so keystrokes in the editor don't
 * re-render the visualizer (and vice versa).
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


export type StepDelta = -1 | 1 | -10 | 10 | 'first' | 'last';

export interface AppState {
  // Challenge selection
  challenges: ChallengeSummary[];
  currentDetail: ChallengeDetail | null;

  // Editor + run args
  source: string;
  n: number;
  seed: number | null;

  // Last run
  isRunning: boolean;
  runResult: RunResponse | null;
  error: string | null;

  // Step player
  opIndex: number;
  isPlaying: boolean;
  /** How long to display each frame in the play loop, in ms.
   *  500 = 2 fps (slow, easy to study), 1000 = 1 fps (default),
   *  250 = 4 fps (fast), 100 = 10 fps (very fast). */
  frameIntervalMs: number;

  // Progress
  progress: ProgressOut | null;

  // --- Actions ---
  loadChallenges(): Promise<void>;
  selectChallenge(id: string): Promise<void>;
  setSource(s: string): void;
  setN(n: number): void;
  setSeed(s: number | null): void;
  run(): Promise<void>;
  reset(): void;
  step(delta: StepDelta): void;
  jumpToOpIndex(i: number): void;
  jumpToFrame(i: number): void;
  setFrameIntervalMs(ms: number): void;
  play(): void;
  pause(): void;
  loadProgress(): Promise<void>;
  markDone(): Promise<void>;
  saveSolution(): Promise<void>;
  loadSolution(): Promise<void>;
}


export const useAppStore = create<AppState>((set, get) => ({
  challenges: [],
  currentDetail: null,
  source: '',
  n: 16,
  seed: 1,
  isRunning: false,
  runResult: null,
  error: null,
  opIndex: 0,
  isPlaying: false,
  frameIntervalMs: 1000,
  progress: null,

  async loadChallenges() {
    const list = await challengesApi.listChallenges();
    set({ challenges: list });
  },

  async selectChallenge(id: string) {
    set({ isRunning: true, error: null, runResult: null, opIndex: 0, isPlaying: false });
    try {
      const detail = await challengesApi.getChallenge(id);
      // Load the player's saved source from disk, or fall back to the starter.
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
    set({ source: s });
  },
  setN(n: number) {
    set({ n });
  },
  setSeed(s: number | null) {
    set({ seed: s });
  },

  async run() {
    const { currentDetail, n, seed } = get();
    if (!currentDetail) return;
    set({ isRunning: true, error: null, isPlaying: false });
    try {
      // The main window no longer embeds the editor, so the source
      // lives in the pop-out editor (or in solutions/{id}.py on
      // disk via the server's saved file). Fetch the latest saved
      // source from the server before each run.
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
      });
      // Persist the source that was actually run so the CodePanel
      // can render it in the second half of the right panel.
      set({ runResult: result, opIndex: 0, source });
      // Side-effect: persist progress if it passed.
      if (result.passed) {
        try {
          await progressApi.markChallengeDone(
            currentDetail.id,
            result.stats.total,
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
    set({ runResult: null, error: null, opIndex: 0, isPlaying: false });
  },

  step(delta: StepDelta) {
    // Step in **op** units, not frame units. The trace fires one
    // frame per Python `line` event; ops fire on each read/write/
    // compare. Multiple ops can happen on the same line, so
    // stepping by op (rather than frame) is what the user wants
    // when they click "next": they want to see the next actual
    // operation, not the next line.
    const { runResult, opIndex } = get();
    if (!runResult) return;
    const last = runResult.ops_log.length - 1;
    let next = opIndex;
    if (delta === 'first') next = 0;
    else if (delta === 'last') next = last;
    else next = Math.max(0, Math.min(last, opIndex + delta));
    set({ opIndex: next });
  },

  jumpToOpIndex(i: number) {
    const { runResult } = get();
    if (!runResult) return;
    const last = runResult.ops_log.length - 1;
    set({ opIndex: Math.max(0, Math.min(last, i)) });
  },

  jumpToFrame(i: number) {
    // Convenience: jump to the op that corresponds to the given
    // trace frame. Used by the op log "click to jump" handler.
    const { runResult } = get();
    if (!runResult) return;
    const trace = runResult.trace;
    if (i < 0 || i >= trace.length) return;
    // The frame's op_index is the op that triggered the line
    // event. Jump to that op.
    set({ opIndex: Math.max(0, Math.min(trace[i].op_index, runResult.ops_log.length - 1)) });
  },

  setSpeed(s: number) {
    // Backwards-compat shim: older callers pass "steps per second".
    // Convert to ms-per-frame.
    set({ frameIntervalMs: Math.max(50, Math.round(1000 / Math.max(1, s))) });
  },

  setFrameIntervalMs(ms: number) {
    set({ frameIntervalMs: Math.max(50, Math.round(ms)) });
  },

  play() {
    if (get().runResult) set({ isPlaying: true });
  },
  pause() {
    set({ isPlaying: false });
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
        runResult.stats.total,
        runResult.actual_complexity,
      );
      await get().loadProgress();
    } catch {
      // ignore
    }
  },

  async saveSolution() {
    const { currentDetail, source } = get();
    if (!currentDetail) return;
    await solutionsApi.putSolution(currentDetail.id, source);
  },

  async loadSolution() {
    const { currentDetail } = get();
    if (!currentDetail) return;
    const saved = await solutionsApi.getSolution(currentDetail.id);
    if (saved.exists) set({ source: saved.source });
  },
}));
