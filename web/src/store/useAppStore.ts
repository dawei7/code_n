/**
 * Zustand store: the single source of truth for the UI.
 *
 * Holds: the challenge list, the current challenge id, a
 * display-only copy of the player's source, the run arguments
 * (n, seed), the last run result, and progress.
 *
 * The v0.9.0 pivot removed:
 *   - The per-step trace + step player (the player debugs in
 *     external IDEs; the in-app debugger owns this now.
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
 *     the server, so editor changes are picked up automatically.
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
  ProfileSummary,
} from '../types/api';
import * as challengesApi from '../api/challenges';
import * as runApi from '../api/run';
import * as progressApi from '../api/progress';
import * as solutionsApi from '../api/solutions';
import * as profilesApi from '../api/profiles';
import type { AlgorithmSetId } from '../lib/algorithmSets';
import { getAlgorithmSetOption, normalizeAlgorithmSet } from '../lib/algorithmSets';


// Re-export so the inline ``import('...')`` in the action
// signature resolves to a named type, not a dynamic one.
export type { ChallengeDetail } from '../types/api';


export type RunMode = 'practice' | 'real_test';
export type Topic = 'reference' | 'mathematical' | 'complexity' | 'coden' | 'career_path';


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
  // so editor changes are always picked up. The zustand copy is
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

  // AI Tutor analysis persistence
  aiAnalysis: string;
  aiStatus: 'idle' | 'loading' | 'loaded' | 'error';
  aiError: string;
  setAiAnalysis: (analysis: string) => void;
  setAiStatus: (status: 'idle' | 'loading' | 'loaded' | 'error') => void;
  setAiError: (error: string) => void;

  // Progress
  progress: ProgressOut | null;
  activeSet: AlgorithmSetId;
  setActiveSet: (setVal: AlgorithmSetId) => Promise<void>;
  activeTopic: Topic;
  setActiveTopic: (topic: Topic) => void;

  // Profiles & Settings
  activeProfile: string;
  profiles: ProfileSummary[];
  loadProfiles: () => Promise<void>;
  createProfile: (name: string, careerMode: boolean, leetcodeUsername: string) => Promise<void>;
  selectProfile: (name: string) => Promise<void>;
  deleteProfile: (name: string) => Promise<void>;
  updateSettings: (careerMode: boolean, leetcodeUsername: string, geminiApiKey: string) => Promise<void>;
  verifyLeetCode: (challengeId: string) => Promise<{ success: boolean; message: string }>;

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
   * Force a re-read of ``solutions/<id>.py`` from disk. The
   * file-on-disk model means a regular Run also picks up the
   * latest content — this is just an explicit refresh for the
   * display copy.
   */
  refreshSourceFromDisk(): Promise<void>;

  switchVersion(version: number): Promise<void>;
  renameVersion(version: number, name: string): Promise<void>;
  resetVersion(version: number): Promise<void>;

  sidebarWidth: number;
  sidebarPosition: 'left' | 'right';
  sidebarCollapsed: boolean;
  setSidebarWidth: (width: number) => void;
  setSidebarPosition: (pos: 'left' | 'right') => void;
  setSidebarCollapsed: (collapsed: boolean) => void;
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
  activeSet: 'neetcode',
  activeTopic: 'reference',
  setActiveTopic: (topic) => set({ activeTopic: topic }),
  activeProfile: 'Default',
  profiles: [],

  // AI Tutor analysis initial state
  aiAnalysis: '',
  aiStatus: 'idle',
  aiError: '',
  setAiAnalysis: (analysis) => set({ aiAnalysis: analysis }),
  setAiStatus: (status) => set({ aiStatus: status }),
  setAiError: (error) => set({ aiError: error }),

  sidebarWidth: Number(localStorage.getItem('coden-sidebar-width')) || 256,
  sidebarPosition: (localStorage.getItem('coden-sidebar-position') as 'left' | 'right') || 'left',
  sidebarCollapsed: localStorage.getItem('coden-sidebar-collapsed') === 'true',
  setSidebarWidth: (width) => set(() => {
    localStorage.setItem('coden-sidebar-width', width.toString());
    return { sidebarWidth: width };
  }),
  setSidebarPosition: (pos) => set(() => {
    localStorage.setItem('coden-sidebar-position', pos);
    return { sidebarPosition: pos };
  }),
  setSidebarCollapsed: (collapsed) => set(() => {
    localStorage.setItem('coden-sidebar-collapsed', collapsed ? 'true' : 'false');
    return { sidebarCollapsed: collapsed };
  }),

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
      aiAnalysis: '',
      aiStatus: 'idle',
      aiError: '',
    });
    try {
      const detail = await challengesApi.getChallenge(id);
      // Load the player's saved source from disk, or fall back
      // to the starter. The file is the source of truth — the
      // user edits it in cOde(n), the run action reads it from
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
    set({ isRunning: true, error: null, aiAnalysis: '', aiStatus: 'idle', aiError: '', activeTopic: 'complexity' });
    try {
      // File on disk is the source of truth. Re-read before
      // every run so saved editor changes are picked up automatically —
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
          await get().loadChallenges();
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
    set({ runResult: null, error: null, aiAnalysis: '', aiStatus: 'idle', aiError: '' });
  },

  async loadProgress() {
    try {
      const p = await progressApi.getProgress();
      set({ 
        progress: p,
        activeSet: normalizeAlgorithmSet(p.active_set)
      });
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
      await get().loadChallenges();
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

  async loadProfiles() {
    try {
      const res = await profilesApi.listProfiles();
      set({ activeProfile: res.active_profile, profiles: res.profiles });
    } catch (e) {
      console.error(e);
    }
  },

  async createProfile(name: string, careerMode: boolean, leetcodeUsername: string) {
    try {
      const res = await profilesApi.createProfile(name, careerMode, leetcodeUsername);
      set({ activeProfile: res.active_profile, profiles: res.profiles });
      await get().loadProgress();
      await get().loadChallenges();
    } catch (e) {
      console.error(e);
      throw e;
    }
  },

  async selectProfile(name: string) {
    try {
      const res = await profilesApi.selectProfile(name);
      set({ activeProfile: res.active_profile, profiles: res.profiles, currentDetail: null, runResult: null });
      await get().loadProgress();
      await get().loadChallenges();
    } catch (e) {
      console.error(e);
    }
  },

  async deleteProfile(name: string) {
    try {
      const res = await profilesApi.deleteProfile(name);
      set({ activeProfile: res.active_profile, profiles: res.profiles });
      await get().loadProgress();
      await get().loadChallenges();
    } catch (e) {
      console.error(e);
    }
  },

  async setActiveSet(setVal: AlgorithmSetId) {
    const updates: Partial<AppState> = {
      activeSet: setVal,
      currentDetail: null,
      openChallengeIds: [],
      source: '',
      runResult: null,
      error: null,
    };
    const setOption = getAlgorithmSetOption(setVal);
    if (!setOption.hasCareerPath && get().activeTopic === 'career_path') {
      updates.activeTopic = 'reference';
    }
    if (!setOption.hasMathematical && get().activeTopic === 'mathematical') {
      updates.activeTopic = 'reference';
    }
    set(updates);
    try {
      const p = await progressApi.updateProgressSettings(undefined, undefined, undefined, undefined, setVal);
      set({ 
        progress: p,
        activeSet: normalizeAlgorithmSet(p.active_set)
      });
      await get().loadChallenges();
    } catch (e) {
      console.error(e);
    }
  },

  async updateSettings(careerMode: boolean, leetcodeUsername: string, geminiApiKey: string) {
    try {
      const activeSet = get().activeSet;
      const p = await progressApi.updateProgressSettings(careerMode, leetcodeUsername, undefined, geminiApiKey, activeSet);
      set({ progress: p });
      await get().loadChallenges();
      await get().loadProfiles();
    } catch (e) {
      console.error(e);
    }
  },

  async verifyLeetCode(challengeId: string) {
    try {
      const res = await progressApi.verifyLeetCode(challengeId);
      if (res.success) {
        await get().loadProgress();
        await get().loadChallenges();
        return { success: true, message: res.message };
      }
      return { success: false, message: res.message };
    } catch (e) {
      console.error(e);
      return { success: false, message: e instanceof Error ? e.message : 'Unknown verification error' };
    }
  },
}));
