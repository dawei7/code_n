export type AlgorithmSetId = 'neetcode' | 'leetcode' | 'gfg' | 'codechef';

export interface AlgorithmSetOption {
  id: AlgorithmSetId;
  label: string;
  shortLabel: string;
  description: string;
  hasCareerPath: boolean;
  hasMathematical: boolean;
}

export const ALGORITHM_SETS: AlgorithmSetOption[] = [
  {
    id: 'neetcode',
    label: 'NeetCode 250',
    shortLabel: 'NeetCode',
    description: 'Curated interview roadmap with dependency locking.',
    hasCareerPath: true,
    hasMathematical: false,
  },
  {
    id: 'leetcode',
    label: 'LeetCode',
    shortLabel: 'LeetCode',
    description: 'Free LeetCode problem dataset, organized by topic.',
    hasCareerPath: false,
    hasMathematical: false,
  },
  {
    id: 'gfg',
    label: 'GeeksforGeeks',
    shortLabel: 'GFG',
    description: 'Standard algorithms library, fully unlocked.',
    hasCareerPath: false,
    hasMathematical: true,
  },
  {
    id: 'codechef',
    label: 'CodeChef',
    shortLabel: 'CodeChef',
    description: 'Python practice course with 14 lessons, 182 problems.',
    hasCareerPath: false,
    hasMathematical: false,
  },
];

export function normalizeAlgorithmSet(value: string | null | undefined): AlgorithmSetId {
  return ALGORITHM_SETS.some((set) => set.id === value)
    ? (value as AlgorithmSetId)
    : 'neetcode';
}

export function getAlgorithmSetLabel(value: string | null | undefined): string {
  return ALGORITHM_SETS.find((set) => set.id === normalizeAlgorithmSet(value))?.label ?? 'NeetCode 250';
}

export function getAlgorithmSetOption(value: string | null | undefined): AlgorithmSetOption {
  return ALGORITHM_SETS.find((set) => set.id === normalizeAlgorithmSet(value)) ?? ALGORITHM_SETS[0]!;
}
