import { Fragment, useState, useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';
import type { ChallengeSummary } from '../types/api';
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

function formatCategory(category: string): string {
  if (category in CATEGORY_DISPLAY_NAMES) {
    return CATEGORY_DISPLAY_NAMES[category];
  }
  if (category.includes('____')) {
    const lesson = category.split('____')[1].replace(/^\d+_/, '');
    return lesson.replace(/_/g, ' ');
  }
  if (category.includes('___')) {
    const lesson = category.split('___')[1].replace(/^\d+_/, '');
    return lesson.replace(/_/g, ' ');
  }
  const cleaned = category.replace(/^(leetcode|neetcode|gfg|codechef)_/i, '');
  return cleaned.replace(/_/g, ' ');
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

function formatChallengeTitle(
  challenge: ChallengeSummary,
  activeSet: string,
  number?: ChallengeNumber,
): string {
  if (number) return `${number.display}. ${challenge.name}`;
  if (activeSet !== 'leetcode') return challenge.name;
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? `${match[1]}. ${challenge.name}` : challenge.name;
}

function formatDifficultyLine(challenge: ChallengeSummary, activeSet: string): string {
  if (activeSet === 'codechef') {
    return /^\d+$/.test(challenge.difficulty_label)
      ? `CodeChef rating ${challenge.difficulty_label}`
      : 'CodeChef rating Unknown';
  }
  if (activeSet === 'leetcode') {
    return `Difficulty ${challenge.difficulty}/10 · ${challenge.difficulty_label}`;
  }
  return challenge.required_complexity;
}

function codeChefGroup(category: string): { key: string; label: string } | null {
  if (!category.startsWith('codechef_') || !category.includes('__')) return null;
  const key = category.split('__', 1)[0];
  const labels: Record<string, string> = {
    codechef_become_5_star: 'Become 5 star - Career Mode',
    codechef_data_structures_and_algorithms: 'Data Structures and Algorithms',
  };
  return { key, label: labels[key] ?? formatCategory(key) };
}

function codeChefCourse(category: string): { key: string; label: string } | null {
  if (!category.startsWith('codechef_') || !category.includes('___')) {
    return null;
  }
  const key = category.split('___')[0];
  const encodedLabel = key.split('__')[1]?.replace(/^\d+_/, '').replace(/_/g, ' ');
  return { key, label: CATEGORY_DISPLAY_NAMES[key] ?? encodedLabel ?? formatCategory(key) };
}

function codeChefSubcourse(category: string): { key: string; label: string } | null {
  if (!category.startsWith('codechef_become_5_star__') || !category.includes('____')) {
    return null;
  }
  const key = category.split('____')[0];
  const encodedLabel = key.split('___')[1]?.replace(/^\d+_/, '').replace(/_/g, ' ');
  return { key, label: encodedLabel ?? formatCategory(key) };
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

function isFullySolved(challenges: ChallengeSummary[], completed: Set<string>): boolean {
  const ids = uniqueChallengeIds(challenges);
  return ids.size > 0 && Array.from(ids).every((id) => completed.has(id));
}

function progressHeading(
  label: string,
  challenges: ChallengeSummary[],
  completed: Set<string>,
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
      <span className={countClassName}>({progressLabel(challenges, completed)})</span>
    </span>
  );
}

function categoryPath(category: string): string[] {
  const group = codeChefGroup(category);
  const course = codeChefCourse(category);
  const subcourse = codeChefSubcourse(category);
  if (group) {
    return [
      group.label,
      ...(course ? [course.label] : []),
      ...(subcourse ? [subcourse.label] : []),
      formatCategory(category),
    ];
  }
  return [formatCategory(category)];
}

function entryForChallenge(challenge: ChallengeSummary, categoryContext?: string): PracticeExportEntry {
  return {
    id: challenge.id,
    path: categoryPath(categoryContext ?? challenge.category),
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

function numberKey(context: string, challengeId: string): string {
  return `${context}::${challengeId}`;
}

function numericLeetcodeId(challenge: ChallengeSummary): number | null {
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? Number(match[1]) : null;
}

function codeChefRatingValue(challenge: ChallengeSummary): number {
  return /^\d+$/.test(challenge.difficulty_label)
    ? Number(challenge.difficulty_label)
    : Number.POSITIVE_INFINITY;
}

function codeChefRootKeys(challenge: ChallengeSummary): string[] {
  const keys = new Set<string>();
  const categories = challenge.categories.length > 0 ? challenge.categories : [challenge.category];
  for (const category of categories) {
    const group = codeChefGroup(category);
    if (group) keys.add(group.key);
  }
  const fallback = codeChefGroup(challenge.category);
  if (fallback) keys.add(fallback.key);
  return Array.from(keys);
}

function numberingContextsForChallenge(challenge: ChallengeSummary, activeSet: string): string[] {
  if (activeSet !== 'codechef') return [activeSet];
  const roots = codeChefRootKeys(challenge);
  return roots.length > 0 ? roots : [activeSet];
}

function numberingContextForDisplay(
  challenge: ChallengeSummary,
  activeSet: string,
  categoryContext?: string,
): string {
  if (activeSet !== 'codechef') return activeSet;
  const contextualGroup = categoryContext ? codeChefGroup(categoryContext) : null;
  if (contextualGroup) return contextualGroup.key;
  return numberingContextsForChallenge(challenge, activeSet)[0] ?? activeSet;
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
      if (activeSet === 'leetcode') {
        const leftId = numericLeetcodeId(left);
        const rightId = numericLeetcodeId(right);
        if (leftId !== null && rightId !== null && leftId !== rightId) return leftId - rightId;
        if (leftId !== null && rightId === null) return -1;
        if (leftId === null && rightId !== null) return 1;
      }
      if (activeSet === 'codechef' && context === 'codechef_become_5_star') {
        const ratingOrder = codeChefRatingValue(left) - codeChefRatingValue(right);
        if (ratingOrder !== 0) return ratingOrder;
        return left.id.localeCompare(right.id);
      }
      return (insertionOrder.get(left.id) ?? 0) - (insertionOrder.get(right.id) ?? 0);
    });

    const largestLeetcodeId = activeSet === 'leetcode'
      ? Math.max(...ordered.map((challenge) => numericLeetcodeId(challenge) ?? 0), 0)
      : 0;
    const width = Math.max(
      3,
      String(activeSet === 'leetcode' ? largestLeetcodeId : ordered.length).length,
    );

    ordered.forEach((challenge, index) => {
      const leetcodeId = activeSet === 'leetcode' ? numericLeetcodeId(challenge) : null;
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
  const currentId = useAppStore((s) => s.currentDetail?.id ?? null);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const activeSet = useAppStore((s) => s.activeSet);
  const localN = useAppStore((s) => s.n);
  const localSeed = useAppStore((s) => s.seed);
  const exportN = useAppStore((s) => s.exportN);
  const exportSeed = useAppStore((s) => s.exportSeed);
  const exportTestCount = useAppStore((s) => s.exportTestCount);
  const setExportN = useAppStore((s) => s.setExportN);
  const setExportSeed = useAppStore((s) => s.setExportSeed);
  const setExportTestCount = useAppStore((s) => s.setExportTestCount);

  const [searchQuery, setSearchQuery] = useState('');
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});
  const [downloadState, setDownloadState] = useState<DownloadState | null>(null);
  const completedSet = useMemo(() => new Set(completed), [completed]);

  const toggleCategory = (category: string) => {
    setExpanded((prev) => ({ ...prev, [category]: !prev[category] }));
  };


  const filteredChallenges = useMemo(() => {
    const isLockedSet = activeSet === 'neetcode';
    let baseList = isLockedSet
      ? challenges.filter(c => c.unlocked)
      : challenges;

    if (activeSet === 'leetcode' && difficultyFilter !== 'all') {
      const selectedDifficulty = Number(difficultyFilter);
      baseList = baseList.filter((challenge) => challenge.difficulty === selectedDifficulty);
    }

    if (!searchQuery.trim()) return baseList;
    const lowerQ = searchQuery.toLowerCase();
    return baseList.filter(c => 
      c.name.toLowerCase().includes(lowerQ) || 
      c.id.toLowerCase().includes(lowerQ) ||
      c.category.toLowerCase().includes(lowerQ) ||
      c.categories.some((category) => category.toLowerCase().includes(lowerQ)) ||
      c.difficulty.toString() === lowerQ ||
      `difficulty ${c.difficulty}`.includes(lowerQ) ||
      c.difficulty_label.toLowerCase().includes(lowerQ)
    );
  }, [challenges, searchQuery, activeSet, difficultyFilter]);

  // Group by category
  const grouped = useMemo(() => {
    const result = filteredChallenges.reduce<Record<string, ChallengeSummary[]>>((acc, c) => {
      const categories = c.categories.length > 0 ? c.categories : [c.category];
      for (const category of new Set(categories)) {
        (acc[category] ??= []).push(c);
      }
      return acc;
    }, {});

    if (activeSet === 'leetcode') {
      for (const items of Object.values(result)) {
        items.sort((left, right) => {
          const difficultyOrder = left.difficulty - right.difficulty;
          if (difficultyOrder !== 0) return difficultyOrder;

          const leftId = Number(left.id.replace(/^lc_/, ''));
          const rightId = Number(right.id.replace(/^lc_/, ''));
          return leftId - rightId;
        });
      }
    }
    return result;
  }, [filteredChallenges, activeSet]);

  const groupedForDisplay = useMemo(() => {
    const entries = Object.entries(grouped);
    if (activeSet === 'codechef') {
      const groupOrder: Record<string, number> = {
        codechef_data_structures_and_algorithms: 0,
        codechef_become_5_star: 1,
      };
      entries.sort(([left], [right]) => {
        const leftGroup = codeChefGroup(left)?.key ?? left;
        const rightGroup = codeChefGroup(right)?.key ?? right;
        const groupDifference = (groupOrder[leftGroup] ?? 99) - (groupOrder[rightGroup] ?? 99);
        return groupDifference || left.localeCompare(right);
      });
    }
    return entries;
  }, [grouped, activeSet]);

  const challengeNumbers = useMemo(
    () => buildChallengeNumberMap(challenges, activeSet),
    [challenges, activeSet],
  );

  const numberForChallenge = (challenge: ChallengeSummary, categoryContext?: string) => {
    const context = numberingContextForDisplay(challenge, activeSet, categoryContext);
    return challengeNumbers.get(numberKey(context, challenge.id));
  };

  const effectiveExportArgs = (challengeId?: string) => ({
    n: challengeId && challengeId === currentId ? localN : exportN,
    seed: challengeId && challengeId === currentId ? localSeed : exportSeed,
  });

  const exportEntryFor = (challenge: ChallengeSummary, categoryContext?: string): PracticeExportEntry => {
    const args = effectiveExportArgs(challenge.id);
    const challengeNumber = numberForChallenge(challenge, categoryContext);
    return {
      ...entryForChallenge(challenge, categoryContext),
      n: Math.min(args.n, challenge.max_n),
      seed: args.seed,
      filename_prefix: challengeNumber?.filename,
      test_count: exportTestCount,
    };
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
    const args = effectiveExportArgs(challenge.id);
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
        Math.min(args.n, challenge.max_n),
        args.seed,
        exportTestCount,
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
        exportN,
        exportSeed,
        exportTestCount,
        updateDownloadProgress(label),
      );
      finishDownload(label);
    } catch (error) {
      failDownload(label, error);
    }
  };

  const renderChallengeRow = (c: ChallengeSummary, categoryContext?: string) => {
    const isCurrent = c.id === currentId;
    const isDone = completed.includes(c.id);
    const isCareerContext =
      activeSet === 'codechef' && (categoryContext ?? c.category).startsWith('codechef_become_5_star');
    const isLocked = !c.unlocked && (activeSet !== 'codechef' || isCareerContext);
    const displayTitle = formatChallengeTitle(c, activeSet, numberForChallenge(c, categoryContext));
    const difficultyDisplay = formatDifficultyLine(c, activeSet);

    let statusIndicator = <span className="w-3 shrink-0" />;
    if (isLocked) {
      statusIndicator = <span className="text-coden-muted shrink-0 text-xs" title="Locked in Career Mode">◆</span>;
    } else if (isDone) {
      statusIndicator = <span className="text-green-400 shrink-0 text-sm font-bold" title="Completed">✓</span>;
    }

    return (
      <li key={c.id} className="flex items-stretch gap-1">
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
          title={isLocked ? "Locked in Career Mode (complete parent nodes first)" : `${c.name} · ${c.required_complexity} · ${c.id}`}
        >
          {statusIndicator}
          <div className="flex-1 min-w-0">
            <div className="truncate">{displayTitle}</div>
            <div
              className={[
                'text-[11px] font-mono truncate mt-0.5',
                isCurrent
                  ? 'text-slate-600 dark:text-coden-muted'
                  : 'text-coden-muted opacity-80',
              ].join(' ')}
            >
              {difficultyDisplay}
            </div>
          </div>
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

  return (
    <div className="flex flex-col h-full overflow-hidden">
      <div className="p-3 shrink-0 border-b border-coden-border bg-coden-surface">
        <input 
          type="text" 
          placeholder="Search challenges"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full bg-coden-bg border border-coden-border rounded px-3 py-1.5 text-sm text-coden-text placeholder-coden-muted focus:outline-none focus:border-coden-accent transition-colors"
        />
        {activeSet === 'leetcode' && (
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
            <optgroup label="Easy">
              <option value="1">Level 1 — Easy</option>
              <option value="2">Level 2 — Easy</option>
              <option value="3">Level 3 — Easy</option>
            </optgroup>
            <optgroup label="Medium">
              <option value="4">Level 4 — Medium</option>
              <option value="5">Level 5 — Medium</option>
              <option value="6">Level 6 — Medium</option>
            </optgroup>
            <optgroup label="Hard">
              <option value="7">Level 7 — Hard</option>
              <option value="8">Level 8 — Hard</option>
              <option value="9">Level 9 — Hard</option>
              <option value="10">Level 10 — Hard</option>
            </optgroup>
          </select>
        )}
        <div className="mt-2 text-[11px] font-mono text-coden-muted">
          {progressLabel(filteredChallenges, completedSet)} solved
          {filteredChallenges.length !== challenges.length && (
            <> · {filteredChallenges.length} of {challenges.length} shown</>
          )}
        </div>
        <div className="mt-2 grid grid-cols-[1fr_1fr_1fr_auto] gap-1 text-[11px]">
          <label className="flex items-center gap-1 text-coden-muted">
            n
            <input
              type="number"
              min={2}
              max={100}
              value={exportN}
              onChange={(event) => setExportN(Math.max(2, Math.min(100, Number(event.target.value) || 16)))}
              className="min-w-0 h-7 bg-coden-bg border border-coden-border rounded px-2 font-mono text-coden-text"
              title="Global n for downloaded practice files"
            />
          </label>
          <label className="flex items-center gap-1 text-coden-muted">
            seed
            <input
              type="number"
              value={exportSeed ?? ''}
              onChange={(event) => setExportSeed(event.target.value === '' ? null : Number(event.target.value))}
              className="min-w-0 h-7 bg-coden-bg border border-coden-border rounded px-2 font-mono text-coden-text"
              title="Global seed for downloaded practice files"
            />
          </label>
          <label className="flex items-center gap-1 text-coden-muted">
            cases
            <input
              type="number"
              min={1}
              max={9}
              value={exportTestCount}
              onChange={(event) => setExportTestCount(Math.max(1, Math.min(9, Number(event.target.value) || 3)))}
              className="min-w-0 h-7 bg-coden-bg border border-coden-border rounded px-2 font-mono text-coden-text"
              title="Number of generated test cases per downloaded practice file"
            />
          </label>
          <button
            type="button"
            onClick={(event) => handleDownloadBundle(
              event,
              filteredChallenges.map((challenge) => exportEntryFor(challenge)),
            )}
            className="h-7 px-2 rounded border border-coden-border text-coden-muted hover:text-coden-text hover:bg-coden-border inline-flex items-center gap-1"
            title="Download all currently shown challenges as standalone Python files"
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
        {groupedForDisplay.map(([category, items]) => {
          // If searching, always expand to show results. Otherwise respect expanded state.
          const isCollapsed = !searchQuery.trim() && !expanded[category];
          const pathGroup = activeSet === 'codechef' ? codeChefGroup(category) : null;
          const groupedEntries = pathGroup
            ? groupedForDisplay.filter(([key]) => codeChefGroup(key)?.key === pathGroup.key)
            : [];
          const isFirstInGroup = !!pathGroup && groupedEntries[0]?.[0] === category;
          const groupItems = groupedEntries.flatMap(([, entryItems]) => entryItems);
          const groupEntries = groupItems.map((item) => exportEntryFor(
            item,
            item.categories.find((itemCategory) => codeChefGroup(itemCategory)?.key === pathGroup?.key) ?? item.category,
          ));
          const groupCollapsed = !!pathGroup && !searchQuery.trim() && !expanded[pathGroup.key];
          const course = activeSet === 'codechef' ? codeChefCourse(category) : null;
          const courseEntries = course
            ? groupedForDisplay.filter(([key]) => codeChefCourse(key)?.key === course.key)
            : [];
          const isFirstInCourse = !!course && courseEntries[0]?.[0] === category;
          const courseItems = courseEntries.flatMap(([, entryItems]) => entryItems);
          const courseBundleEntries = courseItems.map((item) => exportEntryFor(
            item,
            item.categories.find((itemCategory) => codeChefCourse(itemCategory)?.key === course?.key) ?? item.category,
          ));
          const courseCollapsed = !!course && !searchQuery.trim() && !expanded[course.key];
          const subcourse = activeSet === 'codechef' ? codeChefSubcourse(category) : null;
          const subcourseEntries = subcourse
            ? groupedForDisplay.filter(([key]) => codeChefSubcourse(key)?.key === subcourse.key)
            : [];
          const isFirstInSubcourse = !!subcourse && subcourseEntries[0]?.[0] === category;
          const subcourseItems = subcourseEntries.flatMap(([, entryItems]) => entryItems);
          const subcourseBundleEntries = subcourseItems.map((item) => exportEntryFor(
            item,
            item.categories.find((itemCategory) => codeChefSubcourse(itemCategory)?.key === subcourse?.key) ?? item.category,
          ));
          const subcourseCollapsed = !!subcourse && !searchQuery.trim() && !expanded[subcourse.key];
          const categoryEntries = items.map((item) => exportEntryFor(item, category));
          
          return (
            <Fragment key={category}>
            {isFirstInGroup && (
              <div className="mt-2 flex items-center gap-1">
                <button
                  type="button"
                  onClick={() => toggleCategory(pathGroup.key)}
                  className="flex-1 min-w-0 flex items-center justify-between px-2 py-1.5 text-xs leading-5 text-coden-text font-semibold hover:text-coden-accent transition-colors"
                >
                  {progressHeading(pathGroup.label, groupItems, completedSet, "ml-1 text-xs text-coden-muted")}
                  <span style={{ transform: groupCollapsed ? 'rotate(-90deg)' : 'rotate(0deg)' }}>v</span>
                </button>
                <button
                  type="button"
                  onClick={(event) => handleDownloadBundle(event, groupEntries)}
                  className="w-7 h-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
                  title={`Download ${pathGroup.label}`}
                  aria-label={`Download ${pathGroup.label}`}
                >
                  <DownloadIcon className="h-4 w-4" />
                </button>
              </div>
            )}
            {!groupCollapsed && isFirstInCourse && (
              <div className="ml-3 flex items-center gap-1">
                <button
                  type="button"
                  onClick={() => toggleCategory(course.key)}
                  className="flex-1 min-w-0 flex items-center justify-between px-2 py-1.5 text-xs leading-5 text-coden-text font-semibold hover:text-coden-accent transition-colors"
                >
                  {progressHeading(course.label, courseItems, completedSet)}
                  <span style={{ transform: courseCollapsed ? 'rotate(-90deg)' : 'rotate(0deg)' }}>v</span>
                </button>
                <button
                  type="button"
                  onClick={(event) => handleDownloadBundle(event, courseBundleEntries)}
                  className="w-7 h-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
                  title={`Download ${course.label}`}
                  aria-label={`Download ${course.label}`}
                >
                  <DownloadIcon className="h-4 w-4" />
                </button>
              </div>
            )}
            {!groupCollapsed && !courseCollapsed && isFirstInSubcourse && (
              <div className="ml-6 flex items-center gap-1">
                <button
                  type="button"
                  onClick={() => toggleCategory(subcourse.key)}
                  className="flex-1 min-w-0 flex items-center justify-between px-2 py-1.5 text-xs leading-5 text-coden-text font-semibold hover:text-coden-accent transition-colors"
                >
                  {progressHeading(subcourse.label, subcourseItems, completedSet)}
                  <span style={{ transform: subcourseCollapsed ? 'rotate(-90deg)' : 'rotate(0deg)' }}>v</span>
                </button>
                <button
                  type="button"
                  onClick={(event) => handleDownloadBundle(event, subcourseBundleEntries)}
                  className="w-7 h-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
                  title={`Download ${subcourse.label}`}
                  aria-label={`Download ${subcourse.label}`}
                >
                  <DownloadIcon className="h-4 w-4" />
                </button>
              </div>
            )}
            {(!pathGroup || !groupCollapsed) && (!course || !courseCollapsed) && (!subcourse || !subcourseCollapsed) && (
            <div className={`${subcourse ? 'ml-9' : course ? 'ml-6' : pathGroup ? 'ml-3' : ''} mb-3`}>
              <div className="flex items-center gap-1">
                <button
                  onClick={() => toggleCategory(category)}
                  className="flex-1 min-w-0 flex items-center justify-between px-2 py-1.5 text-xs leading-5 text-coden-muted font-semibold hover:text-coden-text transition-colors group select-none"
                >
                  {progressHeading(formatCategory(category), items, completedSet, "ml-1 opacity-60")}
                  <span
                    className="transform transition-transform duration-200 group-hover:text-coden-accent text-[10px]"
                    style={{ transform: isCollapsed ? 'rotate(-90deg)' : 'rotate(0deg)' }}
                  >
                    ▾
                  </span>
                </button>
                <button
                  type="button"
                  onClick={(event) => handleDownloadBundle(event, categoryEntries)}
                  className="w-7 h-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
                  title={`Download ${formatCategory(category)}`}
                  aria-label={`Download ${formatCategory(category)}`}
                >
                  <DownloadIcon className="h-4 w-4" />
                </button>
              </div>
              
              {!isCollapsed && (
                <ul className="mt-1 space-y-0.5">
                  {activeSet === 'codechef' ? items.map((c) => renderChallengeRow(c, category)) : items.map((c) => {
                    const isCurrent = c.id === currentId;
                    const isDone = completed.includes(c.id);
                    const isLocked = !c.unlocked;
                    const displayTitle = formatChallengeTitle(c, activeSet, numberForChallenge(c));
                    const difficultyDisplay = formatDifficultyLine(c, activeSet);

                    let statusIndicator = <span className="w-3 shrink-0" />;
                    if (isLocked) {
                      statusIndicator = <span className="text-coden-muted shrink-0 text-xs" title="Locked in Career Mode">◆</span>;
                    } else if (isDone) {
                      statusIndicator = <span className="text-green-400 shrink-0 text-sm font-bold" title="Completed">✓</span>;
                    }

                    return (
                      <li key={c.id} className="flex items-stretch gap-1">
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
                          title={isLocked ? "Locked in Career Mode (complete parent nodes first)" : `${c.name} · ${c.required_complexity} · ${c.id}`}
                        >
                          {statusIndicator}
                          <div className="flex-1 min-w-0">
                            <div className="truncate">{displayTitle}</div>
                            <div
                              className={[
                                'text-[11px] font-mono truncate mt-0.5',
                                isCurrent
                                  ? 'text-slate-600 dark:text-coden-muted'
                                  : 'text-coden-muted opacity-80',
                              ].join(' ')}
                            >
                              {difficultyDisplay}
                            </div>
                          </div>
                        </button>
                        <button
                          type="button"
                          onClick={(event) => handleDownloadChallenge(event, c)}
                          className="w-7 rounded text-coden-muted hover:text-coden-text hover:bg-coden-border shrink-0 inline-flex items-center justify-center"
                          title={`Download standalone practice file for ${c.name}`}
                          aria-label={`Download ${c.name}`}
                        >
                          <DownloadIcon className="h-4 w-4" />
                        </button>
                      </li>
                    );
                  })}
                </ul>
              )}
            </div>
            )}
            </Fragment>
          );
        })}
        
        {Object.keys(grouped).length === 0 && (
          <div className="flex flex-col items-center justify-center p-8 text-coden-muted space-y-2">
            <span className="text-sm">No algorithms found</span>
            <span className="text-xs">Try a name, id, or category.</span>
          </div>
        )}
      </div>
    </div>
  );
}
