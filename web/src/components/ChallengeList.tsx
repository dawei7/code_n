import { Fragment, useState, useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';
import type { ChallengeSummary } from '../types/api';
import { challengesForAlgorithmSet } from '../lib/algorithmSets';
import { buildUnlockedCareerSequence, resolveCareerSequenceOrder } from '../lib/careerUnlocks';
import {
  downloadChallengePracticeFile,
  downloadPracticeBundle,
  type DownloadProgress,
  type PracticeExportEntry,
} from '../api/practiceExport';

const CATEGORY_DISPLAY_NAMES: Record<string, string> = {
  neetcode_arrays: 'Arrays & Hashing',
  neetcode_two_pointers: 'Two Pointers',
  neetcode_sliding_window: 'Sliding Window',
  neetcode_stack: 'Stack',
  neetcode_binary_search: 'Binary Search',
  neetcode_linked_list: 'Linked List',
  neetcode_trees: 'Trees',
  neetcode_heap: 'Heap / Priority Queue',
  neetcode_backtracking: 'Backtracking',
  neetcode_tries: 'Tries',
  neetcode_graphs: 'Graphs',
  neetcode_advanced_graphs: 'Advanced Graphs',
  neetcode_dp1: '1-D Dynamic',
  neetcode_dp2: '2-D Dynamic',
  neetcode_greedy: 'Greedy',
  neetcode_intervals: 'Intervals',
  neetcode_math: 'Math & Geometry',
  neetcode_bit: 'Bit Manipulation',
};

const LEETCODE_CATEGORY_ORDER = [
  'Algorithms',
  'Database',
  'Shell',
  'Concurrency',
  'JavaScript',
  'pandas',
];

const LEETCODE_TOPIC_ORDER = [
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
  'Brainteaser',
  'Doubly-Linked List',
  'Merge Sort',
  'Randomized',
  'Counting Sort',
  'Iterator',
  'Concurrency',
  'Quickselect',
  'Suffix Array',
  'Sweep Line',
  'Probability and Statistics',
  'Minimum Spanning Tree',
  'Bucket Sort',
  'Shell',
  'Reservoir Sampling',
  'Eulerian Circuit',
  'Radix Sort',
  'Strongly Connected Component',
  'Rejection Sampling',
  'Biconnected Component',
];

const TOPIC_ORDER_INDEX = new Map(
  LEETCODE_TOPIC_ORDER.map((topic, index) => [topic.toLowerCase(), index]),
);

function formatCategory(category: string): string {
  if (category in CATEGORY_DISPLAY_NAMES) {
    return CATEGORY_DISPLAY_NAMES[category];
  }
  const cleaned = category.replace(/^(leetcode|neetcode)_/i, '');
  return cleaned.replace(/_/g, ' ');
}

function slugKey(value: string): string {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'uncategorized';
}

type ChallengeNumber = {
  display: string;
  filename: string;
};

type DownloadState = {
  label: string;
  loaded: number;
  total: number | null;
  percent: number | null;
  status: 'active' | 'done' | 'error';
  message?: string;
};

type NavigationGroup = {
  id: string;
  label: string;
  challenges: ChallengeSummary[];
  children: NavigationGroup[];
  emptyMessage?: string;
  order?: number;
};

type SubmissionNotice = {
  status: 'active' | 'done' | 'error';
  message: string;
};

function isLeetcodeUniverse(activeSet: string): boolean {
  return activeSet === 'leetcode'
    || activeSet === 'leetcode_company'
    || activeSet === 'leetcode_studyplan'
    || activeSet === 'neetcode'
    || activeSet === 'algomaster';
}

function stringField(value: unknown): string {
  return typeof value === 'string' ? value : '';
}

function numberField(value: unknown): number {
  return typeof value === 'number' && Number.isFinite(value) ? value : 0;
}

function optionalNumberField(value: unknown): number | null {
  return typeof value === 'number' && Number.isFinite(value) ? value : null;
}

function leetcodeCategoryTitle(challenge: ChallengeSummary): string {
  return challenge.leetcode_category_title || formatCategory(challenge.category) || 'Uncategorized';
}

function challengeTopics(challenge: ChallengeSummary): Array<{ name: string; slug: string }> {
  const topics = challenge.leetcode_topics
    .map((topic) => {
      const name = stringField(topic.name) || stringField(topic.slug);
      const slug = stringField(topic.slug) || slugKey(name);
      return { name, slug };
    })
    .filter((topic) => topic.name && topic.slug);
  return topics.length > 0 ? topics : [{ name: 'Uncategorized', slug: 'uncategorized' }];
}

function challengeCompanyTags(challenge: ChallengeSummary): Array<{ name: string; slug: string }> {
  return challenge.leetcode_company_tags
    .map((company) => ({
      name: stringField(company.name) || stringField(company.slug),
      slug: stringField(company.slug) || stringField(company.name),
    }))
    .filter((company) => company.name && company.slug);
}

function studyPlanMemberships(challenge: ChallengeSummary): Array<{
  planName: string;
  planSlug: string;
  path: string[];
  order: number | null;
  sectionOrder: number;
  problemOrder: number;
}> {
  return challenge.leetcode_study_plans
    .map((membership) => ({
      planName: stringField(membership.plan_name)
        || stringField(membership.name)
        || stringField(membership.plan_slug)
        || 'Study Plan',
      planSlug: stringField(membership.plan_slug)
        || stringField(membership.slug)
        || stringField(membership.name)
        || 'study-plan',
      path: Array.isArray(membership.path)
        ? membership.path.map((part) => String(part)).filter(Boolean)
        : [],
      order: optionalNumberField(membership.order) ?? optionalNumberField(membership.problem_order),
      sectionOrder: numberField(membership.section_order),
      problemOrder: numberField(membership.problem_order),
    }))
    .filter((membership) => membership.planSlug);
}

function neetcodeMemberships(challenge: ChallengeSummary): Array<{
  subsetName: string;
  subsetSlug: string;
  path: string[];
  order: number | null;
  sectionOrder: number;
  subsetOrder: number;
  problemOrder: number;
}> {
  return challenge.leetcode_external_subsets
    .filter((membership) => stringField(membership.kind) === 'neetcode')
    .map((membership) => ({
      subsetName: stringField(membership.subset_name) || 'NeetCode',
      subsetSlug: stringField(membership.subset_slug) || 'neetcode',
      path: Array.isArray(membership.path)
        ? membership.path.map((part) => String(part)).filter(Boolean)
        : [],
      order: optionalNumberField(membership.order) ?? optionalNumberField(membership.problem_order),
      sectionOrder: numberField(membership.section_order),
      subsetOrder: numberField(membership.subset_order),
      problemOrder: numberField(membership.problem_order),
    }));
}

function algomasterMemberships(challenge: ChallengeSummary): Array<{
  subsetName: string;
  subsetSlug: string;
  path: string[];
  order: number;
  sectionOrder: number;
  subsetOrder: number;
  problemOrder: number;
}> {
  return challenge.leetcode_external_subsets
    .filter((membership) => stringField(membership.kind) === 'algomaster')
    .map((membership) => ({
      subsetName: stringField(membership.subset_name) || 'AlgoMaster',
      subsetSlug: stringField(membership.subset_slug) || 'algomaster',
      path: Array.isArray(membership.path)
        ? membership.path.map((part) => String(part)).filter(Boolean)
        : [],
      order: numberField(membership.order),
      sectionOrder: numberField(membership.section_order),
      subsetOrder: numberField(membership.subset_order),
      problemOrder: numberField(membership.problem_order),
    }));
}

function leetcodeProblemOrder(challenge: ChallengeSummary): number {
  const fromField = Number(challenge.leetcode_frontend_id);
  if (Number.isFinite(fromField) && fromField > 0) return fromField;
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

function sortByLeetcodeId(items: ChallengeSummary[]): ChallengeSummary[] {
  return [...items].sort((left, right) => {
    const byId = leetcodeProblemOrder(left) - leetcodeProblemOrder(right);
    if (byId !== 0) return byId;
    return left.name.localeCompare(right.name);
  });
}

function sortByDifficultyThenId(items: ChallengeSummary[]): ChallengeSummary[] {
  const tierOrder: Record<string, number> = { Easy: 0, Medium: 1, Hard: 2 };
  return [...items].sort((left, right) => {
    const byTier = (tierOrder[left.difficulty_label] ?? 3) - (tierOrder[right.difficulty_label] ?? 3);
    if (byTier !== 0) return byTier;
    if (left.elo_rating !== null && right.elo_rating !== null) {
      const byElo = left.elo_rating - right.elo_rating;
      if (byElo !== 0) return byElo;
    } else if (left.elo_rating !== null) {
      return -1;
    } else if (right.elo_rating !== null) {
      return 1;
    } else if (left.difficulty_estimate !== null && right.difficulty_estimate !== null) {
      const byEstimate = left.difficulty_estimate - right.difficulty_estimate;
      if (byEstimate !== 0) return byEstimate;
    }
    return leetcodeProblemOrder(left) - leetcodeProblemOrder(right);
  });
}

function formatChallengeTitle(
  challenge: ChallengeSummary,
  activeSet: string,
  number?: ChallengeNumber,
): string {
  if (number) return `${number.display}. ${challenge.name}`;
  if (!isLeetcodeUniverse(activeSet)) return challenge.name;
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? `${match[1]}. ${challenge.name}` : challenge.name;
}

function formatDifficultyLine(challenge: ChallengeSummary, activeSet: string): string {
  if (isLeetcodeUniverse(activeSet)) {
    if (challenge.elo_rating !== null) {
      return `${challenge.difficulty_label} · Elo ${Math.round(challenge.elo_rating)}`;
    }
    const estimate = challenge.difficulty_estimate === null
      ? ''
      : ` · Legacy estimate ${challenge.difficulty_estimate}/10`;
    return `${challenge.difficulty_label}${estimate}`;
  }
  return challenge.required_complexity;
}

function uniqueChallengeIds(challenges: ChallengeSummary[]): Set<string> {
  return new Set(challenges.map((challenge) => challenge.id));
}

function solvedCount(challenges: ChallengeSummary[], completed: Set<string>): number {
  let count = 0;
  for (const id of uniqueChallengeIds(challenges)) {
    if (completed.has(id)) count += 1;
  }
  return count;
}

function progressLabel(challenges: ChallengeSummary[], completed: Set<string>): string {
  const total = uniqueChallengeIds(challenges).size;
  return `${solvedCount(challenges, completed)}/${total}`;
}

function submittedCount(challenges: ChallengeSummary[], submitted: Set<string>): number {
  let count = 0;
  for (const id of uniqueChallengeIds(challenges)) {
    if (submitted.has(id)) count += 1;
  }
  return count;
}

function submissionProgressLabel(challenges: ChallengeSummary[], submitted: Set<string>): string {
  return `${submittedCount(challenges, submitted)}/${uniqueChallengeIds(challenges).size}`;
}

function isFullySolved(challenges: ChallengeSummary[], completed: Set<string>): boolean {
  const ids = uniqueChallengeIds(challenges);
  return ids.size > 0 && Array.from(ids).every((id) => completed.has(id));
}

function progressHeading(
  label: string,
  challenges: ChallengeSummary[],
  completed: Set<string>,
  submitted: Set<string>,
  countClassName = "ml-1 text-coden-muted",
) {
  const solved = isFullySolved(challenges, completed);
  const started = !solved && solvedCount(challenges, completed) > 0;
  return (
    <span className="inline-flex min-w-0 items-center gap-1">
      {solved && <span className="shrink-0 text-green-400 font-bold" title="Completed">✓</span>}
      {started && (
        <span
          className="h-2.5 w-2.5 shrink-0 rounded-full border border-green-400"
          title="Started"
        />
      )}
      <span className="truncate">{label}</span>
      <span className={countClassName}>({progressLabel(challenges, completed)}</span>
      <span className="text-coden-accent opacity-80">· LC {submissionProgressLabel(challenges, submitted)})</span>
    </span>
  );
}

function categoryPath(category: string): string[] {
  return [formatCategory(category)];
}

function entryForChallenge(challenge: ChallengeSummary, categoryContext?: string): PracticeExportEntry {
  return {
    id: challenge.id,
    path: categoryContext
      ? categoryContext.split('/').map((part) => part.trim()).filter(Boolean)
      : categoryPath(challenge.category),
  };
}

function uniqueEntries(entries: PracticeExportEntry[]): PracticeExportEntry[] {
  const seen = new Set<string>();
  const result: PracticeExportEntry[] = [];
  for (const entry of entries) {
    const key = `${entry.path.join('/')}/${entry.id}`;
    if (seen.has(key)) continue;
    seen.add(key);
    result.push(entry);
  }
  return result;
}

function makeGroup(id: string, label: string, order?: number): NavigationGroup {
  return { id, label, challenges: [], children: [], order };
}

function getOrCreateChild(parent: NavigationGroup, id: string, label: string, order?: number): NavigationGroup {
  let child = parent.children.find((item) => item.id === id);
  if (!child) {
    child = makeGroup(id, label, order);
    parent.children.push(child);
  } else if (order !== undefined) {
    child.order = Math.min(child.order ?? order, order);
  }
  return child;
}

function groupChallengesByLabel(
  challenges: ChallengeSummary[],
  labelFor: (challenge: ChallengeSummary) => string,
  idPrefix: string,
): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  for (const challenge of challenges) {
    const label = labelFor(challenge);
    const id = `${idPrefix}:${label.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`;
    getOrCreateChild(root, id, label).challenges.push(challenge);
  }
  for (const child of root.children) {
    child.challenges = sortByDifficultyThenId(child.challenges);
  }
  return root.children.sort((left, right) => left.label.localeCompare(right.label));
}

function challengeCount(group: NavigationGroup): number {
  return uniqueChallengeIds(collectGroupChallenges(group)).size;
}

function sortLeetcodeCategoryNodes(groups: NavigationGroup[]): NavigationGroup[] {
  return groups.sort((left, right) => {
    const leftIndex = LEETCODE_CATEGORY_ORDER.indexOf(left.label);
    const rightIndex = LEETCODE_CATEGORY_ORDER.indexOf(right.label);
    const leftOrder = leftIndex === -1 ? Number.MAX_SAFE_INTEGER : leftIndex;
    const rightOrder = rightIndex === -1 ? Number.MAX_SAFE_INTEGER : rightIndex;
    if (leftOrder !== rightOrder) return leftOrder - rightOrder;
    return left.label.localeCompare(right.label);
  });
}

function sortLeetcodeTopicNodes(groups: NavigationGroup[]): NavigationGroup[] {
  return groups.sort((left, right) => {
    const leftOrder = TOPIC_ORDER_INDEX.get(left.label.toLowerCase()) ?? Number.MAX_SAFE_INTEGER;
    const rightOrder = TOPIC_ORDER_INDEX.get(right.label.toLowerCase()) ?? Number.MAX_SAFE_INTEGER;
    if (leftOrder !== rightOrder) return leftOrder - rightOrder;
    const countDifference = challengeCount(right) - challengeCount(left);
    if (countDifference !== 0) return countDifference;
    return left.label.localeCompare(right.label);
  });
}

function addChallengeToTopicGroups(parent: NavigationGroup, challenge: ChallengeSummary, idPrefix: string): void {
  for (const topic of challengeTopics(challenge)) {
    getOrCreateChild(parent, `${idPrefix}:topic:${topic.slug}`, topic.name).challenges.push(challenge);
  }
}

function buildCategoryGroups(challenges: ChallengeSummary[]): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  for (const challenge of challenges) {
    const category = leetcodeCategoryTitle(challenge);
    const categoryNode = getOrCreateChild(root, `leetcode-category:${slugKey(category)}`, category);
    addChallengeToTopicGroups(categoryNode, challenge, `leetcode-category:${slugKey(category)}`);
  }
  for (const categoryNode of root.children) {
    sortLeetcodeTopicNodes(categoryNode.children);
    for (const topicNode of categoryNode.children) {
      topicNode.challenges = sortByLeetcodeId(topicNode.challenges);
    }
  }
  return sortLeetcodeCategoryNodes(root.children);
}

function buildCompanyGroups(challenges: ChallengeSummary[]): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  const companyCounts = new Map<string, number>();
  for (const challenge of challenges) {
    for (const company of challengeCompanyTags(challenge)) {
      companyCounts.set(company.slug, (companyCounts.get(company.slug) ?? 0) + 1);
      const companyNode = getOrCreateChild(root, `company:${company.slug}`, company.name);
      const category = leetcodeCategoryTitle(challenge);
      const categoryNode = getOrCreateChild(
        companyNode,
        `company:${company.slug}:category:${slugKey(category)}`,
        category,
      );
      addChallengeToTopicGroups(categoryNode, challenge, `company:${company.slug}:category:${slugKey(category)}`);
    }
  }
  for (const companyNode of root.children) {
    sortLeetcodeCategoryNodes(companyNode.children);
    for (const categoryNode of companyNode.children) {
      sortLeetcodeTopicNodes(categoryNode.children);
      for (const topicNode of categoryNode.children) {
        topicNode.challenges = sortByLeetcodeId(topicNode.challenges);
      }
    }
  }
  return root.children.sort((left, right) => {
    const leftCount = companyCounts.get(left.id.replace(/^company:/, '')) ?? 0;
    const rightCount = companyCounts.get(right.id.replace(/^company:/, '')) ?? 0;
    if (leftCount !== rightCount) return rightCount - leftCount;
    return left.label.localeCompare(right.label);
  });
}

function buildStudyPlanGroups(challenges: ChallengeSummary[]): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  for (const challenge of challenges) {
    for (const membership of studyPlanMemberships(challenge)) {
      let current = getOrCreateChild(root, `study:${membership.planSlug}`, membership.planName);
      membership.path.forEach((part, index) => {
        current = getOrCreateChild(
          current,
          `study:${membership.planSlug}:${index}:${part}`,
          part,
          index === 0 ? membership.sectionOrder : index + 1,
        );
      });
      current.challenges.push(challenge);
    }
  }
  const sortRecursive = (group: NavigationGroup) => {
    group.children.sort((left, right) => {
      const byOrder = (left.order ?? Number.MAX_SAFE_INTEGER) - (right.order ?? Number.MAX_SAFE_INTEGER);
      if (byOrder !== 0) return byOrder;
      return left.label.localeCompare(right.label);
    });
    group.challenges = [...group.challenges].sort((left, right) => {
      const leftMembership = studyPlanMemberships(left).find((membership) => group.id.startsWith(`study:${membership.planSlug}`));
      const rightMembership = studyPlanMemberships(right).find((membership) => group.id.startsWith(`study:${membership.planSlug}`));
      const byOrder = (leftMembership?.order ?? 0) - (rightMembership?.order ?? 0);
      if (byOrder !== 0) return byOrder;
      return leetcodeProblemOrder(left) - leetcodeProblemOrder(right);
    });
    group.children.forEach(sortRecursive);
  };
  root.children.forEach(sortRecursive);
  if (root.children.length === 0) {
    return [{
      id: 'studyplan:missing',
      label: 'Official Study Plans',
      challenges: [],
      children: [],
      emptyMessage: 'No official study-plan metadata is synced yet.',
    }];
  }
  return root.children;
}

function buildNeetcodeGroups(challenges: ChallengeSummary[]): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  for (const challenge of challenges) {
    for (const membership of neetcodeMemberships(challenge)) {
      let current = getOrCreateChild(
        root,
        `neetcode:${membership.subsetSlug}`,
        membership.subsetName,
        membership.subsetOrder,
      );
      membership.path.forEach((part, index) => {
        current = getOrCreateChild(
          current,
          `neetcode:${membership.subsetSlug}:${index}:${part}`,
          part,
          index === 0 ? membership.sectionOrder : index + 1,
        );
      });
      current.challenges.push(challenge);
    }
  }
  const sortRecursive = (group: NavigationGroup) => {
    group.children.sort((left, right) => {
      const byOrder = (left.order ?? Number.MAX_SAFE_INTEGER) - (right.order ?? Number.MAX_SAFE_INTEGER);
      if (byOrder !== 0) return byOrder;
      return left.label.localeCompare(right.label);
    });
    group.challenges = [...group.challenges].sort((left, right) => {
      const leftMembership = neetcodeMemberships(left).find((membership) => group.id.startsWith(`neetcode:${membership.subsetSlug}`));
      const rightMembership = neetcodeMemberships(right).find((membership) => group.id.startsWith(`neetcode:${membership.subsetSlug}`));
      const bySection = (leftMembership?.sectionOrder ?? 0) - (rightMembership?.sectionOrder ?? 0);
      if (bySection !== 0) return bySection;
      return (leftMembership?.order ?? 0) - (rightMembership?.order ?? 0);
    });
    group.children.forEach(sortRecursive);
  };
  root.children.forEach(sortRecursive);
  return root.children.sort((left, right) => {
    const byOrder = (left.order ?? Number.MAX_SAFE_INTEGER) - (right.order ?? Number.MAX_SAFE_INTEGER);
    if (byOrder !== 0) return byOrder;
    return left.label.localeCompare(right.label);
  });
}

function buildAlgomasterGroups(challenges: ChallengeSummary[]): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  for (const challenge of challenges) {
    for (const membership of algomasterMemberships(challenge)) {
      let current = getOrCreateChild(
        root,
        `algomaster:${membership.subsetSlug}`,
        membership.subsetName,
        membership.subsetOrder,
      );
      membership.path.forEach((part, index) => {
        current = getOrCreateChild(
          current,
          `algomaster:${membership.subsetSlug}:${index}:${part}`,
          part,
          index === 0 ? membership.sectionOrder : index + 1,
        );
      });
      current.challenges.push(challenge);
    }
  }
  const sortRecursive = (group: NavigationGroup) => {
    group.children.sort((left, right) => {
      const byOrder = (left.order ?? Number.MAX_SAFE_INTEGER) - (right.order ?? Number.MAX_SAFE_INTEGER);
      if (byOrder !== 0) return byOrder;
      return left.label.localeCompare(right.label);
    });
    group.challenges = [...group.challenges].sort((left, right) => {
      const leftMembership = algomasterMemberships(left).find((membership) => (
        group.id.startsWith(`algomaster:${membership.subsetSlug}`)
      ));
      const rightMembership = algomasterMemberships(right).find((membership) => (
        group.id.startsWith(`algomaster:${membership.subsetSlug}`)
      ));
      const byOrder = (leftMembership?.order ?? 0) - (rightMembership?.order ?? 0);
      if (byOrder !== 0) return byOrder;
      return leetcodeProblemOrder(left) - leetcodeProblemOrder(right);
    });
    group.children.forEach(sortRecursive);
  };
  root.children.forEach(sortRecursive);
  return root.children.sort((left, right) => {
    const byOrder = (left.order ?? Number.MAX_SAFE_INTEGER) - (right.order ?? Number.MAX_SAFE_INTEGER);
    if (byOrder !== 0) return byOrder;
    return left.label.localeCompare(right.label);
  });
}

function studyPlanLeafGroupId(membership: ReturnType<typeof studyPlanMemberships>[number]): string {
  let id = `study:${membership.planSlug}`;
  membership.path.forEach((part, index) => {
    id += `:${index}:${part}`;
  });
  return id;
}

function neetcodeLeafGroupId(membership: ReturnType<typeof neetcodeMemberships>[number]): string {
  let id = `neetcode:${membership.subsetSlug}`;
  membership.path.forEach((part, index) => {
    id += `:${index}:${part}`;
  });
  return id;
}

type CareerSequenceItem = {
  challenge: ChallengeSummary;
  order: number;
};

function buildCareerUnlockMap(
  challenges: ChallengeSummary[],
  activeSet: string,
  completed: Set<string>,
): Map<string, Set<string>> {
  if (activeSet !== 'leetcode_studyplan' && activeSet !== 'neetcode') {
    return new Map();
  }

  const sequences = new Map<string, CareerSequenceItem[]>();
  for (const challenge of challenges) {
    if (activeSet === 'leetcode_studyplan') {
      for (const membership of studyPlanMemberships(challenge)) {
        const key = studyPlanLeafGroupId(membership);
        sequences.set(key, [
          ...(sequences.get(key) ?? []),
          {
            challenge,
            order: resolveCareerSequenceOrder(membership.order, leetcodeProblemOrder(challenge)),
          },
        ]);
      }
    }
    if (activeSet === 'neetcode') {
      for (const membership of neetcodeMemberships(challenge)) {
        const key = neetcodeLeafGroupId(membership);
        sequences.set(key, [
          ...(sequences.get(key) ?? []),
          {
            challenge,
            order: resolveCareerSequenceOrder(membership.order, leetcodeProblemOrder(challenge)),
          },
        ]);
      }
    }
  }

  const result = new Map<string, Set<string>>();
  for (const [key, items] of sequences) {
    const unlocked = buildUnlockedCareerSequence(
      items.map((item) => ({
        challengeId: item.challenge.id,
        order: item.order,
        fallbackOrder: leetcodeProblemOrder(item.challenge),
      })),
      completed,
    );
    result.set(key, unlocked);
  }
  return result;
}

function buildNavigationGroups(
  challenges: ChallengeSummary[],
  activeSet: string,
): NavigationGroup[] {
  if (activeSet === 'leetcode') {
    return buildCategoryGroups(challenges);
  }
  if (activeSet === 'leetcode_company') {
    return buildCompanyGroups(challenges);
  }
  if (activeSet === 'leetcode_studyplan') {
    return buildStudyPlanGroups(challenges);
  }
  if (activeSet === 'neetcode') {
    return buildNeetcodeGroups(challenges);
  }
  if (activeSet === 'algomaster') {
    return buildAlgomasterGroups(challenges);
  }
  return groupChallengesByLabel(challenges, (challenge) => formatCategory(challenge.category), 'category');
}

function collectGroupChallenges(group: NavigationGroup): ChallengeSummary[] {
  const result = [...group.challenges];
  for (const child of group.children) {
    result.push(...collectGroupChallenges(child));
  }
  return result;
}

function numberKey(context: string, challengeId: string): string {
  return `${context}::${challengeId}`;
}

function numericLeetcodeId(challenge: ChallengeSummary): number | null {
  const fromField = Number(challenge.leetcode_frontend_id);
  if (Number.isFinite(fromField) && fromField > 0) return fromField;
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? Number(match[1]) : null;
}

function numberingContextsForChallenge(_challenge: ChallengeSummary, activeSet: string): string[] {
  return [activeSet];
}

function numberingContextForDisplay(
  _challenge: ChallengeSummary,
  activeSet: string,
  _categoryContext?: string,
): string {
  return activeSet;
}

function buildChallengeNumberMap(
  challenges: ChallengeSummary[],
  activeSet: string,
): Map<string, ChallengeNumber> {
  const insertionOrder = new Map(challenges.map((challenge, index) => [challenge.id, index]));
  const byContext = new Map<string, Map<string, ChallengeSummary>>();
  for (const challenge of challenges) {
    for (const context of numberingContextsForChallenge(challenge, activeSet)) {
      const contextItems = byContext.get(context) ?? new Map<string, ChallengeSummary>();
      if (!contextItems.has(challenge.id)) {
        contextItems.set(challenge.id, challenge);
      }
      byContext.set(context, contextItems);
    }
  }

  const numbers = new Map<string, ChallengeNumber>();
  for (const [context, contextItems] of byContext) {
    const ordered = Array.from(contextItems.values());
    ordered.sort((left, right) => {
      if (isLeetcodeUniverse(activeSet)) {
        const leftId = numericLeetcodeId(left);
        const rightId = numericLeetcodeId(right);
        if (leftId !== null && rightId !== null && leftId !== rightId) return leftId - rightId;
        if (leftId !== null && rightId === null) return -1;
        if (leftId === null && rightId !== null) return 1;
      }
      return (insertionOrder.get(left.id) ?? 0) - (insertionOrder.get(right.id) ?? 0);
    });

    const largestLeetcodeId = isLeetcodeUniverse(activeSet)
      ? Math.max(...ordered.map((challenge) => numericLeetcodeId(challenge) ?? 0), 0)
      : 0;
    const width = Math.max(
      3,
      String(isLeetcodeUniverse(activeSet) ? largestLeetcodeId : ordered.length).length,
    );

    ordered.forEach((challenge, index) => {
      const leetcodeId = isLeetcodeUniverse(activeSet) ? numericLeetcodeId(challenge) : null;
      const rawNumber = leetcodeId ?? index + 1;
      numbers.set(numberKey(context, challenge.id), {
        display: String(rawNumber),
        filename: String(rawNumber).padStart(width, '0'),
      });
    });
  }
  return numbers;
}

function DownloadIcon({ className = "h-4 w-4" }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      viewBox="0 0 20 20"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M10 3.5v8" />
      <path d="m6.75 8.75 3.25 3.25 3.25-3.25" />
      <path d="M4 14.5v1.25A1.75 1.75 0 0 0 5.75 17.5h8.5A1.75 1.75 0 0 0 16 15.75V14.5" />
    </svg>
  );
}

function StatusTick({ complete, color }: { complete: boolean; color: string }) {
  return (
    <span
      aria-hidden="true"
      className={`text-sm font-black leading-none ${complete ? '' : 'text-slate-500 opacity-[0.38]'}`}
      style={complete ? { color } : undefined}
    >
      ✓
    </span>
  );
}

function SendIcon({ className = "h-4 w-4" }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      viewBox="0 0 20 20"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M10 13.5v-10" />
      <path d="m6.5 7 3.5-3.5L13.5 7" />
      <path d="M4 11.5v3.75A1.75 1.75 0 0 0 5.75 17h8.5A1.75 1.75 0 0 0 16 15.25V11.5" />
    </svg>
  );
}

function formatBytes(value: number): string {
  if (value < 1024) return `${value} B`;
  if (value < 1024 * 1024) return `${(value / 1024).toFixed(1)} KB`;
  return `${(value / 1024 / 1024).toFixed(1)} MB`;
}

/**
 * ChallengeList — left rail with one row per challenge.
 *
 * Each row shows the human title (e.g. "Bubble Sort") as the
 * primary label, full-width. The complexity class sits in a
 * tooltip / on a second line below the title for narrow panes.
 * LeetCode rows prefix the human title with their numeric problem id;
 * other datasets keep showing only the human title. The internal machine
 * id remains available in the detail panel header and tooltip.
 * The engine runner and verifier handle every spec the
 * registry exposes, so all challenges are clickable.
 */
export function ChallengeList() {
  const challenges = useAppStore((s) => s.challenges);
  const challengesLoading = useAppStore((s) => s.challengesLoading);
  const challengesError = useAppStore((s) => s.challengesError);
  const loadChallenges = useAppStore((s) => s.loadChallenges);
  const currentId = useAppStore((s) => s.currentDetail?.id ?? null);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const loadProgress = useAppStore((s) => s.loadProgress);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const leetcodeSubmissions = useAppStore((s) => s.progress?.leetcode_submissions ?? {});
  const activeSet = useAppStore((s) => s.activeSet);

  const [searchQuery, setSearchQuery] = useState('');
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});
  const [downloadState, setDownloadState] = useState<DownloadState | null>(null);
  const [submittingChallengeId, setSubmittingChallengeId] = useState<string | null>(null);
  const [submissionNotice, setSubmissionNotice] = useState<SubmissionNotice | null>(null);
  const completedSet = useMemo(() => new Set(completed), [completed]);
  const submittedSet = useMemo(() => new Set(Object.keys(leetcodeSubmissions)), [leetcodeSubmissions]);

  const toggleCategory = (category: string) => {
    setExpanded((prev) => ({ ...prev, [category]: !prev[category] }));
  };


  const filteredChallenges = useMemo(() => {
    let baseList = challengesForAlgorithmSet(challenges, activeSet);

    if (isLeetcodeUniverse(activeSet) && difficultyFilter !== 'all') {
      baseList = baseList.filter((challenge) => challenge.difficulty_label === difficultyFilter);
    }

    if (!searchQuery.trim()) return baseList;
    const lowerQ = searchQuery.toLowerCase();
    return baseList.filter(c => 
      c.name.toLowerCase().includes(lowerQ) || 
      c.id.toLowerCase().includes(lowerQ) ||
      c.category.toLowerCase().includes(lowerQ) ||
      c.categories.some((category) => category.toLowerCase().includes(lowerQ)) ||
      c.leetcode_category_title.toLowerCase().includes(lowerQ) ||
      c.leetcode_topics.some((topic) => stringField(topic.name).toLowerCase().includes(lowerQ) || stringField(topic.slug).toLowerCase().includes(lowerQ)) ||
      c.leetcode_company_tags.some((company) => stringField(company.name).toLowerCase().includes(lowerQ) || stringField(company.slug).toLowerCase().includes(lowerQ)) ||
      c.leetcode_subsets.some((subset) => subset.toLowerCase().includes(lowerQ)) ||
      c.leetcode_tags.some((tag) => tag.toLowerCase().includes(lowerQ)) ||
      c.leetcode_external_subsets.some((membership) => (
        stringField(membership.subset_name).toLowerCase().includes(lowerQ)
        || stringField(membership.subset_slug).toLowerCase().includes(lowerQ)
        || (Array.isArray(membership.path)
          && membership.path.some((part) => String(part).toLowerCase().includes(lowerQ)))
      )) ||
      (c.elo_rating !== null && (
        Math.round(c.elo_rating).toString() === lowerQ
        || `elo ${Math.round(c.elo_rating)}`.includes(lowerQ)
      )) ||
      (c.difficulty_estimate !== null && (
        c.difficulty_estimate.toString() === lowerQ
        || `estimated ${c.difficulty_estimate}`.includes(lowerQ)
        || `legacy ${c.difficulty_estimate}`.includes(lowerQ)
      )) ||
      c.difficulty_label.toLowerCase().includes(lowerQ)
    );
  }, [challenges, searchQuery, activeSet, difficultyFilter]);

  const navigationGroups = useMemo(
    () => buildNavigationGroups(filteredChallenges, activeSet),
    [filteredChallenges, activeSet],
  );

  const careerUnlocks = useMemo(
    () => buildCareerUnlockMap(challenges, activeSet, completedSet),
    [challenges, activeSet, completedSet],
  );

  const challengeNumbers = useMemo(
    () => buildChallengeNumberMap(challenges, activeSet),
    [challenges, activeSet],
  );

  const numberForChallenge = (challenge: ChallengeSummary, categoryContext?: string) => {
    const context = numberingContextForDisplay(challenge, activeSet, categoryContext);
    return challengeNumbers.get(numberKey(context, challenge.id));
  };

  const exportEntryFor = (challenge: ChallengeSummary, categoryContext?: string): PracticeExportEntry => {
    const challengeNumber = numberForChallenge(challenge, categoryContext);
    return {
      ...entryForChallenge(challenge, categoryContext),
      filename_prefix: challengeNumber?.filename,
    };
  };

  const exportEntryForPath = (challenge: ChallengeSummary, path: string[]): PracticeExportEntry => {
    const context = path.join('/');
    const challengeNumber = numberForChallenge(challenge, context);
    return {
      id: challenge.id,
      path,
      filename_prefix: challengeNumber?.filename,
    };
  };

  const entriesForGroup = (group: NavigationGroup, path: string[]): PracticeExportEntry[] => {
    const direct = group.challenges.map((challenge) => exportEntryForPath(challenge, path));
    const nested = group.children.flatMap((child) => entriesForGroup(child, [...path, child.label]));
    return [...direct, ...nested];
  };

  const updateDownloadProgress = (label: string) => (progress: DownloadProgress) => {
    setDownloadState({
      label,
      loaded: progress.loaded,
      total: progress.total,
      percent: progress.percent,
      status: 'active',
    });
  };

  const finishDownload = (label: string) => {
    setDownloadState({
      label,
      loaded: 0,
      total: null,
      percent: 100,
      status: 'done',
      message: 'Download ready',
    });
    window.setTimeout(() => setDownloadState(null), 2500);
  };

  const failDownload = (label: string, error: unknown) => {
    setDownloadState({
      label,
      loaded: 0,
      total: null,
      percent: null,
      status: 'error',
      message: error instanceof Error ? error.message : 'Download failed',
    });
  };

  const handleDownloadChallenge = async (
    event: React.MouseEvent,
    challenge: ChallengeSummary,
    categoryContext?: string,
  ) => {
    event.stopPropagation();
    const challengeNumber = numberForChallenge(challenge, categoryContext);
    const label = `Downloading ${challenge.name}`;
    setDownloadState({
      label,
      loaded: 0,
      total: null,
      percent: null,
      status: 'active',
      message: 'Preparing file...',
    });
    try {
      await downloadChallengePracticeFile(
        challenge.id,
        challengeNumber?.filename,
        updateDownloadProgress(label),
      );
      finishDownload(label);
    } catch (error) {
      failDownload(label, error);
    }
  };

  const handleDownloadBundle = async (
    event: React.MouseEvent,
    entries: PracticeExportEntry[],
  ) => {
    event.stopPropagation();
    const unique = uniqueEntries(entries);
    const label = `Downloading ${unique.length} file${unique.length === 1 ? '' : 's'}`;
    setDownloadState({
      label,
      loaded: 0,
      total: null,
      percent: null,
      status: 'active',
      message: 'Preparing archive...',
    });
    try {
      await downloadPracticeBundle(
        unique,
        updateDownloadProgress(label),
      );
      finishDownload(label);
    } catch (error) {
      failDownload(label, error);
    }
  };

  const handleLeetCodeSubmit = async (event: React.MouseEvent, challenge: ChallengeSummary) => {
    event.stopPropagation();
    if (!completed.includes(challenge.id)) {
      setSubmissionNotice({ status: 'error', message: `${challenge.name}: complete the full cOde(n) judge first.` });
      return;
    }
    if (challenge.leetcode_submission_status !== 'verified') {
      setSubmissionNotice({ status: 'error', message: `${challenge.name}: no remotely verified LeetCode submission is packaged yet.` });
      return;
    }
    if (!window.electronAPI) {
      setSubmissionNotice({ status: 'error', message: 'Direct LeetCode submission is available in the desktop app.' });
      return;
    }
    setSubmittingChallengeId(challenge.id);
    setSubmissionNotice({ status: 'active', message: `${challenge.name}: checking the LeetCode session…` });
    try {
      const session = await window.electronAPI.getLeetCodeSessionStatus();
      if (session.state !== 'valid') throw new Error(session.message || 'Refresh the LeetCode session in Settings.');
      if (challenge.leetcode_submission_paid_only && !session.is_premium) {
        throw new Error('This problem requires LeetCode Premium access for the connected account.');
      }
      setSubmissionNotice({ status: 'active', message: `${challenge.name}: submitting the reviewed ${challenge.leetcode_submission_language || 'LeetCode'} solution…` });
      const result = await window.electronAPI.submitVerifiedToLeetCode(challenge.id);
      if (!result.accepted) throw new Error(result.message);
      await loadProgress();
      setSubmissionNotice({ status: 'done', message: `${challenge.name}: Accepted by LeetCode · submission ${result.submission_id}` });
    } catch (error) {
      setSubmissionNotice({ status: 'error', message: `${challenge.name}: ${error instanceof Error ? error.message : String(error)}` });
    } finally {
      setSubmittingChallengeId(null);
    }
  };

  const renderChallengeRow = (c: ChallengeSummary, categoryContext?: string, groupId?: string) => {
    const isCurrent = c.id === currentId;
    const isDone = completed.includes(c.id);
    const isSubmitted = Boolean(leetcodeSubmissions[c.id]);
    const isSubmitting = submittingChallengeId === c.id;
    const hasVerifiedSubmission = c.leetcode_submission_status === 'verified';
    const submitTitle = isSubmitted
      ? `Accepted on LeetCode · submission ${leetcodeSubmissions[c.id].submission_id}`
      : !isDone
        ? 'Complete the full cOde(n) judge before submitting to LeetCode'
        : !hasVerifiedSubmission
          ? 'Submission blocked: no remotely verified LeetCode artifact is packaged for this problem'
          : `Send the reviewed ${c.leetcode_submission_language || 'platform-native'} solution to LeetCode`;
    const contextUnlocked = groupId ? careerUnlocks.get(groupId)?.has(c.id) : undefined;
    const isLocked = contextUnlocked === undefined ? !c.unlocked : !contextUnlocked;
    const displayTitle = formatChallengeTitle(c, activeSet, numberForChallenge(c, categoryContext));
    const difficultyDisplay = formatDifficultyLine(c, activeSet);

    return (
      <li key={c.id} className="flex items-stretch gap-1">
        <div className="inline-flex w-9 shrink-0 items-center justify-center gap-0.5" aria-label="Problem completion status">
          <span title={isDone ? 'Completed in cOde(n) by at least one version' : 'Not yet completed in cOde(n)'}>
            <StatusTick complete={isDone} color="#4ade80" />
          </span>
          <span title={isSubmitted ? submitTitle : 'Not yet Accepted on LeetCode'}>
            <StatusTick complete={isSubmitted} color="var(--coden-accent)" />
          </span>
        </div>
        <button
          type="button"
          onClick={() => !isLocked && selectChallenge(c.id)}
          disabled={isLocked}
          className={[
            'flex-1 min-w-0 text-left px-2 py-1.5 rounded text-sm',
            'flex items-center gap-2',
            isLocked
              ? 'opacity-40 cursor-not-allowed'
              : 'hover:bg-coden-border transition-colors duration-150',
            isCurrent
              ? 'bg-sky-100 text-slate-950 ring-1 ring-sky-300 shadow-inner dark:bg-coden-border dark:text-coden-text dark:ring-0'
              : 'text-coden-text',
          ].join(' ')}
          title={isLocked ? "Locked in Career Mode (complete the previous task in this sequence first)" : `${c.name} · ${c.required_complexity} · ${c.id}`}
        >
          {isLocked && <span className="text-coden-muted shrink-0 text-xs" title="Locked in this career sequence">◆</span>}
          <div className="flex-1 min-w-0">
            <div className="truncate">{displayTitle}</div>
            <div
              className={[
                'text-[11px] font-mono truncate mt-0.5',
                isCurrent
                  ? 'text-slate-600 dark:text-coden-muted'
                  : 'text-coden-muted opacity-80',
              ].join(' ')}
              title={c.elo_rating !== null
                ? 'Contest Elo from ZeroTrac; displayed as a rounded whole number'
                : c.difficulty_estimate !== null
                  ? 'Legacy Weekly Contest 1-62 fallback, estimated from the acceptance-rate percentile within the official LeetCode difficulty tier'
                  : 'Official LeetCode difficulty'}
            >
              {difficultyDisplay}
            </div>
          </div>
        </button>
        <button
          type="button"
          onClick={(event) => void handleLeetCodeSubmit(event, c)}
          disabled={isSubmitted || isSubmitting || !isDone || !hasVerifiedSubmission || isLocked}
          className={[
            'w-7 rounded shrink-0 inline-flex items-center justify-center transition-colors',
            isSubmitted
              ? 'cursor-default text-coden-accent opacity-35'
              : isDone && hasVerifiedSubmission && !isLocked
                ? 'cursor-pointer text-coden-accent hover:bg-coden-accent/10'
                : 'cursor-not-allowed text-coden-muted opacity-25',
          ].join(' ')}
          title={submitTitle}
          aria-label={submitTitle}
        >
          <SendIcon className={`h-4 w-4 ${isSubmitting ? 'animate-pulse' : ''}`} />
        </button>
        <button
          type="button"
          onClick={(event) => handleDownloadChallenge(event, c, categoryContext)}
          className="w-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
          title={`Download standalone practice file for ${c.name}`}
          aria-label={`Download ${c.name}`}
        >
          <DownloadIcon className="h-4 w-4" />
        </button>
      </li>
    );
  };

  const renderGroup = (group: NavigationGroup, depth = 0, parentPath: string[] = []) => {
    const path = [...parentPath, group.label];
    const context = path.join('/');
    const groupChallenges = collectGroupChallenges(group);
    const isCollapsed = group.emptyMessage ? false : !searchQuery.trim() && !expanded[group.id];
    const groupEntries = entriesForGroup(group, path);
    const leftPadding = depth === 0 ? '' : depth === 1 ? 'ml-3' : 'ml-5';

    return (
      <Fragment key={group.id}>
        <div className={['mb-2', leftPadding].join(' ')}>
          <div className="flex items-center gap-1">
            <button
              onClick={() => toggleCategory(group.id)}
              className="flex-1 min-w-0 flex items-center justify-between px-2 py-1.5 text-xs leading-5 text-coden-muted font-semibold hover:text-coden-text transition-colors group select-none"
            >
              {progressHeading(group.label, groupChallenges, completedSet, submittedSet, "ml-1 opacity-60")}
              <span
                className="transform transition-transform duration-200 group-hover:text-coden-accent text-[10px]"
              >
                {isCollapsed ? '>' : 'v'}
              </span>
            </button>
            {groupEntries.length > 0 && (
              <button
                type="button"
                onClick={(event) => handleDownloadBundle(event, groupEntries)}
                className="w-7 h-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
                title={`Download ${group.label}`}
                aria-label={`Download ${group.label}`}
              >
                <DownloadIcon className="h-4 w-4" />
              </button>
            )}
          </div>

          {!isCollapsed && group.emptyMessage && (
            <div className="px-2 py-2 text-[11px] text-coden-muted">
              {group.emptyMessage}
            </div>
          )}

          {!isCollapsed && (
            <div className="mt-1">
              {group.children.map((child) => renderGroup(child, depth + 1, path))}
              {group.challenges.length > 0 && (
                <ul className="space-y-0.5">
                  {group.challenges.map((challenge) => renderChallengeRow(challenge, context, group.id))}
                </ul>
              )}
            </div>
          )}
        </div>
      </Fragment>
    );
  };

  return (
    <div className="flex flex-col h-full overflow-hidden">
      <div className="p-3 shrink-0 border-b border-coden-border bg-coden-surface">
        <input 
          type="text" 
          placeholder="Search challenges"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          disabled={challengesLoading && challenges.length === 0}
          className="w-full bg-coden-bg border border-coden-border rounded px-3 py-1.5 text-sm text-coden-text placeholder-coden-muted focus:outline-none focus:border-coden-accent transition-colors"
        />
        {isLeetcodeUniverse(activeSet) && (
          <select
            aria-label="Filter by difficulty"
            value={difficultyFilter}
            onChange={(event) => {
              setDifficultyFilter(event.target.value);
              setExpanded({});
            }}
            className="mt-2 w-full bg-coden-bg border border-coden-border rounded px-3 py-1.5 text-sm text-coden-text focus:outline-none focus:border-coden-accent transition-colors"
          >
            <option value="all">All difficulty levels</option>
            <option value="Easy">Easy</option>
            <option value="Medium">Medium</option>
            <option value="Hard">Hard</option>
          </select>
        )}
        <div className="mt-2 text-[11px] font-mono text-coden-muted">
          {challengesLoading && challenges.length === 0
            ? 'Preparing challenge library...'
            : `${progressLabel(filteredChallenges, completedSet)} solved · ${submissionProgressLabel(filteredChallenges, submittedSet)} LeetCode accepted`}
          {filteredChallenges.length !== challenges.length && (
            <> · {filteredChallenges.length} of {challenges.length} shown</>
          )}
        </div>
        <div className="mt-2 flex justify-end text-[11px]">
          <button
            type="button"
            onClick={(event) => handleDownloadBundle(
              event,
              filteredChallenges.map((challenge) => exportEntryFor(challenge)),
            )}
            className="h-7 px-2 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border inline-flex items-center gap-1"
            disabled={challengesLoading || filteredChallenges.length === 0}
            title="Download all currently shown challenges with every authored validated case"
          >
            <DownloadIcon className="h-3.5 w-3.5" />
            <span>all</span>
          </button>
        </div>
        {downloadState && (
          <div className="mt-2 rounded border border-coden-border bg-coden-bg/60 px-2 py-1.5">
            <div className="flex items-center justify-between gap-2 text-[11px] text-coden-muted">
              <span
                className={[
                  'truncate',
                  downloadState.status === 'error' ? 'text-red-400' : '',
                  downloadState.status === 'done' ? 'text-green-400' : '',
                ].join(' ')}
              >
                {downloadState.message ?? downloadState.label}
              </span>
              <span className="shrink-0 font-mono">
                {downloadState.status === 'active' && downloadState.percent === null && downloadState.loaded === 0
                  ? 'preparing'
                  : downloadState.percent !== null
                  ? `${Math.round(downloadState.percent)}%`
                  : downloadState.total
                    ? `${formatBytes(downloadState.loaded)} / ${formatBytes(downloadState.total)}`
                    : formatBytes(downloadState.loaded)}
              </span>
            </div>
            <div className="mt-1 h-1.5 overflow-hidden rounded-full bg-coden-border">
              <div
                className={[
                  'h-full rounded-full transition-all duration-150',
                  downloadState.status === 'error'
                    ? 'bg-red-400'
                    : downloadState.status === 'done'
                      ? 'bg-green-400'
                      : 'bg-coden-accent',
                  downloadState.status === 'active' && downloadState.percent === null ? 'animate-pulse' : '',
                ].join(' ')}
                style={{
                  width: downloadState.percent === null
                    ? '45%'
                    : `${Math.max(4, Math.min(100, downloadState.percent))}%`,
                }}
              />
            </div>
          </div>
        )}
      </div>
      
      <div className="flex-1 overflow-y-auto p-2 scrollbar-hide">
        {challengesLoading && challenges.length === 0 && (
          <div className="space-y-3 p-2" aria-label="Loading challenges">
            {[72, 88, 64, 80, 56].map((width, index) => (
              <div key={index} className="rounded border border-coden-border/60 bg-coden-surface/60 p-2">
                <div className="h-3 animate-pulse rounded bg-coden-border" style={{ width: `${width}%` }} />
                <div className="mt-2 h-2 animate-pulse rounded bg-coden-border/60" style={{ width: `${Math.max(32, width - 24)}%` }} />
              </div>
            ))}
            <p className="pt-1 text-center text-xs text-coden-muted">
              Loading the complete LeetCode library...
            </p>
          </div>
        )}
        {submissionNotice && (
          <div className={`mt-2 rounded border px-2 py-1.5 text-[11px] ${submissionNotice.status === 'done' ? 'border-coden-accent/40 bg-coden-accent/10 text-coden-accent' : submissionNotice.status === 'error' ? 'border-amber-500/40 bg-amber-500/10 text-amber-300' : 'border-coden-border bg-coden-bg/60 text-coden-muted'}`}>
            {submissionNotice.message}
          </div>
        )}

        {!challengesLoading && challengesError && (
          <div className="flex flex-col items-center justify-center gap-3 p-8 text-center text-coden-muted">
            <span className="text-sm text-red-400">Challenge library unavailable</span>
            <span className="text-xs">{challengesError}</span>
            <button
              type="button"
              onClick={() => void loadChallenges()}
              className="rounded border border-coden-border px-3 py-1.5 text-xs hover:bg-coden-border hover:text-coden-text"
            >
              Retry
            </button>
          </div>
        )}

        {!challengesLoading && !challengesError && navigationGroups.map((group) => renderGroup(group))}

        {!challengesLoading && !challengesError && navigationGroups.length === 0 && (
          <div className="flex flex-col items-center justify-center p-8 text-coden-muted space-y-2">
            <span className="text-sm">No algorithms found</span>
            <span className="text-xs">Try a name, id, or category.</span>
          </div>
        )}
      </div>
    </div>
  );
}
