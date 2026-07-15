import { useMemo } from 'react';

import type {
  ArrayHashMapVisualizationDefinition,
  ArrayHashMapVisualizationStep,
} from '../../../types/api';

export function ArrayHashMapRenderer({
  definition,
  step,
  previousStep,
}: {
  definition: ArrayHashMapVisualizationDefinition;
  step: ArrayHashMapVisualizationStep;
  previousStep: ArrayHashMapVisualizationStep | null;
}) {
  const newlyStoredValues = useMemo(() => {
    const previousValues = new Set((previousStep?.state.seen ?? []).map((entry) => entry.value));
    return new Set(
      step.state.seen
        .filter((entry) => !previousValues.has(entry.value))
        .map((entry) => entry.value),
    );
  }, [previousStep, step.state.seen]);

  return (
    <div className="space-y-4">
      <VariableStrip step={step} />
      <ArrayScene definition={definition} step={step} />
      <DecisionFlow definition={definition} step={step} />
      <HashMapScene step={step} newlyStoredValues={newlyStoredValues} />
    </div>
  );
}

function VariableStrip({ step }: { step: ArrayHashMapVisualizationStep }) {
  const { variables, changed } = step.state;
  return (
    <div className="grid grid-cols-1 gap-2 sm:grid-cols-3" aria-label="Current variables">
      <VariableCard label="index" value={variables.index} updated={changed.includes('index')} />
      <VariableCard label="value" value={variables.value} updated={changed.includes('value')} />
      <VariableCard label="need" value={variables.complement} updated={changed.includes('complement')} />
    </div>
  );
}

function VariableCard({ label, value, updated }: { label: string; value: number | null; updated: boolean }) {
  return (
    <div className={`rounded-lg border border-coden-border bg-coden-inner px-3 py-2 ${updated ? 'coden-visual-updated' : ''}`}>
      <div className="flex items-center justify-between gap-2 text-[10px] uppercase tracking-wide text-coden-muted">
        <span>{label}</span>
        {updated && <span className="text-coden-accent">changed</span>}
      </div>
      <div className="mt-1 font-mono text-lg font-semibold text-coden-text">{value ?? '—'}</div>
    </div>
  );
}

function ArrayScene({
  definition,
  step,
}: {
  definition: ArrayHashMapVisualizationDefinition;
  step: ArrayHashMapVisualizationStep;
}) {
  const state = step.state;
  const resultIndices = new Set(state.result ?? []);
  return (
    <section className="rounded-lg border border-coden-border bg-coden-bg/40 p-4">
      <div className="mb-4 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h3 className="text-xs font-semibold uppercase tracking-wide text-coden-muted">Input array</h3>
          <p className="mt-0.5 text-[11px] text-coden-muted">Processed prefix grows from left to right.</p>
        </div>
        <div className="rounded border border-coden-border bg-coden-inner px-3 py-1.5 font-mono text-xs text-coden-text">
          target = <strong className="text-coden-accent">{definition.example.target}</strong>
        </div>
      </div>

      <div className="flex flex-wrap items-end gap-3" role="list" aria-label="Input array values">
        {definition.example.nums.map((value, index) => {
          const isCurrent = state.current_index === index;
          const isMatch = state.match_index === index;
          const isResult = resultIndices.has(index);
          const isVisited = state.visited_indices.includes(index);
          const role = isResult ? 'answer' : isCurrent ? 'current' : isMatch ? 'match' : isVisited ? 'processed' : 'waiting';
          const tone = isResult
            ? 'border-coden-accent bg-coden-accent/20'
            : isCurrent
              ? 'border-coden-read bg-coden-read/15'
              : isMatch
                ? 'border-coden-compare bg-coden-compare/15'
                : isVisited
                  ? 'border-coden-border bg-coden-inner'
                  : 'border-coden-border bg-coden-surface';
          return (
            <div key={index} role="listitem" aria-label={`Index ${index}, value ${value}, ${role}`} className="text-center">
              <div className="mb-1 h-4 text-[9px] font-semibold uppercase tracking-wide text-coden-muted">
                {(isResult || isCurrent || isMatch) && role}
              </div>
              <div className={`relative flex h-16 min-w-16 items-center justify-center rounded-xl border-2 font-mono text-xl font-semibold text-coden-text transition-all duration-300 ${tone}`}>
                {isCurrent && (
                  <span aria-hidden="true" className="absolute -top-2 h-2 w-2 rotate-45 bg-coden-read" />
                )}
                {value}
              </div>
              <div className="mt-1 font-mono text-[10px] text-coden-muted">index {index}</div>
            </div>
          );
        })}
      </div>
    </section>
  );
}

function DecisionFlow({
  definition,
  step,
}: {
  definition: ArrayHashMapVisualizationDefinition;
  step: ArrayHashMapVisualizationStep;
}) {
  const { variables, event, match_index: matchIndex, changed, result } = step.state;
  let lookup = 'Waiting for a value';
  if (variables.value !== null && variables.complement === null) lookup = 'Compute need next';
  if (variables.complement !== null) lookup = `Check key ${variables.complement}`;
  if (event === 'miss') lookup = 'Not in seen';
  if (event === 'stored') lookup = 'Miss resolved';
  if (event === 'found' || event === 'returned') lookup = `Found index ${matchIndex}`;

  return (
    <section className="rounded-lg border border-coden-border bg-coden-inner/50 p-4" aria-label="Complement lookup flow">
      <div className="mb-3 flex items-center justify-between gap-2">
        <div>
          <h3 className="text-xs font-semibold uppercase tracking-wide text-coden-muted">One question per value</h3>
          <p className="mt-0.5 text-[11px] text-coden-muted">Current value fixes the key we must find.</p>
        </div>
        {result && (
          <span className={`rounded-full border border-coden-accent/40 bg-coden-accent/10 px-2 py-1 font-mono text-[10px] font-semibold text-coden-accent ${changed.includes('result') ? 'coden-visual-updated' : ''}`}>
            return [{result.join(', ')}]
          </span>
        )}
      </div>
      <div className="grid items-stretch gap-2 sm:grid-cols-[1fr_auto_1.25fr_auto_1fr]">
        <FlowNode
          label="Current value"
          value={variables.value === null ? '—' : String(variables.value)}
          updated={changed.includes('value')}
        />
        <FlowArrow />
        <FlowNode
          label="Forced complement"
          value={variables.complement === null
            ? `${definition.example.target} - ?`
            : `${definition.example.target} - ${variables.value} = ${variables.complement}`}
          updated={changed.includes('complement')}
          accent
        />
        <FlowArrow />
        <FlowNode
          label="Hash lookup"
          value={lookup}
          updated={changed.includes('lookup')}
          success={event === 'found' || event === 'returned'}
        />
      </div>
    </section>
  );
}

function FlowNode({
  label,
  value,
  updated,
  accent = false,
  success = false,
}: {
  label: string;
  value: string;
  updated: boolean;
  accent?: boolean;
  success?: boolean;
}) {
  const tone = success
    ? 'border-coden-accent bg-coden-accent/10'
    : accent
      ? 'border-coden-compare/60 bg-coden-compare/10'
      : 'border-coden-border bg-coden-bg';
  return (
    <div className={`flex min-h-16 flex-col justify-center rounded-lg border px-3 py-2 ${tone} ${updated ? 'coden-visual-updated' : ''}`}>
      <div className="text-[9px] font-semibold uppercase tracking-wide text-coden-muted">{label}</div>
      <div className="mt-1 font-mono text-xs font-semibold text-coden-text">{value}</div>
    </div>
  );
}

function FlowArrow() {
  return (
    <div aria-hidden="true" className="hidden items-center text-coden-muted sm:flex">→</div>
  );
}

function HashMapScene({
  step,
  newlyStoredValues,
}: {
  step: ArrayHashMapVisualizationStep;
  newlyStoredValues: Set<number>;
}) {
  const state = step.state;
  return (
    <section className={`rounded-lg border border-coden-border bg-coden-bg/40 p-4 ${state.changed.includes('seen') ? 'coden-visual-updated' : ''}`}>
      <div className="flex items-center justify-between gap-3">
        <div>
          <h3 className="text-xs font-semibold uppercase tracking-wide text-coden-muted">Seen map</h3>
          <p className="mt-0.5 text-[11px] text-coden-muted">value → earlier index</p>
        </div>
        <span className="font-mono text-[10px] text-coden-muted">{state.seen.length} entries</span>
      </div>
      <div className="mt-3 flex min-h-12 flex-wrap items-center gap-2" aria-label="Hash map entries">
        {state.seen.length === 0 ? (
          <div className="rounded border border-dashed border-coden-border px-3 py-2 font-mono text-xs text-coden-muted">empty</div>
        ) : (
          state.seen.map((entry) => {
            const isNew = newlyStoredValues.has(entry.value);
            const isLookup = state.variables.complement === entry.value && (state.event === 'found' || state.event === 'returned');
            return (
              <div
                key={entry.value}
                className={`rounded border px-3 py-2 font-mono text-xs text-coden-text transition-all duration-300 ${
                  isLookup
                    ? 'border-coden-compare bg-coden-compare/15'
                    : 'border-coden-border bg-coden-inner'
                } ${isNew ? 'coden-visual-updated' : ''}`}
              >
                <span className="font-semibold">{entry.value}</span>
                <span className="mx-2 text-coden-muted">→</span>
                <span>{entry.index}</span>
                {isNew && <span className="ml-2 text-[9px] uppercase text-coden-accent">new</span>}
                {isLookup && <span className="ml-2 text-[9px] uppercase text-coden-compare">match</span>}
              </div>
            );
          })
        )}
      </div>
    </section>
  );
}
