/**
 * ResultTab — the verdict + complexity band + return value,
 * rendered as a single card.
 *
 * Shows the run verdict and points the player back to the
 * in-app editor/debugger when they need breakpoints, locals,
 * and step controls.
 *
 * Layout:
 *   - Big status banner (emerald/amber/rose) with the
 *     pass/fail/error message + the actual complexity.
 *   - Compact two-card metric row: your ops vs reference.
 *   - Inline -10% / +5% tolerance band (the simpler one from
 *     ComplexityAnalysis, not the full scientific panel).
 *   - The ``return_value_repr`` in an expandable structured viewer.
 *   - Re-run button + a hint pointing to the in-app debugger.
 */

import ReactMarkdown from 'react-markdown';
import { useState } from 'react';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import 'katex/dist/katex.min.css';
import { useAppStore } from '../../../store/useAppStore';
import { analyzeChallenge } from '../../../api/run';
import { ApiError } from '../../../api/client';


export function ResultTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const result = useAppStore((s) => s.runResult);
  const error = useAppStore((s) => s.error);
  const run = useAppStore((s) => s.run);
  const reset = useAppStore((s) => s.reset);
  const isRunning = useAppStore((s) => s.isRunning);

  const aiStatus = useAppStore((s) => s.aiStatus);
  const aiAnalysis = useAppStore((s) => s.aiAnalysis);
  const aiError = useAppStore((s) => s.aiError);
  const setAiStatus = useAppStore((s) => s.setAiStatus);
  const setAiAnalysis = useAppStore((s) => s.setAiAnalysis);
  const setAiError = useAppStore((s) => s.setAiError);

  const handleAnalyze = async () => {
    if (!detail || !result) return;

    const apiKey = useAppStore.getState().progress?.gemini_api_key;
    if (!apiKey || !apiKey.trim()) {
      setAiStatus('error');
      setAiError('Please configure your Gemini API Key in the Profile settings first (click on your profile name/avatar at the top of the screen).');
      return;
    }

    setAiStatus('loading');
    setAiError('');
    try {
      const res = await analyzeChallenge({
        challengeId: detail.id,
        source: useAppStore.getState().source,
        n: result.n,
        seed: result.seed,
        returned: result.return_value_repr,
        expected: result.reference_return_value_repr || '',
        inputs: result.setup_data_repr || {},
      });
      setAiAnalysis(res.analysis);
      setAiStatus('loaded');
    } catch (e) {
      setAiStatus('error');
      if (e instanceof ApiError && e.detail && typeof e.detail === 'object' && 'detail' in e.detail) {
        setAiError(String((e.detail as any).detail));
      } else {
        setAiError(e instanceof Error ? e.message : String(e));
      }
    }
  };


  if (!detail) {
    return (
      <div className="flex items-center justify-center text-xs text-coden-muted p-4">
        Pick a challenge from the left rail.
      </div>
    );
  }

  // Error path
  if (error) {
    return (
      <div className="space-y-4 p-4">
        <div className="border border-rose-500/40 bg-rose-500/10 rounded p-4">
          <div className="text-rose-300 font-semibold text-sm mb-1">Run failed</div>
          <pre className="text-xs text-coden-text whitespace-pre-wrap font-mono">{error}</pre>
          <button
            type="button"
            onClick={() => void run()}
            disabled={isRunning}
            className="mt-3 px-3 py-1 text-xs rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50"
          >
            {isRunning ? 'Running…' : 'Try again'}
          </button>
        </div>
      </div>
    );
  }

  // No run yet
  if (!result) {
    return (
      <div className="space-y-4 p-4">
        <div className="bg-coden-surface rounded-lg p-6 shadow-md text-sm text-coden-muted">
          <div className="font-semibold text-coden-text mb-1">No run yet</div>
          <p>
            Click <span className="font-mono text-coden-text">▶ Run</span> in the
            transport bar (or press <span className="font-mono">R</span> /{' '}
            <span className="font-mono">F5</span>) to execute the solution from{' '}
            <span className="font-mono text-coden-text">solutions/{detail.id}.py</span>.
          </p>
          <p className="mt-2 text-xs">
            To debug the code, open the cOde(n) editor tab, set breakpoints in
            the gutter, and click <span className="font-mono text-coden-accent">Debug</span>.
          </p>
        </div>
      </div>
    );
  }

  // Determine the status color
  const variant: 'pass' | 'tooSlow' | 'tooEfficient' | 'fail' = result.passed
    ? 'pass'
    : result.too_efficient
      ? 'tooEfficient'
      : result.correct
        ? 'tooSlow'
        : 'fail';

  return (
    <div className="space-y-4 p-4">
      <VerdictCard result={result} variant={variant} />
      <ComplexityCard result={result} requiredComplexity={detail.required_complexity} />
      {!result.passed && (
        <AITutorCard
          status={aiStatus}
          analysis={aiAnalysis}
          error={aiError}
          onAnalyze={handleAnalyze}
        />
      )}
      {result.setup_data_repr && !result.passed && (
        <InputsCard inputs={result.setup_data_repr} />
      )}
      {result.return_value_repr && (
        <ReturnValueCard
          value={result.return_value_repr}
          expected={!result.correct ? result.reference_return_value_repr : undefined}
        />
      )}
      <ActionRow
        onRun={run}
        onReset={reset}
        isRunning={isRunning}
        variant={variant}
        message={result.message}
      />
    </div>
  );
}


function VerdictCard({
  result,
  variant,
}: {
  result: NonNullable<ReturnType<typeof useAppStore.getState>['runResult']>;
  variant: 'pass' | 'tooSlow' | 'tooEfficient' | 'fail';
}) {
  const styles = {
    pass: {
      border: 'border-emerald-500/40',
      bg: 'bg-emerald-500/10',
      icon: 'PASS',
      iconColor: 'text-emerald-300',
      title: result.message.split('\n')[0],
    },
    tooSlow: {
      border: 'border-amber-500/40',
      bg: 'bg-amber-500/10',
      icon: 'SLOW',
      iconColor: 'text-amber-300',
      title: result.message,
    },
    tooEfficient: {
      border: 'border-amber-500/40',
      bg: 'bg-amber-500/10',
      icon: 'REJ',
      iconColor: 'text-amber-300',
      title: result.message,
    },
    fail: {
      border: 'border-rose-500/40',
      bg: 'bg-rose-500/10',
      icon: 'FAIL',
      iconColor: 'text-rose-300',
      title: result.message,
    },
  }[variant];

  return (
    <div className={`${styles.bg} rounded-lg p-5 shadow-sm`}>
      <div className="flex items-baseline justify-between gap-3 mb-1">
        <span className={`font-bold text-base ${styles.iconColor}`}>
          {styles.icon}
        </span>
        <span className="text-xs font-mono text-coden-muted">
          {result.actual_complexity} (required {result.required_complexity})
        </span>
      </div>
      <div className="text-sm text-coden-text">{styles.title}</div>
    </div>
  );
}


function ComplexityCard({
  result,
  requiredComplexity,
}: {
  result: NonNullable<ReturnType<typeof useAppStore.getState>['runResult']>;
  requiredComplexity: string;
}) {
  const user = result.user_ast_ops;
  const ref = result.reference_ast_ops;
  const ciLow = result.reference_ci_low;
  const ciHigh = result.reference_ci_high;

  return (
    <div className="bg-coden-surface rounded-lg p-5 shadow-md mt-4">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2">
        Complexity
      </div>
      <div className="grid grid-cols-2 gap-3">
        <Metric label="Your code (AST)" value={user} />
        <Metric label="Reference (AST)" value={ref} accent="text-coden-accent" />
      </div>
      {ciHigh !== null && ref !== null && ref > 0 && (
        <div className="mt-3">
          <div className="text-xs uppercase text-coden-muted font-semibold mb-1">
            {ciLow !== null ? 'Tolerance band around the reference' : 'Upper bound vs reference'}
          </div>
          <div className="flex items-center gap-2 text-xs font-mono">
            <span className="text-rose-300">{ciLow !== null ? ciLow.toLocaleString() : '—'}</span>
            <div className="flex-1 h-2 rounded bg-coden-bg border border-coden-border relative overflow-hidden">
              {/* The band itself */}
              {user !== null && (
                <div
                  className="absolute top-0 bottom-0 bg-coden-accent/25 border-l border-r border-coden-accent/60"
                  style={{
                    left: `${ciLow !== null ? (ciLow / Math.max(ref * 1.5, user * 1.1)) * 100 : 0}%`,
                    width: `${((ciHigh - (ciLow ?? 0)) / Math.max(ref * 1.5, user * 1.1)) * 100}%`,
                  }}
                />
              )}
              {user !== null && (
                <div
                  className="absolute top-1/2 -translate-y-1/2 w-2 h-2 rounded-full border border-coden-bg"
                  style={{
                    left: `${(user / Math.max(ref * 1.5, user * 1.1)) * 100}%`,
                    backgroundColor:
                      ciLow !== null && user < ciLow ? '#f87171' : user > ciHigh ? '#fbbf24' : '#22c55e',
                  }}
                />
              )}
            </div>
            <span className="text-rose-300">{ciHigh.toLocaleString()}</span>
          </div>
          <div className="mt-1 text-xs text-coden-muted">
            Green dot = within the allowed bound.
            {ciLow !== null ? ' Red = too cheap (likely a cheat).' : ''} Amber = too slow.
            See the <span className="text-coden-accent">Complexity</span> tab
            for the full analysis.
          </div>
        </div>
      )}
      <div className="mt-2 text-xs text-coden-muted">
        Required: <span className="text-coden-text font-semibold">{requiredComplexity}</span>
        {result.actual_complexity && (
          <>
            {' '}· Achieved:{' '}
            <span className="text-coden-text font-semibold">{result.actual_complexity}</span>
          </>
        )}
      </div>
    </div>
  );
}


function Metric({
  label,
  value,
  accent = 'text-coden-text',
}: {
  label: string;
  value: number | null;
  accent?: string;
}) {
  return (
    <div className="rounded-lg p-4 bg-coden-inner shadow-inner">
      <div className="text-xs uppercase tracking-wider text-coden-muted font-semibold">
        {label}
      </div>
      <div className={`text-2xl font-bold tabular-nums mt-0.5 ${accent}`}>
        {value !== null ? value.toLocaleString() : '—'}
      </div>
      <div className="text-xs text-coden-muted">AST ops</div>
    </div>
  );
}


function ReturnValueCard({ value, expected }: { value: string; expected?: string | null }) {
  return (
    <div className="bg-coden-surface rounded-lg p-5 shadow-md mt-4">
      {expected ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <div className="text-xs uppercase text-rose-300 font-semibold mb-2 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
              Returned (Your Solution)
            </div>
            <StructuredValueViewer value={value} borderClass="border-rose-500/20" />
            <div className="mt-1 text-[10px] text-coden-muted">
              What your code's <code className="font-mono text-rose-300">solve()</code> function returned.
            </div>
          </div>
          <div>
            <div className="text-xs uppercase text-emerald-300 font-semibold mb-2 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              Expected (Reference Solution)
            </div>
            <StructuredValueViewer value={expected} borderClass="border-emerald-500/20" />
            <div className="mt-1 text-[10px] text-coden-muted">
              What the canonical reference solution returned.
            </div>
          </div>
        </div>
      ) : (
        <>
          <div className="text-xs uppercase text-coden-muted font-semibold mb-2">
            Returned
          </div>
          <StructuredValueViewer value={value} />
          <div className="mt-1 text-xs text-coden-muted">
            What <span className="font-mono text-coden-text">solve()</span> returned.
          </div>
        </>
      )}
      <div className="mt-3 text-[10px] text-coden-muted border-t border-coden-border/50 pt-2">
        Return values are capped server-side; long lists are truncated with a trailing ellipsis.
      </div>
    </div>
  );
}


function StructuredValueViewer({
  value,
  borderClass = 'border-coden-border/30',
}: {
  value: string;
  borderClass?: string;
}) {
  const [expanded, setExpanded] = useState(false);
  const items = splitTopLevelItems(value);
  const hasItems = items.length > 0;
  return (
    <div className={`bg-coden-inner rounded-lg text-[11px] font-mono shadow-inner border ${borderClass} max-h-64 overflow-y-auto`}>
      <button
        type="button"
        onClick={() => hasItems && setExpanded((v) => !v)}
        className="w-full flex items-start gap-2 p-3 text-left hover:bg-coden-border/30"
      >
        <span className="w-3 text-coden-muted pt-0.5">{hasItems ? (expanded ? '▾' : '▸') : ''}</span>
        <span className="break-words text-coden-text">{compactValue(value)}</span>
      </button>
      {expanded && (
        <div className="border-t border-coden-border/50 px-3 py-2">
          {items.map((item, index) => (
            <div key={`${index}-${item}`} className="grid grid-cols-[48px_minmax(0,1fr)] gap-3 py-1">
              <span className="text-coden-muted text-right select-none">{index}</span>
              <span className="text-coden-text break-words">{item}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}


function compactValue(value: string): string {
  const trimmed = value.trim();
  if (trimmed.length <= 220) return trimmed;
  return `${trimmed.slice(0, 217)}...`;
}


function splitTopLevelItems(value: string): string[] {
  const trimmed = value.trim();
  const open = trimmed[0];
  const close = open === '[' ? ']' : open === '(' ? ')' : open === '{' ? '}' : '';
  if (!close || trimmed[trimmed.length - 1] !== close) return [];
  const inner = trimmed.slice(1, -1).trim();
  if (!inner) return [];
  const items: string[] = [];
  let depth = 0;
  let quote = '';
  let current = '';
  for (let i = 0; i < inner.length; i += 1) {
    const ch = inner[i]!;
    const prev = inner[i - 1];
    if (quote) {
      current += ch;
      if (ch === quote && prev !== '\\') quote = '';
      continue;
    }
    if (ch === '"' || ch === "'") {
      quote = ch;
      current += ch;
      continue;
    }
    if (ch === '[' || ch === '(' || ch === '{') depth += 1;
    if (ch === ']' || ch === ')' || ch === '}') depth -= 1;
    if (ch === ',' && depth === 0) {
      if (current.trim()) items.push(current.trim());
      current = '';
      continue;
    }
    current += ch;
  }
  if (current.trim()) items.push(current.trim());
  return items.length > 1 ? items : [];
}


function ActionRow({
  onRun,
  onReset,
  isRunning,
  variant,
  message,
}: {
  onRun: () => void | Promise<void>;
  onReset: () => void;
  isRunning: boolean;
  variant: 'pass' | 'tooSlow' | 'tooEfficient' | 'fail';
  message: string;
}) {
  return (
    <div className="bg-coden-surface rounded-lg p-5 shadow-md text-xs space-y-3 mt-4">
      <div className="text-coden-muted">
        To debug, open the cOde(n) editor tab and click{' '}
        <span className="font-mono text-coden-accent">Debug</span> — breakpoints in{' '}
        <span className="font-mono text-coden-text">solutions/&lt;id&gt;.py</span>{' '}
        will hit normally. The verdict above is what cOde(n) computed for
        the latest run.
      </div>
      {variant === 'fail' && (
        <div className="text-rose-300/80">
          <span className="font-semibold">Hint:</span> {message}
        </div>
      )}
      <div className="flex gap-2 pt-1">
        <button
          type="button"
          onClick={() => void onRun()}
          disabled={isRunning}
          className="px-3 py-1 text-xs rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isRunning ? 'Running…' : '▶ Run again'}
        </button>
        <button
          type="button"
          onClick={onReset}
          className="px-3 py-1 text-xs rounded border border-coden-border text-coden-text hover:bg-coden-border"
        >
          Reset
        </button>
      </div>
    </div>
  );
}


function InputsCard({ inputs }: { inputs: Record<string, string> }) {
  return (
    <div className="bg-coden-surface rounded-lg p-5 shadow-md mt-4">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2">
        Input Variables
      </div>
      <div className="space-y-3">
        {Object.entries(inputs).map(([name, val]) => (
          <div key={name} className="space-y-1">
            <div className="text-xs font-mono text-coden-accent">{name}</div>
            <pre className="bg-coden-inner rounded-lg p-3 text-[11px] font-mono overflow-x-auto whitespace-pre-wrap break-words max-h-40 overflow-y-auto shadow-inner border border-coden-border/30">
{val}
            </pre>
          </div>
        ))}
      </div>
    </div>
  );
}


interface AITutorCardProps {
  status: 'idle' | 'loading' | 'loaded' | 'error';
  analysis: string;
  error: string;
  onAnalyze: () => void;
}

function AITutorCard({ status, analysis, error, onAnalyze }: AITutorCardProps) {
  if (status === 'idle') {
    return (
      <div className="bg-gradient-to-r from-indigo-950/40 to-purple-950/40 border border-indigo-500/30 rounded-xl p-5 shadow-lg flex flex-col sm:flex-row items-center justify-between gap-4 mt-4">
        <div className="space-y-1 text-center sm:text-left">
          <div className="text-sm font-bold text-white flex items-center justify-center sm:justify-start gap-1.5">
            <span>🤖</span> Gemini AI Tutor
          </div>
          <p className="text-xs text-indigo-200/80 leading-relaxed">
            Stuck? Let Gemini analyze your code, logic, and output mismatch to pinpoint the exact bug.
          </p>
        </div>
        <button
          type="button"
          onClick={onAnalyze}
          className="px-4 py-2 text-xs font-bold rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white shadow-md hover:shadow-indigo-500/20 active:scale-95 transition-all shrink-0"
        >
          Analyze Solution
        </button>
      </div>
    );
  }

  if (status === 'loading') {
    return (
      <div className="bg-coden-surface border border-indigo-500/30 rounded-xl p-6 shadow-md mt-4 flex flex-col items-center justify-center gap-3 text-xs text-indigo-300">
        <div className="w-5 h-5 rounded-full border-2 border-indigo-500 border-t-transparent animate-spin"></div>
        <span>Gemini is analyzing your execution bug...</span>
      </div>
    );
  }

  if (status === 'error') {
    return (
      <div className="bg-coden-surface border border-rose-500/30 rounded-xl p-5 shadow-md mt-4 space-y-3">
        <div className="text-xs font-bold text-rose-300 flex items-center gap-1.5">
          <span>⚠️</span> AI Analysis Failed
        </div>
        <p className="text-xs text-coden-text whitespace-pre-wrap font-mono leading-relaxed bg-rose-950/20 border border-rose-900/30 rounded-lg p-3">
          {error}
        </p>
        <button
          type="button"
          onClick={onAnalyze}
          className="px-3 py-1.5 text-xs rounded bg-indigo-600 hover:bg-indigo-500 text-white font-semibold transition-all"
        >
          Try Again
        </button>
      </div>
    );
  }

  return (
    <div className="bg-coden-surface border border-indigo-500/30 rounded-xl p-5 shadow-md mt-4 space-y-3">
      <div className="text-xs font-bold text-indigo-300 flex items-center gap-1.5 border-b border-coden-border/60 pb-2">
        <span>🤖</span> Gemini AI Debug Analysis
      </div>
      <article className="prose prose-invert prose-xs max-w-none
                          prose-headings:text-indigo-200 prose-headings:font-bold prose-headings:my-2
                          prose-p:text-coden-text prose-p:leading-relaxed prose-p:my-1.5
                          prose-strong:text-indigo-300
                          prose-code:text-indigo-300 prose-code:before:content-none prose-code:after:content-none
                          prose-ul:list-disc prose-ul:pl-4 prose-ul:my-2
                          prose-li:my-0.5">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeRaw, rehypeKatex]}
          components={{
            pre: ({ children, ...props }) => (
              <pre
                {...props}
                className="bg-coden-bg border border-coden-border rounded p-3 text-xs overflow-x-auto my-3 font-mono"
              >
                {children}
              </pre>
            ),
            code: ({ className, children, ...props }) => {
              const isBlock = String(children).includes('\n');
              if (isBlock) {
                return <code {...props} className={className}>{children}</code>;
              }
              return (
                <code
                  {...props}
                  className="bg-coden-bg border border-coden-border rounded px-1 py-0.5 text-indigo-300 text-xs font-mono"
                >
                  {children}
                </code>
              );
            },
          }}
        >
          {analysis}
        </ReactMarkdown>
      </article>
    </div>
  );
}
