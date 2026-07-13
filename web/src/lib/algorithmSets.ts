import type { ChallengeSummary } from '../types/api';

export type AlgorithmSetId =
  | 'leetcode'
  | 'leetcode_company'
  | 'leetcode_studyplan'
  | 'neetcode'
  | 'algomaster';

export interface AlgorithmSetOption {
  id: AlgorithmSetId;
  label: string;
  shortLabel: string;
  category: string;
  description: string;
  hasCareerPath: boolean;
}

export const ALGORITHM_SETS: AlgorithmSetOption[] = [
  {
    id: 'leetcode',
    label: 'All Problems',
    shortLabel: 'All Problems',
    category: 'LeetCode',
    description: 'The canonical LeetCode corpus, grouped by category and topic.',
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
];

export function normalizeAlgorithmSet(value: string | null | undefined): AlgorithmSetId {
  return ALGORITHM_SETS.some((set) => set.id === value)
    ? (value as AlgorithmSetId)
    : 'leetcode';
}

export function getAlgorithmSetLabel(value: string | null | undefined): string {
  return ALGORITHM_SETS.find((set) => set.id === normalizeAlgorithmSet(value))?.label ?? 'All Problems';
}

export function getAlgorithmSetOption(value: string | null | undefined): AlgorithmSetOption {
  return ALGORITHM_SETS.find((set) => set.id === normalizeAlgorithmSet(value)) ?? ALGORITHM_SETS[0]!;
}

function hasExternalMembership(challenge: ChallengeSummary, kind: string): boolean {
  return challenge.leetcode_external_subsets.some((membership) => membership.kind === kind);
}

export function challengeIsInAlgorithmSet(
  challenge: ChallengeSummary,
  value: string | null | undefined,
): boolean {
  switch (normalizeAlgorithmSet(value)) {
    case 'leetcode_company':
      return challenge.leetcode_company_tags.length > 0;
    case 'leetcode_studyplan':
      return challenge.leetcode_study_plans.length > 0;
    case 'neetcode':
      return hasExternalMembership(challenge, 'neetcode');
    case 'algomaster':
      return hasExternalMembership(challenge, 'algomaster');
    default:
      return true;
  }
}

export function challengesForAlgorithmSet(
  challenges: ChallengeSummary[],
  value: string | null | undefined,
): ChallengeSummary[] {
  const activeSet = normalizeAlgorithmSet(value);
  if (activeSet === 'leetcode') return challenges;
  return challenges.filter((challenge) => challengeIsInAlgorithmSet(challenge, activeSet));
}
