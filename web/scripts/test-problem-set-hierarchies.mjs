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

const algorithmSource = await transpile(
  new URL('../src/lib/algorithmSets.ts', import.meta.url),
);
const algorithmUrl = `data:text/javascript;base64,${Buffer.from(algorithmSource).toString('base64')}`;
const eloBandsSource = await transpile(
  new URL('../src/lib/eloBands.ts', import.meta.url),
);
const eloBandsUrl = `data:text/javascript;base64,${Buffer.from(eloBandsSource).toString('base64')}`;
const frequencyBandsSource = await transpile(
  new URL('../src/lib/frequencyBands.ts', import.meta.url),
);
const frequencyBandsUrl = `data:text/javascript;base64,${Buffer.from(frequencyBandsSource).toString('base64')}`;
const {
  FREQUENCY_BANDS,
  frequencyBandForValue,
  formatFrequencyBand,
} = await import(frequencyBandsUrl);
const questOrderSource = await transpile(
  new URL('../src/lib/leetcodeQuestOrder.ts', import.meta.url),
);
const questOrderUrl = `data:text/javascript;base64,${Buffer.from(questOrderSource).toString('base64')}`;
const {
  compareLeetcodeQuestOrder,
  leetcodeQuestGroupId,
} = await import(questOrderUrl);
const hierarchySource = (
  await transpile(new URL('../src/lib/problemSetHierarchies.ts', import.meta.url))
)
  .replace("from './algorithmSets'", `from '${algorithmUrl}'`)
  .replace("from './eloBands'", `from '${eloBandsUrl}'`)
  .replace("from './frequencyBands'", `from '${frequencyBandsUrl}'`);
const hierarchyUrl = `data:text/javascript;base64,${Buffer.from(hierarchySource).toString('base64')}`;
const {
  STANDARD_HIERARCHY_OPTIONS,
  buildPersonalProblemHierarchy,
  buildStandardProblemHierarchy,
  filterProblemHierarchy,
  hierarchyNodesToTemplates,
  hierarchyProblemCount,
} = await import(hierarchyUrl);

function challenge(id, overrides = {}) {
  return {
    id,
    name: `Problem ${id}`,
    category: 'leetcode_algorithms',
    leetcode_category_title: 'Algorithms',
    leetcode_frontend_id: id.replace('lc_', ''),
    leetcode_topics: [{ name: 'Array', slug: 'array' }],
    leetcode_company_tags: [],
    leetcode_study_plans: [],
    leetcode_external_subsets: [],
    elo_rating: null,
    estimated_elo_rating: null,
    frequency: null,
    ...overrides,
  };
}

const challenges = [
  challenge('lc_1', {
    elo_rating: 1200,
    frequency: 90,
    leetcode_topics: [
      { name: 'Array', slug: 'array' },
      { name: 'Hash Table', slug: 'hash-table' },
    ],
    leetcode_company_tags: [{ name: 'Example Corp', slug: 'example-corp' }],
    leetcode_study_plans: [{
      plan_name: 'Interview 30',
      path: ['Week 1'],
      section_order: 1,
      problem_order: 1,
    }],
    leetcode_external_subsets: [{
      kind: 'neetcode',
      subset_name: 'NeetCode 150',
      path: ['Arrays & Hashing'],
      subset_order: 1,
      section_order: 1,
      problem_order: 1,
    }],
  }),
  challenge('lc_2', {
    estimated_elo_rating: 1500,
    frequency: null,
    leetcode_topics: [{ name: 'Array', slug: 'array' }],
    leetcode_external_subsets: [{
      kind: 'algomaster',
      subset_name: 'AlgoMaster 75',
      path: ['Arrays'],
      subset_order: 1,
      section_order: 1,
      problem_order: 2,
    }],
  }),
];

assert.equal(STANDARD_HIERARCHY_OPTIONS.length, 11);
assert.equal(STANDARD_HIERARCHY_OPTIONS[0].label, 'All Problems by Topics');
assert.equal(STANDARD_HIERARCHY_OPTIONS[1].label, 'All Problems by ID');
assert.equal(STANDARD_HIERARCHY_OPTIONS[4].label, 'Frequency by Topics');
assert.equal(STANDARD_HIERARCHY_OPTIONS[5].label, 'Frequency Buckets');
assert.equal(
  FREQUENCY_BANDS.every((band) => band.maximum - band.minimum === 10),
  true,
  'Every Frequency bucket must cover the same 10-point distance.',
);
assert.equal(formatFrequencyBand(FREQUENCY_BANDS[0]), '90–100');
assert.equal(frequencyBandForValue(100)?.label, 'Highest Signal');
assert.equal(frequencyBandForValue(89.999)?.label, 'Top Signal');
assert.equal(frequencyBandForValue(0)?.label, 'Minimal Signal');
assert.equal(
  leetcodeQuestGroupId(
    'data-structures-and-algorithms-quest',
    ['Linear Shoal', 'Array I'],
  ),
  'leetcode-quest:data-structures-and-algorithms-quest:0:Linear Shoal:1:Array I',
  'Quest group identity must preserve the full published unit and level path.',
);
const arrayOneQuestOrder = [
  { id: 'lc_485', problemOrder: 3, order: 3, frontendId: 485 },
  { id: 'lc_1470', problemOrder: 2, order: 2, frontendId: 1470 },
  { id: 'lc_1929', problemOrder: 1, order: 1, frontendId: 1929 },
].sort(compareLeetcodeQuestOrder);
assert.deepEqual(
  arrayOneQuestOrder.map((item) => item.id),
  ['lc_1929', 'lc_1470', 'lc_485'],
  'Array I must follow the published Quest order rather than numeric LeetCode ID.',
);
const allProblems = buildStandardProblemHierarchy('leetcode', challenges);
assert.equal(hierarchyProblemCount(allProblems.nodes), 2);
assert.equal(
  allProblems.nodes[0].children.length,
  2,
  'All Problems must expose the standard category-to-topic hierarchy.',
);
const allProblemsById = buildStandardProblemHierarchy('leetcode_id', [...challenges].reverse());
assert.deepEqual(
  allProblemsById.nodes.map((node) => node.challenge_id),
  ['lc_1', 'lc_2'],
  'All Problems by ID must be one flat numeric frontend-ID sequence.',
);
assert.equal(hierarchyProblemCount(buildStandardProblemHierarchy('elo', challenges).nodes), 1);
const eloBuckets = buildStandardProblemHierarchy('elo_buckets', [
  challenge('lc_2', { elo_rating: 1299 }),
  challenge('lc_1', { elo_rating: 1200 }),
]);
assert.equal(eloBuckets.nodes.length, 1, 'One matching Elo band must produce one bucket only.');
assert.deepEqual(
  eloBuckets.nodes[0].children.map((node) => node.challenge_id),
  ['lc_1', 'lc_2'],
  'Problems inside an Elo bucket must remain in strict ascending Elo order.',
);
assert.equal(hierarchyProblemCount(buildStandardProblemHierarchy('frequency', challenges).nodes), 1);
const frequencyBuckets = buildStandardProblemHierarchy('frequency_buckets', [
  challenge('lc_2', { frequency: 91 }),
  challenge('lc_1', { frequency: 99 }),
]);
assert.equal(frequencyBuckets.nodes.length, 1, 'One matching Frequency band must produce one bucket only.');
assert.deepEqual(
  frequencyBuckets.nodes[0].children.map((node) => node.challenge_id),
  ['lc_1', 'lc_2'],
  'Problems inside a Frequency bucket must remain in strict descending Frequency order.',
);
assert.match(frequencyBuckets.nodes[0].name, /Highest Signal/);
assert.equal(hierarchyProblemCount(buildStandardProblemHierarchy('leetcode_company', challenges).nodes), 1);
const studyPlans = buildStandardProblemHierarchy('leetcode_studyplan', challenges);
assert.equal(hierarchyProblemCount(studyPlans.nodes), 1);
assert.equal(studyPlans.career_mode, true, 'Official Study Plans must advertise Career mode.');
const neetcode = buildStandardProblemHierarchy('neetcode', challenges);
assert.equal(hierarchyProblemCount(neetcode.nodes), 1);
assert.equal(neetcode.career_mode, true, 'NeetCode subsets must advertise Career mode.');
const quests = buildStandardProblemHierarchy('leetcode_quest', challenges);
assert.equal(quests.career_mode, true, 'LeetCode Quests must advertise Career mode.');
assert.equal(hierarchyProblemCount(buildStandardProblemHierarchy('algomaster', challenges).nodes), 1);
assert.equal(allProblems.career_mode, false, 'Non-Career standard sets must remain unlabelled.');
const filteredAndSorted = filterProblemHierarchy(allProblems, ['lc_2']);
assert.equal(hierarchyProblemCount(filteredAndSorted.nodes), 1);
assert.equal(
  hierarchyNodesToTemplates(filteredAndSorted.nodes)
    .flatMap((category) => category.children)
    .flatMap((topic) => topic.children)
    .every((problem) => problem.challenge_id === 'lc_2'),
  true,
  'Shared library filters must prune hierarchy problems and empty branches.',
);

const personal = buildPersonalProblemHierarchy({
  id: 'set_personal',
  name: 'Personal path',
  description: 'Reusable tree',
  career_mode: true,
  nodes: [{
    type: 'group',
    id: 'group_arrays',
    name: 'Arrays',
    children: [{ type: 'problem', id: 'item_one', challenge_id: 'lc_1' }],
  }],
});
assert.equal(personal.kind, 'personal');
assert.equal(personal.career_mode, true);
assert.deepEqual(hierarchyNodesToTemplates(personal.nodes), [{
  type: 'group',
  name: 'Arrays',
  children: [{ type: 'problem', challenge_id: 'lc_1' }],
}]);

console.log('Problem-set hierarchy regressions passed.');
