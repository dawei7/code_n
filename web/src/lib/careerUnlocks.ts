import type {
  CustomProblemSet,
  CustomProblemTreeNode,
} from '../types/api';


/** Preserve zero-based sequence positions; only absent values use the fallback. */
export function resolveCareerSequenceOrder(
  order: number | null | undefined,
  fallbackOrder: number,
): number {
  return order ?? fallbackOrder;
}

export type CareerUnlockEntry = {
  challengeId: string;
  order: number;
  fallbackOrder: number;
};

export type CustomCareerLeaf = {
  key: string;
  path: string[];
  challengeIds: string[];
};

export function collectCustomCareerLeaves(
  customSets: CustomProblemSet[],
): CustomCareerLeaf[] {
  const result: CustomCareerLeaf[] = [];
  const addLeaf = (
    key: string,
    path: string[],
    nodes: CustomProblemTreeNode[],
  ) => {
    const challengeIds = nodes.flatMap((node) => (
      node.type === 'problem' ? [node.challenge_id] : []
    ));
    if (challengeIds.length > 0) result.push({ key, path, challengeIds });
    for (const node of nodes) {
      if (node.type === 'group') {
        addLeaf(
          `custom-group:${node.id}`,
          [...path, node.name],
          node.children,
        );
      }
    }
  };
  for (const set of customSets) {
    if (set.career_mode) addLeaf(`custom-set:${set.id}`, [set.name], set.nodes);
  }
  return result;
}

export function buildUnlockedCareerSequence(
  items: CareerUnlockEntry[],
  completed: Set<string>,
): Set<string> {
  const ordered = [...items].sort((left, right) => {
    const byOrder = left.order - right.order;
    return byOrder !== 0 ? byOrder : left.fallbackOrder - right.fallbackOrder;
  });
  const unlocked = new Set<string>();
  let allPreviousSolved = true;
  for (const item of ordered) {
    if (allPreviousSolved || completed.has(item.challengeId)) {
      unlocked.add(item.challengeId);
    }
    if (!completed.has(item.challengeId)) {
      allPreviousSolved = false;
    }
  }
  return unlocked;
}

export function buildCustomCareerUnlockMap(
  customSets: CustomProblemSet[],
  completed: Set<string>,
  fallbackOrderForChallenge: (challengeId: string) => number = () => 0,
): Map<string, Set<string>> {
  const result = new Map<string, Set<string>>();
  for (const leaf of collectCustomCareerLeaves(customSets)) {
    result.set(leaf.key, buildUnlockedCareerSequence(
        leaf.challengeIds.map((challengeId, index) => ({
          challengeId,
          order: index,
          fallbackOrder: fallbackOrderForChallenge(challengeId),
        })),
        completed,
      ));
  }
  return result;
}
