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
const {
  buildCustomCareerUnlockMap,
  buildUnlockedCareerSequence,
  collectCustomCareerLeaves,
  resolveCareerSequenceOrder,
} = await import(moduleUrl);

assert.equal(
  resolveCareerSequenceOrder(0, 217),
  0,
  'The first zero-based NeetCode item must not fall back to its LeetCode frontend ID.',
);
assert.equal(resolveCareerSequenceOrder(1, 242), 1);
assert.equal(resolveCareerSequenceOrder(null, 217), 217);
assert.equal(resolveCareerSequenceOrder(undefined, 217), 217);

const fixtures = [
  ['lc_217', '../../dsa/leetcode/0217_contains-duplicate/metadata.json'],
  ['lc_242', '../../dsa/leetcode/0242_valid-anagram/metadata.json'],
  ['lc_1', '../../dsa/leetcode/0001_two-sum/metadata.json'],
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

const customCareerSets = [{
  id: 'set_career',
  name: 'Career root',
  description: '',
  career_mode: true,
  nodes: [
    { type: 'problem', id: 'root_one', challenge_id: 'lc_1' },
    { type: 'problem', id: 'root_two', challenge_id: 'lc_2' },
    {
      type: 'group',
      id: 'group_arrays',
      name: 'Arrays',
      children: [
        { type: 'problem', id: 'array_one', challenge_id: 'lc_3' },
        { type: 'problem', id: 'array_two', challenge_id: 'lc_4' },
      ],
    },
  ],
}, {
  id: 'set_open',
  name: 'Open root',
  description: '',
  career_mode: false,
  nodes: [
    { type: 'problem', id: 'open_one', challenge_id: 'lc_5' },
    { type: 'problem', id: 'open_two', challenge_id: 'lc_6' },
  ],
}];
const customInitial = buildCustomCareerUnlockMap(customCareerSets, new Set());
assert.deepEqual(collectCustomCareerLeaves(customCareerSets), [{
  key: 'custom-set:set_career',
  path: ['Career root'],
  challengeIds: ['lc_1', 'lc_2'],
}, {
  key: 'custom-group:group_arrays',
  path: ['Career root', 'Arrays'],
  challengeIds: ['lc_3', 'lc_4'],
}]);
assert.deepEqual([...customInitial.get('custom-set:set_career')], ['lc_1']);
assert.deepEqual([...customInitial.get('custom-group:group_arrays')], ['lc_3']);
assert.equal(
  customInitial.has('custom-set:set_open'),
  false,
  'A Personal root without Career mode must not create locking context.',
);
const customAfterProgress = buildCustomCareerUnlockMap(
  customCareerSets,
  new Set(['lc_1', 'lc_3']),
);
assert.deepEqual([...customAfterProgress.get('custom-set:set_career')], ['lc_1', 'lc_2']);
assert.deepEqual(
  [...customAfterProgress.get('custom-group:group_arrays')],
  ['lc_3', 'lc_4'],
  'Each leaf advances independently inside one Career-mode Personal root.',
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
