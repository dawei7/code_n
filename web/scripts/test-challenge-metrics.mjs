import assert from 'node:assert/strict';
import { Buffer } from 'node:buffer';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';

const sourceUrl = new URL('../src/lib/challengeMetrics.ts', import.meta.url);
const source = await readFile(sourceUrl, 'utf8');
const output = ts.transpileModule(source, {
  compilerOptions: {
    module: ts.ModuleKind.ES2022,
    target: ts.ScriptTarget.ES2022,
  },
}).outputText;
const moduleUrl = `data:text/javascript;base64,${Buffer.from(output).toString('base64')}`;
const {
  calculateDirectEloAverage,
  calculateDirectFrequencyAverage,
  compareFrequencyPriority,
} = await import(moduleUrl);

const lowerEstimatedElo = {
  id: 'lc_1',
  elo_rating: null,
  estimated_elo_rating: 1250,
  frequency: 80,
};
const higherRealElo = {
  id: 'lc_2',
  elo_rating: 1600,
  estimated_elo_rating: null,
  frequency: 80,
};
const higherFrequency = {
  id: 'lc_3',
  elo_rating: 2200,
  estimated_elo_rating: null,
  frequency: 90,
};

assert.deepEqual(
  [higherRealElo, lowerEstimatedElo, higherFrequency]
    .sort(compareFrequencyPriority)
    .map((challenge) => challenge.id),
  ['lc_3', 'lc_1', 'lc_2'],
  'Frequency must sort descending, with lower displayed Elo first on equal Frequency.',
);

assert.deepEqual(
  calculateDirectFrequencyAverage([
    { ...lowerEstimatedElo, frequency: 100 },
    { ...higherRealElo, frequency: 0 },
    { ...lowerEstimatedElo, frequency: 100 },
  ]),
  { value: 50, problemCount: 2 },
  'Frequency averages must include zero and count duplicate problem ids only once.',
);

assert.deepEqual(
  calculateDirectEloAverage([
    lowerEstimatedElo,
    higherRealElo,
    lowerEstimatedElo,
  ]),
  { value: 1425, problemCount: 2, estimatedCount: 1 },
  'Elo averages must remain direct unique-problem means.',
);

console.log('Challenge metric ordering and direct-average regressions passed.');
