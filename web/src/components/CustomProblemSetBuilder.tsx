import { useEffect, useMemo, useState } from 'react';
import { createPortal } from 'react-dom';

import { ApiError } from '../api/client';
import {
  MAX_CUSTOM_GROUP_DEPTH,
  MAX_CUSTOM_ROOT_SETS,
  addGroupToCustomSet,
  addProblemToCustomSet,
  addTemplateToCustomSet,
  cloneCustomProblemSets,
  copyCustomNode,
  countSetProblems,
  createCustomId,
  createCustomSetFromTemplate,
  moveCustomNode,
  removeCustomNode,
  unwrapCustomGroup,
  updateCustomGroupName,
} from '../lib/customProblemSets';
import { eloDisplayForChallenge } from '../lib/challengeMetrics';
import {
  STANDARD_HIERARCHY_OPTIONS,
  buildPersonalProblemHierarchy,
  buildStandardProblemHierarchy,
  filterProblemHierarchy,
  findHierarchyNode,
  hierarchyNodesToTemplates,
  hierarchyProblemCount,
  type ProblemHierarchyNode,
  type ProblemHierarchyRoot,
  type StandardHierarchySetId,
} from '../lib/problemSetHierarchies';
import {
  MAX_PERSONAL_SET_IMPORT_BYTES,
  importPersonalProblemSets,
  personalProblemSetExportFilename,
  serializePersonalProblemSets,
} from '../lib/personalProblemSetExchange';
import type {
  ChallengeSummary,
  CustomProblemGroup,
  CustomProblemSet,
  CustomProblemTreeNode,
} from '../types/api';


type DragPayload =
  | { kind: 'library-problem'; challengeId: string }
  | { kind: 'tree-node'; setId: string; nodeId: string }
  | { kind: 'hierarchy-root'; rootKey: string }
  | { kind: 'hierarchy-node'; rootKey: string; nodeKey: string };

interface CustomProblemSetBuilderProps {
  savedSets: CustomProblemSet[];
  challenges: ChallengeSummary[];
  saving: boolean;
  onClose: () => void;
  onSave: (sets: CustomProblemSet[]) => Promise<void>;
}

const DRAG_FORMAT = 'application/x-coden-custom-problem-set';
const INITIAL_LIBRARY_LIMIT = 200;

type DragAction = 'move' | 'copy';
type LibraryMode = 'problems' | 'sets';
type LibrarySort =
  | 'leetcode_asc'
  | 'elo_asc'
  | 'elo_desc'
  | 'frequency_desc'
  | 'frequency_asc'
  | 'acceptance_desc';

type Destination = {
  key: string;
  setId: string;
  groupId: string | null;
  label: string;
};

function numericLeetCodeId(challenge: ChallengeSummary): number {
  const value = Number(challenge.leetcode_frontend_id);
  if (Number.isFinite(value)) return value;
  const match = /^lc_(\d+)$/.exec(challenge.id);
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

function displayedElo(challenge: ChallengeSummary): number | null {
  return eloDisplayForChallenge(challenge)?.value ?? null;
}

function compareNullableNumber(
  left: number | null,
  right: number | null,
  direction: 'asc' | 'desc',
): number {
  if (left === null && right === null) return 0;
  if (left === null) return 1;
  if (right === null) return -1;
  return direction === 'asc' ? left - right : right - left;
}

function countProblemPlacements(
  sets: CustomProblemSet[],
  challengeId: string,
): number {
  const countNodes = (nodes: CustomProblemTreeNode[]): number => nodes.reduce(
    (total, node) => total + (
      node.type === 'problem'
        ? Number(node.challenge_id === challengeId)
        : countNodes(node.children)
    ),
    0,
  );
  return sets.reduce((total, set) => total + countNodes(set.nodes), 0);
}

function writeDragPayload(event: React.DragEvent, payload: DragPayload): void {
  const serialized = JSON.stringify(payload);
  event.dataTransfer.effectAllowed = 'copyMove';
  event.dataTransfer.setData(DRAG_FORMAT, serialized);
  event.dataTransfer.setData('text/plain', serialized);
}

function readDragPayload(event: React.DragEvent): DragPayload | null {
  const serialized = event.dataTransfer.getData(DRAG_FORMAT)
    || event.dataTransfer.getData('text/plain');
  if (!serialized) return null;
  try {
    const parsed = JSON.parse(serialized) as Partial<DragPayload>;
    if (parsed.kind === 'library-problem' && typeof parsed.challengeId === 'string') {
      return { kind: parsed.kind, challengeId: parsed.challengeId };
    }
    if (
      parsed.kind === 'tree-node'
      && typeof parsed.setId === 'string'
      && typeof parsed.nodeId === 'string'
    ) {
      return { kind: parsed.kind, setId: parsed.setId, nodeId: parsed.nodeId };
    }
    if (parsed.kind === 'hierarchy-root' && typeof parsed.rootKey === 'string') {
      return { kind: parsed.kind, rootKey: parsed.rootKey };
    }
    if (
      parsed.kind === 'hierarchy-node'
      && typeof parsed.rootKey === 'string'
      && typeof parsed.nodeKey === 'string'
    ) {
      return { kind: parsed.kind, rootKey: parsed.rootKey, nodeKey: parsed.nodeKey };
    }
  } catch {
    return null;
  }
  return null;
}

function errorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    const detail = error.detail;
    if (detail && typeof detail === 'object' && 'detail' in detail) {
      const message = (detail as { detail?: unknown }).detail;
      if (typeof message === 'string') return message;
    }
  }
  return error instanceof Error ? error.message : 'The custom sets could not be saved.';
}

function normalizedDraft(sets: CustomProblemSet[]): CustomProblemSet[] {
  const normalizeNodes = (nodes: CustomProblemTreeNode[]): CustomProblemTreeNode[] => (
    nodes.map((node) => node.type === 'group'
      ? {
          ...node,
          name: node.name.trim(),
          children: normalizeNodes(node.children),
        }
      : node)
  );
  return sets.map((set) => ({
    ...set,
    name: set.name.trim(),
    description: set.description.trim(),
    nodes: normalizeNodes(set.nodes),
  }));
}

export function CustomProblemSetBuilder({
  savedSets,
  challenges,
  saving,
  onClose,
  onSave,
}: CustomProblemSetBuilderProps) {
  const [draft, setDraft] = useState(() => cloneCustomProblemSets(savedSets));
  const [selectedSetId, setSelectedSetId] = useState<string | null>(
    savedSets[0]?.id ?? null,
  );
  const [libraryQuery, setLibraryQuery] = useState('');
  const [libraryDifficulty, setLibraryDifficulty] = useState('all');
  const [libraryTopic, setLibraryTopic] = useState('all');
  const [libraryEloSource, setLibraryEloSource] = useState('all');
  const [libraryMinElo, setLibraryMinElo] = useState('');
  const [libraryMaxElo, setLibraryMaxElo] = useState('');
  const [libraryMinFrequency, setLibraryMinFrequency] = useState('');
  const [libraryFrequencyAvailability, setLibraryFrequencyAvailability] = useState('all');
  const [librarySort, setLibrarySort] = useState<LibrarySort>('leetcode_asc');
  const [libraryLimit, setLibraryLimit] = useState(INITIAL_LIBRARY_LIMIT);
  const [libraryTargetKey, setLibraryTargetKey] = useState<string | null>(null);
  const [libraryMode, setLibraryMode] = useState<LibraryMode>('problems');
  const [selectedSourceRootKey, setSelectedSourceRootKey] = useState<string | null>(null);
  const [expandedSourceNodes, setExpandedSourceNodes] = useState<Record<string, boolean>>({});
  const [collapsedTreeGroups, setCollapsedTreeGroups] = useState<Record<string, boolean>>({});
  const [dragAction, setDragAction] = useState<DragAction>('move');
  const [notice, setNotice] = useState<string | null>(null);
  const [saveError, setSaveError] = useState<string | null>(null);
  const [deleteSetId, setDeleteSetId] = useState<string | null>(null);
  const [confirmDiscard, setConfirmDiscard] = useState(false);
  const [dragOverTarget, setDragOverTarget] = useState<string | null>(null);

  const selectedSet = draft.find((set) => set.id === selectedSetId) ?? null;
  const savedHash = JSON.stringify(savedSets);
  const draftHash = JSON.stringify(draft);
  const hasUnsavedChanges = savedHash !== draftHash;
  const challengeById = useMemo(
    () => new Map(challenges.map((challenge) => [challenge.id, challenge])),
    [challenges],
  );
  const destinationOptions = useMemo(() => {
    const result: Destination[] = [];
    const visit = (
      set: CustomProblemSet,
      nodes: CustomProblemTreeNode[],
      path: string[],
    ) => {
      for (const node of nodes) {
        if (node.type !== 'group') continue;
        const nextPath = [...path, node.name || 'Untitled folder'];
        result.push({
          key: `${set.id}:${node.id}`,
          setId: set.id,
          groupId: node.id,
          label: `${set.name || 'Untitled set'} / ${nextPath.join(' / ')}`,
        });
        visit(set, node.children, nextPath);
      }
    };
    for (const set of draft) {
      result.push({
        key: `${set.id}:root`,
        setId: set.id,
        groupId: null,
        label: `${set.name || 'Untitled set'} / Set root`,
      });
      visit(set, set.nodes, []);
    }
    return result;
  }, [draft]);
  const effectiveLibraryTarget = (
    destinationOptions.find((destination) => destination.key === libraryTargetKey)
    ?? destinationOptions.find((destination) => destination.setId === selectedSetId && destination.groupId === null)
    ?? destinationOptions[0]
    ?? null
  );
  const topicOptions = useMemo(() => {
    const topics = new Set<string>();
    for (const challenge of challenges) {
      for (const topic of challenge.leetcode_topics) {
        const name = String(topic.name || '').trim();
        if (name) topics.add(name);
      }
    }
    return [...topics].sort((left, right) => left.localeCompare(right));
  }, [challenges]);
  const filteredLibraryChallenges = useMemo(() => {
    const query = libraryQuery.trim().toLowerCase();
    const minElo = libraryMinElo.trim() === '' ? null : Number(libraryMinElo);
    const maxElo = libraryMaxElo.trim() === '' ? null : Number(libraryMaxElo);
    const minFrequency = libraryMinFrequency.trim() === ''
      ? null
      : Number(libraryMinFrequency);
    const result = [...challenges]
      .filter((challenge) => (
        (libraryDifficulty === 'all' || challenge.difficulty_label === libraryDifficulty)
        && (
          libraryTopic === 'all'
          || challenge.leetcode_topics.some((topic) => String(topic.name || '') === libraryTopic)
        )
        && (
          libraryEloSource === 'all'
          || (libraryEloSource === 'real' && challenge.elo_rating !== null)
          || (
            libraryEloSource === 'estimated'
            && challenge.elo_rating === null
            && challenge.estimated_elo_rating !== null
          )
          || (
            libraryEloSource === 'unrated'
            && challenge.elo_rating === null
            && challenge.estimated_elo_rating === null
          )
        )
        && (
          libraryFrequencyAvailability === 'all'
          || (libraryFrequencyAvailability === 'available' && challenge.frequency !== null)
          || (libraryFrequencyAvailability === 'missing' && challenge.frequency === null)
        )
        && (minElo === null || (displayedElo(challenge) ?? -Infinity) >= minElo)
        && (maxElo === null || (displayedElo(challenge) ?? Infinity) <= maxElo)
        && (
          minFrequency === null
          || (challenge.frequency ?? -Infinity) >= minFrequency
        )
        && (
          !query
          || challenge.name.toLowerCase().includes(query)
          || challenge.id.toLowerCase().includes(query)
          || challenge.leetcode_frontend_id.toLowerCase().includes(query)
          || challenge.leetcode_topics.some((topic) => (
            String(topic.name || '').toLowerCase().includes(query)
            || String(topic.slug || '').toLowerCase().includes(query)
          ))
        )
      ));
    result.sort((left, right) => {
      let comparison = 0;
      if (librarySort === 'elo_asc') {
        comparison = compareNullableNumber(displayedElo(left), displayedElo(right), 'asc');
      } else if (librarySort === 'elo_desc') {
        comparison = compareNullableNumber(displayedElo(left), displayedElo(right), 'desc');
      } else if (librarySort === 'frequency_desc') {
        comparison = compareNullableNumber(left.frequency, right.frequency, 'desc');
      } else if (librarySort === 'frequency_asc') {
        comparison = compareNullableNumber(left.frequency, right.frequency, 'asc');
      } else if (librarySort === 'acceptance_desc') {
        comparison = compareNullableNumber(left.acceptance_rate, right.acceptance_rate, 'desc');
      }
      return comparison || numericLeetCodeId(left) - numericLeetCodeId(right);
    });
    return result;
  }, [
    challenges,
    libraryDifficulty,
    libraryEloSource,
    libraryFrequencyAvailability,
    libraryMaxElo,
    libraryMinElo,
    libraryMinFrequency,
    libraryQuery,
    librarySort,
    libraryTopic,
  ]);
  const libraryChallenges = filteredLibraryChallenges.slice(0, libraryLimit);
  const filteredHierarchyChallengeIds = useMemo(
    () => filteredLibraryChallenges.map((challenge) => challenge.id),
    [filteredLibraryChallenges],
  );
  const hierarchyRootForKey = (rootKey: string): ProblemHierarchyRoot | null => {
    let root: ProblemHierarchyRoot | null = null;
    if (rootKey.startsWith('standard:')) {
      const setId = rootKey.slice('standard:'.length) as StandardHierarchySetId;
      if (!STANDARD_HIERARCHY_OPTIONS.some((option) => option.id === setId)) return null;
      root = buildStandardProblemHierarchy(setId, challenges);
    }
    if (!root && rootKey.startsWith('personal:')) {
      const set = draft.find((candidate) => `personal:${candidate.id}` === rootKey);
      root = set ? buildPersonalProblemHierarchy(set) : null;
    }
    return root ? filterProblemHierarchy(root, filteredHierarchyChallengeIds) : null;
  };
  const selectedSourceRoot = useMemo(
    () => selectedSourceRootKey ? hierarchyRootForKey(selectedSourceRootKey) : null,
    [challenges, draft, filteredHierarchyChallengeIds, selectedSourceRootKey],
  );

  useEffect(() => {
    setLibraryLimit(INITIAL_LIBRARY_LIMIT);
  }, [
    libraryDifficulty,
    libraryEloSource,
    libraryFrequencyAvailability,
    libraryMaxElo,
    libraryMinElo,
    libraryMinFrequency,
    libraryQuery,
    librarySort,
    libraryTopic,
  ]);

  const selectSet = (setId: string) => {
    setSelectedSetId(setId);
    setLibraryTargetKey(`${setId}:root`);
    setDeleteSetId(null);
    setNotice(null);
  };

  const addSet = () => {
    if (draft.length >= MAX_CUSTOM_ROOT_SETS) {
      setNotice(`Personal can contain at most ${MAX_CUSTOM_ROOT_SETS} root sets.`);
      return;
    }
    let suffix = draft.length + 1;
    let name = `My problem set ${suffix}`;
    while (draft.some((set) => set.name === name)) {
      suffix += 1;
      name = `My problem set ${suffix}`;
    }
    const next: CustomProblemSet = {
      id: createCustomId('set'),
      name,
      description: '',
      career_mode: false,
      nodes: [],
    };
    setDraft((sets) => [...sets, next]);
    setSelectedSetId(next.id);
    setLibraryTargetKey(`${next.id}:root`);
    setDeleteSetId(null);
    setNotice('New set created. Give it a clear name, then add problems or folders.');
  };

  const confirmDeleteSet = () => {
    if (!deleteSetId) return;
    const remaining = draft.filter((set) => set.id !== deleteSetId);
    setDraft(remaining);
    setSelectedSetId((current) => (
      current === deleteSetId ? remaining[0]?.id ?? null : current
    ));
    setLibraryTargetKey((current) => (
      current?.startsWith(`${deleteSetId}:`)
        ? remaining[0] ? `${remaining[0].id}:root` : null
        : current
    ));
    setDeleteSetId(null);
    setNotice('Set removed from the draft. Save to apply the change.');
  };

  const changeSet = (
    patch: Partial<Pick<CustomProblemSet, 'name' | 'description' | 'career_mode'>>,
  ) => {
    if (!selectedSetId) return;
    setDraft((sets) => sets.map((set) => (
      set.id === selectedSetId ? { ...set, ...patch } : set
    )));
  };

  const shiftSelectedSet = (direction: -1 | 1) => {
    if (!selectedSetId) return;
    setDraft((sets) => {
      const index = sets.findIndex((set) => set.id === selectedSetId);
      const target = index + direction;
      if (index < 0 || target < 0 || target >= sets.length) return sets;
      const copy = [...sets];
      [copy[index], copy[target]] = [copy[target]!, copy[index]!];
      return copy;
    });
  };

  const exportSets = (sets: CustomProblemSet[], setName?: string) => {
    if (sets.length === 0) {
      setNotice('There are no Personal roots to export.');
      return;
    }
    const blob = new Blob(
      [serializePersonalProblemSets(sets, challenges)],
      { type: 'application/json;charset=utf-8' },
    );
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = personalProblemSetExportFilename(setName);
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 0);
    setNotice(`${sets.length} Personal root${sets.length === 1 ? '' : 's'} exported in cOde(n) exchange format.`);
  };

  const importSets = async (file: File, input: HTMLInputElement) => {
    try {
      if (file.size > MAX_PERSONAL_SET_IMPORT_BYTES) {
        throw new Error('The selected exchange is larger than the 5 MB import limit.');
      }
      const result = importPersonalProblemSets(await file.text(), draft, challenges);
      setDraft(result.sets);
      const firstImportedSet = result.sets[draft.length];
      if (firstImportedSet) {
        setSelectedSetId(firstImportedSet.id);
        setLibraryTargetKey(`${firstImportedSet.id}:root`);
      }
      const details = [
        `${result.importedSetCount} root set(s)`,
        `${result.importedProblemCount} problem placement(s)`,
      ];
      if (result.warnings.length > 0) details.push(result.warnings.join(' '));
      setNotice(`Imported ${details.join(' · ')} Save to apply the imported structure.`);
      setSaveError(null);
    } catch (error) {
      setNotice(null);
      setSaveError(error instanceof Error ? error.message : 'Unable to import Personal sets.');
    } finally {
      input.value = '';
    }
  };

  const applyTreeResult = (
    result: ReturnType<typeof addProblemToCustomSet>,
    successMessage: string,
    ignoredMessage = 'That problem already exists in this leaf, so nothing was added.',
  ) => {
    if (!result.ok) {
      setNotice(result.message);
      return;
    }
    if (result.ignored) {
      setNotice(ignoredMessage);
      setSaveError(null);
      return;
    }
    setDraft(result.sets);
    setNotice(successMessage);
    setSaveError(null);
  };

  const addProblem = (
    challengeId: string,
    targetSetId: string | null,
    targetGroupId: string | null,
  ) => {
    if (!targetSetId) {
      setNotice('Create or select a problem set first.');
      return;
    }
    const challenge = challengeById.get(challengeId);
    applyTreeResult(
      addProblemToCustomSet(draft, targetSetId, targetGroupId, challengeId),
      `${challenge?.name ?? 'Problem'} added. Save when the structure is ready.`,
    );
  };

  const addAllFilteredProblems = () => {
    if (!effectiveLibraryTarget) {
      setNotice('Create or select a problem set first.');
      return;
    }
    if (filteredLibraryChallenges.length === 0) {
      setNotice('No filtered problems are available to add.');
      return;
    }

    const beforeSet = draft.find((set) => set.id === effectiveLibraryTarget.setId);
    const result = addTemplateToCustomSet(
      draft,
      effectiveLibraryTarget.setId,
      effectiveLibraryTarget.groupId,
      filteredLibraryChallenges.map((challenge) => ({
        type: 'problem' as const,
        challenge_id: challenge.id,
      })),
    );
    if (!result.ok) {
      setNotice(result.message);
      return;
    }

    const afterSet = result.sets.find((set) => set.id === effectiveLibraryTarget.setId);
    const addedCount = Math.max(
      0,
      (afterSet ? countSetProblems(afterSet) : 0)
        - (beforeSet ? countSetProblems(beforeSet) : 0),
    );
    const ignoredCount = filteredLibraryChallenges.length - addedCount;
    if (addedCount === 0) {
      setNotice('All filtered problems already exist in this destination leaf.');
      setSaveError(null);
      return;
    }

    setDraft(result.sets);
    setNotice(
      `Added ${addedCount} filtered ${addedCount === 1 ? 'problem' : 'problems'} to `
      + `${effectiveLibraryTarget.label}.`
      + (
        ignoredCount > 0
          ? ` ${ignoredCount} same-leaf ${ignoredCount === 1 ? 'duplicate was' : 'duplicates were'} ignored.`
          : ''
      )
      + ' Save when the structure is ready.',
    );
    setSaveError(null);
  };

  const addGroup = (targetGroupId: string | null) => {
    if (!selectedSetId) return;
    applyTreeResult(
      addGroupToCustomSet(draft, selectedSetId, targetGroupId),
      'Folder added. Rename it to describe the skill or practice stage.',
    );
  };

  const handleDrop = (
    event: React.DragEvent,
    targetSetId: string,
    targetGroupId: string | null,
    beforeNodeId: string | null,
  ) => {
    event.preventDefault();
    event.stopPropagation();
    setDragOverTarget(null);
    const payload = readDragPayload(event);
    if (!payload) {
      setNotice('This item cannot be added to a custom problem set.');
      return;
    }
    if (payload.kind === 'library-problem') {
      const challenge = challengeById.get(payload.challengeId);
      applyTreeResult(
        addProblemToCustomSet(
          draft,
          targetSetId,
          targetGroupId,
          payload.challengeId,
          beforeNodeId,
        ),
        `${challenge?.name ?? 'Problem'} added.`,
      );
      return;
    }
    if (payload.kind === 'hierarchy-root' || payload.kind === 'hierarchy-node') {
      const root = hierarchyRootForKey(payload.rootKey);
      const node = payload.kind === 'hierarchy-node'
        ? root && findHierarchyNode(root.nodes, payload.nodeKey)
        : null;
      if (!root || (payload.kind === 'hierarchy-node' && !node)) {
        setNotice('The source hierarchy is no longer available.');
        return;
      }
      const sourceNodes = node ? [node] : root.nodes;
      applyTreeResult(
        addTemplateToCustomSet(
          draft,
          targetSetId,
          targetGroupId,
          hierarchyNodesToTemplates(sourceNodes),
          beforeNodeId,
        ),
        `${node?.type === 'group' ? node.name : root.name} copied with its complete hierarchy.`,
      );
      return;
    }
    const shouldCopy = dragAction === 'copy' || event.ctrlKey;
    applyTreeResult(
      shouldCopy
        ? copyCustomNode(
            draft,
            payload.setId,
            payload.nodeId,
            targetSetId,
            targetGroupId,
            beforeNodeId,
          )
        : moveCustomNode(
            draft,
            payload.setId,
            payload.nodeId,
            targetSetId,
            targetGroupId,
            beforeNodeId,
          ),
      shouldCopy
        ? 'Item copied with its complete structure. Save to keep it.'
        : 'Item moved to the selected position. Save to keep it.',
    );
  };

  const uniqueRootName = (baseName: string): string => {
    if (!draft.some((set) => set.name === baseName)) return baseName;
    let suffix = 2;
    while (draft.some((set) => set.name === `${baseName} ${suffix}`)) suffix += 1;
    return `${baseName} ${suffix}`;
  };

  const copyHierarchyAsRoot = (rootKey: string) => {
    const root = hierarchyRootForKey(rootKey);
    if (!root) {
      setNotice('The source hierarchy is no longer available.');
      return;
    }
    const result = createCustomSetFromTemplate(
      draft,
      uniqueRootName(root.name),
      root.kind === 'standard'
        ? `Copied from the standard ${root.name} hierarchy.`
        : root.description,
      hierarchyNodesToTemplates(root.nodes),
      root.career_mode,
    );
    if (!result.ok) {
      setNotice(result.message);
      return;
    }
    const created = result.sets[result.sets.length - 1]!;
    setDraft(result.sets);
    setSelectedSetId(created.id);
    setLibraryTargetKey(`${created.id}:root`);
    setNotice(`${root.name} copied as a new Personal root.`);
    setSaveError(null);
  };

  const handleRootDrop = (event: React.DragEvent) => {
    event.preventDefault();
    event.stopPropagation();
    setDragOverTarget(null);
    const payload = readDragPayload(event);
    if (payload?.kind !== 'hierarchy-root') {
      setNotice('Drop a standard or personal set root here to create another Personal root.');
      return;
    }
    copyHierarchyAsRoot(payload.rootKey);
  };

  const copyHierarchyNodeToTarget = (
    node: ProblemHierarchyNode,
  ) => {
    if (!effectiveLibraryTarget) {
      setNotice('Create a Personal root before copying this hierarchy.');
      return;
    }
    applyTreeResult(
      addTemplateToCustomSet(
        draft,
        effectiveLibraryTarget.setId,
        effectiveLibraryTarget.groupId,
        hierarchyNodesToTemplates([node]),
      ),
      `${node.type === 'group' ? node.name : 'Problem'} copied to ${effectiveLibraryTarget.label}.`,
    );
  };

  const handleSave = async () => {
    const clean = normalizedDraft(draft);
    const emptySet = clean.find((set) => !set.name);
    if (emptySet) {
      setSaveError('Every problem set needs a name.');
      setSelectedSetId(emptySet.id);
      return;
    }
    const emptyGroupSet = clean.find((set) => {
      const hasEmpty = (nodes: CustomProblemTreeNode[]): boolean => nodes.some((node) => (
        node.type === 'group' && (!node.name || hasEmpty(node.children))
      ));
      return hasEmpty(set.nodes);
    });
    if (emptyGroupSet) {
      setSaveError('Every folder needs a name.');
      setSelectedSetId(emptyGroupSet.id);
      return;
    }
    setSaveError(null);
    try {
      await onSave(clean);
      onClose();
    } catch (error) {
      setSaveError(errorMessage(error));
    }
  };

  const requestClose = () => {
    if (!hasUnsavedChanges) {
      onClose();
      return;
    }
    setConfirmDiscard(true);
  };

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key !== 'Escape' || saving) return;
      event.preventDefault();
      requestClose();
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  });

  const dropTargetProps = (
    setId: string,
    groupId: string | null,
    beforeNodeId: string | null = null,
  ) => {
    const key = `${setId}:${groupId ?? 'root'}:${beforeNodeId ?? 'end'}`;
    return {
      onDragOver: (event: React.DragEvent) => {
        event.preventDefault();
        event.dataTransfer.dropEffect = dragAction === 'copy' || event.ctrlKey ? 'copy' : 'move';
        setDragOverTarget(key);
      },
      onDragLeave: (event: React.DragEvent) => {
        if (!event.currentTarget.contains(event.relatedTarget as Node | null)) {
          setDragOverTarget((current) => current === key ? null : current);
        }
      },
      onDrop: (event: React.DragEvent) => handleDrop(
        event,
        setId,
        groupId,
        beforeNodeId,
      ),
      isActive: dragOverTarget === key,
    };
  };

  const renderDropSlot = (
    setId: string,
    groupId: string | null,
    beforeNodeId: string | null,
  ) => {
    const drop = dropTargetProps(setId, groupId, beforeNodeId);
    return (
      <div
        key={`drop:${setId}:${groupId ?? 'root'}:${beforeNodeId ?? 'end'}`}
        onDragOver={drop.onDragOver}
        onDragLeave={drop.onDragLeave}
        onDrop={drop.onDrop}
        className={[
          'my-1 flex min-h-4 items-center justify-center rounded border border-dashed text-[10px] transition-all',
          drop.isActive
            ? 'min-h-9 border-coden-accent bg-coden-accent/10 text-coden-accent'
            : 'border-transparent text-transparent hover:border-coden-border hover:text-coden-muted',
        ].join(' ')}
      >
        {drop.isActive ? `${dragAction === 'copy' ? 'Copy' : 'Move'} to this position` : 'Drop position'}
      </div>
    );
  };

  const renderNodeList = (
    nodes: CustomProblemTreeNode[],
    set: CustomProblemSet,
    groupId: string | null,
    depth: number,
  ): React.ReactNode => (
    <>
      {nodes.map((node) => (
        <div key={`position:${node.id}`}>
          {renderDropSlot(set.id, groupId, node.id)}
          {renderTreeNode(node, set, depth)}
        </div>
      ))}
      {renderDropSlot(set.id, groupId, null)}
    </>
  );

  const renderTreeNode = (
    node: CustomProblemTreeNode,
    set: CustomProblemSet,
    depth: number,
  ): React.ReactNode => {
    if (node.type === 'problem') {
      const challenge = challengeById.get(node.challenge_id);
      const elo = challenge ? eloDisplayForChallenge(challenge) : null;
      return (
        <div
          key={node.id}
          draggable
          onDragStart={(event) => writeDragPayload(event, {
            kind: 'tree-node',
            setId: set.id,
            nodeId: node.id,
          })}
          className="group flex items-center gap-2 rounded border border-coden-border bg-coden-bg px-2 py-2"
        >
          <span
            className="cursor-grab select-none font-mono text-coden-muted"
            title={`Drag to ${dragAction} this problem at any insertion line`}
            aria-hidden="true"
          >
            ::
          </span>
          <div className="min-w-0 flex-1">
            <div className="truncate text-sm text-coden-text">
              {challenge?.name ?? node.challenge_id}
            </div>
            <div className="mt-0.5 truncate font-mono text-[10px] text-coden-muted">
              LC {challenge?.leetcode_frontend_id || node.challenge_id.replace('lc_', '')}
              {challenge ? ` · ${challenge.difficulty_label}` : ''}
              {elo ? ` · ${elo.estimated ? 'Est. ' : ''}Elo ${Math.round(elo.value)}` : ' · Elo —'}
              {challenge?.frequency !== null && challenge?.frequency !== undefined
                ? ` · Freq ${challenge.frequency.toFixed(1)}%`
                : ' · Freq —'}
            </div>
          </div>
          <button
            type="button"
            onClick={() => {
              setDraft((sets) => removeCustomNode(sets, set.id, node.id));
              setNotice('Problem removed from the draft. Save to apply.');
            }}
            className="rounded px-1.5 py-1 text-xs text-coden-muted hover:bg-rose-500/15 hover:text-rose-300"
            title="Remove problem from this set"
          >
            Remove
          </button>
        </div>
      );
    }
    return renderGroup(node, set, depth);
  };

  const renderGroup = (
    group: CustomProblemGroup,
    set: CustomProblemSet,
    depth: number,
  ): React.ReactNode => {
    const collapsed = Boolean(collapsedTreeGroups[group.id]);
    return (
      <div
        key={group.id}
        className="rounded-lg border border-coden-border bg-coden-surface/70 p-2"
      >
        <div
          draggable
          onDragStart={(event) => {
            event.stopPropagation();
            writeDragPayload(event, {
              kind: 'tree-node',
              setId: set.id,
              nodeId: group.id,
            });
          }}
          className="flex items-center gap-2"
        >
          <span
            className="cursor-grab select-none font-mono text-coden-muted"
            title={`Drag to ${dragAction} this folder, including every nested folder and problem`}
            aria-hidden="true"
          >
            ::
          </span>
          <button
            type="button"
            draggable={false}
            onClick={(event) => {
              event.stopPropagation();
              setCollapsedTreeGroups((current) => ({
                ...current,
                [group.id]: !current[group.id],
              }));
            }}
            className="flex h-6 w-6 shrink-0 items-center justify-center rounded border border-coden-border font-mono text-[11px] text-coden-muted hover:border-coden-accent hover:text-coden-accent"
            title={`${collapsed ? 'Expand' : 'Collapse'} ${group.name || 'this folder'}`}
            aria-label={`${collapsed ? 'Expand' : 'Collapse'} ${group.name || 'folder'}`}
            aria-expanded={!collapsed}
          >
            {collapsed ? '>' : 'v'}
          </button>
          <span className="shrink-0 rounded bg-coden-border px-1.5 py-0.5 font-mono text-[10px] text-coden-muted">
            Level {depth}
          </span>
          <input
            value={group.name}
            onChange={(event) => setDraft((sets) => updateCustomGroupName(
              sets,
              set.id,
              group.id,
              event.target.value,
            ))}
            maxLength={80}
            aria-label={`Folder name at level ${depth}`}
            className="min-w-0 flex-1 rounded border border-transparent bg-transparent px-1.5 py-1 text-sm font-semibold text-coden-text hover:border-coden-border focus:border-coden-accent focus:outline-none"
          />
          {depth < MAX_CUSTOM_GROUP_DEPTH && (
            <button
              type="button"
              onClick={() => addGroup(group.id)}
              className="rounded border border-coden-border px-2 py-1 text-[11px] text-coden-muted hover:bg-coden-border hover:text-coden-text"
            >
              Add subfolder
            </button>
          )}
          <button
            type="button"
            onClick={() => {
              const result = unwrapCustomGroup(draft, set.id, group.id);
              if (!result.ok) {
                setNotice(result.message);
                return;
              }
              setDraft(result.sets);
              setCollapsedTreeGroups((current) => {
                const next = { ...current };
                delete next[group.id];
                return next;
              });
              setNotice(
                'Folder level removed. Its folders and problems were promoted in place; '
                + 'same-leaf duplicates were ignored.',
              );
            }}
            className="rounded border border-coden-border px-2 py-1 text-[11px] text-coden-muted hover:border-coden-accent hover:text-coden-accent"
            title="Remove only this folder level and promote its contents to the parent"
          >
            Remove level
          </button>
          <button
            type="button"
            onClick={() => {
              setDraft((sets) => removeCustomNode(sets, set.id, group.id));
              setNotice('Folder and its contents removed from the draft. Save to apply.');
            }}
            className="rounded px-1.5 py-1 text-[11px] text-coden-muted hover:bg-rose-500/15 hover:text-rose-300"
            title="Delete this folder and everything inside it"
          >
            Delete branch
          </button>
        </div>
        {!collapsed && (
          <div className="ml-4 mt-2 border-l border-coden-border pl-3">
            {renderNodeList(group.children, set, group.id, depth + 1)}
          </div>
        )}
      </div>
    );
  };

  const renderHierarchyNodes = (
    nodes: ProblemHierarchyNode[],
    rootKey: string,
    depth = 0,
  ): React.ReactNode => (
    <div className={depth === 0 ? 'space-y-1' : 'ml-3 mt-1 space-y-1 border-l border-coden-border pl-2'}>
      {nodes.map((node) => {
        if (node.type === 'problem') {
          const challenge = challengeById.get(node.challenge_id);
          return (
            <div
              key={node.key}
              draggable={Boolean(effectiveLibraryTarget)}
              onDragStart={(event) => writeDragPayload(event, {
                kind: 'hierarchy-node',
                rootKey,
                nodeKey: node.key,
              })}
              className="flex cursor-grab items-center gap-2 rounded border border-transparent px-2 py-1.5 hover:border-coden-border hover:bg-coden-border/30"
            >
              <span className="font-mono text-[10px] text-coden-muted">::</span>
              <div className="min-w-0 flex-1">
                <div className="truncate text-[11px] text-coden-text">
                  {challenge?.name ?? node.challenge_id}
                </div>
                <div className="font-mono text-[9px] text-coden-muted">
                  LC {challenge?.leetcode_frontend_id || node.challenge_id.replace(/^lc_/, '')}
                </div>
              </div>
              <button
                type="button"
                disabled={!effectiveLibraryTarget}
                onClick={() => copyHierarchyNodeToTarget(node)}
                className="rounded border border-coden-border px-1.5 py-1 text-[9px] text-coden-muted hover:border-coden-accent hover:text-coden-accent disabled:opacity-40"
              >
                Copy
              </button>
            </div>
          );
        }
        const expanded = Boolean(expandedSourceNodes[node.key]);
        return (
          <div key={node.key}>
            <div
              draggable={Boolean(effectiveLibraryTarget)}
              onDragStart={(event) => writeDragPayload(event, {
                kind: 'hierarchy-node',
                rootKey,
                nodeKey: node.key,
              })}
              className="flex cursor-grab items-center gap-2 rounded border border-transparent px-2 py-1.5 hover:border-coden-border hover:bg-coden-border/30"
            >
              <button
                type="button"
                onClick={() => setExpandedSourceNodes((current) => ({
                  ...current,
                  [node.key]: !current[node.key],
                }))}
                className="min-w-0 flex-1 text-left"
              >
                <span className="mr-1.5 font-mono text-[9px] text-coden-muted">
                  {expanded ? 'v' : '>'}
                </span>
                <span className="text-[11px] font-semibold text-coden-text">
                  {node.name}
                </span>
                <span className="ml-1.5 font-mono text-[9px] text-coden-muted">
                  {hierarchyProblemCount(node.children)}
                </span>
              </button>
              <button
                type="button"
                disabled={!effectiveLibraryTarget}
                onClick={() => copyHierarchyNodeToTarget(node)}
                className="rounded border border-coden-border px-1.5 py-1 text-[9px] text-coden-muted hover:border-coden-accent hover:text-coden-accent disabled:opacity-40"
                title={`Copy ${node.name} and its complete hierarchy`}
              >
                Copy tree
              </button>
            </div>
            {expanded && renderHierarchyNodes(node.children, rootKey, depth + 1)}
          </div>
        );
      })}
    </div>
  );

  const copyHierarchyRootToTarget = (rootKey: string) => {
    const root = hierarchyRootForKey(rootKey);
    if (!root || !effectiveLibraryTarget) {
      setNotice('Choose a Personal destination before copying this hierarchy.');
      return;
    }
    applyTreeResult(
      addTemplateToCustomSet(
        draft,
        effectiveLibraryTarget.setId,
        effectiveLibraryTarget.groupId,
        hierarchyNodesToTemplates(root.nodes),
      ),
      `${root.name} copied into ${effectiveLibraryTarget.label}.`,
    );
  };

  const renderSourceRoot = (
    rootKey: string,
    name: string,
    description: string,
    kind: 'standard' | 'personal',
    problemCount: number | null,
    careerMode: boolean,
  ) => {
    const selected = selectedSourceRootKey === rootKey;
    return (
      <div
        key={rootKey}
        draggable
        onDragStart={(event) => writeDragPayload(event, {
          kind: 'hierarchy-root',
          rootKey,
        })}
        className={[
          'rounded border',
          selected
            ? 'border-coden-accent bg-coden-accent/5'
            : 'border-coden-border bg-coden-bg/40',
        ].join(' ')}
      >
        <div className="flex items-start gap-2 p-2">
          <button
            type="button"
            onClick={() => setSelectedSourceRootKey(selected ? null : rootKey)}
            className="min-w-0 flex-1 text-left"
          >
            <span className="flex min-w-0 items-center gap-1.5 text-xs font-semibold text-coden-text">
              <span className="mr-1.5 font-mono text-[9px] text-coden-muted">
                {selected ? 'v' : '>'}
              </span>
              <span className="min-w-0 truncate">{name}</span>
              {careerMode && (
                <span className="shrink-0 rounded border border-coden-accent/40 px-1 py-0.5 font-mono text-[9px] text-coden-accent">
                  Career
                </span>
              )}
            </span>
            <span className="mt-0.5 block line-clamp-2 text-[9px] leading-3 text-coden-muted">
              {kind === 'standard' ? 'Standard set' : 'Personal set'}
              {problemCount !== null ? ` · ${problemCount} problems` : ''}
              {' · '}
              {description || 'No description'}
            </span>
          </button>
          <div className="flex shrink-0 flex-col gap-1">
            <button
              type="button"
              disabled={draft.length >= MAX_CUSTOM_ROOT_SETS}
              onClick={() => copyHierarchyAsRoot(rootKey)}
              className="rounded border border-coden-border px-1.5 py-1 text-[9px] text-coden-muted hover:border-coden-accent hover:text-coden-accent disabled:cursor-not-allowed disabled:opacity-35"
              title={`Copy ${name} as another Personal root`}
            >
              Copy as root
            </button>
            <button
              type="button"
              disabled={!effectiveLibraryTarget}
              onClick={() => copyHierarchyRootToTarget(rootKey)}
              className="rounded border border-coden-border px-1.5 py-1 text-[9px] text-coden-muted hover:border-coden-accent hover:text-coden-accent disabled:cursor-not-allowed disabled:opacity-35"
              title={`Copy the complete ${name} hierarchy into the selected destination`}
            >
              Copy into
            </button>
          </div>
        </div>
        {selected && selectedSourceRoot && (
          <div className="max-h-[360px] overflow-y-auto border-t border-coden-border p-2">
            {selectedSourceRoot.nodes.length > 0
              ? renderHierarchyNodes(selectedSourceRoot.nodes, rootKey)
              : (
                  <div className="px-2 py-4 text-center text-[10px] text-coden-muted">
                    This set has no available hierarchy.
                  </div>
                )}
          </div>
        )}
      </div>
    );
  };

  const destinationDrop = effectiveLibraryTarget
    ? dropTargetProps(
        effectiveLibraryTarget.setId,
        effectiveLibraryTarget.groupId,
      )
    : null;
  const rootDropActive = dragOverTarget === 'personal-root-create';

  return createPortal(
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="custom-set-builder-title"
      className="fixed inset-0 z-[100] bg-coden-bg"
    >
      <div className="flex h-screen w-screen flex-col overflow-hidden bg-coden-bg">
        <div className="flex items-start justify-between gap-5 border-b border-coden-border bg-coden-surface px-5 py-4">
          <div>
            <div className="flex items-center gap-3">
              <h2 id="custom-set-builder-title" className="text-lg font-semibold text-coden-text">
                Personal problem-set builder
              </h2>
              <span className="rounded-full border border-coden-border px-2 py-0.5 font-mono text-[10px] text-coden-muted">
                Up to 5 Personal roots
              </span>
              <span className="rounded-full border border-coden-border px-2 py-0.5 font-mono text-[10px] text-coden-muted">
                Up to 3 folder levels per root
              </span>
            </div>
            <p className="mt-1 max-w-3xl text-xs leading-5 text-coden-muted">
              Build personal practice paths by placing LeetCode problems at exact positions.
              Everything is stored only in the active profile; canonical problem files stay unchanged.
            </p>
          </div>
          <div className="flex shrink-0 items-center gap-3">
            <div className="flex items-center gap-1 rounded-lg border border-coden-border bg-coden-bg p-1">
              <button
                type="button"
                disabled={!selectedSet}
                onClick={() => selectedSet && exportSets([selectedSet], selectedSet.name)}
                className="rounded px-2 py-1.5 text-[10px] font-semibold text-coden-muted hover:bg-coden-border hover:text-coden-text disabled:cursor-not-allowed disabled:opacity-35"
                title="Export the selected Personal root with its complete hierarchy"
              >
                Export selected
              </button>
              <button
                type="button"
                disabled={draft.length === 0}
                onClick={() => exportSets(draft)}
                className="rounded px-2 py-1.5 text-[10px] font-semibold text-coden-muted hover:bg-coden-border hover:text-coden-text disabled:cursor-not-allowed disabled:opacity-35"
                title="Export every Personal root"
              >
                Export all
              </button>
              <label
                className="cursor-pointer rounded px-2 py-1.5 text-[10px] font-semibold text-coden-muted hover:bg-coden-border hover:text-coden-text"
                title="Import a versioned cOde(n) Personal-set exchange"
              >
                Import
                <input
                  type="file"
                  accept="application/json,.json"
                  className="sr-only"
                  onChange={(event) => {
                    const file = event.target.files?.[0];
                    if (file) void importSets(file, event.currentTarget);
                  }}
                />
              </label>
            </div>
            <div className="rounded-lg border border-coden-border bg-coden-bg p-1">
              <span className="px-2 text-[10px] font-semibold uppercase tracking-wider text-coden-muted">
                Drag action
              </span>
              {(['move', 'copy'] as const).map((action) => (
                <button
                  key={action}
                  type="button"
                  onClick={() => setDragAction(action)}
                  className={[
                    'rounded px-3 py-1.5 text-xs font-semibold capitalize',
                    dragAction === action
                      ? 'bg-coden-accent text-[var(--coden-accent-contrast)]'
                      : 'text-coden-muted hover:bg-coden-border hover:text-coden-text',
                  ].join(' ')}
                >
                  {action}
                </button>
              ))}
            </div>
            <div className="max-w-[260px] text-[10px] leading-4 text-coden-muted">
              {dragAction === 'copy'
                ? 'Copy duplicates a complete folder tree and every problem inside it.'
                : 'Move relocates an item to the exact insertion line. Hold Ctrl while dropping to copy.'}
            </div>
            <button
              type="button"
              onClick={requestClose}
              disabled={saving}
              className="rounded border border-coden-border px-3 py-1.5 text-xs text-coden-muted hover:bg-coden-border hover:text-coden-text disabled:opacity-50"
            >
              Close
            </button>
          </div>
        </div>

        <div className="grid min-h-0 flex-1 grid-cols-[260px_minmax(480px,1fr)_440px] overflow-x-auto">
          <aside className="flex min-h-0 flex-col border-r border-coden-border bg-coden-surface/50">
            <div className="border-b border-coden-border p-3">
              <div
                onDragOver={(event) => {
                  event.preventDefault();
                  event.dataTransfer.dropEffect = 'copy';
                  setDragOverTarget('personal-root-create');
                }}
                onDragLeave={(event) => {
                  if (!event.currentTarget.contains(event.relatedTarget as Node | null)) {
                    setDragOverTarget((current) => (
                      current === 'personal-root-create' ? null : current
                    ));
                  }
                }}
                onDrop={handleRootDrop}
                className={[
                  'rounded border border-dashed p-1 transition-colors',
                  rootDropActive
                    ? 'border-coden-accent bg-coden-accent/10'
                    : 'border-transparent',
                ].join(' ')}
              >
                <button
                  type="button"
                  onClick={addSet}
                  disabled={draft.length >= MAX_CUSTOM_ROOT_SETS}
                  className="w-full rounded bg-coden-accent px-3 py-2 text-sm font-semibold text-[var(--coden-accent-contrast)] hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-40"
                >
                  New Personal root ({draft.length}/{MAX_CUSTOM_ROOT_SETS})
                </button>
                <div className="mt-1 text-center text-[9px] text-coden-muted">
                  Drop a standard or personal set here to copy its whole hierarchy as a root.
                </div>
              </div>
              <p className="mt-2 text-[10px] leading-4 text-coden-muted">
                Each entry below is a root under Personal. Drop an item on a root to
                {dragAction === 'copy' ? ' copy' : ' move'} it to that set's root.
              </p>
            </div>
            <div className="min-h-0 flex-1 space-y-1 overflow-y-auto p-2">
              {draft.map((set) => {
                const drop = dropTargetProps(set.id, null);
                return (
                  <button
                    key={set.id}
                    type="button"
                    onClick={() => selectSet(set.id)}
                    onDragOver={drop.onDragOver}
                    onDragLeave={drop.onDragLeave}
                    onDrop={drop.onDrop}
                    className={[
                      'w-full rounded border px-3 py-2 text-left transition-colors',
                      selectedSetId === set.id
                        ? 'border-coden-accent bg-coden-accent/10'
                        : 'border-transparent hover:border-coden-border hover:bg-coden-border/50',
                      drop.isActive ? 'ring-2 ring-coden-accent' : '',
                    ].join(' ')}
                  >
                    <span className="block truncate text-sm font-medium text-coden-text">
                      {set.name || 'Untitled set'}
                    </span>
                    <span className="mt-0.5 block font-mono text-[10px] text-coden-muted">
                      {countSetProblems(set)} {countSetProblems(set) === 1 ? 'problem' : 'problems'}
                      {set.career_mode ? ' · Career mode' : ''}
                    </span>
                  </button>
                );
              })}
              {draft.length === 0 && (
                <div className="px-3 py-8 text-center text-xs leading-5 text-coden-muted">
                  No personal sets yet.
                  <br />
                  Start with “New Personal root” or copy a standard hierarchy.
                </div>
              )}
            </div>
          </aside>

          <main className="flex min-h-0 flex-col">
            {selectedSet ? (
              <>
                <div className="border-b border-coden-border p-4">
                  <div className="flex items-start gap-3">
                    <div className="min-w-0 flex-1 space-y-2">
                      <label className="block">
                        <span className="mb-1 block text-[10px] font-semibold uppercase tracking-wider text-coden-muted">
                          Set name
                        </span>
                        <input
                          value={selectedSet.name}
                          onChange={(event) => changeSet({ name: event.target.value })}
                          maxLength={80}
                          className="w-full rounded border border-coden-border bg-coden-surface px-3 py-2 text-sm font-semibold text-coden-text focus:border-coden-accent focus:outline-none"
                        />
                      </label>
                      <label className="flex cursor-pointer items-start gap-2 rounded border border-coden-border bg-coden-surface px-3 py-2">
                        <input
                          type="checkbox"
                          checked={selectedSet.career_mode}
                          onChange={(event) => changeSet({ career_mode: event.target.checked })}
                          className="mt-0.5 accent-[var(--coden-accent)]"
                        />
                        <span>
                          <span className="block text-xs font-semibold text-coden-text">
                            Career mode for this Personal root
                          </span>
                          <span className="mt-0.5 block text-[10px] leading-4 text-coden-muted">
                            Problems unlock in order within each leaf. Other Personal roots keep
                            their own setting.
                          </span>
                        </span>
                      </label>
                      <label className="block">
                        <span className="sr-only">Set description</span>
                        <input
                          value={selectedSet.description}
                          onChange={(event) => changeSet({ description: event.target.value })}
                          maxLength={500}
                          placeholder="Optional purpose, target, or study note"
                          className="w-full rounded border border-coden-border bg-coden-surface px-3 py-1.5 text-xs text-coden-text placeholder-coden-muted focus:border-coden-accent focus:outline-none"
                        />
                      </label>
                    </div>
                    <button
                      type="button"
                      onClick={() => shiftSelectedSet(-1)}
                      className="mt-5 rounded border border-coden-border px-2.5 py-1.5 text-xs text-coden-muted hover:bg-coden-border hover:text-coden-text"
                    >
                      Move set up
                    </button>
                    <button
                      type="button"
                      onClick={() => shiftSelectedSet(1)}
                      className="mt-5 rounded border border-coden-border px-2.5 py-1.5 text-xs text-coden-muted hover:bg-coden-border hover:text-coden-text"
                    >
                      Move set down
                    </button>
                    <button
                      type="button"
                      onClick={() => setDeleteSetId(selectedSet.id)}
                      className="mt-5 rounded border border-rose-500/30 px-2.5 py-1.5 text-xs text-rose-300 hover:bg-rose-500/10"
                    >
                      Delete set
                    </button>
                  </div>
                  {deleteSetId === selectedSet.id && (
                    <div className="mt-3 flex items-center justify-between gap-3 rounded border border-rose-500/30 bg-rose-500/10 px-3 py-2 text-xs text-rose-100">
                      <span>Remove this set and all of its custom organization?</span>
                      <span className="flex shrink-0 gap-2">
                        <button
                          type="button"
                          onClick={() => setDeleteSetId(null)}
                          className="rounded border border-coden-border px-2 py-1 hover:bg-coden-border"
                        >
                          Keep
                        </button>
                        <button
                          type="button"
                          onClick={confirmDeleteSet}
                          className="rounded bg-rose-500 px-2 py-1 font-semibold text-white hover:bg-rose-400"
                        >
                          Remove
                        </button>
                      </span>
                    </div>
                  )}
                </div>
                <div className="min-h-0 flex-1 overflow-y-auto p-4">
                  <div className="mb-3 flex items-center justify-between gap-3">
                    <div>
                      <h3 className="text-sm font-semibold text-coden-text">Structure</h3>
                      <p className="mt-0.5 text-[11px] text-coden-muted">
                        Folders describe topics, stages, or review groups. Problems may also stay at the root.
                      </p>
                    </div>
                    <button
                      type="button"
                      onClick={() => addGroup(null)}
                      className="rounded border border-coden-border px-3 py-1.5 text-xs text-coden-muted hover:bg-coden-border hover:text-coden-text"
                    >
                      Add root folder
                    </button>
                  </div>
                  <div>
                    {renderNodeList(selectedSet.nodes, selectedSet, null, 1)}
                  </div>
                </div>
              </>
            ) : (
              <div className="flex flex-1 items-center justify-center p-8 text-center">
                <div>
                  <div className="text-base font-semibold text-coden-text">
                    Create your first Personal root
                  </div>
                  <p className="mt-2 max-w-md text-sm leading-6 text-coden-muted">
                    Use sets for goals such as “Backend interview”, “Weak areas”, or
                    “30-day review”, then organize them with up to three folder levels.
                    Each root can independently enable Career mode.
                  </p>
                  <button
                    type="button"
                    onClick={addSet}
                    disabled={draft.length >= MAX_CUSTOM_ROOT_SETS}
                    className="mt-4 rounded bg-coden-accent px-4 py-2 text-sm font-semibold text-[var(--coden-accent-contrast)] hover:brightness-110"
                  >
                    Create a Personal root
                  </button>
                </div>
              </div>
            )}
          </main>

          <aside className="flex min-h-0 flex-col border-l border-coden-border bg-coden-surface/40">
            <div className="border-b border-coden-border p-3">
              <div className="flex items-center justify-between gap-3">
                <h3 className="text-sm font-semibold text-coden-text">
                  {libraryMode === 'problems' ? 'Problem library' : 'Set hierarchy library'}
                </h3>
                <span className="font-mono text-[10px] text-coden-muted">
                  {libraryMode === 'problems'
                    ? `${filteredLibraryChallenges.length} matches`
                    : `${STANDARD_HIERARCHY_OPTIONS.length + draft.length} roots · ${filteredLibraryChallenges.length} matches`}
                </span>
              </div>
              <p className="mt-1 text-[10px] leading-4 text-coden-muted">
                {libraryMode === 'problems'
                  ? 'Drag into any insertion line, or choose any existing set and folder below.'
                  : 'Browse every standard and Personal set. Copy or drag a complete hierarchy.'}
              </p>
              <div className="mt-2 grid grid-cols-2 rounded border border-coden-border bg-coden-bg p-1">
                <button
                  type="button"
                  onClick={() => setLibraryMode('problems')}
                  className={[
                    'rounded px-2 py-1 text-[10px] font-semibold',
                    libraryMode === 'problems'
                      ? 'bg-coden-accent text-[var(--coden-accent-contrast)]'
                      : 'text-coden-muted hover:bg-coden-border',
                  ].join(' ')}
                >
                  Individual problems
                </button>
                <button
                  type="button"
                  onClick={() => setLibraryMode('sets')}
                  className={[
                    'rounded px-2 py-1 text-[10px] font-semibold',
                    libraryMode === 'sets'
                      ? 'bg-coden-accent text-[var(--coden-accent-contrast)]'
                      : 'text-coden-muted hover:bg-coden-border',
                  ].join(' ')}
                >
                  Sets and hierarchies
                </button>
              </div>
              <input
                value={libraryQuery}
                onChange={(event) => setLibraryQuery(event.target.value)}
                placeholder="Search title, LC id, or topic"
                className="mt-3 w-full rounded border border-coden-border bg-coden-bg px-3 py-2 text-xs text-coden-text placeholder-coden-muted focus:border-coden-accent focus:outline-none"
              />
              <div className="mt-2 grid grid-cols-2 gap-2">
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Sort by</span>
                  <select
                    value={librarySort}
                    onChange={(event) => setLibrarySort(event.target.value as LibrarySort)}
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text focus:border-coden-accent focus:outline-none"
                  >
                    <option value="leetcode_asc">LeetCode number</option>
                    <option value="elo_asc">Elo: easiest first</option>
                    <option value="elo_desc">Elo: hardest first</option>
                    <option value="frequency_desc">Frequency: highest first</option>
                    <option value="frequency_asc">Frequency: lowest first</option>
                    <option value="acceptance_desc">Acceptance: highest first</option>
                  </select>
                </label>
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Topic</span>
                  <select
                    value={libraryTopic}
                    onChange={(event) => setLibraryTopic(event.target.value)}
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text focus:border-coden-accent focus:outline-none"
                  >
                    <option value="all">All topics</option>
                    {topicOptions.map((topic) => (
                      <option key={topic} value={topic}>{topic}</option>
                    ))}
                  </select>
                </label>
              </div>
              <div className="mt-2 grid grid-cols-3 gap-2">
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Difficulty</span>
                  <select
                    value={libraryDifficulty}
                    onChange={(event) => setLibraryDifficulty(event.target.value)}
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text focus:border-coden-accent focus:outline-none"
                  >
                    <option value="all">All</option>
                    <option value="Easy">Easy</option>
                    <option value="Medium">Medium</option>
                    <option value="Hard">Hard</option>
                  </select>
                </label>
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Elo source</span>
                  <select
                    value={libraryEloSource}
                    onChange={(event) => setLibraryEloSource(event.target.value)}
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text focus:border-coden-accent focus:outline-none"
                  >
                    <option value="all">All</option>
                    <option value="real">Real Elo</option>
                    <option value="estimated">Estimated</option>
                    <option value="unrated">No Elo</option>
                  </select>
                </label>
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Frequency</span>
                  <select
                    value={libraryFrequencyAvailability}
                    onChange={(event) => setLibraryFrequencyAvailability(event.target.value)}
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text focus:border-coden-accent focus:outline-none"
                  >
                    <option value="all">All</option>
                    <option value="available">Available</option>
                    <option value="missing">Missing</option>
                  </select>
                </label>
              </div>
              <div className="mt-2 grid grid-cols-3 gap-2">
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Min Elo</span>
                  <input
                    type="number"
                    value={libraryMinElo}
                    onChange={(event) => setLibraryMinElo(event.target.value)}
                    placeholder="Any"
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text placeholder-coden-muted focus:border-coden-accent focus:outline-none"
                  />
                </label>
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Max Elo</span>
                  <input
                    type="number"
                    value={libraryMaxElo}
                    onChange={(event) => setLibraryMaxElo(event.target.value)}
                    placeholder="Any"
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text placeholder-coden-muted focus:border-coden-accent focus:outline-none"
                  />
                </label>
                <label>
                  <span className="mb-1 block text-[10px] text-coden-muted">Min Freq.</span>
                  <input
                    type="number"
                    min="0"
                    max="100"
                    step="0.1"
                    value={libraryMinFrequency}
                    onChange={(event) => setLibraryMinFrequency(event.target.value)}
                    placeholder="Any"
                    className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text placeholder-coden-muted focus:border-coden-accent focus:outline-none"
                  />
                </label>
              </div>
              <label
                className={[
                  'mt-2 block rounded border p-2 transition-colors',
                  destinationDrop?.isActive
                    ? 'border-coden-accent bg-coden-accent/10'
                    : 'border-transparent',
                ].join(' ')}
                onDragOver={destinationDrop?.onDragOver}
                onDragLeave={destinationDrop?.onDragLeave}
                onDrop={destinationDrop?.onDrop}
              >
                <span className="mb-1 block text-[10px] font-semibold text-coden-muted">
                  Add-button destination — all personal sets
                </span>
                <select
                  value={effectiveLibraryTarget?.key ?? ''}
                  onChange={(event) => setLibraryTargetKey(event.target.value || null)}
                  disabled={destinationOptions.length === 0}
                  className="w-full rounded border border-coden-border bg-coden-bg px-2 py-1.5 text-[11px] text-coden-text focus:border-coden-accent focus:outline-none disabled:opacity-40"
                >
                  {destinationOptions.length === 0 && <option value="">Create a set first</option>}
                  {destinationOptions.map((destination) => (
                    <option key={destination.key} value={destination.key}>
                      {destination.label}
                    </option>
                  ))}
                </select>
                <span className="mt-1 block text-[9px] text-coden-muted">
                  {libraryMode === 'sets'
                    ? 'Hierarchy-library drops always create a deep copy here.'
                    : `Drag a problem or complete folder onto this box to ${dragAction} it here.`}
                </span>
              </label>
              {libraryMode === 'problems' && (
                <button
                  type="button"
                  onClick={addAllFilteredProblems}
                  disabled={!effectiveLibraryTarget || filteredLibraryChallenges.length === 0}
                  className="mt-2 w-full rounded border border-coden-accent bg-coden-accent/10 px-3 py-2 text-xs font-semibold text-coden-accent hover:bg-coden-accent/20 disabled:cursor-not-allowed disabled:border-coden-border disabled:bg-transparent disabled:text-coden-muted disabled:opacity-50"
                  title={effectiveLibraryTarget
                    ? `Add every filtered match to ${effectiveLibraryTarget.label}, including matches not currently rendered`
                    : 'Create a personal set first'}
                >
                  Add all {filteredLibraryChallenges.length} filtered
                  {' '}
                  {filteredLibraryChallenges.length === 1 ? 'problem' : 'problems'}
                </button>
              )}
            </div>
            <div className="min-h-0 flex-1 space-y-1 overflow-y-auto p-2">
              {libraryMode === 'problems' ? (
                <>
                  {libraryChallenges.map((challenge) => {
                const elo = eloDisplayForChallenge(challenge);
                const placements = countProblemPlacements(draft, challenge.id);
                const difficultyClass = challenge.difficulty_label === 'Easy'
                  ? 'border-emerald-500/30 text-emerald-300'
                  : challenge.difficulty_label === 'Medium'
                    ? 'border-amber-500/30 text-amber-300'
                    : 'border-rose-500/30 text-rose-300';
                return (
                  <div
                    key={challenge.id}
                    draggable={destinationOptions.length > 0}
                    onDragStart={(event) => writeDragPayload(event, {
                      kind: 'library-problem',
                      challengeId: challenge.id,
                    })}
                    className="cursor-grab rounded border border-transparent px-2.5 py-2 hover:border-coden-border hover:bg-coden-border/40"
                  >
                    <div className="flex items-start gap-2">
                      <div className="min-w-0 flex-1">
                        <div className="truncate text-xs font-medium text-coden-text">
                          {challenge.name}
                        </div>
                        <div className="mt-1 flex flex-wrap items-center gap-1 font-mono text-[9px]">
                          <span className="rounded border border-coden-border px-1.5 py-0.5 text-coden-muted">
                            LC {challenge.leetcode_frontend_id}
                          </span>
                          <span className={`rounded border px-1.5 py-0.5 ${difficultyClass}`}>
                            {challenge.difficulty_label}
                          </span>
                          <span className="rounded border border-coden-border px-1.5 py-0.5 text-coden-muted">
                            {elo
                              ? `${elo.estimated ? 'Est. ' : ''}Elo ${Math.round(elo.value)}`
                              : 'Elo —'}
                          </span>
                          <span className="rounded border border-coden-border px-1.5 py-0.5 text-coden-muted">
                            Freq {challenge.frequency === null ? '—' : `${challenge.frequency.toFixed(1)}%`}
                          </span>
                          <span className="rounded border border-coden-border px-1.5 py-0.5 text-coden-muted">
                            Accept {challenge.acceptance_rate === null ? '—' : `${challenge.acceptance_rate.toFixed(1)}%`}
                          </span>
                          {placements > 0 && (
                            <span className="rounded border border-coden-accent/40 px-1.5 py-0.5 text-coden-accent">
                              Placed {placements}×
                            </span>
                          )}
                        </div>
                      </div>
                      <button
                        type="button"
                        disabled={!effectiveLibraryTarget}
                        onClick={() => addProblem(
                          challenge.id,
                          effectiveLibraryTarget?.setId ?? null,
                          effectiveLibraryTarget?.groupId ?? null,
                        )}
                        className="shrink-0 rounded border border-coden-border px-2 py-1 text-[10px] text-coden-muted hover:border-coden-accent hover:text-coden-accent disabled:cursor-not-allowed disabled:opacity-40"
                        title={effectiveLibraryTarget
                          ? `Add to ${effectiveLibraryTarget.label}`
                          : 'Create a personal set first'}
                      >
                        Add
                      </button>
                    </div>
                  </div>
                );
                  })}
                  {libraryChallenges.length === 0 && (
                    <div className="p-5 text-center text-xs text-coden-muted">
                      No problems match this search.
                    </div>
                  )}
                  {libraryChallenges.length < filteredLibraryChallenges.length && (
                    <button
                      type="button"
                      onClick={() => setLibraryLimit((limit) => limit + INITIAL_LIBRARY_LIMIT)}
                      className="w-full rounded border border-coden-border px-3 py-2 text-xs text-coden-muted hover:bg-coden-border hover:text-coden-text"
                    >
                      Show {Math.min(
                        INITIAL_LIBRARY_LIMIT,
                        filteredLibraryChallenges.length - libraryChallenges.length,
                      )} more
                    </button>
                  )}
                </>
              ) : (
                <div className="space-y-3">
                  <section>
                    <div className="mb-1.5 flex items-center justify-between px-1">
                      <h4 className="text-[10px] font-semibold uppercase tracking-wider text-coden-muted">
                        Standard sets
                      </h4>
                      <span className="font-mono text-[9px] text-coden-muted">
                        {STANDARD_HIERARCHY_OPTIONS.length}
                      </span>
                    </div>
                    <div className="space-y-1.5">
                      {STANDARD_HIERARCHY_OPTIONS.map((option) => renderSourceRoot(
                        `standard:${option.id}`,
                        option.label,
                        option.description,
                        'standard',
                        selectedSourceRootKey === `standard:${option.id}` && selectedSourceRoot
                          ? hierarchyProblemCount(selectedSourceRoot.nodes)
                          : null,
                        option.hasCareerPath,
                      ))}
                    </div>
                  </section>
                  <section>
                    <div className="mb-1.5 flex items-center justify-between px-1">
                      <h4 className="text-[10px] font-semibold uppercase tracking-wider text-coden-muted">
                        Personal sets
                      </h4>
                      <span className="font-mono text-[9px] text-coden-muted">
                        {draft.length}/{MAX_CUSTOM_ROOT_SETS}
                      </span>
                    </div>
                    <div className="space-y-1.5">
                      {draft.map((set) => renderSourceRoot(
                        `personal:${set.id}`,
                        set.name || 'Untitled set',
                        set.description,
                        'personal',
                        countSetProblems(set),
                        set.career_mode,
                      ))}
                      {draft.length === 0 && (
                        <div className="rounded border border-dashed border-coden-border px-3 py-5 text-center text-[10px] text-coden-muted">
                          Create a Personal root to make it available as a reusable hierarchy.
                        </div>
                      )}
                    </div>
                  </section>
                </div>
              )}
            </div>
            <div className="border-t border-coden-border px-3 py-2 text-[10px] text-coden-muted">
              {libraryMode === 'problems'
                ? (
                    <>
                      Showing {libraryChallenges.length} of {filteredLibraryChallenges.length} matching problems
                      {' · '}{challenges.length} total.
                    </>
                  )
                : (
                    <>
                      {filteredLibraryChallenges.length} matching problems · Drag a root to “New Personal root”,
                      or copy any opened branch into the selected destination.
                    </>
                  )}
            </div>
          </aside>
        </div>

        <div className="flex items-center justify-between gap-4 border-t border-coden-border bg-coden-surface px-5 py-3">
          <div className="min-w-0 flex-1">
            {(saveError || notice) && (
              <div className={`truncate text-xs ${saveError ? 'text-rose-300' : 'text-coden-muted'}`}>
                {saveError || notice}
              </div>
            )}
            {!saveError && !notice && (
              <div className="text-xs text-coden-muted">
                {hasUnsavedChanges ? 'Unsaved changes' : 'Everything is saved'}
              </div>
            )}
          </div>
          {confirmDiscard ? (
            <div className="flex items-center gap-2">
              <span className="text-xs text-amber-300">Discard all unsaved changes?</span>
              <button
                type="button"
                onClick={() => setConfirmDiscard(false)}
                className="rounded border border-coden-border px-3 py-1.5 text-xs text-coden-muted hover:bg-coden-border"
              >
                Continue editing
              </button>
              <button
                type="button"
                onClick={onClose}
                className="rounded border border-amber-400/40 px-3 py-1.5 text-xs text-amber-300 hover:bg-amber-400/10"
              >
                Discard changes
              </button>
            </div>
          ) : (
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={requestClose}
                disabled={saving}
                className="rounded border border-coden-border px-4 py-2 text-sm text-coden-muted hover:bg-coden-border hover:text-coden-text disabled:opacity-50"
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={() => void handleSave()}
                disabled={saving || !hasUnsavedChanges}
                className="rounded bg-coden-accent px-5 py-2 text-sm font-semibold text-[var(--coden-accent-contrast)] hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-40"
              >
                {saving ? 'Saving…' : 'Save personal sets'}
              </button>
            </div>
          )}
        </div>
      </div>
    </div>,
    document.body,
  );
}
