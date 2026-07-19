import type {
  CustomProblemGroup,
  CustomProblemSet,
  CustomProblemTreeNode,
} from '../types/api';


export const MAX_CUSTOM_GROUP_DEPTH = 3;
export const MAX_CUSTOM_ROOT_SETS = 5;

export type CustomProblemTreeTemplate =
  | { type: 'problem'; challenge_id: string }
  | { type: 'group'; name: string; children: CustomProblemTreeTemplate[] };

export function createCustomId(prefix: 'set' | 'group' | 'item'): string {
  const uuid = typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function'
    ? crypto.randomUUID()
    : `${Date.now()}-${Math.random().toString(16).slice(2)}`;
  return `${prefix}_${uuid.replace(/[^A-Za-z0-9_-]/g, '-')}`;
}

export function cloneCustomProblemSets(sets: CustomProblemSet[]): CustomProblemSet[] {
  return sets.map((set) => ({
    ...set,
    nodes: cloneNodes(set.nodes),
  }));
}

export function customNodesToTemplates(
  nodes: CustomProblemTreeNode[],
): CustomProblemTreeTemplate[] {
  return nodes.map((node) => node.type === 'group'
    ? {
        type: 'group',
        name: node.name,
        children: customNodesToTemplates(node.children),
      }
    : { type: 'problem', challenge_id: node.challenge_id });
}

function cloneNodes(nodes: CustomProblemTreeNode[]): CustomProblemTreeNode[] {
  return nodes.map((node) => node.type === 'group'
    ? { ...node, children: cloneNodes(node.children) }
    : { ...node });
}

export function collectCustomChallengeIds(sets: CustomProblemSet[]): Set<string> {
  const result = new Set<string>();
  const visit = (nodes: CustomProblemTreeNode[]) => {
    for (const node of nodes) {
      if (node.type === 'problem') result.add(node.challenge_id);
      else visit(node.children);
    }
  };
  sets.forEach((set) => visit(set.nodes));
  return result;
}

export function collectSetChallengeIds(set: CustomProblemSet): Set<string> {
  return collectCustomChallengeIds([set]);
}

export function countSetProblems(set: CustomProblemSet): number {
  const countNodes = (nodes: CustomProblemTreeNode[]): number => nodes.reduce(
    (total, node) => total + (
      node.type === 'problem' ? 1 : countNodes(node.children)
    ),
    0,
  );
  return countNodes(set.nodes);
}

export function maxGroupDepth(nodes: CustomProblemTreeNode[], depth = 0): number {
  let maximum = depth;
  for (const node of nodes) {
    if (node.type === 'group') {
      maximum = Math.max(maximum, maxGroupDepth(node.children, depth + 1));
    }
  }
  return maximum;
}

export function findGroupDepth(
  nodes: CustomProblemTreeNode[],
  groupId: string,
  depth = 1,
): number | null {
  for (const node of nodes) {
    if (node.type !== 'group') continue;
    if (node.id === groupId) return depth;
    const nested = findGroupDepth(node.children, groupId, depth + 1);
    if (nested !== null) return nested;
  }
  return null;
}

export function findNode(
  nodes: CustomProblemTreeNode[],
  nodeId: string,
): CustomProblemTreeNode | null {
  for (const node of nodes) {
    if (node.id === nodeId) return node;
    if (node.type === 'group') {
      const nested = findNode(node.children, nodeId);
      if (nested) return nested;
    }
  }
  return null;
}

export function nodeContains(node: CustomProblemTreeNode, nodeId: string): boolean {
  if (node.id === nodeId) return true;
  return node.type === 'group'
    ? node.children.some((child) => nodeContains(child, nodeId))
    : false;
}

function removeNode(
  nodes: CustomProblemTreeNode[],
  nodeId: string,
): { nodes: CustomProblemTreeNode[]; removed: CustomProblemTreeNode | null } {
  let removed: CustomProblemTreeNode | null = null;
  const next: CustomProblemTreeNode[] = [];
  for (const node of nodes) {
    if (!removed && node.id === nodeId) {
      removed = node;
      continue;
    }
    if (!removed && node.type === 'group') {
      const nested = removeNode(node.children, nodeId);
      if (nested.removed) {
        removed = nested.removed;
        next.push({ ...node, children: nested.nodes });
        continue;
      }
    }
    next.push(node);
  }
  return { nodes: next, removed };
}

function unwrapGroup(
  nodes: CustomProblemTreeNode[],
  groupId: string,
): { nodes: CustomProblemTreeNode[]; unwrapped: boolean } {
  const index = nodes.findIndex((node) => node.id === groupId);
  if (index >= 0) {
    const group = nodes[index];
    if (group?.type !== 'group') return { nodes, unwrapped: false };
    const siblingProblemIds = directProblemIds([
      ...nodes.slice(0, index),
      ...nodes.slice(index + 1),
    ]);
    const promoted: CustomProblemTreeNode[] = [];
    for (const child of group.children) {
      if (child.type === 'problem') {
        if (siblingProblemIds.has(child.challenge_id)) continue;
        siblingProblemIds.add(child.challenge_id);
      }
      promoted.push(child);
    }
    return {
      nodes: [
        ...nodes.slice(0, index),
        ...promoted,
        ...nodes.slice(index + 1),
      ],
      unwrapped: true,
    };
  }

  let unwrapped = false;
  const next = nodes.map((node) => {
    if (unwrapped || node.type !== 'group') return node;
    const nested = unwrapGroup(node.children, groupId);
    if (!nested.unwrapped) return node;
    unwrapped = true;
    return { ...node, children: nested.nodes };
  });
  return { nodes: next, unwrapped };
}

function insertNode(
  nodes: CustomProblemTreeNode[],
  targetGroupId: string | null,
  node: CustomProblemTreeNode,
  beforeNodeId: string | null = null,
): { nodes: CustomProblemTreeNode[]; inserted: boolean } {
  if (targetGroupId === null) {
    const index = beforeNodeId === null
      ? nodes.length
      : nodes.findIndex((current) => current.id === beforeNodeId);
    const copy = [...nodes];
    copy.splice(index < 0 ? copy.length : index, 0, node);
    return { nodes: copy, inserted: true };
  }
  let inserted = false;
  const next = nodes.map((current) => {
    if (current.type !== 'group') return current;
    if (current.id === targetGroupId) {
      inserted = true;
      const index = beforeNodeId === null
        ? current.children.length
        : current.children.findIndex((child) => child.id === beforeNodeId);
      const children = [...current.children];
      children.splice(index < 0 ? children.length : index, 0, node);
      return { ...current, children };
    }
    if (inserted) return current;
    const nested = insertNode(current.children, targetGroupId, node, beforeNodeId);
    if (nested.inserted) {
      inserted = true;
      return { ...current, children: nested.nodes };
    }
    return current;
  });
  return { nodes: next, inserted };
}

export type TreeEditResult =
  | { ok: true; sets: CustomProblemSet[]; ignored?: boolean }
  | { ok: false; message: string };

function directProblemIds(nodes: CustomProblemTreeNode[]): Set<string> {
  return new Set(
    nodes
      .filter((node): node is Extract<CustomProblemTreeNode, { type: 'problem' }> => (
        node.type === 'problem'
      ))
      .map((node) => node.challenge_id),
  );
}

function containerProblemIds(
  nodes: CustomProblemTreeNode[],
  targetGroupId: string | null,
): Set<string> | null {
  if (targetGroupId === null) return directProblemIds(nodes);
  const group = findNode(nodes, targetGroupId);
  return group?.type === 'group' ? directProblemIds(group.children) : null;
}

function templateDepth(nodes: CustomProblemTreeTemplate[], depth = 0): number {
  let maximum = depth;
  for (const node of nodes) {
    if (node.type === 'group') {
      maximum = Math.max(maximum, templateDepth(node.children, depth + 1));
    }
  }
  return maximum;
}

function instantiateTemplateNodes(
  nodes: CustomProblemTreeTemplate[],
): CustomProblemTreeNode[] {
  const problemIds = new Set<string>();
  const result: CustomProblemTreeNode[] = [];
  for (const node of nodes) {
    if (node.type === 'problem') {
      if (problemIds.has(node.challenge_id)) continue;
      problemIds.add(node.challenge_id);
      result.push({
        type: 'problem',
        id: createCustomId('item'),
        challenge_id: node.challenge_id,
      });
      continue;
    }
    result.push({
      type: 'group',
      id: createCustomId('group'),
      name: node.name,
      children: instantiateTemplateNodes(node.children),
    });
  }
  return result;
}

export function addProblemToCustomSet(
  sets: CustomProblemSet[],
  setId: string,
  targetGroupId: string | null,
  challengeId: string,
  beforeNodeId: string | null = null,
): TreeEditResult {
  const targetSet = sets.find((set) => set.id === setId);
  if (!targetSet) return { ok: false, message: 'Choose a problem set first.' };
  if (targetGroupId !== null && findGroupDepth(targetSet.nodes, targetGroupId) === null) {
    return { ok: false, message: 'The destination folder no longer exists.' };
  }
  const existingIds = containerProblemIds(targetSet.nodes, targetGroupId);
  if (existingIds?.has(challengeId)) {
    return { ok: true, sets, ignored: true };
  }
  const item: CustomProblemTreeNode = {
    type: 'problem',
    id: createCustomId('item'),
    challenge_id: challengeId,
  };
  return {
    ok: true,
    sets: sets.map((set) => {
      if (set.id !== setId) return set;
      const inserted = insertNode(set.nodes, targetGroupId, item, beforeNodeId);
      return { ...set, nodes: inserted.nodes };
    }),
  };
}

export function addTemplateToCustomSet(
  sets: CustomProblemSet[],
  setId: string,
  targetGroupId: string | null,
  templates: CustomProblemTreeTemplate[],
  beforeNodeId: string | null = null,
): TreeEditResult {
  const targetSet = sets.find((set) => set.id === setId);
  if (!targetSet) return { ok: false, message: 'Choose a problem set first.' };
  const targetDepth = targetGroupId === null
    ? 0
    : findGroupDepth(targetSet.nodes, targetGroupId);
  if (targetDepth === null) {
    return { ok: false, message: 'The destination folder no longer exists.' };
  }
  if (targetDepth + templateDepth(templates) > MAX_CUSTOM_GROUP_DEPTH) {
    return {
      ok: false,
      message: `That copy would exceed the ${MAX_CUSTOM_GROUP_DEPTH}-level folder limit.`,
    };
  }

  const existingIds = containerProblemIds(targetSet.nodes, targetGroupId) ?? new Set<string>();
  const filteredTemplates = templates.filter((template) => (
    template.type === 'group' || !existingIds.has(template.challenge_id)
  ));
  const nodes = instantiateTemplateNodes(filteredTemplates);
  if (nodes.length === 0) return { ok: true, sets, ignored: true };

  let insertedAny = false;
  let workingNodes = targetSet.nodes;
  for (const node of nodes) {
    const inserted = insertNode(
      workingNodes,
      targetGroupId,
      node,
      beforeNodeId,
    );
    workingNodes = inserted.nodes;
    insertedAny ||= inserted.inserted;
  }
  if (!insertedAny) {
    return { ok: false, message: 'The destination folder no longer exists.' };
  }
  return {
    ok: true,
    sets: sets.map((set) => (
      set.id === setId ? { ...set, nodes: workingNodes } : set
    )),
  };
}

export function createCustomSetFromTemplate(
  sets: CustomProblemSet[],
  name: string,
  description: string,
  templates: CustomProblemTreeTemplate[],
  careerMode = false,
): TreeEditResult {
  if (sets.length >= MAX_CUSTOM_ROOT_SETS) {
    return {
      ok: false,
      message: `Personal can contain at most ${MAX_CUSTOM_ROOT_SETS} root sets.`,
    };
  }
  if (templateDepth(templates) > MAX_CUSTOM_GROUP_DEPTH) {
    return {
      ok: false,
      message: `The copied hierarchy exceeds the ${MAX_CUSTOM_GROUP_DEPTH}-level folder limit.`,
    };
  }
  const next: CustomProblemSet = {
    id: createCustomId('set'),
    name,
    description,
    career_mode: careerMode,
    nodes: instantiateTemplateNodes(templates),
  };
  return { ok: true, sets: [...sets, next] };
}

export function addGroupToCustomSet(
  sets: CustomProblemSet[],
  setId: string,
  targetGroupId: string | null,
  name = 'New folder',
  beforeNodeId: string | null = null,
): TreeEditResult {
  const targetSet = sets.find((set) => set.id === setId);
  if (!targetSet) return { ok: false, message: 'Choose a problem set first.' };
  const targetDepth = targetGroupId === null
    ? 0
    : findGroupDepth(targetSet.nodes, targetGroupId);
  if (targetDepth === null) {
    return { ok: false, message: 'The destination folder no longer exists.' };
  }
  if (targetDepth >= MAX_CUSTOM_GROUP_DEPTH) {
    return {
      ok: false,
      message: `Folders can be nested at most ${MAX_CUSTOM_GROUP_DEPTH} levels.`,
    };
  }
  const group: CustomProblemGroup = {
    type: 'group',
    id: createCustomId('group'),
    name,
    children: [],
  };
  return {
    ok: true,
    sets: sets.map((set) => {
      if (set.id !== setId) return set;
      const inserted = insertNode(set.nodes, targetGroupId, group, beforeNodeId);
      return { ...set, nodes: inserted.nodes };
    }),
  };
}

export function removeCustomNode(
  sets: CustomProblemSet[],
  setId: string,
  nodeId: string,
): CustomProblemSet[] {
  return sets.map((set) => set.id === setId
    ? { ...set, nodes: removeNode(set.nodes, nodeId).nodes }
    : set);
}

export function unwrapCustomGroup(
  sets: CustomProblemSet[],
  setId: string,
  groupId: string,
): TreeEditResult {
  const targetSet = sets.find((set) => set.id === setId);
  if (!targetSet) return { ok: false, message: 'The Personal root no longer exists.' };
  const group = findNode(targetSet.nodes, groupId);
  if (!group || group.type !== 'group') {
    return { ok: false, message: 'The folder level no longer exists.' };
  }
  const unwrapped = unwrapGroup(targetSet.nodes, groupId);
  if (!unwrapped.unwrapped) {
    return { ok: false, message: 'The folder level could not be removed.' };
  }
  return {
    ok: true,
    sets: sets.map((set) => (
      set.id === setId ? { ...set, nodes: unwrapped.nodes } : set
    )),
  };
}

export function updateCustomGroupName(
  sets: CustomProblemSet[],
  setId: string,
  groupId: string,
  name: string,
): CustomProblemSet[] {
  const updateNodes = (nodes: CustomProblemTreeNode[]): CustomProblemTreeNode[] => (
    nodes.map((node) => node.type === 'group'
      ? {
          ...node,
          name: node.id === groupId ? name : node.name,
          children: updateNodes(node.children),
        }
      : node)
  );
  return sets.map((set) => set.id === setId
    ? { ...set, nodes: updateNodes(set.nodes) }
    : set);
}

export function moveCustomNode(
  sets: CustomProblemSet[],
  sourceSetId: string,
  nodeId: string,
  targetSetId: string,
  targetGroupId: string | null,
  beforeNodeId: string | null = null,
): TreeEditResult {
  const sourceSet = sets.find((set) => set.id === sourceSetId);
  const targetSet = sets.find((set) => set.id === targetSetId);
  if (!sourceSet || !targetSet) {
    return { ok: false, message: 'The source or destination set no longer exists.' };
  }
  const node = findNode(sourceSet.nodes, nodeId);
  if (!node) return { ok: false, message: 'The dragged item no longer exists.' };
  if (node.type === 'group' && targetGroupId && nodeContains(node, targetGroupId)) {
    return { ok: false, message: 'A folder cannot be moved inside itself.' };
  }
  const targetDepth = targetGroupId === null
    ? 0
    : findGroupDepth(targetSet.nodes, targetGroupId);
  if (targetDepth === null) {
    return { ok: false, message: 'The destination folder no longer exists.' };
  }
  if (
    node.type === 'group'
    && targetDepth + maxGroupDepth([node]) > MAX_CUSTOM_GROUP_DEPTH
  ) {
    return {
      ok: false,
      message: `That move would exceed the ${MAX_CUSTOM_GROUP_DEPTH}-level folder limit.`,
    };
  }
  if (sourceSetId === targetSetId && nodeId === beforeNodeId) {
    return { ok: true, sets };
  }
  if (
    node.type === 'problem'
    && containerProblemIds(targetSet.nodes, targetGroupId)?.has(node.challenge_id)
  ) {
    const targetNode = beforeNodeId ? findNode(targetSet.nodes, beforeNodeId) : null;
    const movingWithinSameLeaf = sourceSetId === targetSetId && (
      targetNode?.id === node.id
      || containerProblemIds(
        removeNode(targetSet.nodes, node.id).nodes,
        targetGroupId,
      )?.has(node.challenge_id) === false
    );
    if (!movingWithinSameLeaf) return { ok: true, sets, ignored: true };
  }

  let working = sets.map((set) => {
    if (set.id !== sourceSetId) return set;
    return { ...set, nodes: removeNode(set.nodes, nodeId).nodes };
  });
  working = working.map((set) => {
    if (set.id !== targetSetId) return set;
    const inserted = insertNode(set.nodes, targetGroupId, node, beforeNodeId);
    return inserted.inserted ? { ...set, nodes: inserted.nodes } : set;
  });
  return { ok: true, sets: working };
}

function cloneNodeWithFreshIds(node: CustomProblemTreeNode): CustomProblemTreeNode {
  if (node.type === 'problem') {
    return {
      ...node,
      id: createCustomId('item'),
    };
  }
  return {
    ...node,
    id: createCustomId('group'),
    children: node.children.map(cloneNodeWithFreshIds),
  };
}

export function copyCustomNode(
  sets: CustomProblemSet[],
  sourceSetId: string,
  nodeId: string,
  targetSetId: string,
  targetGroupId: string | null,
  beforeNodeId: string | null = null,
): TreeEditResult {
  const sourceSet = sets.find((set) => set.id === sourceSetId);
  const targetSet = sets.find((set) => set.id === targetSetId);
  if (!sourceSet || !targetSet) {
    return { ok: false, message: 'The source or destination set no longer exists.' };
  }
  const sourceNode = findNode(sourceSet.nodes, nodeId);
  if (!sourceNode) return { ok: false, message: 'The dragged item no longer exists.' };
  const targetDepth = targetGroupId === null
    ? 0
    : findGroupDepth(targetSet.nodes, targetGroupId);
  if (targetDepth === null) {
    return { ok: false, message: 'The destination folder no longer exists.' };
  }
  if (
    sourceNode.type === 'group'
    && targetDepth + maxGroupDepth([sourceNode]) > MAX_CUSTOM_GROUP_DEPTH
  ) {
    return {
      ok: false,
      message: `That copy would exceed the ${MAX_CUSTOM_GROUP_DEPTH}-level folder limit.`,
    };
  }
  if (
    sourceNode.type === 'problem'
    && containerProblemIds(targetSet.nodes, targetGroupId)?.has(sourceNode.challenge_id)
  ) {
    return { ok: true, sets, ignored: true };
  }
  const copiedNode = cloneNodeWithFreshIds(sourceNode);
  return {
    ok: true,
    sets: sets.map((set) => {
      if (set.id !== targetSetId) return set;
      const inserted = insertNode(set.nodes, targetGroupId, copiedNode, beforeNodeId);
      return inserted.inserted ? { ...set, nodes: inserted.nodes } : set;
    }),
  };
}

export function shiftCustomNode(
  sets: CustomProblemSet[],
  setId: string,
  nodeId: string,
  direction: -1 | 1,
): CustomProblemSet[] {
  const shift = (nodes: CustomProblemTreeNode[]): CustomProblemTreeNode[] => {
    const index = nodes.findIndex((node) => node.id === nodeId);
    if (index >= 0) {
      const target = index + direction;
      if (target < 0 || target >= nodes.length) return nodes;
      const copy = [...nodes];
      [copy[index], copy[target]] = [copy[target]!, copy[index]!];
      return copy;
    }
    return nodes.map((node) => node.type === 'group'
      ? { ...node, children: shift(node.children) }
      : node);
  };
  return sets.map((set) => set.id === setId ? { ...set, nodes: shift(set.nodes) } : set);
}
