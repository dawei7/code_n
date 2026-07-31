export function leetcodeQuestGroupId(
  subsetSlug: string,
  path: readonly string[],
): string {
  let id = `leetcode-quest:${subsetSlug}`;
  path.forEach((part, index) => {
    id += `:${index}:${part}`;
  });
  return id;
}

export type LeetcodeQuestOrderKey = {
  problemOrder: number;
  order: number;
  frontendId: number;
};

export function compareLeetcodeQuestOrder(
  left: LeetcodeQuestOrderKey,
  right: LeetcodeQuestOrderKey,
): number {
  const byProblemOrder = left.problemOrder - right.problemOrder;
  if (byProblemOrder !== 0) return byProblemOrder;
  const byOrder = left.order - right.order;
  if (byOrder !== 0) return byOrder;
  return left.frontendId - right.frontendId;
}
