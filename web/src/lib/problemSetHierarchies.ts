import type {
  AlgorithmSetId,
  AlgorithmSetOption,
} from './algorithmSets';
import { ALGORITHM_SETS } from './algorithmSets';
import type { CustomProblemTreeTemplate } from './customProblemSets';
import type {
  ChallengeSummary,
  CustomProblemSet,
  CustomProblemTreeNode,
} from '../types/api';


export type StandardHierarchySetId = Exclude<AlgorithmSetId, 'custom'>;

export type ProblemHierarchyNode =
  | {
      type: 'problem';
      key: string;
      challenge_id: string;
      order: number;
    }
  | {
      type: 'group';
      key: string;
      name: string;
      children: ProblemHierarchyNode[];
      order: number;
    };

export interface ProblemHierarchyRoot {
  key: string;
  name: string;
  description: string;
  kind: 'standard' | 'personal';
  career_mode: boolean;
  nodes: ProblemHierarchyNode[];
}

export const STANDARD_HIERARCHY_OPTIONS: AlgorithmSetOption[] = ALGORITHM_SETS.filter(
  (option) => option.id !== 'custom',
);

type MutableFolder = {
  key: string;
  name: string;
  order: number;
  folders: Map<string, MutableFolder>;
  problems: Map<string, { challenge: ChallengeSummary; order: number }>;
};

const CATEGORY_ORDER = [
  'Algorithms',
  'Database',
  'Shell',
  'Concurrency',
  'JavaScript',
  'pandas',
];

const TOPIC_ORDER = [
  'Array',
  'String',
  'Hash Table',
  'Math',
  'Dynamic Programming',
  'Sorting',
  'Greedy',
  'Depth-First Search',
  'Binary Search',
  'Database',
  'Bit Manipulation',
  'Matrix',
  'Tree',
  'Prefix Sum',
  'Breadth-First Search',
  'Two Pointers',
  'Heap (Priority Queue)',
  'Simulation',
  'Counting',
  'Graph Theory',
  'Binary Tree',
  'Stack',
  'Sliding Window',
  'Enumeration',
  'Design',
  'Backtracking',
  'Number Theory',
  'Union-Find',
  'Linked List',
  'Segment Tree',
  'Ordered Set',
  'Monotonic Stack',
  'Divide and Conquer',
  'Combinatorics',
  'Trie',
  'Queue',
  'Bitmask',
  'Recursion',
  'Geometry',
  'Binary Indexed Tree',
  'Hash Function',
  'Memoization',
  'Binary Search Tree',
  'Shortest Path',
  'Topological Sort',
  'String Matching',
  'Rolling Hash',
  'Game Theory',
  'Monotonic Queue',
  'Interactive',
  'Data Stream',
];

const TOPIC_INDEX = new Map(
  TOPIC_ORDER.map((topic, index) => [topic.toLowerCase(), index]),
);

function stringField(value: unknown): string {
  return typeof value === 'string' ? value : '';
}

function numberField(value: unknown): number {
  return typeof value === 'number' && Number.isFinite(value)
    ? value
    : Number.MAX_SAFE_INTEGER;
}

function slugKey(value: string): string {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '')
    || 'uncategorized';
}

function challengeOrder(challenge: ChallengeSummary): number {
  const frontendId = Number(challenge.leetcode_frontend_id);
  if (Number.isFinite(frontendId)) return frontendId;
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

function categoryName(challenge: ChallengeSummary): string {
  return challenge.leetcode_category_title
    || challenge.category.replace(/^(leetcode|neetcode)_/i, '').replace(/_/g, ' ')
    || 'Uncategorized';
}

function categoryOrder(name: string): number {
  const index = CATEGORY_ORDER.indexOf(name);
  return index < 0 ? Number.MAX_SAFE_INTEGER : index;
}

function topicOrder(name: string): number {
  return TOPIC_INDEX.get(name.toLowerCase()) ?? Number.MAX_SAFE_INTEGER;
}

function challengeTopics(
  challenge: ChallengeSummary,
): Array<{ name: string; slug: string }> {
  const topics = challenge.leetcode_topics
    .map((topic) => {
      const name = stringField(topic.name) || stringField(topic.slug);
      const slug = stringField(topic.slug) || slugKey(name);
      return { name, slug };
    })
    .filter((topic) => topic.name && topic.slug);
  return topics.length > 0
    ? topics
    : [{ name: 'Uncategorized', slug: 'uncategorized' }];
}

function rootFolder(key: string, name: string): MutableFolder {
  return {
    key,
    name,
    order: 0,
    folders: new Map(),
    problems: new Map(),
  };
}

function childFolder(
  parent: MutableFolder,
  name: string,
  order = Number.MAX_SAFE_INTEGER,
): MutableFolder {
  const localKey = slugKey(name);
  let child = parent.folders.get(localKey);
  if (!child) {
    child = rootFolder(`${parent.key}/${localKey}`, name);
    child.order = order;
    parent.folders.set(localKey, child);
  } else {
    child.order = Math.min(child.order, order);
  }
  return child;
}

function fitFolderPath(parts: string[]): string[] {
  const clean = parts.map((part) => part.trim()).filter(Boolean);
  if (clean.length <= 3) return clean;
  return [clean[0]!, clean[1]!, clean.slice(2).join(' / ')];
}

function ensurePath(
  root: MutableFolder,
  parts: string[],
  orders: number[] = [],
): MutableFolder {
  return fitFolderPath(parts).reduce(
    (parent, part, index) => childFolder(parent, part, orders[index]),
    root,
  );
}

function addProblem(
  folder: MutableFolder,
  challenge: ChallengeSummary,
  order = challengeOrder(challenge),
): void {
  const existing = folder.problems.get(challenge.id);
  if (!existing || order < existing.order) {
    folder.problems.set(challenge.id, { challenge, order });
  }
}

function compareFolders(left: MutableFolder, right: MutableFolder): number {
  return left.order - right.order || left.name.localeCompare(right.name);
}

function finalizeFolder(folder: MutableFolder): ProblemHierarchyNode[] {
  const groups: ProblemHierarchyNode[] = [...folder.folders.values()]
    .sort(compareFolders)
    .map((child) => ({
      type: 'group',
      key: child.key,
      name: child.name,
      order: child.order,
      children: finalizeFolder(child),
    }));
  const problems: ProblemHierarchyNode[] = [...folder.problems.values()]
    .sort((left, right) => (
      left.order - right.order
      || challengeOrder(left.challenge) - challengeOrder(right.challenge)
      || left.challenge.name.localeCompare(right.challenge.name)
    ))
    .map(({ challenge, order }) => ({
      type: 'problem',
      key: `${folder.key}/problem/${challenge.id}`,
      challenge_id: challenge.id,
      order,
    }));
  return [...groups, ...problems];
}

function buildAllProblems(
  root: MutableFolder,
  challenges: ChallengeSummary[],
): void {
  for (const challenge of challenges) {
    const category = categoryName(challenge);
    for (const topic of challengeTopics(challenge)) {
      const leaf = ensurePath(
        root,
        [category, topic.name],
        [categoryOrder(category), topicOrder(topic.name)],
      );
      addProblem(leaf, challenge);
    }
  }
}

function buildMetricSet(
  root: MutableFolder,
  challenges: ChallengeSummary[],
  metric: 'elo' | 'frequency',
): void {
  const eligible = challenges.filter((challenge) => (
    metric === 'elo' ? challenge.elo_rating !== null : challenge.frequency !== null
  ));
  for (const challenge of eligible) {
    for (const topic of challengeTopics(challenge)) {
      const leaf = ensurePath(root, [topic.name], [topicOrder(topic.name)]);
      const order = metric === 'elo'
        ? challenge.elo_rating!
        : -(challenge.frequency ?? 0);
      addProblem(leaf, challenge, order);
    }
  }
}

function buildCompanies(
  root: MutableFolder,
  challenges: ChallengeSummary[],
): void {
  const companyCounts = new Map<string, Set<string>>();
  for (const challenge of challenges) {
    for (const company of challenge.leetcode_company_tags) {
      const companyName = stringField(company.name) || stringField(company.slug);
      if (!companyName) continue;
      const companyKey = slugKey(companyName);
      const seen = companyCounts.get(companyKey) ?? new Set<string>();
      seen.add(challenge.id);
      companyCounts.set(companyKey, seen);
      const category = categoryName(challenge);
      for (const topic of challengeTopics(challenge)) {
        const leaf = ensurePath(
          root,
          [companyName, category, topic.name],
          [
            0,
            categoryOrder(category),
            topicOrder(topic.name),
          ],
        );
        addProblem(leaf, challenge);
      }
    }
  }
  for (const folder of root.folders.values()) {
    const slug = slugKey(folder.name);
    folder.order = -(companyCounts.get(slug)?.size ?? 0);
  }
}

function buildStudyPlans(
  root: MutableFolder,
  challenges: ChallengeSummary[],
): void {
  for (const challenge of challenges) {
    for (const membership of challenge.leetcode_study_plans) {
      const planName = stringField(membership.plan_name)
        || stringField(membership.name)
        || stringField(membership.plan_slug)
        || 'Study Plan';
      const path = Array.isArray(membership.path)
        ? membership.path.map(String).filter(Boolean)
        : [];
      const leaf = ensurePath(
        root,
        [planName, ...path],
        [
          numberField(membership.plan_order),
          numberField(membership.section_order),
        ],
      );
      addProblem(
        leaf,
        challenge,
        numberField(membership.order ?? membership.problem_order),
      );
    }
  }
}

function buildExternalSubsets(
  root: MutableFolder,
  challenges: ChallengeSummary[],
  kind: 'neetcode' | 'algomaster',
): void {
  for (const challenge of challenges) {
    for (const membership of challenge.leetcode_external_subsets) {
      if (stringField(membership.kind) !== kind) continue;
      const subsetName = stringField(membership.subset_name)
        || (kind === 'neetcode' ? 'NeetCode' : 'AlgoMaster');
      const path = Array.isArray(membership.path)
        ? membership.path.map(String).filter(Boolean)
        : [];
      const leaf = ensurePath(
        root,
        [subsetName, ...path],
        [
          numberField(membership.subset_order),
          numberField(membership.section_order),
        ],
      );
      addProblem(
        leaf,
        challenge,
        numberField(membership.order ?? membership.problem_order),
      );
    }
  }
}

export function buildStandardProblemHierarchy(
  setId: StandardHierarchySetId,
  challenges: ChallengeSummary[],
): ProblemHierarchyRoot {
  const option = STANDARD_HIERARCHY_OPTIONS.find((candidate) => candidate.id === setId);
  if (!option) throw new Error(`Unsupported standard problem set: ${setId}`);
  const root = rootFolder(`standard:${setId}`, option.label);
  if (setId === 'leetcode') buildAllProblems(root, challenges);
  else if (setId === 'elo') buildMetricSet(root, challenges, 'elo');
  else if (setId === 'frequency') buildMetricSet(root, challenges, 'frequency');
  else if (setId === 'leetcode_company') buildCompanies(root, challenges);
  else if (setId === 'leetcode_studyplan') buildStudyPlans(root, challenges);
  else if (setId === 'neetcode') buildExternalSubsets(root, challenges, 'neetcode');
  else if (setId === 'algomaster') buildExternalSubsets(root, challenges, 'algomaster');
  return {
    key: root.key,
    name: option.label,
    description: option.description,
    kind: 'standard',
    career_mode: option.hasCareerPath,
    nodes: finalizeFolder(root),
  };
}

function personalNode(
  setId: string,
  node: CustomProblemTreeNode,
): ProblemHierarchyNode {
  if (node.type === 'problem') {
    return {
      type: 'problem',
      key: `personal:${setId}:${node.id}`,
      challenge_id: node.challenge_id,
      order: 0,
    };
  }
  return {
    type: 'group',
    key: `personal:${setId}:${node.id}`,
    name: node.name,
    children: node.children.map((child) => personalNode(setId, child)),
    order: 0,
  };
}

export function buildPersonalProblemHierarchy(
  set: CustomProblemSet,
): ProblemHierarchyRoot {
  return {
    key: `personal:${set.id}`,
    name: set.name,
    description: set.description,
    kind: 'personal',
    career_mode: set.career_mode,
    nodes: set.nodes.map((node) => personalNode(set.id, node)),
  };
}

export function hierarchyNodesToTemplates(
  nodes: ProblemHierarchyNode[],
): CustomProblemTreeTemplate[] {
  return nodes.map((node) => node.type === 'problem'
    ? { type: 'problem', challenge_id: node.challenge_id }
    : {
        type: 'group',
        name: node.name,
        children: hierarchyNodesToTemplates(node.children),
      });
}

export function hierarchyProblemCount(nodes: ProblemHierarchyNode[]): number {
  const ids = new Set<string>();
  const visit = (items: ProblemHierarchyNode[]) => {
    for (const item of items) {
      if (item.type === 'problem') ids.add(item.challenge_id);
      else visit(item.children);
    }
  };
  visit(nodes);
  return ids.size;
}

/**
 * Apply the shared problem-library filter order without changing folder names
 * or their relative positions. Empty folders are pruned from the view only.
 */
export function filterProblemHierarchy(
  root: ProblemHierarchyRoot,
  orderedChallengeIds: string[],
): ProblemHierarchyRoot {
  const rank = new Map(
    orderedChallengeIds.map((challengeId, index) => [challengeId, index]),
  );
  const filterNodes = (nodes: ProblemHierarchyNode[]): ProblemHierarchyNode[] => {
    const visible = nodes.flatMap((node): ProblemHierarchyNode[] => {
      if (node.type === 'problem') {
        return rank.has(node.challenge_id) ? [node] : [];
      }
      const children = filterNodes(node.children);
      return children.length > 0 ? [{ ...node, children }] : [];
    });
    const orderedProblems = visible
      .filter((node): node is Extract<ProblemHierarchyNode, { type: 'problem' }> => (
        node.type === 'problem'
      ))
      .sort((left, right) => (
        (rank.get(left.challenge_id) ?? Number.MAX_SAFE_INTEGER)
        - (rank.get(right.challenge_id) ?? Number.MAX_SAFE_INTEGER)
      ));
    let problemIndex = 0;
    return visible.map((node) => (
      node.type === 'problem' ? orderedProblems[problemIndex++]! : node
    ));
  };
  return { ...root, nodes: filterNodes(root.nodes) };
}

export function findHierarchyNode(
  nodes: ProblemHierarchyNode[],
  key: string,
): ProblemHierarchyNode | null {
  for (const node of nodes) {
    if (node.key === key) return node;
    if (node.type === 'group') {
      const nested = findHierarchyNode(node.children, key);
      if (nested) return nested;
    }
  }
  return null;
}
