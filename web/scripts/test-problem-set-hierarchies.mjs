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
const hierarchySource = (
  await transpile(new URL('../src/lib/problemSetHierarchies.ts', import.meta.url))
).replace("from './algorithmSets'", `from '${algorithmUrl}'`);
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

assert.equal(STANDARD_HIERARCHY_OPTIONS.length, 7);
const allProblems = buildStandardProblemHierarchy('leetcode', challenges);
assert.equal(hierarchyProblemCount(allProblems.nodes), 2);
assert.equal(
  allProblems.nodes[0].children.length,
  2,
  'All Problems must expose the standard category-to-topic hierarchy.',
);
assert.equal(hierarchyProblemCount(buildStandardProblemHierarchy('elo', challenges).nodes), 1);
assert.equal(hierarchyProblemCount(buildStandardProblemHierarchy('frequency', challenges).nodes), 1);
assert.equal(hierarchyProblemCount(buildStandardProblemHierarchy('leetcode_company', challenges).nodes), 1);
const studyPlans = buildStandardProblemHierarchy('leetcode_studyplan', challenges);
assert.equal(hierarchyProblemCount(studyPlans.nodes), 1);
assert.equal(studyPlans.career_mode, true, 'Official Study Plans must advertise Career mode.');
const neetcode = buildStandardProblemHierarchy('neetcode', challenges);
assert.equal(hierarchyProblemCount(neetcode.nodes), 1);
assert.equal(neetcode.career_mode, true, 'NeetCode subsets must advertise Career mode.');
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
