import type { ChallengeSummary } from '../types/api';

export type AlgorithmSetId =
  | 'leetcode'
  | 'leetcode_id'
  | 'elo'
  | 'elo_buckets'
  | 'frequency'
  | 'frequency_buckets'
  | 'leetcode_company'
  | 'leetcode_studyplan'
  | 'leetcode_quest'
  | 'neetcode'
  | 'algomaster'
  | 'euler_level'
  | 'euler_category'
  | 'custom';

export interface AlgorithmSetOption {
  id: AlgorithmSetId;
  label: string;
  shortLabel: string;
  category: string;
  description: string;
  hasCareerPath: boolean;
}

export const LEETCODE_SETS: AlgorithmSetOption[] = [
  {
    id: 'leetcode',
    label: 'All Problems by Topics',
    shortLabel: 'Problems by Topics',
    category: 'LeetCode',
    description: 'The canonical LeetCode corpus, grouped by category and topic.',
    hasCareerPath: false,
  },
  {
    id: 'leetcode_id',
    label: 'All Problems by ID',
    shortLabel: 'Problems by ID',
    category: 'LeetCode',
    description: 'The canonical LeetCode corpus as one flat list in strict numeric frontend-ID order.',
    hasCareerPath: false,
  },
  {
    id: 'elo',
    label: 'Elo by Category',
    shortLabel: 'Elo by Category',
    category: 'LeetCode',
    description: 'LeetCode problems grouped by topic and ordered from lowest to highest Elo (contest and estimated).',
    hasCareerPath: false,
  },
  {
    id: 'elo_buckets',
    label: 'Elo Buckets',
    shortLabel: 'Elo Buckets',
    category: 'LeetCode',
    description: 'LeetCode problems grouped into canonical Elo bands and strictly ordered by Elo (contest and estimated).',
    hasCareerPath: false,
  },
  {
    id: 'frequency',
    label: 'Frequency by Topics',
    shortLabel: 'Frequency by Topics',
    category: 'LeetCode',
    description: 'LeetCode problems grouped by topic and ordered from highest to lowest Frequency.',
    hasCareerPath: false,
  },
  {
    id: 'frequency_buckets',
    label: 'Frequency Buckets',
    shortLabel: 'Frequency Buckets',
    category: 'LeetCode',
    description: 'LeetCode problems grouped into equal 10-point Frequency bands and strictly ordered from highest to lowest Frequency.',
    hasCareerPath: false,
  },
  {
    id: 'leetcode_company',
    label: 'Company View',
    shortLabel: 'Companies',
    category: 'LeetCode',
    description: 'All LeetCode problems grouped by company, then category.',
    hasCareerPath: false,
  },
  {
    id: 'leetcode_studyplan',
    label: 'Study Plans',
    shortLabel: 'Study Plans',
    category: 'LeetCode',
    description: 'Official LeetCode study-plan subsets with sequential locking.',
    hasCareerPath: true,
  },
  {
    id: 'leetcode_quest',
    label: 'LeetCode Quests',
    shortLabel: 'Quests',
    category: 'LeetCode',
    description: 'Official LeetCode Quest problem lists in their published unit and level order.',
    hasCareerPath: true,
  },
  {
    id: 'neetcode',
    label: 'NeetCode Subsets',
    shortLabel: 'NeetCode',
    category: 'LeetCode',
    description: 'NeetCode subsets mapped onto canonical LeetCode problems.',
    hasCareerPath: true,
  },
  {
    id: 'algomaster',
    label: 'AlgoMaster Subsets',
    shortLabel: 'AlgoMaster',
    category: 'LeetCode',
    description: 'AlgoMaster 600, 300, 150, and 75 mapped onto canonical LeetCode problems.',
    hasCareerPath: false,
  },
  {
    id: 'custom',
    label: 'Personal',
    shortLabel: 'Personal',
    category: 'Personal',
    description: 'Your profile-specific top-level problem sets and learning paths.',
    hasCareerPath: false,
  },
];

export const EULER_SETS: AlgorithmSetOption[] = [
  {
    id: 'euler_level',
    label: 'Problems by Level',
    shortLabel: 'By Level',
    category: 'Project Euler',
    description: 'Project Euler problems grouped by difficulty level and ordered by Euler ID.',
    hasCareerPath: false,
  },
  {
    id: 'euler_category',
    label: 'Problems by Category',
    shortLabel: 'By Category',
    category: 'Project Euler',
    description: 'Project Euler problems grouped by category, ordered by Level, then by Euler ID.',
    hasCareerPath: false,
  },
  {
    id: 'custom',
    label: 'Personal',
    shortLabel: 'Personal',
    category: 'Personal',
    description: 'Your profile-specific top-level problem sets and learning paths.',
    hasCareerPath: false,
  },
];

export const ALGORITHM_SETS: AlgorithmSetOption[] = [
  ...LEETCODE_SETS.filter((s) => s.id !== 'custom'),
  ...EULER_SETS,
];

export function getAlgorithmSetsForMode(appMode: 'coden' | 'euler'): AlgorithmSetOption[] {
  return appMode === 'euler' ? EULER_SETS : LEETCODE_SETS;
}

export function isEulerSet(setId: string | null | undefined): boolean {
  return setId === 'euler_level' || setId === 'euler_category';
}

export function normalizeAlgorithmSet(
  value: string | null | undefined,
  appMode: 'coden' | 'euler' = 'coden',
): AlgorithmSetId {
  const sets = getAlgorithmSetsForMode(appMode);
  if (sets.some((set) => set.id === value)) {
    return value as AlgorithmSetId;
  }
  return appMode === 'euler' ? 'euler_level' : 'leetcode';
}

export function getAlgorithmSetLabel(
  value: string | null | undefined,
  appMode: 'coden' | 'euler' = 'coden',
): string {
  const normalized = normalizeAlgorithmSet(value, appMode);
  return ALGORITHM_SETS.find((set) => set.id === normalized)?.label
    ?? (appMode === 'euler' ? 'Problems by Level' : 'All Problems by Topics');
}

export function getAlgorithmSetOption(
  value: string | null | undefined,
  appMode: 'coden' | 'euler' = 'coden',
): AlgorithmSetOption {
  const normalized = normalizeAlgorithmSet(value, appMode);
  return ALGORITHM_SETS.find((set) => set.id === normalized) ?? (appMode === 'euler' ? EULER_SETS[0]! : LEETCODE_SETS[0]!);
}

function hasExternalMembership(challenge: ChallengeSummary, kind: string): boolean {
  return challenge.leetcode_external_subsets.some((membership) => membership.kind === kind);
}

export function challengeIsInAlgorithmSet(
  challenge: ChallengeSummary,
  value: string | null | undefined,
): boolean {
  const isEuler = challenge.dataset === 'euler' || challenge.id.startsWith('euler_');
  if (value === 'euler_level' || value === 'euler_category') {
    return isEuler;
  }
  if (isEuler) {
    return false;
  }
  switch (value) {
    case 'elo':
    case 'elo_buckets':
      return challenge.elo_rating !== null || challenge.estimated_elo_rating !== null;
    case 'frequency':
    case 'frequency_buckets':
      return challenge.frequency !== null;
    case 'leetcode_company':
      return challenge.leetcode_company_tags.length > 0;
    case 'leetcode_studyplan':
      return challenge.leetcode_study_plans.length > 0;
    case 'leetcode_quest':
      return hasExternalMembership(challenge, 'leetcode_quest');
    case 'neetcode':
      return hasExternalMembership(challenge, 'neetcode');
    case 'algomaster':
      return hasExternalMembership(challenge, 'algomaster');
    case 'custom':
      return false;
    default:
      return !isEuler;
  }
}

export function challengesForAlgorithmSet(
  challenges: ChallengeSummary[],
  value: string | null | undefined,
): ChallengeSummary[] {
  return challenges.filter((challenge) => challengeIsInAlgorithmSet(challenge, value));
}
