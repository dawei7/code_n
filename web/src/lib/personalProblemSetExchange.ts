import type {
  ChallengeSummary,
  CustomProblemSet,
  CustomProblemTreeNode,
} from '../types/api';
import {
  MAX_CUSTOM_GROUP_DEPTH,
  MAX_CUSTOM_ROOT_SETS,
  createCustomId,
} from './customProblemSets';


export const PERSONAL_SET_EXCHANGE_FORMAT = 'coden.personal-problem-sets';
export const PERSONAL_SET_EXCHANGE_VERSION = 1;
export const PERSONAL_SET_EXCHANGE_SCHEMA = 'urn:coden:personal-problem-sets:1';
export const MAX_PERSONAL_SET_IMPORT_BYTES = 5 * 1024 * 1024;

type ExchangeProblem = {
  type: 'problem';
  provider: 'leetcode';
  canonical_id: string;
  frontend_id: string;
  title_slug: string;
  title: string;
  url: string;
};

type ExchangeFolder = {
  type: 'folder';
  name: string;
  children: ExchangeNode[];
};

type ExchangeNode = ExchangeProblem | ExchangeFolder;

export interface PersonalProblemSetExchange {
  schema: typeof PERSONAL_SET_EXCHANGE_SCHEMA;
  format: typeof PERSONAL_SET_EXCHANGE_FORMAT;
  version: typeof PERSONAL_SET_EXCHANGE_VERSION;
  exported_at: string;
  sets: Array<{
    name: string;
    description: string;
    career_mode: boolean;
    nodes: ExchangeNode[];
  }>;
}

export interface PersonalProblemSetImportResult {
  sets: CustomProblemSet[];
  importedSetCount: number;
  skippedSetCount: number;
  importedProblemCount: number;
  skippedProblemCount: number;
  warnings: string[];
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function cleanText(value: unknown, maximum: number): string {
  return typeof value === 'string' ? value.trim().slice(0, maximum) : '';
}

function exportNodes(
  nodes: CustomProblemTreeNode[],
  challengeById: Map<string, ChallengeSummary>,
): ExchangeNode[] {
  return nodes.flatMap((node): ExchangeNode[] => {
    if (node.type === 'group') {
      return [{
        type: 'folder',
        name: node.name,
        children: exportNodes(node.children, challengeById),
      }];
    }
    const challenge = challengeById.get(node.challenge_id);
    if (!challenge) {
      throw new Error(`Cannot export unknown canonical problem "${node.challenge_id}".`);
    }
    return [{
      type: 'problem',
      provider: 'leetcode',
      canonical_id: challenge.id,
      frontend_id: challenge.leetcode_frontend_id,
      title_slug: challenge.leetcode_slug,
      title: challenge.leetcode_title || challenge.name,
      url: challenge.leetcode_url,
    }];
  });
}

export function buildPersonalProblemSetExchange(
  sets: CustomProblemSet[],
  challenges: ChallengeSummary[],
  exportedAt = new Date(),
): PersonalProblemSetExchange {
  const challengeById = new Map(challenges.map((challenge) => [challenge.id, challenge]));
  return {
    schema: PERSONAL_SET_EXCHANGE_SCHEMA,
    format: PERSONAL_SET_EXCHANGE_FORMAT,
    version: PERSONAL_SET_EXCHANGE_VERSION,
    exported_at: exportedAt.toISOString(),
    sets: sets.map((set) => ({
      name: set.name,
      description: set.description,
      career_mode: set.career_mode,
      nodes: exportNodes(set.nodes, challengeById),
    })),
  };
}

export function serializePersonalProblemSets(
  sets: CustomProblemSet[],
  challenges: ChallengeSummary[],
  exportedAt = new Date(),
): string {
  return `${JSON.stringify(buildPersonalProblemSetExchange(sets, challenges, exportedAt), null, 2)}\n`;
}

function normalizeSlug(value: unknown): string {
  return cleanText(value, 200).toLowerCase();
}

function challengeIndexes(challenges: ChallengeSummary[]) {
  return {
    byCanonicalId: new Map(challenges.map((challenge) => [challenge.id, challenge])),
    byFrontendId: new Map(challenges.map((challenge) => [
      challenge.leetcode_frontend_id,
      challenge,
    ])),
    bySlug: new Map(challenges.map((challenge) => [
      challenge.leetcode_slug.toLowerCase(),
      challenge,
    ])),
  };
}

function resolveChallenge(
  raw: Record<string, unknown>,
  indexes: ReturnType<typeof challengeIndexes>,
): ChallengeSummary | null {
  if (raw.provider !== 'leetcode') return null;
  const frontendId = cleanText(raw.frontend_id, 40);
  if (frontendId && indexes.byFrontendId.has(frontendId)) {
    return indexes.byFrontendId.get(frontendId)!;
  }
  const canonicalId = cleanText(raw.canonical_id, 100);
  if (canonicalId && indexes.byCanonicalId.has(canonicalId)) {
    return indexes.byCanonicalId.get(canonicalId)!;
  }
  const slug = normalizeSlug(raw.title_slug);
  return slug ? indexes.bySlug.get(slug) ?? null : null;
}

function parseExchange(value: string | unknown): Record<string, unknown> {
  let parsed: unknown = value;
  if (typeof value === 'string') {
    try {
      parsed = JSON.parse(value);
    } catch {
      throw new Error('The selected file is not valid JSON.');
    }
  }
  if (!isRecord(parsed)) {
    throw new Error('The Personal-set exchange must be a JSON object.');
  }
  if (parsed.format !== PERSONAL_SET_EXCHANGE_FORMAT) {
    throw new Error(`Unsupported exchange format. Expected "${PERSONAL_SET_EXCHANGE_FORMAT}".`);
  }
  if (parsed.version !== PERSONAL_SET_EXCHANGE_VERSION) {
    throw new Error(
      `Unsupported Personal-set exchange version "${String(parsed.version)}". `
      + `This app supports version ${PERSONAL_SET_EXCHANGE_VERSION}.`,
    );
  }
  if (!Array.isArray(parsed.sets)) {
    throw new Error('The Personal-set exchange does not contain a valid sets array.');
  }
  return parsed;
}

export function importPersonalProblemSets(
  value: string | unknown,
  currentSets: CustomProblemSet[],
  challenges: ChallengeSummary[],
): PersonalProblemSetImportResult {
  const exchange = parseExchange(value);
  const indexes = challengeIndexes(challenges);
  const availableSlots = Math.max(0, MAX_CUSTOM_ROOT_SETS - currentSets.length);
  const rawSets = exchange.sets as unknown[];
  const warnings: string[] = [];
  let skippedProblemCount = 0;
  let importedProblemCount = 0;
  let nodeCount = 0;

  const parseNodes = (
    rawNodes: unknown,
    depth: number,
    directProblemIds = new Set<string>(),
  ): CustomProblemTreeNode[] => {
    if (!Array.isArray(rawNodes)) return [];
    const nodes: CustomProblemTreeNode[] = [];
    for (const rawNode of rawNodes) {
      nodeCount += 1;
      if (nodeCount > 250_000) {
        throw new Error('The exchange contains too many tree items to import safely.');
      }
      if (!isRecord(rawNode)) continue;
      if (rawNode.type === 'problem') {
        const challenge = resolveChallenge(rawNode, indexes);
        if (!challenge || directProblemIds.has(challenge.id)) {
          skippedProblemCount += 1;
          continue;
        }
        directProblemIds.add(challenge.id);
        importedProblemCount += 1;
        nodes.push({
          type: 'problem',
          id: createCustomId('item'),
          challenge_id: challenge.id,
        });
        continue;
      }
      if (rawNode.type !== 'folder') continue;
      if (depth >= MAX_CUSTOM_GROUP_DEPTH) {
        throw new Error(
          `The exchange contains folders deeper than ${MAX_CUSTOM_GROUP_DEPTH} levels.`,
        );
      }
      const name = cleanText(rawNode.name, 80);
      if (!name) continue;
      nodes.push({
        type: 'group',
        id: createCustomId('group'),
        name,
        children: parseNodes(rawNode.children, depth + 1),
      });
    }
    return nodes;
  };

  const importedSets: CustomProblemSet[] = [];
  for (const rawSet of rawSets) {
    if (importedSets.length >= availableSlots) break;
    if (!isRecord(rawSet)) continue;
    const name = cleanText(rawSet.name, 80);
    if (!name) continue;
    importedSets.push({
      id: createCustomId('set'),
      name,
      description: cleanText(rawSet.description, 500),
      career_mode: rawSet.career_mode === true,
      nodes: parseNodes(rawSet.nodes, 0),
    });
  }

  const skippedSetCount = rawSets.length - importedSets.length;
  if (rawSets.length > availableSlots) {
    warnings.push(
      `${rawSets.length - availableSlots} root set(s) did not fit within the `
      + `${MAX_CUSTOM_ROOT_SETS}-root Personal limit.`,
    );
  }
  if (skippedProblemCount > 0) {
    warnings.push(
      `${skippedProblemCount} unresolved or same-leaf duplicate problem placement(s) were skipped.`,
    );
  }
  return {
    sets: [...currentSets, ...importedSets],
    importedSetCount: importedSets.length,
    skippedSetCount,
    importedProblemCount,
    skippedProblemCount,
    warnings,
  };
}

export function personalProblemSetExportFilename(setName?: string): string {
  const suffix = setName
    ? setName.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '')
    : 'all';
  return `coden-personal-problem-sets-${suffix || 'set'}.json`;
}
