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
 *   - Inline dataset-aware reference band / upper bound (the
 *     simpler one from ComplexityAnalysis, not the full
 *     scientific panel).
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
import type { RunCaseResult, SupportedLanguage, TestCaseSummary, TutorChatMessage } from '../../../types/api';
import { formatCaseValue } from '../../../lib/formatCaseValue';


export interface TutorChatSession {
  id: string;
  challengeId: string;
  challengeName: string;
  language: SupportedLanguage;
  createdAt: string;
  updatedAt: string;
  messages: TutorChatMessage[];
}


function solutionPath(
  frontendId: string,
  slug: string,
  language: SupportedLanguage,
  version: number,
): string {
  const extensionByLanguage: Record<SupportedLanguage, string> = {
    python: 'py',
    cpp: 'cpp',
    java: 'java',
    csharp: 'cs',
    javascript: 'js',
    go: 'go',
    kotlin: 'kt',
    sql: 'sql',
    bash: 'sh',
  };
  const extension = extensionByLanguage[language];
  return `user data/dsa/leetcode/${frontendId}_${slug}/user_solutions/${language}_v${version}.${extension}`;
}


function sessionLabel(session: TutorChatSession): string {
  const firstQuestion = session.messages.find((message) => message.role === 'user')?.content.trim();
  if (firstQuestion) return compactText(firstQuestion, 44);
  return `Analysis ${formatSessionDate(session.createdAt)}`;
}


function compactText(value: string, maxLength: number): string {
  const normalized = value.replace(/\s+/g, ' ').trim();
  return normalized.length <= maxLength ? normalized : `${normalized.slice(0, maxLength - 3)}...`;
}


function formatSessionDate(value: string): string {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return 'saved chat';
  return date.toLocaleString([], {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
}


export function ResultTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const result = useAppStore((s) => s.runResult);
  const error = useAppStore((s) => s.error);
  const run = useAppStore((s) => s.run);
  const reset = useAppStore((s) => s.reset);
  const isRunning = useAppStore((s) => s.isRunning);
  const codeLanguage = useAppStore((s) => s.codeLanguage);
  const activeVersion = useAppStore((s) => s.activeVersion);
  const selectedCaseIds = useAppStore((s) => s.selectedCaseIds);
  const setSelectedCaseIds = useAppStore((s) => s.setSelectedCaseIds);
  const runAllTrialCases = useAppStore((s) => s.runAllTrialCases);
  const customCaseInput = useAppStore((s) => s.customCaseInput);
  const setCustomCaseInput = useAppStore((s) => s.setCustomCaseInput);


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
            className="mt-3 px-3 py-1 text-xs rounded bg-coden-accent text-coden-accentContrast hover:opacity-90 disabled:opacity-50"
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
        <PracticeCasesCard
          detail={detail}
          result={null}
          selectedCaseIds={selectedCaseIds}
          onSelectCase={(id) => setSelectedCaseIds([id])}
          onRunSelected={run}
          onRunAll={runAllTrialCases}
          isRunning={isRunning}
          customCaseInput={customCaseInput}
          onCustomInputChange={setCustomCaseInput}
        />
        <div className="bg-coden-surface rounded-lg p-6 shadow-md text-sm text-coden-muted">
          <div className="font-semibold text-coden-text mb-1">No run yet</div>
          <p>
            Click <span className="font-mono text-coden-text">▶ Run</span> in the
            transport bar (or press <span className="font-mono">R</span> /{' '}
            <span className="font-mono">F5</span>) to execute the solution from{' '}
            <span className="font-mono text-coden-text">
              {solutionPath(detail.leetcode_frontend_id, detail.leetcode_slug, codeLanguage, activeVersion)}
            </span>.
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
      <PracticeCasesCard
        detail={detail}
        result={result}
        selectedCaseIds={selectedCaseIds}
        onSelectCase={(id) => setSelectedCaseIds([id])}
        onRunSelected={run}
        onRunAll={runAllTrialCases}
        isRunning={isRunning}
        customCaseInput={customCaseInput}
        onCustomInputChange={setCustomCaseInput}
      />
      <VerdictCard result={result} variant={variant} />
      {result.case_results?.length > 0 && (
        <CaseResultsCard results={result.case_results} />
      )}
      <ComplexityCard
        result={result}
        requiredComplexity={detail.required_complexity}
      />
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
          {result.complexity_check
            ? `target ${result.required_complexity} | ${formatCertificateMethod(result.complexity_method)}`
            : `target ${result.required_complexity} | runtime benchmark`}
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
  if (result.complexity_check) {
    return (
      <div className="mt-4 rounded-lg border border-emerald-500/30 bg-emerald-500/[0.08] p-5 shadow-md">
        <div className="text-xs font-semibold uppercase text-emerald-300">Complexity certificate</div>
        <div className="mt-2 text-sm font-bold text-coden-text">{formatCertificateMethod(result.complexity_method)}</div>
        <div className="mt-1 text-xs leading-relaxed text-coden-muted">
          {result.complexity_message || 'Complexity is verified by machine-validated package evidence; runtime scaling is not applicable.'}
        </div>
        <div className="mt-3 text-xs text-coden-muted">
          Required: <span className="font-semibold text-coden-text">{requiredComplexity}</span> · Runtime tiers: <span className="font-semibold text-coden-text">not applicable</span>
        </div>
      </div>
    );
  }
  const userMs = result.runtime_user_ms ?? null;
  const refMs = result.runtime_reference_ms ?? null;
  const limitMs = result.runtime_limit_ms ?? null;
  const runtimeOk = result.runtime_passed;

  return (
    <div className="bg-coden-surface rounded-lg p-5 shadow-md mt-4">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2">
        Runtime check
      </div>
      <div className="grid grid-cols-2 gap-3">
        <Metric label="Your code" value={formatMs(userMs)} />
        <Metric label="Optimal reference" value={formatMs(refMs)} accent="text-coden-accent" />
      </div>
      {limitMs !== null && (
        <div className="mt-3">
          <div className="text-xs uppercase text-coden-muted font-semibold mb-1">
            Reference +50% limit
          </div>
          <div className="flex items-center gap-2 text-xs font-mono">
            <span className="text-coden-muted">0 ms</span>
            <div className="flex-1 h-2 rounded bg-coden-bg border border-coden-border relative overflow-hidden">
              <div className="absolute top-0 bottom-0 left-0 right-0 bg-coden-accent/25 border-r border-coden-accent/60" />
              {userMs !== null && (
                <div
                  className="absolute top-1/2 -translate-y-1/2 w-2 h-2 rounded-full border border-coden-bg"
                  style={{
                    left: `${Math.min(100, (userMs / limitMs) * 100)}%`,
                    backgroundColor: runtimeOk === false ? '#fbbf24' : '#22c55e',
                  }}
                />
              )}
            </div>
            <span className="text-coden-accent">{formatMs(limitMs)}</span>
          </div>
          <div className="mt-1 text-xs text-coden-muted">
            Green dot = within reference +50%. Amber = too slow.
            See the <span className="text-coden-accent">Complexity</span> tab
            for the full analysis.
          </div>
        </div>
      )}
      <div className="mt-2 text-xs text-coden-muted">
        Required: <span className="text-coden-text font-semibold">{requiredComplexity}</span>
        {result.runtime_check && (
          <>
            {' '}· Benchmark:{' '}
            <span className="text-coden-text font-semibold">
              {result.case_results?.length || result.selected_case_ids.length || 1} case{(result.case_results?.length || result.selected_case_ids.length || 1) === 1 ? '' : 's'}, trials={result.runtime_trials}
            </span>
          </>
        )}
        {result.runtime_message && (
          <div className="mt-1 text-coden-text">{result.runtime_message}</div>
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
  value: string;
  accent?: string;
}) {
  return (
    <div className="rounded-lg p-4 bg-coden-inner shadow-inner">
      <div className="text-xs uppercase tracking-wider text-coden-muted font-semibold">
        {label}
      </div>
      <div className={`text-2xl font-bold tabular-nums mt-0.5 ${accent}`}>
        {value}
      </div>
      <div className="text-xs text-coden-muted">Median runtime</div>
    </div>
  );
}


function PracticeCasesCard({
  detail,
  result,
  selectedCaseIds,
  onSelectCase,
  onRunSelected,
  onRunAll,
  isRunning,
  customCaseInput,
  onCustomInputChange,
}: {
  detail: NonNullable<ReturnType<typeof useAppStore.getState>['currentDetail']>;
  result: ReturnType<typeof useAppStore.getState>['runResult'];
  selectedCaseIds: string[];
  onSelectCase: (id: string) => void;
  onRunSelected: () => Promise<void>;
  onRunAll: () => void;
  isRunning: boolean;
  customCaseInput: string;
  onCustomInputChange: (value: string) => void;
}) {
  const [activePanel, setActivePanel] = useState<'cases' | 'output' | 'feedback' | 'submissions'>('cases');
  const selectedId = selectedCaseIds[0] ?? '';
  const visibleCases = detail.test_cases;
  const selectedCase =
    visibleCases.find((testCase) => testCase.id === selectedId) ??
    visibleCases[0] ??
    null;
  const hasCustomInput = customCaseInput.trim().length > 0;
  const canRunSelected = !isRunning && (detail.test_cases.length > 0 || hasCustomInput);
  const resultById = new Map((result?.case_results ?? []).map((caseResult) => [caseResult.id, caseResult]));
  const selectedResult = selectedCase ? resultById.get(selectedCase.id) : undefined;
  const ranAllTrial = result?.selected_case_ids?.includes('__all_trial__') || (result?.case_results?.length ?? 0) > 1;

  return (
    <div className="overflow-hidden rounded-lg border border-coden-border bg-coden-surface shadow-md">
      <div className="flex flex-wrap items-center justify-between gap-2 border-b border-coden-border bg-coden-bg/70 px-4 py-2">
        <div className="flex min-w-0 items-center gap-1">
          <PanelTab label="Test Cases" active={activePanel === 'cases'} onClick={() => setActivePanel('cases')} />
          <PanelTab label="Output" active={activePanel === 'output'} onClick={() => setActivePanel('output')} />
          <PanelTab label="Feedback" active={activePanel === 'feedback'} onClick={() => setActivePanel('feedback')} />
          <PanelTab label="Submissions" active={activePanel === 'submissions'} onClick={() => setActivePanel('submissions')} />
        </div>
        <div className="flex shrink-0 items-center gap-2">
          <button
            type="button"
            onClick={() => void onRunSelected()}
            disabled={!canRunSelected}
            className="h-8 rounded bg-coden-accent px-3 text-xs font-semibold text-coden-accentContrast hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {isRunning ? 'Running...' : 'Run'}
          </button>
          <button
            type="button"
            onClick={() => {
              onRunAll();
              void onRunSelected();
            }}
            disabled={isRunning || detail.test_cases.length === 0}
            className="h-8 rounded border border-coden-border px-3 text-xs text-coden-text hover:bg-coden-border disabled:cursor-not-allowed disabled:opacity-50"
          >
            Run all
          </button>
        </div>
      </div>

      <div className="px-4 py-4">
        {activePanel === 'cases' && (
          <div className="space-y-4">
            {detail.test_cases.length === 0 ? (
              <div className="rounded border border-amber-500/30 bg-amber-500/10 p-3 text-xs text-amber-100">
                No validated practice cases exist for this challenge yet.
              </div>
            ) : (
              <>
                <CasePillStrip
                  cases={visibleCases}
                  resultById={resultById}
                  selectedId={selectedCase?.id ?? ''}
                  onSelectCase={onSelectCase}
                />
                {selectedCase && (
                  <CasePreview
                    testCase={selectedCase}
                    caseNumber={visibleCases.findIndex((item) => item.id === selectedCase.id) + 1}
                    result={selectedResult}
                  />
                )}
              </>
            )}
            <CustomInputEditor
              value={customCaseInput}
              onChange={onCustomInputChange}
              active={hasCustomInput}
            />
          </div>
        )}

        {activePanel === 'output' && (
          <OutputPanel
            result={result}
            selectedCase={selectedCase}
            selectedResult={selectedResult}
            ranAllTrial={ranAllTrial}
          />
        )}

        {activePanel === 'feedback' && (
          <FeedbackPanel result={result} />
        )}

        {activePanel === 'submissions' && (
          <SubmissionsPanel result={result} detailName={detail.name} />
        )}
      </div>
    </div>
  );
}


function PanelTab({
  label,
  active,
  onClick,
}: {
  label: string;
  active: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={[
        'h-9 rounded-t px-3 text-sm font-semibold transition-colors',
        active
          ? 'border-b-2 border-coden-accent text-coden-text'
          : 'text-coden-muted hover:text-coden-text',
      ].join(' ')}
    >
      {label}
    </button>
  );
}


function CasePillStrip({
  cases,
  resultById,
  selectedId,
  onSelectCase,
}: {
  cases: TestCaseSummary[];
  resultById: Map<string, RunCaseResult>;
  selectedId: string;
  onSelectCase: (id: string) => void;
}) {
  return (
    <div className="flex gap-1.5 overflow-x-auto pb-1">
      {cases.map((testCase, index) => {
        const caseResult = resultById.get(testCase.id);
        const active = selectedId === testCase.id;
        const stateClass = caseResult
          ? caseResult.correct
            ? 'border-emerald-500/50 bg-emerald-500/10 text-emerald-100'
            : 'border-rose-500/50 bg-rose-500/10 text-rose-100'
          : active
            ? 'border-coden-accent bg-coden-accent/15 text-coden-text'
            : 'border-transparent bg-coden-inner text-coden-muted hover:text-coden-text';
        return (
          <button
            key={testCase.id}
            type="button"
            onClick={() => onSelectCase(testCase.id)}
            className={[
              'flex h-9 min-w-[76px] items-center justify-center rounded-md border px-3 text-sm font-semibold transition-colors',
              active ? 'ring-1 ring-coden-accent/70' : '',
              stateClass,
            ].join(' ')}
            title={testCase.name}
          >
            Case {index + 1}
          </button>
        );
      })}
    </div>
  );
}


function CasePreview({
  testCase,
  caseNumber,
  result,
}: {
  testCase: TestCaseSummary;
  caseNumber: number;
  result?: RunCaseResult;
}) {
  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <div className="min-w-0">
          <div className="text-sm font-semibold text-coden-text">
            Case {caseNumber}
          </div>
          <div className="truncate text-xs text-coden-muted">{testCase.name}</div>
        </div>
        <div className="flex items-center gap-2">
          <span className="rounded border border-coden-border px-2 py-1 text-[10px] font-mono uppercase text-coden-muted">
            {testCase.kind}
          </span>
          {result && (
            <span
              className={[
                'rounded px-2 py-1 text-[10px] font-bold uppercase',
                result.correct ? 'bg-emerald-500/15 text-emerald-200' : 'bg-rose-500/15 text-rose-200',
              ].join(' ')}
            >
              {result.correct ? 'Passed' : 'Failed'}
            </span>
          )}
        </div>
      </div>
      <div className="grid grid-cols-1 gap-3 lg:grid-cols-2">
        <ValuePane title="Input" value={testCase.input_repr} />
        <ValuePane title="Expected" value={testCase.expected_repr || '(no expected value)'} tone="expected" />
      </div>
      {result && !result.correct && (
        <ValuePane title="Your output" value={result.return_value_repr || '(no output)'} tone="actual" />
      )}
    </div>
  );
}


function ValuePane({
  title,
  value,
  tone = 'neutral',
}: {
  title: string;
  value: string;
  tone?: 'neutral' | 'expected' | 'actual';
}) {
  const toneClass = {
    neutral: 'border-coden-border/40',
    expected: 'border-emerald-500/25',
    actual: 'border-rose-500/25',
  }[tone];
  return (
    <div className={`rounded-md border ${toneClass} bg-coden-inner`}>
      <div className="border-b border-coden-border/50 px-3 py-2 text-[10px] font-bold uppercase tracking-wide text-coden-muted">
        {title}
      </div>
      <pre className="max-h-48 overflow-auto whitespace-pre-wrap break-words px-3 py-3 text-xs font-mono leading-relaxed text-coden-text">
{formatCaseValue(value)}
      </pre>
    </div>
  );
}


function CustomInputEditor({
  value,
  onChange,
  active,
}: {
  value: string;
  onChange: (value: string) => void;
  active: boolean;
}) {
  return (
    <details className="group rounded-md border border-coden-border bg-coden-inner/60" open={active}>
      <summary className="cursor-pointer px-3 py-2 text-xs font-semibold text-coden-muted hover:text-coden-text">
        Custom input JSON
      </summary>
      <div className="border-t border-coden-border/50 p-3">
        <textarea
          value={value}
          onChange={(event) => onChange(event.target.value)}
          placeholder='{"nums":[3,4,5,1,2]}'
          className="min-h-20 w-full resize-y rounded border border-coden-border bg-coden-bg px-3 py-2 font-mono text-xs text-coden-text placeholder:text-coden-muted focus:outline-none focus:ring-1 focus:ring-coden-accent"
        />
      </div>
    </details>
  );
}


function OutputPanel({
  result,
  selectedCase,
  selectedResult,
  ranAllTrial,
}: {
  result: ReturnType<typeof useAppStore.getState>['runResult'];
  selectedCase: TestCaseSummary | null;
  selectedResult?: RunCaseResult;
  ranAllTrial: boolean;
}) {
  if (!result) {
    return <EmptyPanel title="No output yet" body="Run a case to see output here." />;
  }
  if (ranAllTrial && result.case_results.length > 0) {
    return <CaseResultsCard results={result.case_results} compact />;
  }
  if (selectedResult) {
    return (
      <div className="space-y-3">
        <CasePreview
          testCase={selectedCase ?? {
            id: selectedResult.id,
            name: selectedResult.name,
            kind: selectedResult.kind,
            visible: true,
            input_repr: selectedResult.input_repr,
            expected_repr: selectedResult.expected_repr ?? '',
            tags: [],
          }}
          caseNumber={1}
          result={selectedResult}
        />
        <ValuePane title="Returned" value={selectedResult.return_value_repr || '(no output)'} />
      </div>
    );
  }
  return <ValuePane title="Returned" value={result.return_value_repr || '(no output)'} />;
}


function FeedbackPanel({
  result,
}: {
  result: ReturnType<typeof useAppStore.getState>['runResult'];
}) {
  if (!result) {
    return <EmptyPanel title="No feedback yet" body="Run a case to get correctness and runtime feedback." />;
  }
  return (
    <div className="space-y-3">
      <div className={[
        'rounded-md border px-4 py-3',
        result.passed
          ? 'border-emerald-500/30 bg-emerald-500/10'
          : result.correct
            ? 'border-amber-500/30 bg-amber-500/10'
            : 'border-rose-500/30 bg-rose-500/10',
      ].join(' ')}>
        <div className="text-sm font-semibold text-coden-text">{result.passed ? 'Accepted' : result.correct ? 'Correct but too slow' : 'Wrong answer'}</div>
        <div className="mt-1 text-xs text-coden-muted">{result.message}</div>
      </div>
      {result.runtime_message && (
        <ValuePane title="Runtime" value={result.runtime_message} />
      )}
    </div>
  );
}


function SubmissionsPanel({
  result,
  detailName,
}: {
  result: ReturnType<typeof useAppStore.getState>['runResult'];
  detailName: string;
}) {
  if (!result) {
    return <EmptyPanel title="No local submission yet" body="The latest run summary will appear here." />;
  }
  return (
    <div className="grid grid-cols-1 gap-3 md:grid-cols-3">
      <SummaryTile label="Challenge" value={detailName} />
      <SummaryTile label="Cases" value={String(result.case_results?.length || result.selected_case_ids?.length || 1)} />
      <SummaryTile label="Runtime" value={formatMs(result.runtime_user_ms)} accent={result.runtime_passed === false ? 'text-amber-200' : 'text-emerald-200'} />
    </div>
  );
}


function SummaryTile({
  label,
  value,
  accent = 'text-coden-text',
}: {
  label: string;
  value: string;
  accent?: string;
}) {
  return (
    <div className="rounded-md border border-coden-border bg-coden-inner px-3 py-3">
      <div className="text-[10px] font-bold uppercase tracking-wide text-coden-muted">{label}</div>
      <div className={`mt-1 truncate text-sm font-semibold ${accent}`}>{value}</div>
    </div>
  );
}


function EmptyPanel({ title, body }: { title: string; body: string }) {
  return (
    <div className="rounded-md border border-coden-border bg-coden-inner px-4 py-6">
      <div className="text-sm font-semibold text-coden-text">{title}</div>
      <div className="mt-1 text-xs text-coden-muted">{body}</div>
    </div>
  );
}


function CaseResultsCard({
  results,
  compact = false,
}: {
  results: NonNullable<ReturnType<typeof useAppStore.getState>['runResult']>['case_results'];
  compact?: boolean;
}) {
  return (
    <div className={compact ? '' : 'bg-coden-surface rounded-lg p-5 shadow-md'}>
      <div className="mb-3 text-xs font-semibold uppercase text-coden-muted">
        Case results
      </div>
      <div className="space-y-2">
        {results.map((caseResult) => (
          <div
            key={caseResult.id}
            className={[
              'rounded border p-3',
              caseResult.correct ? 'border-emerald-500/30 bg-emerald-500/10' : 'border-rose-500/30 bg-rose-500/10',
            ].join(' ')}
          >
            <div className="flex items-center justify-between gap-3">
              <div className="min-w-0">
                <div className="text-xs font-semibold text-coden-text truncate">{caseResult.name}</div>
                <div className="text-[10px] uppercase font-mono text-coden-muted">
                  {caseResult.hidden ? 'hidden' : caseResult.counts_toward_verdict ? caseResult.kind : 'custom · informational'}
                </div>
              </div>
              <div className={caseResult.correct ? 'text-emerald-300 text-xs font-bold' : 'text-rose-300 text-xs font-bold'}>
                {caseResult.correct ? 'PASS' : 'FAIL'}
              </div>
            </div>
            {!caseResult.correct && !caseResult.hidden && (
              <div className="mt-2 grid grid-cols-1 lg:grid-cols-3 gap-2 text-xs">
                <StructuredValueViewer value={caseResult.input_repr} borderClass="border-coden-border" />
                <StructuredValueViewer value={caseResult.return_value_repr || '(no output)'} borderClass="border-rose-500/20" />
                <StructuredValueViewer value={caseResult.expected_repr || '(no expected value)'} borderClass="border-emerald-500/20" />
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

function formatMs(value: number | null | undefined): string {
  if (value === null || value === undefined) return '—';
  if (value < 10) return `${value.toFixed(2)} ms`;
  if (value < 100) return `${value.toFixed(1)} ms`;
  return `${Math.round(value).toLocaleString()} ms`;
}


function ReturnValueCard({
  value,
  expected,
}: {
  value: string;
  expected?: string | null;
}) {
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
              What the reference solution returned.
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
        <span className="font-mono text-coden-text">the active Python file</span>{' '}
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
          className="px-3 py-1 text-xs rounded bg-coden-accent text-coden-accentContrast hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
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


function InputsCard({
  inputs,
}: {
  inputs: Record<string, string>;
}) {
  return (
    <div className="bg-coden-surface rounded-lg p-5 shadow-md mt-4">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2">
        Input Variables
      </div>
      <div className="space-y-3">
        {Object.entries(inputs).map(([name, val]) => (
          <div key={name} className="space-y-1">
            <div className="text-xs font-mono text-coden-accent">
              {name}
            </div>
            <pre className="bg-coden-inner rounded-lg p-3 text-[11px] font-mono overflow-x-auto whitespace-pre-wrap break-words max-h-40 overflow-y-auto shadow-inner border border-coden-border/30">
{val}
            </pre>
          </div>
        ))}
      </div>
    </div>
  );
}


function formatCertificateMethod(method: string): string {
  if (!method) return 'Verified certificate';
  return method.split('_').map((word) => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}


interface AITutorCardProps {
  status: 'idle' | 'loading' | 'loaded' | 'error';
  analysis: string;
  messages: TutorChatMessage[];
  sessions: TutorChatSession[];
  activeSessionId: string | null;
  error: string;
  onAnalyze: () => void;
  onAskFollowUp: (question: string) => void | Promise<void>;
  onSelectSession: (sessionId: string) => void;
  onDeleteSession: (sessionId: string) => void;
  onNewChat: () => void;
}

export function AITutorCard({
  status,
  analysis,
  messages,
  sessions,
  activeSessionId,
  error,
  onAnalyze,
  onAskFollowUp,
  onSelectSession,
  onDeleteSession,
  onNewChat,
}: AITutorCardProps) {
  const [draft, setDraft] = useState('');
  const hasMessages = messages.length > 0;
  const isLoading = status === 'loading';
  const activeSavedSessionId = sessions.some((session) => session.id === activeSessionId)
    ? activeSessionId
    : null;

  const submitFollowUp = () => {
    const question = draft.trim();
    if (!question || isLoading) return;
    setDraft('');
    void onAskFollowUp(question);
  };

  if (status === 'idle' && !hasMessages) {
    return (
      <>
        <div className="bg-coden-surface border border-indigo-500/30 rounded-lg p-5 shadow-md flex flex-col sm:flex-row items-center justify-between gap-4 mt-4">
          <div className="space-y-1 text-center sm:text-left">
            <div className="text-sm font-bold text-coden-text flex items-center justify-center sm:justify-start gap-1.5">
              <span className="text-indigo-300 font-mono">AI</span> Gemini Tutor
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
        {sessions.length > 0 && (
          <TutorHistoryPanel
            sessions={sessions}
            activeSessionId={activeSessionId}
            onSelectSession={onSelectSession}
            onDeleteSession={onDeleteSession}
          />
        )}
      </>
    );
  }

  if (status === 'loading' && !hasMessages) {
    return (
      <div className="bg-coden-surface border border-indigo-500/30 rounded-lg p-6 shadow-md mt-4 flex flex-col items-center justify-center gap-3 text-xs text-indigo-300">
        <div className="w-5 h-5 rounded-full border-2 border-indigo-500 border-t-transparent animate-spin"></div>
        <span>Gemini is analyzing your execution bug...</span>
      </div>
    );
  }

  if (status === 'error' && !hasMessages) {
    return (
      <>
        <div className="bg-coden-surface border border-rose-500/30 rounded-lg p-5 shadow-md mt-4 space-y-3">
          <div className="text-xs font-bold text-rose-300 flex items-center gap-1.5">
            <span className="font-mono">!</span> AI Analysis Failed
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
        {sessions.length > 0 && (
          <TutorHistoryPanel
            sessions={sessions}
            activeSessionId={activeSessionId}
            onSelectSession={onSelectSession}
            onDeleteSession={onDeleteSession}
          />
        )}
      </>
    );
  }

  return (
    <div className="bg-coden-surface border border-indigo-500/30 rounded-lg p-5 shadow-md mt-4 space-y-4">
      <div className="flex flex-col gap-3 border-b border-coden-border/60 pb-3">
        <div className="flex items-center justify-between gap-3">
          <div className="text-xs font-bold text-indigo-300 flex items-center gap-1.5">
            <span className="font-mono">AI</span> Gemini Tutor
          </div>
          <div className="flex items-center gap-2">
            {sessions.length > 0 && (
              <select
                value={activeSavedSessionId ?? ''}
                onChange={(event) => {
                  if (event.target.value) onSelectSession(event.target.value);
                }}
                className="max-w-44 rounded border border-coden-border bg-coden-inner px-2 py-1 text-xs text-coden-text focus:outline-none focus:ring-1 focus:ring-indigo-500"
              >
                <option value="">Saved chats</option>
                {sessions.map((session) => (
                  <option key={session.id} value={session.id}>
                    {sessionLabel(session)}
                  </option>
                ))}
              </select>
            )}
            <button
              type="button"
              onClick={onNewChat}
              disabled={isLoading}
              className="px-2 py-1 text-xs rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50"
            >
              New
            </button>
            <button
              type="button"
              onClick={() => activeSavedSessionId && onDeleteSession(activeSavedSessionId)}
              disabled={!activeSavedSessionId || isLoading}
              className="px-2 py-1 text-xs rounded border border-rose-500/30 text-rose-200 hover:bg-rose-500/10 disabled:opacity-50"
            >
              Delete
            </button>
          </div>
        </div>
        {activeSavedSessionId && (
          <div className="text-[10px] uppercase tracking-wider text-coden-muted">
            Saved chat history
          </div>
        )}
      </div>
      <div className="space-y-3 max-h-[34rem] overflow-y-auto pr-1">
        {(hasMessages ? messages : [{ role: 'assistant' as const, content: analysis }]).map((message, index) => (
          <TutorBubble
            key={`${message.role}-${index}-${message.content.slice(0, 24)}`}
            message={message}
          />
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="rounded-lg border border-indigo-500/20 bg-coden-inner px-3 py-2 text-xs text-indigo-300 flex items-center gap-2">
              <span className="w-3 h-3 rounded-full border-2 border-indigo-500 border-t-transparent animate-spin"></span>
              Thinking...
            </div>
          </div>
        )}
      </div>
      {status === 'error' && error && (
        <div className="text-xs text-rose-200 bg-rose-950/20 border border-rose-900/30 rounded-lg p-3 whitespace-pre-wrap">
          {error}
        </div>
      )}
      <form
        className="border-t border-coden-border/60 pt-3 flex flex-col gap-2"
        onSubmit={(event) => {
          event.preventDefault();
          submitFollowUp();
        }}
      >
        <textarea
          value={draft}
          onChange={(event) => setDraft(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === 'Enter' && !event.shiftKey) {
              event.preventDefault();
              submitFollowUp();
            }
          }}
          disabled={isLoading}
          rows={2}
          placeholder="Ask a follow-up..."
          className="w-full resize-none rounded-lg border border-coden-border bg-coden-inner px-3 py-2 text-xs text-coden-text placeholder:text-coden-muted focus:outline-none focus:ring-1 focus:ring-indigo-500 disabled:opacity-60"
        />
        <div className="flex justify-end">
          <button
            type="submit"
            disabled={isLoading || !draft.trim()}
            className="px-3 py-1.5 text-xs rounded bg-indigo-600 hover:bg-indigo-500 text-white font-semibold disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Send
          </button>
        </div>
      </form>
    </div>
  );
}


function TutorHistoryPanel({
  sessions,
  activeSessionId,
  onSelectSession,
  onDeleteSession,
}: {
  sessions: TutorChatSession[];
  activeSessionId: string | null;
  onSelectSession: (sessionId: string) => void;
  onDeleteSession: (sessionId: string) => void;
}) {
  return (
    <div className="bg-coden-surface border border-coden-border/70 rounded-lg p-4 shadow-md mt-3 space-y-3">
      <div className="flex items-center justify-between gap-3">
        <div className="text-xs uppercase tracking-wider text-coden-muted font-semibold">
          Saved tutor chats
        </div>
        <div className="text-[10px] text-coden-muted">
          {sessions.length} saved
        </div>
      </div>
      <div className="space-y-2 max-h-48 overflow-y-auto pr-1">
        {sessions.map((session) => (
          <div
            key={session.id}
            className={`rounded-lg border p-3 ${
              session.id === activeSessionId
                ? 'border-indigo-500/50 bg-indigo-500/10'
                : 'border-coden-border/50 bg-coden-inner'
            }`}
          >
            <button
              type="button"
              onClick={() => onSelectSession(session.id)}
              className="w-full text-left"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="min-w-0">
                  <div className="text-xs text-coden-text font-semibold truncate">
                    {sessionLabel(session)}
                  </div>
                  <div className="text-[10px] text-coden-muted mt-0.5">
                    {formatSessionDate(session.updatedAt)}
                  </div>
                </div>
                <div className="text-[10px] text-coden-muted shrink-0">
                  {session.messages.length} msgs
                </div>
              </div>
            </button>
            <div className="mt-2 flex justify-end">
              <button
                type="button"
                onClick={() => onDeleteSession(session.id)}
                className="px-2 py-1 text-[10px] rounded border border-rose-500/30 text-rose-200 hover:bg-rose-500/10"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}


function TutorBubble({ message }: { message: TutorChatMessage }) {
  const isUser = message.role === 'user';
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={
          isUser
            ? 'max-w-[85%] rounded-lg bg-indigo-600/30 border border-indigo-400/30 px-3 py-2 text-xs text-coden-text whitespace-pre-wrap'
            : 'max-w-[92%] rounded-lg bg-coden-inner border border-coden-border/60 px-3 py-2'
        }
      >
        {isUser ? message.content : <TutorMarkdown content={message.content} />}
      </div>
    </div>
  );
}


function TutorMarkdown({ content }: { content: string }) {
  return (
    <article className="prose prose-invert prose-xs max-w-none
                        prose-headings:text-indigo-200 prose-headings:font-bold prose-headings:my-2
                        prose-p:text-coden-text prose-p:leading-relaxed prose-p:my-1.5
                        prose-strong:text-indigo-300
                        prose-code:text-indigo-300 prose-code:before:content-none prose-code:after:content-none
                        prose-ul:list-disc prose-ul:pl-4 prose-ul:my-2
                        prose-ol:list-decimal prose-ol:pl-4 prose-ol:my-2
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
        {content}
      </ReactMarkdown>
    </article>
  );
}
