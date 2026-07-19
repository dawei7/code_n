import assert from 'node:assert/strict';
import { Buffer } from 'node:buffer';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';


async function transpile(sourceUrl) {
  const source = await readFile(sourceUrl, 'utf8');
  return ts.transpileModule(source, {
    compilerOptions: {
      module: ts.ModuleKind.ES2022,
      target: ts.ScriptTarget.ES2022,
    },
  }).outputText;
}

const customSource = await transpile(
  new URL('../src/lib/customProblemSets.ts', import.meta.url),
);
const customUrl = `data:text/javascript;base64,${Buffer.from(customSource).toString('base64')}`;
const exchangeSource = (
  await transpile(new URL('../src/lib/personalProblemSetExchange.ts', import.meta.url))
).replace("from './customProblemSets'", `from '${customUrl}'`);
const exchangeUrl = `data:text/javascript;base64,${Buffer.from(exchangeSource).toString('base64')}`;
const {
  PERSONAL_SET_EXCHANGE_FORMAT,
  PERSONAL_SET_EXCHANGE_SCHEMA,
  buildPersonalProblemSetExchange,
  importPersonalProblemSets,
  serializePersonalProblemSets,
} = await import(exchangeUrl);

function challenge(id, frontendId, slug) {
  return {
    id,
    name: `Problem ${frontendId}`,
    leetcode_frontend_id: frontendId,
    leetcode_slug: slug,
    leetcode_title: `Problem ${frontendId}`,
    leetcode_url: `https://leetcode.com/problems/${slug}/`,
  };
}

const challenges = [
  challenge('lc_1', '1', 'two-sum'),
  challenge('lc_2', '2', 'add-two-numbers'),
];
const sourceSets = [{
  id: 'local_set_id',
  name: 'Interview path',
  description: 'Shareable structure',
  career_mode: true,
  nodes: [{
    type: 'group',
    id: 'local_group_id',
    name: 'Arrays',
    children: [
      { type: 'problem', id: 'local_item_one', challenge_id: 'lc_1' },
      { type: 'problem', id: 'local_item_two', challenge_id: 'lc_2' },
    ],
  }],
}];

const exchange = buildPersonalProblemSetExchange(
  sourceSets,
  challenges,
  new Date('2026-07-18T12:00:00.000Z'),
);
assert.equal(exchange.schema, PERSONAL_SET_EXCHANGE_SCHEMA);
assert.equal(exchange.format, PERSONAL_SET_EXCHANGE_FORMAT);
assert.equal(exchange.version, 1);
assert.equal(exchange.sets[0].nodes[0].type, 'folder');
assert.equal(
  JSON.stringify(exchange).includes('local_group_id'),
  false,
  'Internal editor ids must never leak into the portable exchange.',
);

const serialized = serializePersonalProblemSets(
  sourceSets,
  challenges,
  new Date('2026-07-18T12:00:00.000Z'),
);
const imported = importPersonalProblemSets(serialized, [], challenges);
assert.equal(imported.importedSetCount, 1);
assert.equal(imported.importedProblemCount, 2);
assert.equal(imported.sets[0].career_mode, true);
assert.notEqual(imported.sets[0].id, sourceSets[0].id);
assert.notEqual(imported.sets[0].nodes[0].id, sourceSets[0].nodes[0].id);

const smartIdentity = structuredClone(exchange);
smartIdentity.sets[0].nodes[0].children[0].canonical_id = 'obsolete-local-id';
const smartImport = importPersonalProblemSets(smartIdentity, [], challenges);
assert.equal(
  smartImport.sets[0].nodes[0].children[0].challenge_id,
  'lc_1',
  'The stable LeetCode frontend id must recover from an obsolete local canonical id.',
);

const unknownProblem = structuredClone(exchange);
unknownProblem.sets[0].nodes[0].children.push({
  type: 'problem',
  provider: 'leetcode',
  canonical_id: 'lc_999999',
  frontend_id: '999999',
  title_slug: 'not-in-this-library',
  title: 'Unknown',
  url: 'https://leetcode.com/problems/not-in-this-library/',
});
const withUnknown = importPersonalProblemSets(unknownProblem, [], challenges);
assert.equal(withUnknown.skippedProblemCount, 1);
assert.equal(withUnknown.importedProblemCount, 2);

const existing = Array.from({ length: 5 }, (_, index) => ({
  id: `set_${index}`,
  name: `Existing ${index}`,
  description: '',
  career_mode: false,
  nodes: [],
}));
const full = importPersonalProblemSets(exchange, existing, challenges);
assert.equal(full.importedSetCount, 0);
assert.equal(full.skippedSetCount, 1);
assert.equal(full.sets.length, 5);

assert.throws(
  () => importPersonalProblemSets({ ...exchange, version: 2 }, [], challenges),
  /supports version 1/,
);

console.log('Personal problem-set exchange regressions passed.');
