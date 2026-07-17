import assert from 'node:assert/strict';
import { Buffer } from 'node:buffer';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';

const sourceUrl = new URL('../src/lib/customProblemSets.ts', import.meta.url);
const source = await readFile(sourceUrl, 'utf8');
const output = ts.transpileModule(source, {
  compilerOptions: {
    module: ts.ModuleKind.ES2022,
    target: ts.ScriptTarget.ES2022,
  },
}).outputText;
const moduleUrl = `data:text/javascript;base64,${Buffer.from(output).toString('base64')}`;
const {
  addGroupToCustomSet,
  addProblemToCustomSet,
  collectCustomChallengeIds,
  copyCustomNode,
  countSetProblems,
  maxGroupDepth,
  moveCustomNode,
} = await import(moduleUrl);

const base = [{
  id: 'set_one',
  name: 'Interview path',
  description: '',
  nodes: [],
}];

const levelOne = addGroupToCustomSet(base, 'set_one', null, 'Level one');
assert.equal(levelOne.ok, true);
const levelOneId = levelOne.sets[0].nodes[0].id;
const levelTwo = addGroupToCustomSet(levelOne.sets, 'set_one', levelOneId, 'Level two');
assert.equal(levelTwo.ok, true);
const levelTwoId = levelTwo.sets[0].nodes[0].children[0].id;
const levelThree = addGroupToCustomSet(levelTwo.sets, 'set_one', levelTwoId, 'Level three');
assert.equal(levelThree.ok, true);
const levelThreeId = levelThree.sets[0].nodes[0].children[0].children[0].id;
assert.equal(maxGroupDepth(levelThree.sets[0].nodes), 3);

const levelFour = addGroupToCustomSet(levelThree.sets, 'set_one', levelThreeId, 'Level four');
assert.equal(levelFour.ok, false, 'The builder must reject a fourth nested group level.');

const withProblem = addProblemToCustomSet(levelThree.sets, 'set_one', levelThreeId, 'lc_1');
assert.equal(withProblem.ok, true);
assert.deepEqual([...collectCustomChallengeIds(withProblem.sets)], ['lc_1']);
const repeatedProblem = addProblemToCustomSet(withProblem.sets, 'set_one', null, 'lc_1');
assert.equal(repeatedProblem.ok, true, 'A problem may be placed in multiple study stages.');
assert.equal(countSetProblems(repeatedProblem.sets[0]), 2);

const intoDescendant = moveCustomNode(
  withProblem.sets,
  'set_one',
  levelOneId,
  'set_one',
  levelThreeId,
);
assert.equal(
  intoDescendant.ok,
  false,
  'A group must not be movable into one of its own descendants.',
);

const rootItems = [{
  id: 'set_order',
  name: 'Order',
  description: '',
  nodes: [
    { type: 'problem', id: 'item_a', challenge_id: 'lc_1' },
    { type: 'problem', id: 'item_b', challenge_id: 'lc_2' },
  ],
}];
const freelyMoved = moveCustomNode(
  rootItems,
  'set_order',
  'item_b',
  'set_order',
  null,
  'item_a',
);
assert.equal(freelyMoved.ok, true);
assert.deepEqual(
  freelyMoved.sets[0].nodes.map((node) => node.id),
  ['item_b', 'item_a'],
  'Dropping before an exact sibling must place the item at that position.',
);

const copySource = [{
  id: 'set_source',
  name: 'Source',
  description: '',
  nodes: [{
    type: 'group',
    id: 'group_source',
    name: 'Graphs',
    children: [{
      type: 'group',
      id: 'group_nested',
      name: 'Traversal',
      children: [{ type: 'problem', id: 'item_graph', challenge_id: 'lc_1' }],
    }],
  }],
}, {
  id: 'set_target',
  name: 'Target',
  description: '',
  nodes: [],
}];
const copied = copyCustomNode(
  copySource,
  'set_source',
  'group_source',
  'set_target',
  null,
);
assert.equal(copied.ok, true);
assert.equal(copied.sets[0].nodes.length, 1, 'Copying must preserve the source tree.');
assert.equal(copied.sets[1].nodes[0].name, 'Graphs');
assert.equal(copied.sets[1].nodes[0].children[0].name, 'Traversal');
assert.equal(
  copied.sets[1].nodes[0].children[0].children[0].challenge_id,
  'lc_1',
  'Copying a folder must preserve every nested problem.',
);
assert.notEqual(
  copied.sets[1].nodes[0].id,
  'group_source',
  'Every copied tree item must receive a fresh persistent id.',
);
assert.notEqual(copied.sets[1].nodes[0].children[0].id, 'group_nested');
assert.notEqual(
  copied.sets[1].nodes[0].children[0].children[0].id,
  'item_graph',
  'Fresh ids must be assigned recursively throughout the copied structure.',
);

console.log('Custom problem-set tree regressions passed.');
