import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { Buffer } from 'node:buffer';
import ts from 'typescript';

const sourceUrl = new URL('../src/lib/careerUnlocks.ts', import.meta.url);
const source = await readFile(sourceUrl, 'utf8');
const output = ts.transpileModule(source, {
  compilerOptions: {
    module: ts.ModuleKind.ES2022,
    target: ts.ScriptTarget.ES2022,
  },
}).outputText;
const moduleUrl = `data:text/javascript;base64,${Buffer.from(output).toString('base64')}`;
const { buildUnlockedCareerSequence, resolveCareerSequenceOrder } = await import(moduleUrl);

assert.equal(
  resolveCareerSequenceOrder(0, 217),
  0,
  'The first zero-based NeetCode item must not fall back to its LeetCode frontend ID.',
);
assert.equal(resolveCareerSequenceOrder(1, 242), 1);
assert.equal(resolveCareerSequenceOrder(null, 217), 217);
assert.equal(resolveCareerSequenceOrder(undefined, 217), 217);

const fixtures = [
  ['lc_217', '../../dsa/leetcode/217_contains-duplicate/metadata.json'],
  ['lc_242', '../../dsa/leetcode/242_valid-anagram/metadata.json'],
  ['lc_1', '../../dsa/leetcode/1_two-sum/metadata.json'],
];
const entries = [];
for (const [challengeId, relativePath] of fixtures) {
  const metadata = JSON.parse(await readFile(new URL(relativePath, import.meta.url), 'utf8'));
  const membership = metadata.neetcode_subsets.find(
    (item) => item.subset_slug === 'neetcode150' && item.path.join('/') === 'Arrays & Hashing',
  );
  assert.ok(membership, `${challengeId} must belong to NeetCode 150 Arrays & Hashing.`);
  entries.push({
    challengeId,
    order: resolveCareerSequenceOrder(membership.order, Number(challengeId.slice(3))),
    fallbackOrder: Number(challengeId.slice(3)),
  });
}

assert.deepEqual(
  [...buildUnlockedCareerSequence(entries, new Set())],
  ['lc_217'],
  'Contains Duplicate must be the initially unlocked NeetCode 150 problem.',
);
assert.deepEqual(
  [...buildUnlockedCareerSequence(entries, new Set(['lc_217']))],
  ['lc_217', 'lc_242'],
  'Completing Contains Duplicate must unlock Valid Anagram next.',
);
assert.deepEqual(
  [...buildUnlockedCareerSequence(entries, new Set(['lc_1']))],
  ['lc_217', 'lc_1'],
  'An already completed later problem must not lock the first problem or skip the unsolved predecessor.',
);

console.log('Career unlock ordering regression passed.');
