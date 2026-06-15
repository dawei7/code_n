/**
 * AiReportTab — renders the structured AI report for the
 * most recent run, plus a "Get hint" button that calls
 * local Ollama.
 *
 * Visible only when `aiMode` is on (the tab registry hides it
 * otherwise). Shows:
 *   - Challenge meta
 *   - Test setup (n, seed)
 *   - Result (pass/fail, op counts, complexity, too-efficient)
 *   - Locals at failure (when present)
 *   - The "💡 Get hint" button → POSTs to /api/ai/hint and
 *     displays the result in a popover
 */
import { useEffect, useState, useCallback } from 'react';

import { useAppStore } from '../../../store/useAppStore';
import { apiPost } from '../../../api/client';
import { AiReport, RunResponse } from '../../../types/api';


type HintState =
  | { kind: 'idle' }
  | { kind: 'loading' }
  | { kind: 'loaded'; hint: string; model: string; fallback: boolean; latency_ms: number }
  | { kind: 'error'; message: string };


export function AiReportTab() {
  const runResult = useAppStore((s) => s.runResult);
  const aiReport = (runResult as (RunResponse & { ai_report?: AiReport }) | null)?.ai_report ?? null;
  const [hintState, setHintState] = useState<HintState>({ kind: 'idle' });

  // Clear the hint when a new run lands — the report is fresh,
  // the old hint is stale.
  useEffect(() => {
    setHintState({ kind: 'idle' });
  }, [runResult]);

  const requestHint = useCallback(async () => {
    if (!aiReport) return;
    setHintState({ kind: 'loading' });
    try {
      const res = await apiPost<{
        hint: string;
        model: string;
        latency_ms: number;
        fallback: boolean;
      }>('/ai/hint', { report: aiReport });
      setHintState({
        kind: 'loaded',
        hint: res.hint,
        model: res.model,
        fallback: res.fallback,
        latency_ms: res.latency_ms,
      });
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      setHintState({ kind: 'error', message });
    }
  }, [aiReport]);

  if (!runResult || !aiReport) {
    return (
      <div className="h-full flex items-center justify-center text-xs text-coden-muted">
        Run a challenge to see the AI report.
      </div>
    );
  }

  return (
    <div className="h-full overflow-y-auto p-4 space-y-4">
      <header className="border-b border-coden-border pb-2">
        <h2 className="text-base font-semibold text-coden-text">
          AI Report · {aiReport.challenge_name}
        </h2>
        <div className="text-[10px] text-coden-muted font-mono mt-1">
          {aiReport.challenge_id} · {aiReport.category} · required {aiReport.required_complexity}
        </div>
      </header>

      <ResultBlock result={aiReport.result} />
      <TestBlock test={aiReport.test} />
      <SourceBlock source={aiReport.user_source} />
      {aiReport.locals_at_failure && <LocalsBlock locals={aiReport.locals_at_failure} />}
      {aiReport.algorithm_hint && (
        <div className="border border-coden-border rounded p-3 bg-coden-surface">
          <h3 className="text-xs uppercase text-coden-muted font-semibold mb-1">
            Algorithm hint
          </h3>
          <div className="text-sm text-coden-text">{aiReport.algorithm_hint}</div>
        </div>
      )}

      <HintBlock state={hintState} onRequest={requestHint} />
    </div>
  );
}


function ResultBlock({ result }: { result: AiReport['result'] }) {
  const passLabel = result.passed
    ? '✅ Passed'
    : result.too_efficient
    ? '⚠️ Too efficient'
    : result.correct
    ? '🐢 Too slow'
    : '❌ Incorrect';
  return (
    <div className="border border-coden-border rounded p-3 bg-coden-surface">
      <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">Result</h3>
      <div className="text-sm font-semibold text-coden-text mb-2">{passLabel}</div>
      <table className="text-xs w-full">
        <tbody>
          <Row label="Actual complexity" value={result.actual_complexity} />
          <Row label="Op count" value={String(result.ops_total)} />
          <Row
            label="Within threshold"
            value={result.within_threshold ? 'yes' : 'no'}
          />
          <Row
            label="Too efficient"
            value={result.too_efficient ? `yes — ${result.too_efficient_reason}` : 'no'}
          />
        </tbody>
      </table>
      {result.message && (
        <div className="mt-2 text-xs text-coden-muted whitespace-pre-wrap">
          {result.message}
        </div>
      )}
    </div>
  );
}


function TestBlock({ test }: { test: AiReport['test'] }) {
  return (
    <div className="border border-coden-border rounded p-3 bg-coden-surface">
      <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">Test setup</h3>
      <div className="text-xs text-coden-text font-mono">
        n = <span className="text-coden-accent">{test.n}</span>
        {test.seed !== null && (
          <>
            {' · '}
            seed = <span className="text-coden-accent">{test.seed}</span>
          </>
        )}
      </div>
    </div>
  );
}


function SourceBlock({ source }: { source: string }) {
  return (
    <div className="border border-coden-border rounded p-3 bg-coden-surface">
      <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">
        Your code
      </h3>
      <pre className="bg-coden-bg border border-coden-border rounded p-2 text-[11px] font-mono overflow-x-auto whitespace-pre">
{source}
      </pre>
    </div>
  );
}


function LocalsBlock({ locals }: { locals: NonNullable<AiReport['locals_at_failure']> }) {
  return (
    <div className="border border-coden-border rounded p-3 bg-coden-surface">
      <h3 className="text-xs uppercase text-coden-muted font-semibold mb-2">
        Locals at line {locals.line_no} ({locals.event})
      </h3>
      {locals.return_value && (
        <div className="text-xs text-coden-muted mb-1">
          return: <span className="font-mono text-coden-text">{locals.return_value}</span>
        </div>
      )}
      <pre className="bg-coden-bg border border-coden-border rounded p-2 text-[11px] font-mono overflow-x-auto whitespace-pre">
{JSON.stringify(locals.locals, null, 2)}
      </pre>
    </div>
  );
}


function HintBlock({
  state,
  onRequest,
}: {
  state: HintState;
  onRequest: () => void;
}) {
  return (
    <div className="border border-coden-border rounded p-3 bg-coden-surface">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-xs uppercase text-coden-muted font-semibold">
          AI hint (local Ollama)
        </h3>
        <button
          type="button"
          onClick={onRequest}
          disabled={state.kind === 'loading'}
          className="px-2 py-1 text-xs rounded border border-coden-accent text-coden-accent hover:bg-coden-accent hover:text-coden-bg disabled:opacity-50"
        >
          {state.kind === 'loading' ? 'Asking…' : '💡 Get hint'}
        </button>
      </div>
      {state.kind === 'idle' && (
        <div className="text-xs text-coden-muted">
          Click "Get hint" to ask the local model (qwen2.5-coder:7b) for a
          short hint about this run.
        </div>
      )}
      {state.kind === 'loading' && (
        <div className="text-xs text-coden-muted">Waiting for Ollama…</div>
      )}
      {state.kind === 'error' && (
        <div className="text-xs text-red-400 whitespace-pre-wrap">{state.message}</div>
      )}
      {state.kind === 'loaded' && (
        <>
          <div className="text-xs text-coden-muted mb-2">
            {state.fallback
              ? `Server-generated hint (Ollama unavailable)`
              : `Model: ${state.model} · ${state.latency_ms} ms`}
          </div>
          <div className="text-sm text-coden-text whitespace-pre-wrap">
            {state.hint}
          </div>
        </>
      )}
    </div>
  );
}


function Row({ label, value }: { label: string; value: string }) {
  return (
    <tr>
      <td className="text-coden-muted pr-2 align-top py-0.5">{label}</td>
      <td className="text-coden-text font-mono align-top py-0.5">{value}</td>
    </tr>
  );
}
