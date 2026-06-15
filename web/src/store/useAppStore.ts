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
export type RunMode = 'practice' | 'real_test';
export type DebugStatus = 'idle' | 'starting' | 'running' | 'paused' | 'exited' | 'error';

export interface DebugLocal {
  name: string;
  value: string;
  type: string;
  scope: string;
  variablesReference?: number;
}

export interface AppState {
  // Challenge selection
  challenges: ChallengeSummary[];
  currentDetail: ChallengeDetail | null;

  // Editor + run args
  source: string;
  n: number;
  seed: number | null;
  /** Practice = the user picks n + seed (default). Real-test = the
   *  server picks a "reasonable" n and a random seed; the UI
   *  disables the n / seed inputs and shows the actual values the
   *  server used once the run completes. */
  mode: RunMode;
  /** When ON, the AI Report tab is visible and a "Get hint" button
   *  is available in the transport bar. Toggle in the header. */
  aiMode: boolean;

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

  // Debug session (set of line numbers the user has clicked).
  // This is the SINGLE source of truth for breakpoints: the
  // editor gutter reads from here, the Debug tab writes here,
  // and the useDebugSession hook pushes changes to the server.
  breakpoints: Set<number>;
  /** Debug session lifecycle: idle (no session), starting (POST
   *  in flight), running (paused inside solve()), paused
   *  (similar to running but the server explicitly paused us),
   *  exited (the run completed), error (something broke). */
  debugStatus: DebugStatus;
  /** The most recent stopped event's data. Re-renders of the
   * Debug tab subscribe to this slice. */
  debugCurrentLine: number | null;
  debugLocals: DebugLocal[];
  debugStoppedReason: string;
  /** Server-side error message when debugStatus = 'error'. */
  debugError: string;

  // --- Actions ---
  loadChallenges(): Promise<void>;
  selectChallenge(id: string): Promise<void>;
  setSource(s: string): void;
  setN(n: number): void;
  setSeed(s: number | null): void;
  setMode(m: RunMode): void;
  setAiMode(on: boolean): void;
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
  toggleBreakpoint(line: number): void;
  clearBreakpoints(): void;
  /**
   * Apply a snapshot that came from another window via the
   * BroadcastChannel. Sets the sentinel `applyingRemoteRef`
   * so the broadcast subscriber does not re-broadcast this
   * change. Always defers via setTimeout(0) at the call site
   * to break the synchronous subscribe→setState loop.
   */
  _applyRemoteSnapshot(s: Partial<AppState>): void;
}


/**
 * Module-scope ref-sentinel: true while a remote snapshot is
 * being applied. A real Zustand field would re-fire subscribers;
 * a ref does not. The broadcast subscriber in web/src/lib/
 * broadcastSync.ts reads this to skip re-broadcasting.
 */
export const applyingRemoteRef = { current: false };


export const useAppStore = create<AppState>((set, get) => ({
  challenges: [],
  currentDetail: null,
  source: '',
  n: 16,
  seed: 1,
  mode: 'practice',
  aiMode: false,
  isRunning: false,
  runResult: null,
  error: null,
  opIndex: 0,
  isPlaying: false,
  frameIntervalMs: 1000,
  progress: null,
  breakpoints: new Set<number>(),
  debugStatus: 'idle',
  debugCurrentLine: null,
  debugLocals: [],
  debugStoppedReason: '',
  debugError: '',

  async loadChallenges() {
    const list = await challengesApi.listChallenges();
    set({ challenges: list });
  },

  async selectChallenge(id: string) {
    set({
      isRunning: true,
      error: null,
      runResult: null,
      opIndex: 0,
      isPlaying: false,
      // Breakpoints are line-number-scoped to one source
      // file; switching challenges invalidates them. Clear
      // the set so the new challenge's gutter doesn't show
      // stale markers.
      breakpoints: new Set<number>(),
      debugStatus: 'idle',
      debugCurrentLine: null,
      debugLocals: [],
      debugStoppedReason: '',
      debugError: '',
    });
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

  setMode(m: RunMode) {
    set({ mode: m });
  },

  setAiMode(on: boolean) {
    set({ aiMode: on });
  },

  async run() {
    const { currentDetail, n, seed, mode } = get();
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
        mode,
      });
      // After a real-test run, sync the UI n/seed to what the
      // server actually used (it ignored our values).
      if (mode === 'real_test') {
        set({ n: result.n, seed: result.seed });
      }
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

  toggleBreakpoint(line: number) {
    // The set lives in zustand state. We replace the
    // reference (rather than mutating) so subscribers
    // re-render — zustand uses shallow identity checks.
    const next = new Set(get().breakpoints);
    if (next.has(line)) next.delete(line); else next.add(line);
    set({ breakpoints: next });
  },

  clearBreakpoints() {
    set({ breakpoints: new Set() });
  },

  _applyRemoteSnapshot(s) {
    applyingRemoteRef.current = true;
    try {
      set(s);
    } finally {
      // Reset on the next microtask so any in-flight subscriber
      // calls finish first. requestAnimationFrame is sufficient
      // and cheap; subscribers run during the same tick anyway.
      queueMicrotask(() => { applyingRemoteRef.current = false; });
    }
  },
}));
