import { Fragment, useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { useAppStore } from '../store/useAppStore';
import type {
  ChallengeSummary,
  CustomProblemSet,
  CustomProblemTreeNode,
} from '../types/api';
import { challengesForAlgorithmSet, getAlgorithmSetLabel } from '../lib/algorithmSets';
import { collectSetChallengeIds } from '../lib/customProblemSets';
import {
  buildCustomCareerUnlockMap,
  buildUnlockedCareerSequence,
  resolveCareerSequenceOrder,
} from '../lib/careerUnlocks';
import {
  calculateDirectEloAverage,
  calculateDirectFrequencyAverage,
  compareFrequencyPriority,
  eloDisplayForChallenge,
  type EloAverage,
  type FrequencyAverage,
} from '../lib/challengeMetrics';
import {
  buildPdfBundleFilename,
  exportChallengePdfBundle,
  type PdfTocNode,
} from './pdf/PdfBundleExport';
import {
  downloadChallengePracticeFile,
  downloadPracticeBundle,
  type DownloadProgress,
  type PracticeExportEntry,
} from '../api/practiceExport';
import {
  resetProgress,
  type ProgressResetScope,
} from '../api/progress';
import { CustomProblemSetBuilder } from './CustomProblemSetBuilder';

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

const ELO_HEAT_GREEN_LIMIT = 1200;
const ELO_HEAT_RED_LIMIT = 2400;
const ELO_HEAT_COLORS: ReadonlyArray<readonly [number, number, number]> = [
  [26, 152, 80],
  [102, 189, 99],
  [166, 217, 106],
  [217, 239, 139],
  [255, 255, 191],
  [254, 224, 139],
  [253, 174, 97],
  [244, 109, 67],
  [215, 48, 39],
];
const ELO_HEAT_SCALE_DESCRIPTION = 'Heat color is clamped: Elo 1200 and below is green; Elo 2400 and above is red.';

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
  orderedItems?: NavigationItem[];
  emptyMessage?: string;
  order?: number;
  careerMode?: boolean;
};

type NavigationItem =
  | { type: 'group'; group: NavigationGroup }
  | { type: 'problem'; challenge: ChallengeSummary; placementId: string };

type SubmissionNotice = {
  status: 'active' | 'done' | 'error';
  message: string;
};

type ProgressResetRequest = {
  scope: ProgressResetScope;
  challengeIds: string[];
  targetLabel: string;
};

const RESET_SCOPE_COPY: Record<ProgressResetScope, { label: string; description: string }> = {
  all: {
    label: 'All progress',
    description: 'Delete personal solutions and clear cOde(n) completions plus LeetCode acceptances.',
  },
  coden: {
    label: 'cOde(n) completions',
    description: 'Delete personal solutions and clear local completion marks plus result history.',
  },
  leetcode: {
    label: 'LeetCode acceptances',
    description: 'Clear stored Accepted submission marks only.',
  },
};

function isLeetcodeUniverse(activeSet: string): boolean {
  return activeSet === 'leetcode'
    || activeSet === 'elo'
    || activeSet === 'frequency'
    || activeSet === 'leetcode_company'
    || activeSet === 'leetcode_studyplan'
    || activeSet === 'neetcode'
    || activeSet === 'algomaster'
    || activeSet === 'custom';
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

function sortByEloAscending(items: ChallengeSummary[]): ChallengeSummary[] {
  return [...items].sort((left, right) => {
    if (left.elo_rating !== null && right.elo_rating !== null) {
      const byElo = left.elo_rating - right.elo_rating;
      if (byElo !== 0) return byElo;
    } else if (left.elo_rating !== null) {
      return -1;
    } else if (right.elo_rating !== null) {
      return 1;
    }
    return leetcodeProblemOrder(left) - leetcodeProblemOrder(right);
  });
}

function sortByFrequencyDescending(items: ChallengeSummary[]): ChallengeSummary[] {
  return [...items].sort((left, right) => {
    const byFrequencyAndElo = compareFrequencyPriority(left, right);
    if (byFrequencyAndElo !== 0) return byFrequencyAndElo;
    return leetcodeProblemOrder(left) - leetcodeProblemOrder(right);
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
    }
    return leetcodeProblemOrder(left) - leetcodeProblemOrder(right);
  });
}

function formatChallengeTitle(
  challenge: ChallengeSummary,
  number?: ChallengeNumber,
): string {
  return number ? `${number.display}. ${challenge.name}` : challenge.name;
}

function eloHeatColor(value: number): string {
  const position = Math.max(
    0,
    Math.min(
      1,
      (value - ELO_HEAT_GREEN_LIMIT) / (ELO_HEAT_RED_LIMIT - ELO_HEAT_GREEN_LIMIT),
    ),
  );
  const scaled = position * (ELO_HEAT_COLORS.length - 1);
  const lowerIndex = Math.floor(scaled);
  const upperIndex = Math.min(lowerIndex + 1, ELO_HEAT_COLORS.length - 1);
  const mix = scaled - lowerIndex;
  const lower = ELO_HEAT_COLORS[lowerIndex]!;
  const upper = ELO_HEAT_COLORS[upperIndex]!;
  const channel = (index: number) => Math.round(lower[index]! + (upper[index]! - lower[index]!) * mix);
  return `rgb(${channel(0)} ${channel(1)} ${channel(2)})`;
}

function eloAverageTitle(average: EloAverage): string {
  const estimateDetail = average.estimatedCount === 0
    ? 'All inputs are real contest Elo ratings.'
    : `${average.estimatedCount} ${average.estimatedCount === 1 ? 'problem uses' : 'problems use'} an official-difficulty and acceptance-rate Elo estimate.`;
  return `Direct mean: sum of ${average.problemCount} individual problem Elo values divided by ${average.problemCount} unique problems. ${estimateDetail} Child-group averages are not used. ${ELO_HEAT_SCALE_DESCRIPTION}`;
}

function frequencyAverageTitle(average: FrequencyAverage): string {
  return `Direct mean: sum of ${average.problemCount} individual LeetCode Frequency values divided by ${average.problemCount} unique problems. Zero-frequency problems are included. Child-group averages are not used.`;
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
  eloAverage: EloAverage | null,
  frequencyAverage: FrequencyAverage | null,
  careerMode = false,
) {
  const solved = isFullySolved(challenges, completed);
  const started = !solved && solvedCount(challenges, completed) > 0;
  const solvedProgress = progressLabel(challenges, completed);
  const submittedProgress = submissionProgressLabel(challenges, submitted);
  return (
    <span className="flex min-w-0 flex-1 flex-col items-start text-left">
      <span className="flex w-full min-w-0 items-center gap-1">
        {solved && <span className="shrink-0 text-green-400 font-bold" title="Completed">✓</span>}
        {started && (
          <span
            className="h-2.5 w-2.5 shrink-0 rounded-full border border-green-400"
            title="Started"
          />
        )}
        <span className="min-w-0 truncate">{label}</span>
        <span className="shrink-0 font-mono text-[10px] font-normal text-coden-muted">
          · {solvedProgress} solved
        </span>
        <span className="shrink-0 font-mono text-[10px] font-normal text-coden-accent opacity-80">
          · LC {submittedProgress}
        </span>
        {careerMode && (
          <span className="shrink-0 rounded border border-coden-accent/40 px-1 py-0.5 font-mono text-[9px] text-coden-accent">
            Career
          </span>
        )}
      </span>
      <span className="mt-0.5 flex min-h-4 items-center gap-1 pl-4 font-mono text-[10px] font-normal">
        {eloAverage !== null && (
          <span
            className="shrink-0"
            style={{ color: eloHeatColor(eloAverage.value) }}
            title={eloAverageTitle(eloAverage)}
          >
            Avg Elo{eloAverage.estimatedCount > 0 ? ' ~' : ' '}{Math.round(eloAverage.value)}
          </span>
        )}
        {eloAverage !== null && frequencyAverage !== null && (
          <span className="text-coden-muted opacity-60" aria-hidden="true">·</span>
        )}
        {frequencyAverage !== null && (
          <span
            className="shrink-0 text-coden-accent"
            title={frequencyAverageTitle(frequencyAverage)}
          >
            Avg Freq {frequencyAverage.value.toFixed(1)}%
          </span>
        )}
        {eloAverage === null && frequencyAverage === null && (
          <span className="text-coden-muted">Average metrics unavailable</span>
        )}
      </span>
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

function buildEloGroups(challenges: ChallengeSummary[]): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  for (const challenge of challenges) {
    if (challenge.elo_rating === null) continue;
    addChallengeToTopicGroups(root, challenge, 'elo');
  }
  sortLeetcodeTopicNodes(root.children);
  for (const topicNode of root.children) {
    topicNode.challenges = sortByEloAscending(topicNode.challenges);
  }
  return root.children;
}

function buildFrequencyGroups(challenges: ChallengeSummary[]): NavigationGroup[] {
  const root = makeGroup('root', 'root');
  for (const challenge of challenges) {
    if (challenge.frequency === null) continue;
    addChallengeToTopicGroups(root, challenge, 'frequency');
  }
  sortLeetcodeTopicNodes(root.children);
  for (const topicNode of root.children) {
    topicNode.challenges = sortByFrequencyDescending(topicNode.challenges);
  }
  return root.children;
}

function buildCustomGroups(
  challenges: ChallengeSummary[],
  customSets: CustomProblemSet[],
): NavigationGroup[] {
  const challengeById = new Map(challenges.map((challenge) => [challenge.id, challenge]));

  const convertNodes = (
    nodes: CustomProblemTreeNode[],
  ): {
    challenges: ChallengeSummary[];
    children: NavigationGroup[];
    orderedItems: NavigationItem[];
  } => {
    const directChallenges: ChallengeSummary[] = [];
    const children: NavigationGroup[] = [];
    const orderedItems: NavigationItem[] = [];
    for (const node of nodes) {
      if (node.type === 'problem') {
        const challenge = challengeById.get(node.challenge_id);
        if (challenge) {
          directChallenges.push(challenge);
          orderedItems.push({ type: 'problem', challenge, placementId: node.id });
        }
        continue;
      }
      const converted = convertNodes(node.children);
      if (converted.challenges.length === 0 && converted.children.length === 0) continue;
      const child: NavigationGroup = {
        id: `custom-group:${node.id}`,
        label: node.name,
        challenges: converted.challenges,
        children: converted.children,
        orderedItems: converted.orderedItems,
      };
      children.push(child);
      orderedItems.push({ type: 'group', group: child });
    }
    return { challenges: directChallenges, children, orderedItems };
  };

  return customSets.map((set) => {
    const converted = convertNodes(set.nodes);
    const isEmpty = converted.challenges.length === 0 && converted.children.length === 0;
    return {
      id: `custom-set:${set.id}`,
      label: set.name,
      challenges: converted.challenges,
      children: converted.children,
      orderedItems: converted.orderedItems,
      careerMode: set.career_mode,
      emptyMessage: isEmpty
        ? 'No problems in this set match the current filters. Open the builder to add or organize problems.'
        : undefined,
    };
  });
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
  customSets: CustomProblemSet[] = [],
): Map<string, Set<string>> {
  if (activeSet === 'custom') {
    const challengeOrder = new Map(
      challenges.map((challenge) => [challenge.id, leetcodeProblemOrder(challenge)]),
    );
    return buildCustomCareerUnlockMap(
      customSets,
      completed,
      (challengeId) => challengeOrder.get(challengeId) ?? Number.MAX_SAFE_INTEGER,
    );
  }
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
  customSets: CustomProblemSet[] = [],
): NavigationGroup[] {
  if (activeSet === 'leetcode') {
    return buildCategoryGroups(challenges);
  }
  if (activeSet === 'elo') {
    return buildEloGroups(challenges);
  }
  if (activeSet === 'frequency') {
    return buildFrequencyGroups(challenges);
  }
  if (activeSet === 'leetcode_company') {
    return buildCompanyGroups(challenges);
  }
  if (activeSet === 'leetcode_studyplan') {
    return buildStudyPlanGroups(challenges).map((group) => ({
      ...group,
      careerMode: true,
    }));
  }
  if (activeSet === 'neetcode') {
    return buildNeetcodeGroups(challenges).map((group) => ({
      ...group,
      careerMode: true,
    }));
  }
  if (activeSet === 'algomaster') {
    return buildAlgomasterGroups(challenges);
  }
  if (activeSet === 'custom') {
    return buildCustomGroups(challenges, customSets);
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

function collectGroupChallengesInSetOrder(group: NavigationGroup): ChallengeSummary[] {
  if (group.orderedItems) {
    return group.orderedItems.flatMap((item) => (
      item.type === 'problem'
        ? [item.challenge]
        : collectGroupChallengesInSetOrder(item.group)
    ));
  }
  const result = group.children.flatMap(collectGroupChallengesInSetOrder);
  result.push(...group.challenges);
  return result;
}

function uniqueChallengesInOrder(challenges: ChallengeSummary[]): ChallengeSummary[] {
  const seen = new Set<string>();
  return challenges.filter((challenge) => {
    if (seen.has(challenge.id)) return false;
    seen.add(challenge.id);
    return true;
  });
}

function challengesInSetOrder(
  navigationGroups: NavigationGroup[],
  filteredChallenges: ChallengeSummary[],
  activeSet: string,
): ChallengeSummary[] {
  if (activeSet === 'leetcode') {
    return sortByLeetcodeId(filteredChallenges);
  }
  const ordered = uniqueChallengesInOrder(
    navigationGroups.flatMap(collectGroupChallengesInSetOrder),
  );
  const seen = new Set(ordered.map((challenge) => challenge.id));
  ordered.push(...filteredChallenges.filter((challenge) => !seen.has(challenge.id)));
  return ordered;
}

function pdfTocProblem(challenge: ChallengeSummary): PdfTocNode {
  return {
    kind: 'problem',
    challengeId: challenge.id,
    frontendId: challenge.leetcode_frontend_id || challenge.id.replace(/^lc_/, ''),
    label: challenge.name,
    difficultyLabel: challenge.difficulty_label,
    eloRating: challenge.elo_rating,
    estimatedEloRating: challenge.estimated_elo_rating,
    frequency: challenge.frequency,
  };
}

function pdfTocGroup(group: NavigationGroup): PdfTocNode {
  const children = group.orderedItems
    ? group.orderedItems.flatMap((item): PdfTocNode[] => {
        if (item.type === 'problem') return [pdfTocProblem(item.challenge)];
        return collectGroupChallenges(item.group).length > 0
          ? [pdfTocGroup(item.group)]
          : [];
      })
    : [
        ...group.children
          .filter((child) => collectGroupChallenges(child).length > 0)
          .map(pdfTocGroup),
        ...group.challenges.map(pdfTocProblem),
      ];
  return {
    kind: 'group',
    id: group.id,
    label: group.label,
    children,
  };
}

function pdfTocForNavigation(
  groups: NavigationGroup[],
  scopedChallenges: ChallengeSummary[],
): PdfTocNode[] {
  const nodes = groups
    .filter((group) => collectGroupChallenges(group).length > 0)
    .map(pdfTocGroup);
  const groupedIds = new Set(
    groups.flatMap(collectGroupChallengesInSetOrder).map((challenge) => challenge.id),
  );
  nodes.push(
    ...scopedChallenges
      .filter((challenge) => !groupedIds.has(challenge.id))
      .map(pdfTocProblem),
  );
  return nodes;
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

function numberingContextForDisplay(
  _challenge: ChallengeSummary,
  activeSet: string,
  categoryContext?: string,
): string {
  return categoryContext || activeSet;
}

function buildChallengeNumberMap(
  navigationGroups: NavigationGroup[],
  challenges: ChallengeSummary[],
  activeSet: string,
): Map<string, ChallengeNumber> {
  const numbers = new Map<string, ChallengeNumber>();
  const addContext = (context: string, contextChallenges: ChallengeSummary[]) => {
    const ordered = uniqueChallengesInOrder(contextChallenges);
    const width = Math.max(3, String(ordered.length).length);
    ordered.forEach((challenge, index) => {
      const rawNumber = index + 1;
      numbers.set(numberKey(context, challenge.id), {
        display: String(rawNumber),
        filename: String(rawNumber).padStart(width, '0'),
      });
    });
  };

  const visitGroup = (group: NavigationGroup, parentPath: string[]) => {
    const path = [...parentPath, group.label];
    addContext(path.join('/'), group.challenges);
    group.children.forEach((child) => visitGroup(child, path));
  };
  navigationGroups.forEach((group) => visitGroup(group, []));

  addContext(
    activeSet,
    challengesInSetOrder(navigationGroups, challenges, activeSet),
  );
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

function PdfIcon({ className = "h-4 w-4" }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      viewBox="0 0 20 20"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M5 2.5h6l4 4v11H5z" />
      <path d="M11 2.5v4h4" />
      <text
        x="6.4"
        y="14.2"
        fill="currentColor"
        stroke="none"
        fontSize="5.2"
        fontWeight="700"
        fontFamily="Arial, sans-serif"
      >
        PDF
      </text>
    </svg>
  );
}

type PdfMenuButtonProps = {
  disabled?: boolean;
  className: string;
  iconClassName?: string;
  label?: string;
  title: string;
  ariaLabel: string;
  onSelect: (includeSolution: boolean) => void;
};

function PdfMenuButton({
  disabled = false,
  className,
  iconClassName = 'h-4 w-4',
  label,
  title,
  ariaLabel,
  onSelect,
}: PdfMenuButtonProps) {
  const buttonRef = useRef<HTMLButtonElement>(null);
  const menuRef = useRef<HTMLDivElement>(null);
  const [menuPosition, setMenuPosition] = useState<{ left: number; top: number } | null>(null);

  useEffect(() => {
    if (!menuPosition) return undefined;

    const closeIfOutside = (event: PointerEvent) => {
      const target = event.target as Node | null;
      if (target && (buttonRef.current?.contains(target) || menuRef.current?.contains(target))) return;
      setMenuPosition(null);
    };
    const close = () => setMenuPosition(null);
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        close();
        buttonRef.current?.focus();
      }
    };

    document.addEventListener('pointerdown', closeIfOutside);
    document.addEventListener('keydown', closeOnEscape);
    window.addEventListener('resize', close);
    window.addEventListener('scroll', close, true);
    return () => {
      document.removeEventListener('pointerdown', closeIfOutside);
      document.removeEventListener('keydown', closeOnEscape);
      window.removeEventListener('resize', close);
      window.removeEventListener('scroll', close, true);
    };
  }, [menuPosition]);

  const toggleMenu = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.stopPropagation();
    if (disabled) return;
    if (menuPosition) {
      setMenuPosition(null);
      return;
    }
    const rect = buttonRef.current?.getBoundingClientRect();
    if (!rect) return;
    const menuWidth = 224;
    const menuHeight = 104;
    const left = Math.max(8, Math.min(rect.right - menuWidth, window.innerWidth - menuWidth - 8));
    const below = rect.bottom + 4;
    const top = below + menuHeight <= window.innerHeight - 8
      ? below
      : Math.max(8, rect.top - menuHeight - 4);
    setMenuPosition({ left, top });
  };

  const choose = (event: React.MouseEvent, includeSolution: boolean) => {
    event.stopPropagation();
    setMenuPosition(null);
    onSelect(includeSolution);
  };

  return (
    <>
      <button
        ref={buttonRef}
        type="button"
        onClick={toggleMenu}
        disabled={disabled}
        className={className}
        title={title}
        aria-label={ariaLabel}
        aria-haspopup="menu"
        aria-expanded={menuPosition !== null}
      >
        <PdfIcon className={iconClassName} />
        {label && <span>{label}</span>}
      </button>
      {menuPosition && createPortal(
        <div
          ref={menuRef}
          role="menu"
          aria-label="PDF contents"
          className="fixed z-[300] w-56 overflow-hidden rounded border border-coden-border bg-coden-surface shadow-2xl"
          style={menuPosition}
          onClick={(event) => event.stopPropagation()}
        >
          <button
            type="button"
            role="menuitem"
            className="block w-full px-3 py-2 text-left hover:bg-coden-border focus:bg-coden-border focus:outline-none"
            onClick={(event) => choose(event, false)}
          >
            <span className="block text-xs font-semibold text-coden-text">Without solution</span>
            <span className="block text-[10px] text-coden-muted">Reference and Guided Example</span>
          </button>
          <button
            type="button"
            role="menuitem"
            className="block w-full border-t border-coden-border px-3 py-2 text-left hover:bg-coden-border focus:bg-coden-border focus:outline-none"
            onClick={(event) => choose(event, true)}
          >
            <span className="block text-xs font-semibold text-coden-text">With solution</span>
            <span className="block text-[10px] text-coden-muted">Add each problem's primary language</span>
          </button>
        </div>,
        document.body,
      )}
    </>
  );
}

function ResetIcon({ className = "h-4 w-4" }: { className?: string }) {
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
      <path d="M4 4.5v4h4" />
      <path d="M4.35 8.5A6 6 0 1 1 5.8 14.8" />
    </svg>
  );
}

type ResetMenuButtonProps = {
  disabled?: boolean;
  className: string;
  iconClassName?: string;
  label?: string;
  title: string;
  ariaLabel: string;
  onSelect: (scope: ProgressResetScope) => void;
};

function ResetMenuButton({
  disabled = false,
  className,
  iconClassName = 'h-4 w-4',
  label,
  title,
  ariaLabel,
  onSelect,
}: ResetMenuButtonProps) {
  const buttonRef = useRef<HTMLButtonElement>(null);
  const menuRef = useRef<HTMLDivElement>(null);
  const [menuPosition, setMenuPosition] = useState<{ left: number; top: number } | null>(null);

  useEffect(() => {
    if (!menuPosition) return undefined;

    const closeIfOutside = (event: PointerEvent) => {
      const target = event.target as Node | null;
      if (target && (buttonRef.current?.contains(target) || menuRef.current?.contains(target))) return;
      setMenuPosition(null);
    };
    const close = () => setMenuPosition(null);
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        close();
        buttonRef.current?.focus();
      }
    };

    document.addEventListener('pointerdown', closeIfOutside);
    document.addEventListener('keydown', closeOnEscape);
    window.addEventListener('resize', close);
    window.addEventListener('scroll', close, true);
    return () => {
      document.removeEventListener('pointerdown', closeIfOutside);
      document.removeEventListener('keydown', closeOnEscape);
      window.removeEventListener('resize', close);
      window.removeEventListener('scroll', close, true);
    };
  }, [menuPosition]);

  const toggleMenu = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.stopPropagation();
    if (disabled) return;
    if (menuPosition) {
      setMenuPosition(null);
      return;
    }
    const rect = buttonRef.current?.getBoundingClientRect();
    if (!rect) return;
    const menuWidth = 256;
    const menuHeight = 174;
    const left = Math.max(8, Math.min(rect.right - menuWidth, window.innerWidth - menuWidth - 8));
    const below = rect.bottom + 4;
    const top = below + menuHeight <= window.innerHeight - 8
      ? below
      : Math.max(8, rect.top - menuHeight - 4);
    setMenuPosition({ left, top });
  };

  const choose = (event: React.MouseEvent, scope: ProgressResetScope) => {
    event.stopPropagation();
    setMenuPosition(null);
    onSelect(scope);
  };

  return (
    <>
      <button
        ref={buttonRef}
        type="button"
        onClick={toggleMenu}
        disabled={disabled}
        className={className}
        title={title}
        aria-label={ariaLabel}
        aria-haspopup="menu"
        aria-expanded={menuPosition !== null}
      >
        <ResetIcon className={iconClassName} />
        {label && <span>{label}</span>}
      </button>
      {menuPosition && createPortal(
        <div
          ref={menuRef}
          role="menu"
          aria-label="Reset progress options"
          className="fixed z-[300] w-64 overflow-hidden rounded border border-rose-500/35 bg-coden-surface shadow-2xl"
          style={menuPosition}
          onClick={(event) => event.stopPropagation()}
        >
          {(Object.keys(RESET_SCOPE_COPY) as ProgressResetScope[]).map((scope, index) => {
            const copy = RESET_SCOPE_COPY[scope];
            return (
              <button
                key={scope}
                type="button"
                role="menuitem"
                className={[
                  'block w-full px-3 py-2 text-left hover:bg-rose-500/10 focus:bg-rose-500/10 focus:outline-none',
                  index > 0 ? 'border-t border-coden-border' : '',
                ].join(' ')}
                onClick={(event) => choose(event, scope)}
              >
                <span className="block text-xs font-semibold text-rose-300">{copy.label}</span>
                <span className="block text-[10px] leading-4 text-coden-muted">{copy.description}</span>
              </button>
            );
          })}
        </div>,
        document.body,
      )}
    </>
  );
}

function ResetProgressDialog({
  request,
  busy,
  error,
  onCancel,
  onConfirm,
}: {
  request: ProgressResetRequest;
  busy: boolean;
  error: string | null;
  onCancel: () => void;
  onConfirm: (confirmation: string) => void;
}) {
  const [confirmation, setConfirmation] = useState('');
  const [clipboardBlocked, setClipboardBlocked] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const copy = RESET_SCOPE_COPY[request.scope];
  const deletesSolutions = request.scope === 'all' || request.scope === 'coden';
  const problemLabel = request.challengeIds.length === 1 ? '1 problem' : `${request.challengeIds.length} problems`;
  const confirmed = confirmation === 'RESET';

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  useEffect(() => {
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape' && !busy) onCancel();
    };
    document.addEventListener('keydown', closeOnEscape);
    return () => document.removeEventListener('keydown', closeOnEscape);
  }, [busy, onCancel]);

  const blockClipboard = (event: React.SyntheticEvent) => {
    event.preventDefault();
    setClipboardBlocked(true);
  };

  const handleBeforeInput = (event: React.FormEvent<HTMLInputElement>) => {
    const inputType = (event.nativeEvent as InputEvent).inputType;
    if (inputType === 'insertFromPaste' || inputType === 'insertFromDrop') {
      blockClipboard(event);
    }
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if ((event.ctrlKey || event.metaKey) && ['c', 'v', 'x'].includes(event.key.toLowerCase())) {
      blockClipboard(event);
    }
  };

  return createPortal(
    <div
      className="fixed inset-0 z-[400] flex items-center justify-center bg-black/70 p-4"
      role="presentation"
      onMouseDown={(event) => {
        if (event.target === event.currentTarget && !busy) onCancel();
      }}
    >
      <form
        role="dialog"
        aria-modal="true"
        aria-labelledby="reset-progress-title"
        className="w-full max-w-md rounded-xl border border-rose-500/45 bg-coden-surface p-5 shadow-2xl"
        onSubmit={(event) => {
          event.preventDefault();
          if (confirmed && !busy) onConfirm(confirmation);
        }}
      >
        <div className="flex items-start gap-3">
          <div className="mt-0.5 rounded-full bg-rose-500/15 p-2 text-rose-300">
            <ResetIcon className="h-5 w-5" />
          </div>
          <div className="min-w-0">
            <h2 id="reset-progress-title" className="text-lg font-bold text-coden-text">
              Reset {copy.label}?
            </h2>
            <p className="mt-1 text-sm text-coden-muted">
              {problemLabel} in <span className="font-semibold text-coden-text">{request.targetLabel}</span>
            </p>
          </div>
        </div>

        <div className="mt-4 rounded-lg border border-rose-500/25 bg-rose-500/[0.08] p-3">
          <p className="text-sm text-rose-100">{copy.description}</p>
          <p className="mt-2 text-xs leading-5 text-coden-muted">
            {deletesSolutions
              ? 'Every personal solution version for these problems will be permanently deleted. Profile settings and packaged reference solutions will not be changed.'
              : 'Personal solution files and profile settings will not be changed.'}
            {' '}This reset cannot be undone.
          </p>
        </div>

        <label htmlFor="reset-progress-confirmation" className="mt-5 block text-sm text-coden-text">
          Type the word below by hand to continue:
        </label>
        <div className="select-none py-3 text-center font-mono text-3xl font-black tracking-[0.35em] text-rose-300">
          RESET
        </div>
        <input
          ref={inputRef}
          id="reset-progress-confirmation"
          type="text"
          value={confirmation}
          disabled={busy}
          autoComplete="off"
          spellCheck={false}
          aria-describedby="reset-progress-input-help"
          onChange={(event) => {
            setConfirmation(event.target.value);
            setClipboardBlocked(false);
          }}
          onBeforeInput={handleBeforeInput}
          onKeyDown={handleKeyDown}
          onPaste={blockClipboard}
          onCopy={blockClipboard}
          onCut={blockClipboard}
          onDrop={blockClipboard}
          className="w-full rounded border border-coden-border bg-coden-bg px-3 py-2 text-center font-mono text-xl font-bold tracking-[0.25em] text-coden-text outline-none transition-colors focus:border-rose-400 disabled:opacity-60"
          placeholder="Type RESET"
        />
        <p
          id="reset-progress-input-help"
          className={`mt-2 text-center text-xs ${clipboardBlocked ? 'text-amber-300' : 'text-coden-muted'}`}
          aria-live="polite"
        >
          {clipboardBlocked
            ? 'Clipboard actions and drag-and-drop are disabled. Type RESET manually.'
            : 'The confirmation is case-sensitive. Pasting is disabled.'}
        </p>

        {error && (
          <div className="mt-3 rounded border border-amber-500/35 bg-amber-500/10 px-3 py-2 text-xs text-amber-200">
            {error}
          </div>
        )}

        <div className="mt-5 flex justify-end gap-2">
          <button
            type="button"
            disabled={busy}
            onClick={onCancel}
            className="rounded border border-coden-border px-3 py-2 text-sm text-coden-muted hover:bg-coden-border hover:text-coden-text disabled:opacity-50"
          >
            Cancel
          </button>
          <button
            type="submit"
            disabled={!confirmed || busy}
            className="rounded bg-rose-600 px-3 py-2 text-sm font-bold text-white hover:bg-rose-500 disabled:cursor-not-allowed disabled:opacity-35"
          >
            {busy ? 'Resetting...' : `Reset ${copy.label}`}
          </button>
        </div>
      </form>
    </div>,
    document.body,
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
 * LeetCode rows show their canonical problem id on the metadata line;
 * other datasets keep showing their required complexity. The internal
 * machine id remains available in the detail panel header and tooltip.
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
  const clearSolutionStateAfterReset = useAppStore((s) => s.clearSolutionStateAfterReset);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const leetcodeSubmissions = useAppStore((s) => s.progress?.leetcode_submissions ?? {});
  const activeSet = useAppStore((s) => s.activeSet);
  const activeCustomSetId = useAppStore((s) => s.activeCustomSetId);
  const language = useAppStore((s) => s.language);
  const customProblemSets = useAppStore((s) => s.customProblemSets);
  const customProblemSetsLoading = useAppStore((s) => s.customProblemSetsLoading);
  const customProblemSetsError = useAppStore((s) => s.customProblemSetsError);
  const saveCustomProblemSets = useAppStore((s) => s.saveCustomProblemSets);

  const [searchQuery, setSearchQuery] = useState('');
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});
  const [downloadState, setDownloadState] = useState<DownloadState | null>(null);
  const [pdfExporting, setPdfExporting] = useState(false);
  const [submittingChallengeId, setSubmittingChallengeId] = useState<string | null>(null);
  const [submissionNotice, setSubmissionNotice] = useState<SubmissionNotice | null>(null);
  const [resetRequest, setResetRequest] = useState<ProgressResetRequest | null>(null);
  const [resetting, setResetting] = useState(false);
  const [resetError, setResetError] = useState<string | null>(null);
  const [resetNotice, setResetNotice] = useState<SubmissionNotice | null>(null);
  const [showCustomBuilder, setShowCustomBuilder] = useState(false);
  const completedSet = useMemo(() => new Set(completed), [completed]);
  const submittedSet = useMemo(() => new Set(Object.keys(leetcodeSubmissions)), [leetcodeSubmissions]);
  const activeCustomProblemSets = useMemo(() => {
    if (activeSet !== 'custom') return customProblemSets;
    const selected = customProblemSets.find((set) => set.id === activeCustomSetId);
    return selected ? [selected] : [];
  }, [activeCustomSetId, activeSet, customProblemSets]);
  const activeSetLabel = activeSet === 'custom'
    ? activeCustomProblemSets[0]?.name || 'Personal'
    : getAlgorithmSetLabel(activeSet);

  const toggleCategory = (category: string) => {
    setExpanded((prev) => ({ ...prev, [category]: !prev[category] }));
  };


  const activeSetChallenges = useMemo(
    () => {
      if (activeSet !== 'custom') return challengesForAlgorithmSet(challenges, activeSet);
      const selectedSet = activeCustomProblemSets[0];
      if (!selectedSet) return [];
      const customIds = collectSetChallengeIds(selectedSet);
      return challenges.filter((challenge) => customIds.has(challenge.id));
    },
    [challenges, activeSet, activeCustomProblemSets],
  );

  const filteredChallenges = useMemo(() => {
    let baseList = activeSetChallenges;
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
      (c.estimated_elo_rating !== null && (
        Math.round(c.estimated_elo_rating).toString() === lowerQ
        || `est elo ${Math.round(c.estimated_elo_rating)}`.includes(lowerQ)
      )) ||
      (c.frequency !== null && (
        c.frequency.toFixed(1) === lowerQ
        || `freq ${c.frequency.toFixed(1)}`.includes(lowerQ)
        || `frequency ${c.frequency.toFixed(1)}`.includes(lowerQ)
      )) ||
      c.difficulty_label.toLowerCase().includes(lowerQ)
    );
  }, [activeSetChallenges, searchQuery, activeSet, difficultyFilter]);

  const filteredEloAverage = useMemo(
    () => calculateDirectEloAverage(filteredChallenges),
    [filteredChallenges],
  );

  const filteredFrequencyAverage = useMemo(
    () => calculateDirectFrequencyAverage(filteredChallenges),
    [filteredChallenges],
  );

  const navigationGroups = useMemo(
    () => buildNavigationGroups(filteredChallenges, activeSet, activeCustomProblemSets),
    [filteredChallenges, activeSet, activeCustomProblemSets],
  );

  const shownChallengesForPdf = useMemo(
    () => challengesInSetOrder(navigationGroups, filteredChallenges, activeSet),
    [navigationGroups, filteredChallenges, activeSet],
  );

  const shownTocForPdf = useMemo(
    () => pdfTocForNavigation(navigationGroups, shownChallengesForPdf),
    [navigationGroups, shownChallengesForPdf],
  );

  const careerUnlocks = useMemo(
    () => buildCareerUnlockMap(challenges, activeSet, completedSet, activeCustomProblemSets),
    [challenges, activeSet, completedSet, activeCustomProblemSets],
  );

  const challengeNumbers = useMemo(
    () => buildChallengeNumberMap(
      buildNavigationGroups(activeSetChallenges, activeSet, activeCustomProblemSets),
      activeSetChallenges,
      activeSet,
    ),
    [activeSetChallenges, activeSet, activeCustomProblemSets],
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
    if (group.orderedItems) {
      return group.orderedItems.flatMap((item): PracticeExportEntry[] => (
        item.type === 'problem'
          ? [exportEntryForPath(item.challenge, path)]
          : entriesForGroup(item.group, [...path, item.group.label])
      ));
    }
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

  const handlePdfBundle = async (
    scopedChallenges: ChallengeSummary[],
    scopeLabel: string,
    toc: PdfTocNode[],
    includeSolution: boolean,
  ) => {
    if (pdfExporting) return;

    const orderedChallenges = uniqueChallengesInOrder(scopedChallenges);
    const label = `Preparing ${orderedChallenges.length}-problem PDF${includeSolution ? ' with solutions' : ''}`;
    setPdfExporting(true);
    setDownloadState({
      label,
      loaded: 0,
      total: null,
      percent: null,
      status: 'active',
      message: includeSolution
        ? 'Loading References, Guided Examples, and primary-language solutions...'
        : 'Loading References and Guided Examples...',
    });

    try {
      const result = await exportChallengePdfBundle({
        challenges: orderedChallenges,
        language,
        title: `${scopeLabel} - References and Guided Examples${includeSolution ? ' with Solutions' : ''}`,
        suggestedFilename: buildPdfBundleFilename(
          scopeLabel,
          orderedChallenges,
          includeSolution,
        ),
        toc,
        includeSolution,
        onProgress: ({ completed, total, message }) => {
          setDownloadState({
            label,
            loaded: completed,
            total,
            percent: total > 0 ? completed / total * 100 : null,
            status: 'active',
            message,
          });
        },
      });
      if (result.status === 'error') {
        throw new Error(result.message || 'The PDF could not be saved.');
      }
      if (result.status === 'cancelled') {
        setDownloadState(null);
        return;
      }
      setDownloadState({
        label,
        loaded: orderedChallenges.length,
        total: orderedChallenges.length,
        percent: 100,
        status: 'done',
        message: 'PDF saved',
      });
      window.setTimeout(() => setDownloadState(null), 2500);
    } catch (error) {
      failDownload(label, error);
    } finally {
      setPdfExporting(false);
    }
  };

  const requestProgressReset = (
    scope: ProgressResetScope,
    scopedChallenges: ChallengeSummary[],
    targetLabel: string,
  ) => {
    const challengeIds = uniqueChallengesInOrder(scopedChallenges).map((challenge) => challenge.id);
    if (challengeIds.length === 0) return;
    setResetError(null);
    setResetRequest({ scope, challengeIds, targetLabel });
  };

  const confirmProgressReset = async (confirmation: string) => {
    if (!resetRequest || resetting) return;
    const request = resetRequest;
    setResetting(true);
    setResetError(null);
    try {
      await resetProgress(request.scope, request.challengeIds, confirmation);
      if (request.scope === 'all' || request.scope === 'coden') {
        clearSolutionStateAfterReset(request.challengeIds);
      }
      await loadProgress();
      const copy = RESET_SCOPE_COPY[request.scope];
      const count = request.challengeIds.length;
      setResetRequest(null);
      setResetNotice({
        status: 'done',
        message: request.scope === 'leetcode'
          ? `${copy.label} cleared for ${count} ${count === 1 ? 'problem' : 'problems'} in ${request.targetLabel}.`
          : `${copy.label} cleared and personal solutions deleted for ${count} ${count === 1 ? 'problem' : 'problems'} in ${request.targetLabel}.`,
      });
      window.setTimeout(() => setResetNotice(null), 4000);
    } catch {
      setResetError('Reset did not complete. Check the selected problems before retrying.');
    } finally {
      setResetting(false);
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
    const displayTitle = formatChallengeTitle(c, numberForChallenge(c, categoryContext));
    const leetcodeId = numericLeetcodeId(c);
    const eloDisplay = isLeetcodeUniverse(activeSet)
      ? eloDisplayForChallenge(c)
      : null;
    const ratingTitle = eloDisplay === null
      ? 'Official LeetCode difficulty'
      : eloDisplay.estimated
        ? `Stored estimated Elo, not a contest rating. It is recalculated from official difficulty, acceptance percentile, real-Elo bands, and the calibrated legacy cohort by tools/update_leetcode_metrics.py. ${ELO_HEAT_SCALE_DESCRIPTION}`
        : `Contest Elo from ZeroTrac; displayed as a rounded whole number. ${ELO_HEAT_SCALE_DESCRIPTION}`;
    const frequencyTitle = c.frequency === null
      ? 'LeetCode Frequency is unavailable until the authenticated Premium metadata updater succeeds.'
      : `LeetCode Frequency ${c.frequency.toFixed(1)} / 100. This is LeetCode's mutable relative-frequency attribute, not the acceptance rate or a guaranteed interview probability.`;
    const metricTitle = `${ratingTitle} ${frequencyTitle}`;

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
                  : 'text-coden-muted',
              ].join(' ')}
              title={isLeetcodeUniverse(activeSet)
                ? metricTitle
                : c.required_complexity}
            >
              {isLeetcodeUniverse(activeSet) ? (
                <>
                  {leetcodeId !== null && (
                    <>
                      <span className="opacity-80">LC {leetcodeId}</span>
                      <span className="opacity-60" aria-hidden="true"> · </span>
                    </>
                  )}
                  <span className="opacity-80">{c.difficulty_label}</span>
                  {eloDisplay !== null && (
                    <>
                      <span className="opacity-60" aria-hidden="true"> · </span>
                      <span
                        className="font-semibold"
                        style={{ color: eloHeatColor(eloDisplay.value) }}
                      >
                        {eloDisplay.estimated ? 'Est. Elo' : 'Elo'} {Math.round(eloDisplay.value)}
                      </span>
                    </>
                  )}
                  <span className="opacity-60" aria-hidden="true"> · </span>
                  <span className="opacity-80">
                    Freq {c.frequency === null ? '—' : `${c.frequency.toFixed(1)}%`}
                  </span>
                </>
              ) : c.required_complexity}
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
        <PdfMenuButton
          disabled={pdfExporting}
          className="w-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center disabled:cursor-wait disabled:opacity-40"
          title={`Save Reference and Guided Example for ${c.name} as PDF`}
          ariaLabel={`Save PDF for ${c.name}`}
          onSelect={(includeSolution) => void handlePdfBundle(
            [c],
            `LeetCode ${c.leetcode_frontend_id || c.id.replace(/^lc_/, '')} - ${c.name}`,
            [pdfTocProblem(c)],
            includeSolution,
          )}
        />
        <ResetMenuButton
          disabled={resetting}
          className="w-7 rounded text-coden-muted hover:text-rose-300 hover:bg-rose-500/10 shrink-0 inline-flex items-center justify-center disabled:cursor-wait disabled:opacity-40"
          title={`Reset tracked progress for ${c.name}`}
          ariaLabel={`Reset progress for ${c.name}`}
          onSelect={(scope) => requestProgressReset(
            scope,
            [c],
            `LeetCode ${c.leetcode_frontend_id || c.id.replace(/^lc_/, '')} - ${c.name}`,
          )}
        />
      </li>
    );
  };

  const renderGroup = (group: NavigationGroup, depth = 0, parentPath: string[] = []) => {
    const path = [...parentPath, group.label];
    const context = path.join('/');
    const groupChallenges = collectGroupChallenges(group);
    const groupEloAverage = calculateDirectEloAverage(groupChallenges);
    const groupFrequencyAverage = calculateDirectFrequencyAverage(groupChallenges);
    const isCollapsed = group.emptyMessage ? false : !searchQuery.trim() && !expanded[group.id];
    const groupEntries = entriesForGroup(group, path);
    const leftPadding = depth === 0 ? '' : depth === 1 ? 'ml-3' : 'ml-5';

    return (
      <Fragment key={group.id}>
        <div className={['mb-2', leftPadding].join(' ')}>
          <div className="flex items-center gap-1">
            <button
              onClick={() => toggleCategory(group.id)}
              className="group flex min-w-0 flex-1 items-start rounded px-2 py-1.5 text-xs font-semibold text-coden-muted transition-colors hover:bg-coden-border/35 hover:text-coden-text select-none"
            >
              <span
                className="mr-1 mt-0.5 shrink-0 transform text-[10px] transition-transform duration-200 group-hover:text-coden-accent"
              >
                {isCollapsed ? '>' : 'v'}
              </span>
              {progressHeading(
                group.label,
                groupChallenges,
                completedSet,
                submittedSet,
                groupEloAverage,
                groupFrequencyAverage,
                group.careerMode,
              )}
            </button>
            {groupEntries.length > 0 && (
              <>
                <button
                  type="button"
                  onClick={(event) => handleDownloadBundle(event, groupEntries)}
                  className="w-7 h-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
                  title={`Download ${group.label}`}
                  aria-label={`Download ${group.label}`}
                >
                  <DownloadIcon className="h-4 w-4" />
                </button>
                <PdfMenuButton
                  disabled={pdfExporting}
                  className="w-7 h-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center disabled:cursor-wait disabled:opacity-40"
                  title={`Save ${group.label} References and Guided Examples as one PDF`}
                  ariaLabel={`Save ${group.label} PDF`}
                  onSelect={(includeSolution) => void handlePdfBundle(
                    collectGroupChallengesInSetOrder(group),
                    `${activeSetLabel} - ${path.join(' - ')}`,
                    [pdfTocGroup(group)],
                    includeSolution,
                  )}
                />
                <ResetMenuButton
                  disabled={resetting}
                  className="w-7 h-7 rounded text-coden-muted hover:text-rose-300 hover:bg-rose-500/10 shrink-0 inline-flex items-center justify-center disabled:cursor-wait disabled:opacity-40"
                  title={`Reset tracked progress for ${group.label}`}
                  ariaLabel={`Reset progress for ${group.label}`}
                  onSelect={(scope) => requestProgressReset(
                    scope,
                    collectGroupChallengesInSetOrder(group),
                    path.join(' / '),
                  )}
                />
              </>
            )}
          </div>

          {!isCollapsed && group.emptyMessage && (
            <div className="px-2 py-2 text-[11px] text-coden-muted">
              {group.emptyMessage}
            </div>
          )}

          {!isCollapsed && (
            <div className="mt-1">
              {group.orderedItems
                ? group.orderedItems.map((item) => item.type === 'group'
                    ? renderGroup(item.group, depth + 1, path)
                    : (
                        <ul key={`${group.id}:${item.placementId}`} className="space-y-0.5">
                          {renderChallengeRow(item.challenge, context, group.id)}
                        </ul>
                      ))
                : (
                    <>
                      {group.children.map((child) => renderGroup(child, depth + 1, path))}
                      {group.challenges.length > 0 && (
                        <ul className="space-y-0.5">
                          {group.challenges.map((challenge) => renderChallengeRow(challenge, context, group.id))}
                        </ul>
                      )}
                    </>
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
          {filteredEloAverage !== null && (
            <>
              {' · '}
              <span
                className="font-semibold"
                style={{ color: eloHeatColor(filteredEloAverage.value) }}
                title={eloAverageTitle(filteredEloAverage)}
              >
                Avg Elo{filteredEloAverage.estimatedCount > 0 ? ' ~' : ' '}
                {Math.round(filteredEloAverage.value)}
              </span>
            </>
          )}
          {filteredFrequencyAverage !== null && (
            <>
              {' · '}
              <span
                className="font-semibold text-coden-accent"
                title={frequencyAverageTitle(filteredFrequencyAverage)}
              >
                Avg Freq {filteredFrequencyAverage.value.toFixed(1)}%
              </span>
            </>
          )}
        </div>
        <div className="mt-2 flex justify-end gap-1 text-[11px]">
          {activeSet === 'custom' && (
            <button
              type="button"
              onClick={() => setShowCustomBuilder(true)}
              className="mr-auto h-7 rounded border border-coden-accent/50 bg-coden-accent/10 px-2.5 font-semibold text-coden-accent hover:bg-coden-accent/20"
            >
              Edit personal sets
            </button>
          )}
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
          <PdfMenuButton
            className="h-7 px-2 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border inline-flex items-center gap-1 disabled:cursor-wait disabled:opacity-40"
            disabled={challengesLoading || filteredChallenges.length === 0 || pdfExporting}
            title="Save all currently shown problems as one ordered Reference and Guided Example PDF"
            ariaLabel="Save all currently shown problems as PDF"
            iconClassName="h-3.5 w-3.5"
            label="all"
            onSelect={(includeSolution) => void handlePdfBundle(
              shownChallengesForPdf,
              `${activeSetLabel} - currently shown`,
              shownTocForPdf,
              includeSolution,
            )}
          />
          <ResetMenuButton
            className="h-7 px-2 rounded border border-rose-500/25 text-coden-muted hover:text-rose-300 hover:bg-rose-500/10 inline-flex items-center gap-1 disabled:cursor-wait disabled:opacity-40"
            disabled={challengesLoading || filteredChallenges.length === 0 || resetting}
            title="Reset tracked progress for all currently shown problems"
            ariaLabel="Reset progress for all currently shown problems"
            iconClassName="h-3.5 w-3.5"
            label="all"
            onSelect={(scope) => requestProgressReset(
              scope,
              shownChallengesForPdf,
              `${activeSetLabel} - currently shown`,
            )}
          />
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
        {resetNotice && (
          <div className="mt-2 rounded border border-rose-500/30 bg-rose-500/10 px-2 py-1.5 text-[11px] text-rose-200">
            {resetNotice.message}
          </div>
        )}
        {activeSet === 'custom' && customProblemSetsError && (
          <div className="mt-2 rounded border border-amber-500/40 bg-amber-500/10 px-2 py-1.5 text-[11px] text-amber-300">
            {customProblemSetsError}
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

        {!challengesLoading && !challengesError && navigationGroups.length === 0 && activeSet === 'custom' && (
          <div className="flex flex-col items-center justify-center p-8 text-center text-coden-muted">
            <span className="text-sm font-semibold text-coden-text">Your Personal view is ready</span>
            <span className="mt-2 text-xs leading-5">
              Create a personal problem set, then drag LeetCode problems into up to three folder levels.
            </span>
            <button
              type="button"
              onClick={() => setShowCustomBuilder(true)}
              className="mt-4 rounded bg-coden-accent px-3 py-2 text-xs font-semibold text-[var(--coden-accent-contrast)] hover:brightness-110"
            >
              Create the first set
            </button>
          </div>
        )}

        {!challengesLoading && !challengesError && navigationGroups.length === 0 && activeSet !== 'custom' && (
          <div className="flex flex-col items-center justify-center p-8 text-coden-muted space-y-2">
            <span className="text-sm">No algorithms found</span>
            <span className="text-xs">Try a name, id, or category.</span>
          </div>
        )}
      </div>
      {resetRequest && (
        <ResetProgressDialog
          request={resetRequest}
          busy={resetting}
          error={resetError}
          onCancel={() => {
            if (resetting) return;
            setResetError(null);
            setResetRequest(null);
          }}
          onConfirm={(confirmation) => void confirmProgressReset(confirmation)}
        />
      )}
      {showCustomBuilder && (
        <CustomProblemSetBuilder
          savedSets={customProblemSets}
          challenges={challenges}
          saving={customProblemSetsLoading}
          onClose={() => setShowCustomBuilder(false)}
          onSave={saveCustomProblemSets}
        />
      )}
    </div>
  );
}
