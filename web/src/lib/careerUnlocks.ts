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
