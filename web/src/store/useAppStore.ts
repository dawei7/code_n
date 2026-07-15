/**
 * Zustand store: the single source of truth for the UI.
 *
 * Holds: the challenge list, the current challenge id, a
 * display-only copy of the player's source, selected validated cases,
 * the last run result, and progress.
 *
 * The current app is intentionally single-window:
 *   - Monaco editing and in-app debugging live in the cOde(n) tab.
 *   - Detached editor/debug pop-outs are gone.
 *   - The AI tutor chat lives in its own AI tab.
 *
 * Core state:
 *   - Challenge selection (left rail, current detail).
 *   - Source-of-truth model: ``source`` is a display-only
 *     copy of the active language's solution file on disk. The
 *     ``run()`` action re-reads that file before sending it to the
 *     server, so editor changes are picked up automatically.
 *   - Run mode and selected validated cases.
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
  SupportedLanguage,
  TutorChatMessage,
} from '../types/api';
import * as challengesApi from '../api/challenges';
import * as runApi from '../api/run';
import * as progressApi from '../api/progress';
import * as solutionsApi from '../api/solutions';
import * as profilesApi from '../api/profiles';
import type { AlgorithmSetId } from '../lib/algorithmSets';
import { getAlgorithmSetOption, normalizeAlgorithmSet } from '../lib/algorithmSets';
import { DEFAULT_ACCENT_COLORS, normalizeAccentColors } from '../lib/accentColors';


// Re-export so the inline ``import('...')`` in the action
// signature resolves to a named type, not a dynamic one.
export type { ChallengeDetail } from '../types/api';


export type RunMode = 'practice' | 'real_test';
export type Topic = 'reference' | 'visualization' | 'complexity' | 'coden' | 'ai' | 'career_path';
export const MAX_DEBUG_CASES = 9;
const allTrialCasesId = '__all_trial__';

const solutionLanguageStorageKey = 'coden-solution-language';
const userCaseStoragePrefix = 'coden-user-cases-v1';

export interface UserTestCase {
  id: string;
  name: string;
  input: string;
  createdAt: number;
}

function userCaseStorageKey(challengeId: string, language: SupportedLanguage): string {
  return `${userCaseStoragePrefix}:${challengeId}:${language}`;
}

function loadUserCases(challengeId: string, language: SupportedLanguage): UserTestCase[] {
  try {
    const raw = JSON.parse(localStorage.getItem(userCaseStorageKey(challengeId, language)) || '[]');
    if (!Array.isArray(raw)) return [];
    return raw.filter((item): item is UserTestCase => (
      item && typeof item.id === 'string' && typeof item.name === 'string' && typeof item.input === 'string'
    ));
  } catch {
    return [];
  }
}

function persistUserCases(challengeId: string, language: SupportedLanguage, cases: UserTestCase[]): void {
  localStorage.setItem(userCaseStorageKey(challengeId, language), JSON.stringify(cases));
}

function starterForLanguage(detail: ChallengeDetail, language: SupportedLanguage): string {
  return detail.starter_sources?.[language] ?? detail.starter_source;
}


export interface AppState {
  theme: 'light' | 'dark';
  toggleTheme: () => void;

  language: 'en' | 'de';
  setLanguage: (lang: 'en' | 'de') => void;

  baseFontSize: number;
  increaseFontSize: () => void;
  decreaseFontSize: () => void;
  paneFontScales: Record<string, number>;
  setPaneFontScale: (scope: string, scale: number) => void;
  accentColors: { light: string; dark: string };
  saveAccentColors: (colors: { light: string; dark: string }) => Promise<void>;

  // Challenge selection
  challenges: ChallengeSummary[];
  challengesLoading: boolean;
  challengesError: string | null;
  currentDetail: ChallengeDetail | null;
  openChallengeIds: string[];

  // Display-only copy of the active language's solution file. The
  // run() action re-reads the file from disk before sending it to
  // the server, so editor changes are always picked up. The zustand
  // copy is updated after Run (and on challenge select) so the UI
  // always shows what's on disk.
  source: string;
  codeLanguage: SupportedLanguage;
  activeVersion: number;
  versions: number[];
  versionNames: Record<number, string>;
  modifiedVersions: number[];

  // Run args
  mode: RunMode;
  selectedCaseIds: string[];
  customCaseInput: string;
  userCases: UserTestCase[];

  // Last run
  isRunning: boolean;
  runResult: RunResponse | null;
  error: string | null;

  // AI Tutor analysis persistence
  aiAnalysis: string;
  aiMessages: TutorChatMessage[];
  aiStatus: 'idle' | 'loading' | 'loaded' | 'error';
  aiError: string;
  setAiAnalysis: (analysis: string) => void;
  setAiMessages: (messages: TutorChatMessage[]) => void;
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
  setCodeLanguage(language: SupportedLanguage): Promise<void>;
  setSource(s: string): void;
  saveSource(s: string): Promise<void>;
  setMode(m: RunMode): void;
  setSelectedCaseIds(ids: string[]): void;
  runAllTrialCases(): void;
  setCustomCaseInput(value: string): void;
  addUserCase(initialInput?: string): string;
  updateUserCase(id: string, patch: Partial<Pick<UserTestCase, 'name' | 'input'>>): void;
  deleteUserCase(id: string): void;
  run(): Promise<void>;
  reset(): void;
  loadProgress(): Promise<void>;
  markDone(): Promise<void>;
  /**
   * Force a re-read of the active language's solution from disk. The
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
  paneSizes: Record<string, number>;
  setSidebarWidth: (width: number) => void;
  setSidebarPosition: (pos: 'left' | 'right') => void;
  setSidebarCollapsed: (collapsed: boolean) => void;
  saveSidebarWidthToBackend: (width: number) => Promise<void>;
  setPaneSize: (scope: string, size: number) => void;
  savePaneSizesToBackend: () => Promise<void>;
}


/**
 * Module-scope ref-sentinel: kept for the broadcastSync
 * integration (the main window and any future detached
 * surfaces may still need to suppress echo broadcasts).
 * Currently a no-op because there are no detached windows —
 * detached editor/debug pop-outs were removed.
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
  paneFontScales: {},
  setPaneFontScale: (scope, scale) => {
    const normalized = Math.max(0.75, Math.min(1.5, Math.round(scale * 100) / 100));
    const next = { ...get().paneFontScales, [scope]: normalized };
    set((state) => ({
      paneFontScales: next,
      progress: state.progress ? { ...state.progress, pane_font_scales: next } : state.progress,
    }));
    void progressApi.updateProgressSettings({ pane_font_scales: next }).catch(() => {
      // Keep the in-window zoom responsive if persistence is temporarily unavailable.
    });
  },
  accentColors: { ...DEFAULT_ACCENT_COLORS },
  saveAccentColors: async (colors) => {
    const normalized = normalizeAccentColors(colors);
    const progress = await progressApi.updateProgressSettings({ accent_colors: normalized });
    set({
      accentColors: normalizeAccentColors(progress.accent_colors),
      progress,
    });
  },

  challenges: [],
  challengesLoading: true,
  challengesError: null,
  currentDetail: null,
  openChallengeIds: [],
  source: '',
  codeLanguage: (localStorage.getItem(solutionLanguageStorageKey) as SupportedLanguage) || 'python',
  activeVersion: 1,
  versions: [],
  versionNames: {},
  modifiedVersions: [],
  mode: 'practice',
  selectedCaseIds: [],
  customCaseInput: '',
  userCases: [],
  isRunning: false,
  runResult: null,
  error: null,
  progress: null,
  activeSet: 'leetcode',
  activeTopic: 'reference',
  setActiveTopic: (topic) => set({ activeTopic: topic }),
  activeProfile: 'Default',
  profiles: [],

  // AI Tutor analysis initial state
  aiAnalysis: '',
  aiMessages: [],
  aiStatus: 'idle',
  aiError: '',
  setAiAnalysis: (analysis) => set({ aiAnalysis: analysis }),
  setAiMessages: (messages) => set({ aiMessages: messages }),
  setAiStatus: (status) => set({ aiStatus: status }),
  setAiError: (error) => set({ aiError: error }),

  sidebarWidth: Number(localStorage.getItem('coden-sidebar-width')) || 256,
  sidebarPosition: (localStorage.getItem('coden-sidebar-position') as 'left' | 'right') || 'left',
  sidebarCollapsed: localStorage.getItem('coden-sidebar-collapsed') === 'true',
  paneSizes: {},
  setSidebarWidth: (width) => set(() => {
    localStorage.setItem('coden-sidebar-width', width.toString());
    return { sidebarWidth: width };
  }),
  setSidebarPosition: (pos) => set(() => {
    localStorage.setItem('coden-sidebar-position', pos);
    void progressApi.updateProgressSettings({ sidebar_position: pos });
    return { sidebarPosition: pos };
  }),
  setSidebarCollapsed: (collapsed) => set(() => {
    localStorage.setItem('coden-sidebar-collapsed', collapsed ? 'true' : 'false');
    void progressApi.updateProgressSettings({ sidebar_collapsed: collapsed });
    return { sidebarCollapsed: collapsed };
  }),
  saveSidebarWidthToBackend: async (width) => {
    try {
      await progressApi.updateProgressSettings({ sidebar_width: width });
    } catch {
      // ignore
    }
  },

  async loadChallenges() {
    set({ challengesLoading: true, challengesError: null });
    try {
      const list = await challengesApi.listChallenges();
      set({ challenges: list, challengesLoading: false });
    } catch (error) {
      set({
        challengesLoading: false,
        challengesError: error instanceof Error ? error.message : 'Unable to load challenges',
      });
    }
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
      aiMessages: [],
      aiStatus: 'idle',
      aiError: '',
    });
    try {
      const detail = await challengesApi.getChallenge(id);
      // Load the player's saved source from disk, or fall back
      // to the starter. The file is the source of truth — the
      // user edits it in cOde(n), the run action reads it from
      // disk, and the cOde(n) UI shows a display copy.
      const codeLanguage = get().codeLanguage;
      let source = starterForLanguage(detail, codeLanguage);
      try {
        const saved = await solutionsApi.getSolution(id, codeLanguage);
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
      const firstVisibleCase = detail.test_cases?.[0]?.id;
      const userCases = loadUserCases(id, codeLanguage);
      set({
        currentDetail: detail,
        source,
        userCases,
        selectedCaseIds: firstVisibleCase ? [firstVisibleCase] : userCases[0] ? [userCases[0].id] : [],
        customCaseInput: firstVisibleCase ? '' : userCases[0]?.input || '',
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
        set({ currentDetail: null, source: '', userCases: [], runResult: null, error: null });
      }
    }
  },

  async setCodeLanguage(language: SupportedLanguage) {
    localStorage.setItem(solutionLanguageStorageKey, language);
    const { currentDetail } = get();
    set({
      codeLanguage: language,
      runResult: null,
      error: null,
      aiAnalysis: '',
      aiMessages: [],
      aiStatus: 'idle',
      aiError: '',
    });
    if (!currentDetail) return;
    const userCases = loadUserCases(currentDetail.id, language);
    const firstVisibleCase = currentDetail.test_cases?.[0]?.id;
    set({
      userCases,
      selectedCaseIds: firstVisibleCase ? [firstVisibleCase] : userCases[0] ? [userCases[0].id] : [],
      customCaseInput: firstVisibleCase ? '' : userCases[0]?.input || '',
    });
    try {
      const saved = await solutionsApi.getSolution(currentDetail.id, language);
      set({
        source: saved.source || starterForLanguage(currentDetail, language),
        activeVersion: saved.active_version,
        versions: saved.versions,
        versionNames: saved.version_names,
        modifiedVersions: saved.modified_versions,
      });
    } catch {
      set({
        source: starterForLanguage(currentDetail, language),
        activeVersion: 1,
        versions: [],
        versionNames: {},
        modifiedVersions: [],
      });
    }
  },
  setPaneSize: (scope, size) => set((state) => {
    const next = { ...state.paneSizes, [scope]: size };
    return {
      paneSizes: next,
      progress: state.progress ? { ...state.progress, pane_sizes: next } : state.progress,
    };
  }),
  savePaneSizesToBackend: async () => {
    try {
      await progressApi.updateProgressSettings({ pane_sizes: get().paneSizes });
    } catch {
      // Keep the current-session layout when profile persistence is temporarily unavailable.
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
    const { currentDetail, codeLanguage } = get();
    if (!currentDetail) return;
    try {
      // Optimistic update
      set({ source: s });
      await solutionsApi.putSolution(currentDetail.id, s, codeLanguage);
    } catch (e) {
      console.error('Failed to save source:', e);
    }
  },
  setMode(m: RunMode) {
    set({ mode: m });
  },
  setSelectedCaseIds(ids: string[]) {
    const selectedUserCase = get().userCases.find((testCase) => testCase.id === ids[0]);
    set({ selectedCaseIds: ids, customCaseInput: selectedUserCase?.input || '' });
  },
  runAllTrialCases() {
    set({ selectedCaseIds: [allTrialCasesId], customCaseInput: '' });
  },
  setCustomCaseInput(value: string) {
    const { currentDetail, codeLanguage, selectedCaseIds, userCases } = get();
    const selectedId = selectedCaseIds[0];
    if (currentDetail && selectedId && userCases.some((testCase) => testCase.id === selectedId)) {
      const next = userCases.map((testCase) => testCase.id === selectedId ? { ...testCase, input: value } : testCase);
      persistUserCases(currentDetail.id, codeLanguage, next);
      set({ customCaseInput: value, userCases: next });
      return;
    }
    set({ customCaseInput: value });
  },
  addUserCase(initialInput = '{\n  \n}') {
    const { currentDetail, codeLanguage, userCases } = get();
    if (!currentDetail) return '';
    if ((currentDetail.test_cases?.length ?? 0) + userCases.length >= MAX_DEBUG_CASES) return '';
    const id = `user-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
    const nextCase: UserTestCase = {
      id,
      name: `Custom ${userCases.length + 1}`,
      input: initialInput,
      createdAt: Date.now(),
    };
    const next = [...userCases, nextCase];
    persistUserCases(currentDetail.id, codeLanguage, next);
    set({
      userCases: next,
      selectedCaseIds: [id],
      customCaseInput: initialInput,
      mode: 'practice',
    });
    return id;
  },
  updateUserCase(id, patch) {
    const { currentDetail, codeLanguage, userCases, selectedCaseIds } = get();
    if (!currentDetail) return;
    const next = userCases.map((testCase) => testCase.id === id ? { ...testCase, ...patch } : testCase);
    persistUserCases(currentDetail.id, codeLanguage, next);
    set({
      userCases: next,
      customCaseInput: selectedCaseIds[0] === id && patch.input !== undefined ? patch.input : get().customCaseInput,
    });
  },
  deleteUserCase(id) {
    const { currentDetail, codeLanguage, userCases, selectedCaseIds } = get();
    if (!currentDetail) return;
    const next = userCases.filter((testCase) => testCase.id !== id);
    persistUserCases(currentDetail.id, codeLanguage, next);
    if (selectedCaseIds[0] !== id) {
      set({ userCases: next });
      return;
    }
    const fallbackSystemId = currentDetail.test_cases?.[0]?.id;
    const fallbackUser = next[0];
    set({
      userCases: next,
      selectedCaseIds: fallbackSystemId ? [fallbackSystemId] : fallbackUser ? [fallbackUser.id] : [],
      customCaseInput: fallbackSystemId ? '' : fallbackUser?.input || '',
    });
  },

  async run() {
    const { currentDetail, mode, codeLanguage, selectedCaseIds, customCaseInput, userCases } = get();
    if (!currentDetail) return;
    let customInput: Record<string, unknown> | null = null;
    const selectedUserCase = userCases.find((testCase) => testCase.id === selectedCaseIds[0]);
    if (customCaseInput.trim() && !selectedUserCase) {
      try {
        const parsed = JSON.parse(customCaseInput);
        if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
          throw new Error('Custom input must be a JSON object matching solve(...) parameters.');
        }
        customInput = parsed as Record<string, unknown>;
      } catch (e) {
        set({ error: (e as Error).message, runResult: null });
        return;
      }
    }
    const relevantUserCases = mode === 'real_test'
      ? userCases
      : selectedCaseIds.includes(allTrialCasesId)
        ? userCases
        : selectedUserCase ? [selectedUserCase] : [];
    const customCases: Array<{ id: string; name: string; input: Record<string, unknown> }> = [];
    for (const testCase of relevantUserCases) {
      try {
        const parsed = JSON.parse(testCase.input);
        if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
          throw new Error('Input must be a JSON object.');
        }
        customCases.push({ id: testCase.id, name: testCase.name, input: parsed as Record<string, unknown> });
      } catch (e) {
        set({ error: `${testCase.name}: ${(e as Error).message}`, runResult: null });
        return;
      }
    }
    set({
      isRunning: true,
      error: null,
      activeTopic: 'complexity',
    });
    try {
      // File on disk is the source of truth. Re-read before
      // every run so saved editor changes are picked up automatically —
      // no need for an explicit "Save" button.
      let source: string;
      try {
        const saved = await solutionsApi.getSolution(currentDetail.id, codeLanguage);
        source = saved && saved.source ? saved.source : starterForLanguage(currentDetail, codeLanguage);
      } catch {
        source = starterForLanguage(currentDetail, codeLanguage);
      }
      const result = await runApi.runChallenge({
        challengeId: currentDetail.id,
        source,
        language: codeLanguage,
        mode,
        caseIds: selectedCaseIds,
        customInput,
        customCases,
      });
      const updates: Partial<AppState> = {
        runResult: result,
        source,
      };
      set(updates);
      // Side-effect: persist progress if it passed.
      if (result.passed) {
        try {
          await progressApi.markChallengeDone(
            currentDetail.id,
            Math.max(0, Math.round(result.runtime_user_ms ?? result.user_ast_ops ?? 0)),
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
      set({ 
        progress: p,
        activeSet: normalizeAlgorithmSet(p.active_set),
        paneFontScales: p.pane_font_scales ?? {},
        paneSizes: p.pane_sizes ?? {},
        accentColors: normalizeAccentColors(p.accent_colors),
      });
      if (p.sidebar_width) {
        set({ sidebarWidth: p.sidebar_width });
      }
      if (p.sidebar_position) {
        set({ sidebarPosition: p.sidebar_position });
      }
      if (p.sidebar_collapsed !== undefined) {
        set({ sidebarCollapsed: p.sidebar_collapsed });
      }
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
        Math.max(0, Math.round(runResult.runtime_user_ms ?? runResult.user_ast_ops ?? 0)),
        runResult.actual_complexity,
      );
      await get().loadProgress();
    } catch {
      // ignore
    }
  },


  async refreshSourceFromDisk() {
    const { currentDetail, codeLanguage } = get();
    if (!currentDetail) return;
    try {
      const saved = await solutionsApi.getSolution(currentDetail.id, codeLanguage);
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
    const { currentDetail, codeLanguage } = get();
    if (!currentDetail) return;
    try {
      const res = await solutionsApi.switchVersion(currentDetail.id, version, codeLanguage);
      set({ source: res.source, activeVersion: res.active_version, versions: res.versions, versionNames: res.version_names, modifiedVersions: res.modified_versions });
    } catch (e) {
      console.error(e);
    }
  },

  async renameVersion(version: number, name: string) {
    const { currentDetail, codeLanguage } = get();
    if (!currentDetail) return;
    try {
      const res = await solutionsApi.renameVersion(currentDetail.id, version, name, codeLanguage);
      set({ source: res.source, activeVersion: res.active_version, versions: res.versions, versionNames: res.version_names, modifiedVersions: res.modified_versions });
    } catch (e) {
      console.error(e);
    }
  },

  async resetVersion(version: number) {
    const { currentDetail, codeLanguage } = get();
    if (!currentDetail) return;
    try {
      const res = await solutionsApi.resetVersion(currentDetail.id, version, codeLanguage);
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
    } catch (e) {
      console.error(e);
    }
  },

  async deleteProfile(name: string) {
    try {
      const res = await profilesApi.deleteProfile(name);
      set({ activeProfile: res.active_profile, profiles: res.profiles });
      await get().loadProgress();
    } catch (e) {
      console.error(e);
    }
  },

  async setActiveSet(setVal: AlgorithmSetId) {
    const previousSet = get().activeSet;
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
    set(updates);
    try {
      const p = await progressApi.updateProgressSettings({ active_set: setVal });
      set({ 
        progress: p,
        activeSet: normalizeAlgorithmSet(p.active_set)
      });
    } catch (e) {
      console.error(e);
      set({
        activeSet: previousSet,
        error: e instanceof Error ? e.message : 'Unable to change challenge view',
      });
    }
  },

  async updateSettings(careerMode: boolean, leetcodeUsername: string, geminiApiKey: string) {
    try {
      const activeSet = get().activeSet;
      const p = await progressApi.updateProgressSettings({
        career_mode: careerMode,
        leetcode_username: leetcodeUsername,
        gemini_api_key: geminiApiKey,
        active_set: activeSet,
      });
      set({ progress: p });
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
        return { success: true, message: res.message };
      }
      return { success: false, message: res.message };
    } catch (e) {
      console.error(e);
      return { success: false, message: e instanceof Error ? e.message : 'Unknown verification error' };
    }
  },
}));
