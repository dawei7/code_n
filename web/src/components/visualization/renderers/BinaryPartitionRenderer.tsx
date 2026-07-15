import { Fragment, useMemo } from 'react';

import type {
  BinaryPartitionBoundary,
  BinaryPartitionVisualizationDefinition,
  BinaryPartitionVisualizationStep,
} from '../../../types/api';

export function BinaryPartitionRenderer({
  definition,
  step,
  previousStep,
}: {
  definition: BinaryPartitionVisualizationDefinition;
  step: BinaryPartitionVisualizationStep;
  previousStep: BinaryPartitionVisualizationStep | null;
}) {
  const leftSize = Math.floor(
    (definition.example.nums1.length + definition.example.nums2.length + 1) / 2,
  );
  const newlyDiscardedCuts = useMemo(() => {
    const previous = previousStep?.state;
    const current = step.state;
    if (!previous || previous.low === null || previous.high === null || current.low === null || current.high === null) {
      return new Set<number>();
    }
    const discarded = new Set<number>();
    for (let cut = previous.low; cut <= previous.high; cut += 1) {
      if (cut < current.low || cut > current.high) discarded.add(cut);
    }
    return discarded;
  }, [previousStep, step.state]);

  return (
    <div className="space-y-4">
      <PartitionVariables definition={definition} step={step} leftSize={leftSize} />
      <SearchRange
        size={definition.example.nums1.length}
        step={step}
        newlyDiscardedCuts={newlyDiscardedCuts}
      />
      <section className="rounded-lg border border-coden-border bg-coden-bg/40 p-4">
        <div className="mb-4 flex flex-wrap items-start justify-between gap-2">
          <div>
            <h3 className="text-xs font-semibold uppercase tracking-wide text-coden-muted">Balanced partition</h3>
            <p className="mt-0.5 text-[11px] text-coden-muted">
              Exactly {leftSize} values must lie left of the two cuts.
            </p>
          </div>
          <div className="flex items-center gap-3 text-[10px] text-coden-muted" aria-label="Partition legend">
            <span className="inline-flex items-center gap-1.5"><span className="h-2.5 w-2.5 rounded-sm bg-coden-accent/20" />left half</span>
            <span className="inline-flex items-center gap-1.5"><span className="h-3 w-0.5 bg-coden-compare" />cut</span>
          </div>
        </div>
        <div className={`space-y-4 ${step.state.changed.includes('cuts') || step.state.changed.includes('boundaries') ? 'coden-visual-updated' : ''}`}>
          <PartitionedArray
            name="A · shorter"
            values={definition.example.nums1}
            cut={step.state.cut1}
          />
          <PartitionedArray
            name="B · longer"
            values={definition.example.nums2}
            cut={step.state.cut2}
          />
        </div>
      </section>
      <BoundaryChecks step={step} />
      <PartitionDecision definition={definition} step={step} />
    </div>
  );
}

function PartitionVariables({
  definition,
  step,
  leftSize,
}: {
  definition: BinaryPartitionVisualizationDefinition;
  step: BinaryPartitionVisualizationStep;
  leftSize: number;
}) {
  const state = step.state;
  const total = definition.example.nums1.length + definition.example.nums2.length;
  const values = [
    { label: 'total', value: total, updated: false },
    { label: 'left size', value: leftSize, updated: false },
    { label: 'search [low, high]', value: state.low === null ? '—' : `[${state.low}, ${state.high}]`, updated: state.changed.includes('range') },
    { label: 'cuts [A, B]', value: state.cut1 === null ? '—' : `[${state.cut1}, ${state.cut2}]`, updated: state.changed.includes('cuts') },
  ];
  return (
    <div className="grid grid-cols-2 gap-2 lg:grid-cols-4" aria-label="Partition variables">
      {values.map((item) => (
        <div key={item.label} className={`rounded-lg border border-coden-border bg-coden-inner px-3 py-2 ${item.updated ? 'coden-visual-updated' : ''}`}>
          <div className="text-[9px] font-semibold uppercase tracking-wide text-coden-muted">{item.label}</div>
          <div className="mt-1 font-mono text-base font-semibold text-coden-text">{item.value}</div>
        </div>
      ))}
    </div>
  );
}

function SearchRange({
  size,
  step,
  newlyDiscardedCuts,
}: {
  size: number;
  step: BinaryPartitionVisualizationStep;
  newlyDiscardedCuts: Set<number>;
}) {
  const { low, high, cut1 } = step.state;
  return (
    <section className={`rounded-lg border border-coden-border bg-coden-inner/50 p-4 ${step.state.changed.includes('range') ? 'coden-visual-updated' : ''}`}>
      <div className="mb-3 flex flex-wrap items-end justify-between gap-2">
        <div>
          <h3 className="text-xs font-semibold uppercase tracking-wide text-coden-muted">Search only A's cut positions</h3>
          <p className="mt-0.5 text-[11px] text-coden-muted">The cut in B is forced by the required left-half size.</p>
        </div>
        <span className="font-mono text-[10px] text-coden-muted">{size + 1} possible cuts</span>
      </div>
      <div className="grid gap-2" style={{ gridTemplateColumns: `repeat(${size + 1}, minmax(0, 1fr))` }} role="list" aria-label="Binary search cut positions">
        {Array.from({ length: size + 1 }, (_, cut) => {
          const selected = cut1 === cut;
          const candidate = low !== null && high !== null && cut >= low && cut <= high;
          const newlyDiscarded = newlyDiscardedCuts.has(cut);
          return (
            <div
              key={cut}
              role="listitem"
              aria-label={`Cut ${cut}, ${selected ? 'selected' : candidate ? 'still possible' : 'discarded'}`}
              className={`rounded border px-1 py-2 text-center font-mono text-xs transition-all duration-300 ${
                selected
                  ? 'border-coden-compare bg-coden-compare/15 text-coden-text'
                  : candidate
                    ? 'border-coden-border bg-coden-bg text-coden-text'
                    : 'border-coden-border/50 bg-coden-bg/30 text-coden-muted opacity-50'
              } ${newlyDiscarded ? 'coden-visual-updated' : ''}`}
            >
              <span className="block text-[8px] uppercase tracking-wide text-coden-muted">cut</span>
              {cut}
            </div>
          );
        })}
      </div>
    </section>
  );
}

function PartitionedArray({ name, values, cut }: { name: string; values: number[]; cut: number | null }) {
  return (
    <div>
      <div className="mb-2 flex items-center justify-between gap-2">
        <span className="text-[10px] font-semibold uppercase tracking-wide text-coden-muted">{name}</span>
        <span className="font-mono text-[10px] text-coden-muted">cut = {cut ?? '—'}</span>
      </div>
      <div className="flex min-w-0 items-stretch" role="list" aria-label={`${name} values`}>
        {values.map((value, index) => {
          const onLeft = cut !== null && index < cut;
          const boundary = cut !== null && (index === cut - 1 || index === cut);
          return (
            <Fragment key={`${name}-${index}`}>
              {cut === index && <CutMarker />}
              <div
                role="listitem"
                aria-label={`${value}, index ${index}, ${onLeft ? 'left' : 'right'} partition${boundary ? ', boundary value' : ''}`}
                className={`flex min-w-0 flex-1 flex-col items-center justify-center border-y border-r border-coden-border px-1 py-2 font-mono text-sm text-coden-text first:border-l ${
                  onLeft ? 'bg-coden-accent/10' : 'bg-coden-inner'
                } ${boundary ? 'font-semibold' : ''}`}
              >
                <span>{value}</span>
                <span className="mt-0.5 text-[8px] font-normal text-coden-muted">{index}</span>
              </div>
            </Fragment>
          );
        })}
        {cut === values.length && <CutMarker />}
      </div>
    </div>
  );
}

function CutMarker() {
  return <span aria-hidden="true" className="w-0 shrink-0 border-l-2 border-coden-compare" />;
}

function BoundaryChecks({ step }: { step: BinaryPartitionVisualizationStep }) {
  const { boundaries, comparison, changed } = step.state;
  return (
    <section className={`grid gap-2 sm:grid-cols-2 ${changed.includes('comparison') ? 'coden-visual-updated' : ''}`} aria-label="Cross-boundary checks">
      <ComparisonCard
        label="A.left ≤ B.right"
        left={boundaries.left1}
        right={boundaries.right2}
        passed={comparison.left1_le_right2}
      />
      <ComparisonCard
        label="B.left ≤ A.right"
        left={boundaries.left2}
        right={boundaries.right1}
        passed={comparison.left2_le_right1}
      />
    </section>
  );
}

function ComparisonCard({
  label,
  left,
  right,
  passed,
}: {
  label: string;
  left: BinaryPartitionBoundary | null;
  right: BinaryPartitionBoundary | null;
  passed: boolean | null;
}) {
  const tone = passed === true
    ? 'border-coden-accent bg-coden-accent/10'
    : passed === false
      ? 'border-coden-compare bg-coden-compare/10'
      : 'border-coden-border bg-coden-bg/40';
  return (
    <div className={`rounded-lg border px-4 py-3 ${tone}`}>
      <div className="flex items-center justify-between gap-2">
        <span className="text-[10px] font-semibold uppercase tracking-wide text-coden-muted">{label}</span>
        <span className="font-mono text-[9px] font-semibold uppercase text-coden-text">
          {passed === null ? 'not checked' : passed ? 'pass' : 'fail'}
        </span>
      </div>
      <div className="mt-2 font-mono text-base font-semibold text-coden-text">
        {formatBoundary(left)} <span className="text-coden-muted">≤</span> {formatBoundary(right)}
      </div>
    </div>
  );
}

function PartitionDecision({
  definition,
  step,
}: {
  definition: BinaryPartitionVisualizationDefinition;
  step: BinaryPartitionVisualizationStep;
}) {
  const { violation, result, boundaries, changed } = step.state;
  let title = 'Find a balanced cut';
  let detail = 'Both cross-boundary inequalities must hold at the same time.';
  if (violation === 'left2-too-large') {
    title = 'A is cut too far left';
    detail = 'B.left is larger than A.right, so move A’s cut right and discard smaller cuts.';
  } else if (violation === 'left1-too-large') {
    title = 'A is cut too far right';
    detail = 'A.left is larger than B.right, so move A’s cut left and discard larger cuts.';
  } else if (violation === 'valid') {
    title = 'The partition is globally sorted';
    detail = 'Every value in the combined left half is now at most every value in the combined right half.';
  }

  const total = definition.example.nums1.length + definition.example.nums2.length;
  const medianFormula = total % 2
    ? `max(${formatBoundary(boundaries.left1)}, ${formatBoundary(boundaries.left2)}) = ${result}`
    : `(max(left) + min(right)) / 2 = ${result}`;
  return (
    <section className={`rounded-lg border border-coden-border bg-coden-bg/40 px-4 py-3 ${changed.includes('result') ? 'coden-visual-updated' : ''}`} aria-live="polite">
      <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h3 className="text-xs font-semibold text-coden-text">{title}</h3>
          <p className="mt-0.5 text-[11px] leading-relaxed text-coden-muted">{detail}</p>
        </div>
        {result !== null && (
          <div className="shrink-0 rounded border border-coden-accent/40 bg-coden-accent/10 px-3 py-2 text-right">
            <div className="text-[9px] font-semibold uppercase tracking-wide text-coden-accent">median</div>
            <div className="mt-0.5 font-mono text-xs font-semibold text-coden-text">{medianFormula}</div>
          </div>
        )}
      </div>
    </section>
  );
}

function formatBoundary(value: BinaryPartitionBoundary | null): string {
  if (value === null) return '—';
  if (value === '-inf') return '−∞';
  if (value === 'inf') return '+∞';
  return String(value);
}
