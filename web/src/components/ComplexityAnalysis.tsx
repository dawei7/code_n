import type { ReactNode } from 'react';
import { useAppStore } from '../store/useAppStore';
import type { RunCaseResult, RunResponse } from '../types/api';


type AnalysisTone = 'success' | 'warning' | 'danger' | 'neutral';


export function ComplexityAnalysis() {
  const detail = useAppStore((s) => s.currentDetail);
  const runResult = useAppStore((s) => s.runResult);
  const error = useAppStore((s) => s.error);
  const setActiveTopic = useAppStore((s) => s.setActiveTopic);

  if (!detail) return null;

  const baselineLabel = 'Optimal reference';
  const workloadLabel = 'hidden benchmark cases';

  if (error && !runResult) {
    return (
      <AnalysisShell title="Runtime analysis" requiredComplexity={detail.required_complexity}>
        <EmptyAnalysis
          tone="danger"
          title="The last run could not be analyzed"
          body={error}
          actionLabel="Open editor and cases"
          onAction={() => setActiveTopic('coden')}
        />
      </AnalysisShell>
    );
  }

  if (!runResult) {
    return (
      <AnalysisShell title="Runtime analysis" requiredComplexity={detail.required_complexity}>
        <EmptyAnalysis
          tone="neutral"
          title="Run your solution to measure it"
          body="Press Run to check every visible case, every custom case, and the hidden judge suite."
          actionLabel="Open editor and cases"
          onAction={() => setActiveTopic('coden')}
        />
      </AnalysisShell>
    );
  }

  const customFailures = runResult.case_results.filter(
    (caseResult) => !caseResult.counts_toward_verdict && !caseResult.correct,
  );
  const state = analysisState(runResult, customFailures.length);
  const runtimeReady = Boolean(
    runResult.correct
      && runResult.runtime_check
      && runResult.runtime_user_ms != null
      && runResult.runtime_reference_ms != null
      && runResult.runtime_limit_ms != null,
  );

  return (
    <AnalysisShell title="Runtime analysis" requiredComplexity={detail.required_complexity}>
      <VerdictHero
        tone={state.tone}
        title={state.title}
        body={state.body}
        result={runResult}
      />

      <CorrectnessBreakdown
        results={runResult.case_results}
        officialCorrect={runResult.correct}
        onOpenEditor={() => setActiveTopic('coden')}
      />

      {runResult.correct && (runtimeReady ? (
        (runResult.runtime_scaling_data?.length ?? 0) >= 2
          ? <ScalingRuntimeComparison result={runResult} baselineLabel={baselineLabel} />
          : <RuntimeComparison result={runResult} baselineLabel={baselineLabel} />
      ) : (
        <BenchmarkUnavailable result={runResult} onOpenEditor={() => setActiveTopic('coden')} />
      ))}

      <div className="grid grid-cols-1 gap-3 md:grid-cols-3">
        <ContextCard
          label="Correctness"
          value={runResult.correct ? 'Verified' : 'Needs work'}
          note={runResult.case_results.length
            ? officialCorrectnessNote(runResult.case_results)
            : runResult.correct ? 'Output verified by the challenge judge' : 'The challenge judge rejected the output'}
          tone={runResult.correct ? 'success' : 'danger'}
        />
        <ContextCard
          label="Expected complexity"
          value={detail.required_complexity || 'Not specified'}
          note="The target algorithmic growth for this challenge"
          tone="neutral"
        />
        <ContextCard
          label="Evaluation"
          value={runResult.mode === 'real_test' ? 'Full run' : runResult.case_results.length > 1 ? 'Multiple cases' : 'Single case'}
          note={runResult.runtime_check ? `Timed against ${workloadLabel}` : 'Correctness run without a comparable baseline'}
          tone="neutral"
        />
      </div>

      {runResult.correct && runResult.runtime_check && (
        <BenchmarkDetails result={runResult} baselineLabel={baselineLabel} workloadLabel={workloadLabel} />
      )}
    </AnalysisShell>
  );
}


function AnalysisShell({
  title,
  requiredComplexity,
  children,
}: {
  title: string;
  requiredComplexity: string;
  children: ReactNode;
}) {
  return (
    <div className="flex w-full flex-col gap-5">
      <header className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <div className="text-[10px] font-bold uppercase tracking-[0.18em] text-coden-accent">Performance</div>
          <h2 className="mt-1 text-xl font-bold tracking-tight text-coden-text">{title}</h2>
          <p className="mt-1 max-w-2xl text-xs leading-relaxed text-coden-muted">
            See whether the solution is correct, how it compares with the benchmark, and what to improve next.
          </p>
        </div>
        <div className="rounded-full border border-coden-border bg-coden-inner px-3 py-1.5 text-[11px] text-coden-muted">
          Expected <span className="ml-1 font-mono font-bold text-coden-text">{requiredComplexity || '—'}</span>
        </div>
      </header>
      {children}
    </div>
  );
}


function VerdictHero({
  tone,
  title,
  body,
  result,
}: {
  tone: AnalysisTone;
  title: string;
  body: string;
  result: RunResponse;
}) {
  const style = toneStyles(tone);
  return (
    <section className={`rounded-xl border p-5 ${style.border} ${style.background}`}>
      <div className="flex items-start gap-4">
        <span className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${style.iconBackground} ${style.text}`}>
          <AnalysisIcon tone={tone} />
        </span>
        <div className="min-w-0 flex-1">
          <div className={`text-base font-bold ${style.text}`}>{title}</div>
          <p className="mt-1 text-sm leading-relaxed text-coden-text/90">{body}</p>
          <div className="mt-3 flex flex-wrap gap-2">
            <StatusPill label={result.correct ? 'Correct output' : 'Incorrect output'} good={result.correct} />
            {result.runtime_check && (
              <StatusPill label={result.runtime_passed === false ? 'Over runtime target' : 'Within runtime target'} good={result.runtime_passed !== false} />
            )}
            <span className="rounded-full border border-coden-border/70 bg-coden-surface/50 px-2.5 py-1 text-[10px] font-semibold text-coden-muted">
              {result.mode === 'real_test' ? 'Full evaluation' : 'Practice evaluation'}
            </span>
          </div>
        </div>
      </div>
    </section>
  );
}


function RuntimeComparison({ result, baselineLabel }: { result: RunResponse; baselineLabel: string }) {
  const userMs = result.runtime_user_ms!;
  const referenceMs = result.runtime_reference_ms!;
  const limitMs = result.runtime_limit_ms!;
  const passed = result.runtime_passed !== false;
  const maxValue = Math.max(userMs, limitMs, referenceMs, 0.001) * 1.12;
  const marker = (value: number) => `${Math.max(1.5, Math.min(98.5, (value / maxValue) * 100))}%`;
  const headroom = limitMs > 0 ? ((limitMs - userMs) / limitMs) * 100 : 0;
  const versusReference = referenceMs > 0 ? userMs / referenceMs : null;

  return (
    <section className="overflow-hidden rounded-xl border border-coden-border bg-coden-surface shadow-sm">
      <div className="border-b border-coden-border px-5 py-4">
        <div className="text-sm font-bold text-coden-text">Runtime target</div>
        <div className="mt-1 text-xs text-coden-muted">Your measured runtime must stay at or below the allowed limit.</div>
      </div>
      <div className="grid grid-cols-1 gap-5 p-5 lg:grid-cols-[minmax(0,1.25fr)_minmax(240px,.75fr)]">
        <div>
          <div className="grid grid-cols-2 gap-3">
            <PrimaryMetric label="Your runtime" value={formatMs(userMs)} tone={passed ? 'success' : 'warning'} />
            <PrimaryMetric label="Allowed limit" value={formatMs(limitMs)} tone="neutral" />
          </div>

          <div className="mt-6">
            <div className="relative h-12">
              <div className="absolute inset-x-0 top-4 h-3 overflow-hidden rounded-full bg-coden-inner ring-1 ring-coden-border/80">
                <div className="h-full bg-emerald-500/[0.18]" style={{ width: marker(limitMs) }} />
              </div>
              <div
                className="absolute top-2 z-20 -translate-x-1/2"
                style={{ left: marker(referenceMs) }}
                title={`${baselineLabel}: ${formatMs(referenceMs)}`}
              >
                <span className="block h-7 w-3 rounded-full border-2 border-coden-surface bg-emerald-400 shadow" />
              </div>
              <div className="absolute top-0 h-11 w-px bg-coden-text/70" style={{ left: marker(limitMs) }} />
              <div
                className="absolute top-2 z-30 -translate-x-1/2"
                style={{ left: marker(userMs) }}
                title={`Your code: ${formatMs(userMs)}`}
              >
                <span className="block h-7 w-3 rounded-full border-2 border-coden-surface bg-coden-accent shadow" />
              </div>
            </div>
            <div className="mt-1 flex flex-wrap gap-x-5 gap-y-2 text-[10px] text-coden-muted">
              <Legend color="bg-coden-accent" label="Your code" shape="bar" />
              <Legend color="bg-emerald-400" label={baselineLabel} shape="bar" />
              <Legend color="bg-coden-text/70" label="Allowed limit" shape="line" />
            </div>
          </div>
        </div>

        <div className={`rounded-lg border p-4 ${passed ? 'border-emerald-500/25 bg-emerald-500/[0.08]' : 'border-amber-500/30 bg-amber-500/10'}`}>
          <div className={`text-xs font-bold uppercase tracking-wide ${passed ? 'text-emerald-300' : 'text-amber-300'}`}>
            {passed ? 'Healthy headroom' : 'Optimization needed'}
          </div>
          <div className="mt-2 text-3xl font-bold tabular-nums text-coden-text">
            {passed ? `${Math.max(0, headroom).toFixed(0)}%` : `${Math.abs(headroom).toFixed(0)}%`}
          </div>
          <div className="mt-1 text-xs leading-relaxed text-coden-muted">
            {passed ? 'of the allowed runtime remains.' : 'over the allowed runtime.'}
          </div>
          {versusReference !== null && (
            <div className="mt-4 border-t border-coden-border/70 pt-3 text-xs leading-relaxed text-coden-text">
              Your code ran <span className="font-mono font-bold">{versusReference.toFixed(2)}×</span> the benchmark runtime.
            </div>
          )}
        </div>
      </div>
    </section>
  );
}


function ScalingRuntimeComparison({ result, baselineLabel }: { result: RunResponse; baselineLabel: string }) {
  const samples = result.runtime_scaling_data ?? [];
  const first = samples[0]!;
  const last = samples[samples.length - 1]!;
  const sizeSpan = last.size / first.size;
  const logSizes = samples.map((sample) => Math.log(sample.size));
  const logRatios = samples.map((sample) => Math.log(Math.max(sample.ratio, 1e-9)));
  const meanSize = logSizes.reduce((total, value) => total + value, 0) / logSizes.length;
  const meanRatio = logRatios.reduce((total, value) => total + value, 0) / logRatios.length;
  const slopeNumerator = logSizes.reduce(
    (total, value, index) => total + (value - meanSize) * (logRatios[index]! - meanRatio),
    0,
  );
  const slopeDenominator = logSizes.reduce((total, value) => total + (value - meanSize) ** 2, 0);
  const extraExponent = slopeDenominator > 0 ? slopeNumerator / slopeDenominator : 0;
  const passed = result.runtime_passed !== false;

  return (
    <section className="overflow-hidden rounded-xl border border-coden-border bg-coden-surface shadow-sm">
      <div className="border-b border-coden-border px-5 py-4">
        <div className="text-sm font-bold text-coden-text">Complexity scaling</div>
        <div className="mt-1 text-xs text-coden-muted">
          The user/reference ratio should remain approximately flat as the authored input size grows.
        </div>
      </div>
      <div className="grid grid-cols-1 gap-5 p-5 lg:grid-cols-[minmax(0,1.25fr)_minmax(240px,.75fr)]">
        <div>
          <div className="grid grid-cols-2 gap-3">
            <PrimaryMetric label="Largest-size ratio" value={`${last.ratio.toFixed(2)}×`} tone="neutral" />
            <PrimaryMetric label="Extra growth exponent" value={`${extraExponent >= 0 ? '+' : ''}${extraExponent.toFixed(2)}`} tone={passed ? 'success' : 'warning'} />
          </div>
          <div className="mt-4 overflow-hidden rounded-lg border border-coden-border/80">
            <div className="grid grid-cols-4 gap-2 border-b border-coden-border bg-coden-inner/70 px-3 py-2 text-[9px] font-bold uppercase tracking-wider text-coden-muted">
              <span>Size</span><span>Your code</span><span>{baselineLabel}</span><span>Ratio</span>
            </div>
            {samples.map((sample) => (
              <div key={sample.size} className="grid grid-cols-4 gap-2 border-b border-coden-border/60 px-3 py-2.5 text-xs last:border-b-0">
                <span className="font-mono font-bold text-coden-text">{sample.size.toLocaleString()}</span>
                <span className="font-mono text-coden-accent">{formatMs(sample.user_ms)}</span>
                <span className="font-mono text-emerald-400">{formatMs(sample.reference_ms)}</span>
                <span className="font-mono text-coden-text">{sample.ratio.toFixed(2)}×</span>
              </div>
            ))}
          </div>
        </div>
        <div className={`rounded-lg border p-4 ${passed ? 'border-emerald-500/25 bg-emerald-500/[0.08]' : 'border-amber-500/30 bg-amber-500/10'}`}>
          <div className={`text-xs font-bold uppercase tracking-wide ${passed ? 'text-emerald-300' : 'text-amber-300'}`}>
            {passed ? 'Growth remains compatible' : 'Growth class appears too slow'}
          </div>
          <div className="mt-2 text-3xl font-bold tabular-nums text-coden-text">{sizeSpan.toFixed(0)}×</div>
          <div className="mt-1 text-xs leading-relaxed text-coden-muted">input-size span across benchmark tiers.</div>
          <div className="mt-4 border-t border-coden-border/70 pt-3 text-xs leading-relaxed text-coden-text">
            Constant implementation overhead is tolerated; a ratio that rises with size indicates worse asymptotic growth.
          </div>
        </div>
      </div>
    </section>
  );
}


function CorrectnessBreakdown({
  results,
  officialCorrect,
  onOpenEditor,
}: {
  results: RunCaseResult[];
  officialCorrect: boolean;
  onOpenEditor: () => void;
}) {
  const visibleCases = results.filter((caseResult) => (
    caseResult.counts_toward_verdict && !caseResult.hidden
  ));
  const customCases = results.filter((caseResult) => !caseResult.counts_toward_verdict);
  const hiddenCases = results.filter((caseResult) => caseResult.hidden);
  const officialCases = results.filter((caseResult) => caseResult.counts_toward_verdict);
  const officialPassed = officialCases.filter((caseResult) => caseResult.correct).length;

  return (
    <section className="overflow-hidden rounded-xl border border-coden-border bg-coden-surface shadow-sm">
      <div className="flex flex-wrap items-start justify-between gap-3 border-b border-coden-border px-5 py-4">
        <div>
          <div className="flex flex-wrap items-center gap-2">
            <div className="text-sm font-bold text-coden-text">Case-by-case correctness</div>
            <span className={`rounded-full border px-2 py-0.5 text-[10px] font-bold ${officialCorrect ? 'border-emerald-500/25 bg-emerald-500/10 text-emerald-300' : 'border-rose-500/25 bg-rose-500/10 text-rose-300'}`}>
              {officialPassed}/{officialCases.length} official passed
            </span>
          </div>
          <p className="mt-1 text-xs leading-relaxed text-coden-muted">
            Visible, hidden, and benchmark cases decide acceptance. Benchmarks appear under Hidden; custom cases are feedback only.
          </p>
        </div>
        <button type="button" onClick={onOpenEditor} className="rounded-md border border-coden-border px-3 py-2 text-xs font-bold text-coden-text hover:bg-coden-inner">
          Open editor and cases
        </button>
      </div>
      <div className="space-y-4 p-5">
        <CaseResultGroup title="Visible cases" results={visibleCases} empty="No visible cases were executed." />
        <CaseResultGroup title="Custom cases" results={customCases} empty="No custom cases." informational />
        <CaseResultGroup title="Hidden cases" results={hiddenCases} empty="No hidden cases were executed." hidden />
      </div>
    </section>
  );
}


function CaseResultGroup({
  title,
  results,
  empty,
  informational = false,
  hidden = false,
}: {
  title: string;
  results: RunCaseResult[];
  empty: string;
  informational?: boolean;
  hidden?: boolean;
}) {
  const passed = results.filter((caseResult) => caseResult.correct).length;
  return (
    <div className="min-w-0 overflow-hidden rounded-lg border border-coden-border/80">
      <div className="flex items-center justify-between gap-2 border-b border-coden-border/70 bg-coden-inner/60 px-3 py-2.5">
        <div className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">{title}</div>
        <div className="flex items-center gap-1.5">
          {informational && <span className="rounded-full border border-coden-border px-1.5 py-0.5 text-[8px] font-bold uppercase text-coden-muted">Informational</span>}
          <span className="text-[10px] font-semibold tabular-nums text-coden-muted">{passed}/{results.length}</span>
        </div>
      </div>
      <div className="divide-y divide-coden-border/60">
        {results.map((caseResult, index) => (
          <CaseResultRow
            key={caseResult.id}
            result={caseResult}
            label={hidden ? `Hidden case ${index + 1}` : caseResult.name}
            hidden={hidden}
            informational={informational}
          />
        ))}
        {!results.length && (
          <div className="px-3 py-3 text-[11px] text-coden-muted">{empty}</div>
        )}
      </div>
    </div>
  );
}


function CaseResultRow({
  result,
  label,
  hidden,
  informational,
}: {
  result: RunCaseResult;
  label: string;
  hidden: boolean;
  informational: boolean;
}) {
  return (
    <div className={`px-3 py-3 ${result.correct ? 'bg-emerald-500/[0.035]' : 'bg-rose-500/[0.07]'}`}>
      <div className="flex items-center gap-2">
        <span className={`flex h-5 w-5 shrink-0 items-center justify-center rounded-full ${result.correct ? 'bg-emerald-500/15 text-emerald-300' : 'bg-rose-500/15 text-rose-300'}`}>
          <CaseStatusIcon passed={result.correct} />
        </span>
        <div className="min-w-0 flex-1 truncate text-xs font-semibold text-coden-text">{label}</div>
        <span className={`text-[9px] font-bold uppercase ${result.correct ? 'text-emerald-300' : 'text-rose-300'}`}>
          {result.correct ? 'Pass' : 'Fail'}
        </span>
      </div>
      {informational && !result.correct && (
        <div className="mt-2 text-[10px] text-coden-muted">This custom failure does not affect acceptance.</div>
      )}
      {!hidden && !result.correct && (
        <div className="mt-3 space-y-2">
          {result.message && <div className="text-[11px] leading-relaxed text-rose-200">{result.message}</div>}
          <div className="grid grid-cols-1 gap-2">
            <Evidence label="Input" value={result.input_repr || '(no input)'} />
            <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
              <Evidence label="Returned" value={result.return_value_repr || '(no value)'} />
              <Evidence label="Expected" value={result.expected_repr || '(validator-defined)'} />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}


function CaseStatusIcon({ passed }: { passed: boolean }) {
  return passed
    ? <svg viewBox="0 0 20 20" className="h-3 w-3" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"><path d="m4 10 4 4 8-9" /></svg>
    : <svg viewBox="0 0 20 20" className="h-3 w-3" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round"><path d="m5 5 10 10m0-10L5 15" /></svg>;
}


function BenchmarkUnavailable({ result, onOpenEditor }: { result: RunResponse; onOpenEditor: () => void }) {
  return (
    <section className="rounded-xl border border-coden-border bg-coden-surface p-5 shadow-sm">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="max-w-2xl">
          <div className="text-sm font-bold text-coden-text">Correct result; no comparable runtime target</div>
          <p className="mt-1 text-xs leading-relaxed text-coden-muted">
            {result.runtime_message || 'This run verified correctness, but no compatible reference benchmark was available. No speed verdict was inferred.'}
          </p>
        </div>
        <button type="button" onClick={onOpenEditor} className="rounded-md border border-coden-border px-3 py-2 text-xs font-bold text-coden-text hover:bg-coden-inner">Run another mode</button>
      </div>
      {result.runtime_user_ms != null && (
        <div className="mt-4 rounded-lg bg-coden-inner p-4">
          <div className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">Observed runtime</div>
          <div className="mt-1 text-2xl font-bold tabular-nums text-coden-text">{formatMs(result.runtime_user_ms)}</div>
          <div className="mt-1 text-xs text-coden-muted">Shown for context only; it is not an acceptance threshold.</div>
        </div>
      )}
    </section>
  );
}


function ContextCard({ label, value, note, tone }: { label: string; value: string; note: string; tone: AnalysisTone }) {
  const style = toneStyles(tone);
  return (
    <div className="rounded-lg border border-coden-border bg-coden-inner/60 p-4">
      <div className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">{label}</div>
      <div className={`mt-1 text-base font-bold ${tone === 'neutral' ? 'text-coden-text' : style.text}`}>{value}</div>
      <div className="mt-1 text-[11px] leading-relaxed text-coden-muted">{note}</div>
    </div>
  );
}


function BenchmarkDetails({ result, baselineLabel, workloadLabel }: { result: RunResponse; baselineLabel: string; workloadLabel: string }) {
  const usesScaling = (result.runtime_scaling_data?.length ?? 0) >= 2;
  return (
    <section className="rounded-lg border border-coden-border bg-coden-surface">
      <div className="border-b border-coden-border px-4 py-3 text-xs font-semibold text-coden-text">Benchmark details</div>
      <div className="px-4 py-4">
        <dl className="grid grid-cols-1 gap-x-8 gap-y-3 text-xs sm:grid-cols-2">
          <Detail label="Your runtime" value={formatMs(result.runtime_user_ms)} />
          <Detail label={baselineLabel} value={formatMs(result.runtime_reference_ms)} />
          <Detail label={usesScaling ? 'Largest-tier safety limit' : 'Allowed limit'} value={formatMs(result.runtime_limit_ms)} />
          <Detail label="Runtime ratio" value={result.runtime_ratio != null ? `${result.runtime_ratio.toFixed(2)}× baseline` : 'Not measured'} />
          <Detail label="Timing trials" value={result.runtime_check ? String(result.runtime_trials) : 'Not measured'} />
          <Detail label="Benchmark output" value={result.runtime_check ? result.benchmark_correct ? 'Verified' : 'Mismatch' : 'Not evaluated'} />
          <Detail label="Workload" value={result.runtime_check ? workloadLabel : 'No comparable benchmark'} />
          <Detail label="Evaluation mode" value={result.mode === 'real_test' ? 'Full suite' : 'Practice'} />
        </dl>
        {result.runtime_message && (
          <div className="mt-4 rounded-md border border-coden-border bg-coden-inner p-3 text-xs leading-relaxed text-coden-muted">{result.runtime_message}</div>
        )}
        <p className="mt-3 text-[11px] leading-relaxed text-coden-muted">
          {usesScaling
            ? 'The primary gate estimates how the user/reference ratio grows across authored input sizes. Constant-factor differences are tolerated; the largest tier also has a generous 8× safety cap. Each tier uses repeated paired measurements, alternating order, normalized amplification, and medians.'
            : 'This package still has one benchmark tier, so it uses the legacy 1.5× runtime target. Repeated paired measurements, alternating order, normalized amplification, and medians reduce timing noise.'}
        </p>
      </div>
    </section>
  );
}


function EmptyAnalysis({ tone, title, body, actionLabel, onAction }: { tone: AnalysisTone; title: string; body: string; actionLabel: string; onAction: () => void }) {
  const style = toneStyles(tone);
  return (
    <div className={`rounded-xl border p-8 text-center ${style.border} ${style.background}`}>
      <span className={`mx-auto flex h-12 w-12 items-center justify-center rounded-full ${style.iconBackground} ${style.text}`}><AnalysisIcon tone={tone} /></span>
      <div className="mt-4 text-base font-bold text-coden-text">{title}</div>
      <p className="mx-auto mt-2 max-w-xl text-sm leading-relaxed text-coden-muted">{body}</p>
      <button type="button" onClick={onAction} className="mt-5 rounded-md bg-coden-accent px-4 py-2.5 text-xs font-bold text-coden-accentContrast hover:brightness-110">{actionLabel}</button>
    </div>
  );
}


function PrimaryMetric({ label, value, tone }: { label: string; value: string; tone: AnalysisTone }) {
  const style = toneStyles(tone);
  return (
    <div className="rounded-lg border border-coden-border bg-coden-inner p-4">
      <div className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">{label}</div>
      <div className={`mt-1 text-2xl font-bold tabular-nums ${tone === 'neutral' ? 'text-coden-text' : style.text}`}>{value}</div>
    </div>
  );
}


function StatusPill({ label, good }: { label: string; good: boolean }) {
  return <span className={`rounded-full border px-2.5 py-1 text-[10px] font-semibold ${good ? 'border-emerald-500/25 bg-emerald-500/10 text-emerald-300' : 'border-rose-500/25 bg-rose-500/10 text-rose-300'}`}>{label}</span>;
}


function Legend({ color, label, shape }: { color: string; label: string; shape: 'bar' | 'line' }) {
  return (
    <span className="flex items-center gap-1.5">
      <span className={`${shape === 'bar' ? 'h-3 w-1.5 rounded-full' : 'h-3 w-px'} ${color}`} />
      {label}
    </span>
  );
}


function Evidence({ label, value }: { label: string; value: string }) {
  return <div className="rounded-md bg-coden-inner p-2"><div className="text-[9px] font-bold uppercase text-coden-muted">{label}</div><div className="mt-1 break-words font-mono text-[11px] text-coden-text">{value}</div></div>;
}


function Detail({ label, value }: { label: string; value: string }) {
  return <div className="flex items-start justify-between gap-4 border-b border-coden-border/50 pb-2"><dt className="text-coden-muted">{label}</dt><dd className="text-right font-semibold text-coden-text">{value}</dd></div>;
}


function AnalysisIcon({ tone }: { tone: AnalysisTone }) {
  if (tone === 'success') return <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m5 12 4 4L19 6" /></svg>;
  if (tone === 'warning') return <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3 2 21h20L12 3Z" /><path d="M12 9v5m0 3v.01" /></svg>;
  if (tone === 'danger') return <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="9" /><path d="m9 9 6 6m0-6-6 6" /></svg>;
  return <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="9" /><path d="M12 11v5m0-8v.01" /></svg>;
}


function officialCorrectnessNote(results: RunCaseResult[]): string {
  const official = results.filter((caseResult) => caseResult.counts_toward_verdict);
  const officialPassed = official.filter((caseResult) => caseResult.correct).length;
  const custom = results.filter((caseResult) => !caseResult.counts_toward_verdict);
  const customFailed = custom.filter((caseResult) => !caseResult.correct).length;
  const customNote = custom.length
    ? `; ${custom.length - customFailed}/${custom.length} custom passed (informational)`
    : '';
  return `${officialPassed}/${official.length} official cases passed${customNote}`;
}


function analysisState(result: RunResponse, customFailureCount: number): { tone: AnalysisTone; title: string; body: string } {
  const customNote = customFailureCount
    ? ` ${customFailureCount} custom case${customFailureCount === 1 ? '' : 's'} failed, but custom cases do not affect acceptance.`
    : '';
  if (!result.correct) {
    return { tone: 'danger', title: 'Fix correctness first', body: firstSentence(result.message) || 'At least one case produced the wrong output.' };
  }
  if (result.too_efficient) {
    return { tone: 'warning', title: 'Correct output, but the submission was rejected', body: firstSentence(result.too_efficient_reason || result.message) || 'Review the judge feedback before submitting again.' };
  }
  if (!result.runtime_check) {
    return { tone: 'neutral', title: 'Official cases passed — runtime target unavailable', body: `The official outputs are correct, but this run has no compatible benchmark for a fair speed comparison.${customNote}` };
  }
  if (result.runtime_passed === false) {
    return { tone: 'warning', title: 'Official cases passed, but runtime is over target', body: `${firstSentence(result.runtime_message || result.message) || 'The algorithm needs a faster implementation.'}${customNote}` };
  }
  return { tone: 'success', title: 'All official cases passed', body: `${firstSentence(result.runtime_message || result.message) || 'The solution meets both correctness and performance requirements.'}${customNote}` };
}


function toneStyles(tone: AnalysisTone) {
  if (tone === 'success') return { border: 'border-emerald-500/30', background: 'bg-emerald-500/[0.08]', iconBackground: 'bg-emerald-500/15', text: 'text-emerald-300' };
  if (tone === 'warning') return { border: 'border-amber-500/35', background: 'bg-amber-500/10', iconBackground: 'bg-amber-500/15', text: 'text-amber-300' };
  if (tone === 'danger') return { border: 'border-rose-500/30', background: 'bg-rose-500/[0.08]', iconBackground: 'bg-rose-500/15', text: 'text-rose-300' };
  return { border: 'border-coden-border', background: 'bg-coden-inner/50', iconBackground: 'bg-coden-border/70', text: 'text-coden-muted' };
}


function firstSentence(value: string): string {
  const trimmed = value.trim();
  const match = trimmed.match(/^.*?[.!?](?:\s|$)/);
  return (match?.[0] || trimmed).trim();
}


function formatMs(value: number | null | undefined): string {
  if (value === null || value === undefined) return 'Not measured';
  if (value < 0.01) return `${value.toFixed(3)} ms`;
  if (value < 10) return `${value.toFixed(2)} ms`;
  if (value < 100) return `${value.toFixed(1)} ms`;
  return `${Math.round(value).toLocaleString()} ms`;
}
