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
  addTemplateToCustomSet,
  collectCustomChallengeIds,
  copyCustomNode,
  countSetProblems,
  createCustomSetFromTemplate,
  maxGroupDepth,
  moveCustomNode,
  unwrapCustomGroup,
} = await import(moduleUrl);

const base = [{
  id: 'set_one',
  name: 'Interview path',
  description: '',
  career_mode: false,
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
const ignoredSameLeaf = addProblemToCustomSet(
  repeatedProblem.sets,
  'set_one',
  null,
  'lc_1',
);
assert.equal(ignoredSameLeaf.ok, true);
assert.equal(ignoredSameLeaf.ignored, true, 'A repeated problem in the same leaf is ignored.');
assert.equal(countSetProblems(ignoredSameLeaf.sets[0]), 2);
const bulkFilteredProblems = addTemplateToCustomSet(
  ignoredSameLeaf.sets,
  'set_one',
  null,
  [
    { type: 'problem', challenge_id: 'lc_1' },
    { type: 'problem', challenge_id: 'lc_2' },
    { type: 'problem', challenge_id: 'lc_3' },
  ],
);
assert.equal(bulkFilteredProblems.ok, true);
assert.deepEqual(
  bulkFilteredProblems.sets[0].nodes
    .filter((node) => node.type === 'problem')
    .map((node) => node.challenge_id),
  ['lc_1', 'lc_2', 'lc_3'],
  'Bulk additions must preserve filter order and ignore same-leaf duplicates.',
);
const nestedProblemId = ignoredSameLeaf.sets[0]
  .nodes[0].children[0].children[0].children[0].id;
const ignoredMoveIntoDuplicateLeaf = moveCustomNode(
  ignoredSameLeaf.sets,
  'set_one',
  nestedProblemId,
  'set_one',
  null,
);
assert.equal(ignoredMoveIntoDuplicateLeaf.ok, true);
assert.equal(
  ignoredMoveIntoDuplicateLeaf.ignored,
  true,
  'Moving a problem into a leaf that already contains it must leave the source placement intact.',
);
assert.equal(countSetProblems(ignoredMoveIntoDuplicateLeaf.sets[0]), 2);

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

const unwrapFixture = [{
  id: 'set_unwrap',
  name: 'Flatten copied hierarchy',
  description: '',
  career_mode: false,
  nodes: [
    { type: 'problem', id: 'root_one', challenge_id: 'lc_1' },
    {
      type: 'group',
      id: 'middle_level',
      name: 'Algorithms',
      children: [
        { type: 'problem', id: 'duplicate_one', challenge_id: 'lc_1' },
        {
          type: 'group',
          id: 'preserved_child',
          name: 'String',
          children: [
            { type: 'problem', id: 'nested_three', challenge_id: 'lc_3' },
          ],
        },
        { type: 'problem', id: 'promoted_two', challenge_id: 'lc_2' },
      ],
    },
    { type: 'problem', id: 'root_four', challenge_id: 'lc_4' },
  ],
}];
const unwrapped = unwrapCustomGroup(unwrapFixture, 'set_unwrap', 'middle_level');
assert.equal(unwrapped.ok, true);
assert.deepEqual(
  unwrapped.sets[0].nodes.map((node) => node.id),
  ['root_one', 'preserved_child', 'promoted_two', 'root_four'],
  'Removing a folder level must promote its children at the folder position and preserve order.',
);
assert.equal(
  unwrapped.sets[0].nodes[1].children[0].id,
  'nested_three',
  'Promoted child folders must retain their complete subtrees and placement ids.',
);
assert.equal(
  countSetProblems(unwrapped.sets[0]),
  4,
  'A promoted problem already present in the parent leaf must be ignored.',
);

const rootItems = [{
  id: 'set_order',
  name: 'Order',
  description: '',
  career_mode: false,
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
  career_mode: true,
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
  career_mode: false,
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

const copiedDuplicateProblem = copyCustomNode(
  copied.sets,
  'set_source',
  'item_graph',
  'set_target',
  copied.sets[1].nodes[0].children[0].id,
);
assert.equal(copiedDuplicateProblem.ok, true);
assert.equal(
  copiedDuplicateProblem.ignored,
  true,
  'Copying a problem into a leaf that already contains it is idempotent.',
);

const fiveRoots = Array.from({ length: 5 }, (_, index) => ({
  id: `set_limit_${index}`,
  name: `Root ${index}`,
  description: '',
  career_mode: false,
  nodes: [],
}));
const sixthRoot = createCustomSetFromTemplate(
  fiveRoots,
  'Root 6',
  '',
  [{ type: 'problem', challenge_id: 'lc_1' }],
);
assert.equal(sixthRoot.ok, false, 'Personal must reject a sixth root.');

const hierarchyRoot = createCustomSetFromTemplate(
  [],
  'Copied hierarchy',
  'Complete source tree',
  [{
    type: 'group',
    name: 'Arrays',
    children: [
      { type: 'problem', challenge_id: 'lc_1' },
      { type: 'problem', challenge_id: 'lc_1' },
      {
        type: 'group',
        name: 'Second leaf',
        children: [{ type: 'problem', challenge_id: 'lc_1' }],
      },
    ],
  }],
  true,
);
assert.equal(hierarchyRoot.ok, true);
assert.equal(hierarchyRoot.sets[0].career_mode, true);
assert.equal(
  hierarchyRoot.sets[0].nodes[0].children.filter((node) => node.type === 'problem').length,
  1,
  'Hierarchy import must suppress duplicates only within one leaf.',
);
assert.equal(countSetProblems(hierarchyRoot.sets[0]), 2);

console.log('Custom problem-set tree regressions passed.');
