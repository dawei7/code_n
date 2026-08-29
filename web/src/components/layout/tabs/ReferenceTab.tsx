/**
 * ReferenceTab — renders the per-algorithm markdown documentation
 * for the currently-selected challenge with high visual polish,
 * rich KaTeX mathematics typesetting, and a unified single
 * Canonical Optimal Approach & Solution view.
 */
import { Children, isValidElement, useEffect, useState, useCallback } from 'react';
import type { ReactNode } from 'react';
import { Editor } from '@monaco-editor/react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import 'katex/dist/katex.min.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLeetcode } from '@fortawesome/free-brands-svg-icons/faLeetcode';

import { ApiError, apiText } from '../../../api/client';
import {
  MermaidDiagram,
  mermaidSourceFromPreChildren,
} from '../../markdown/MermaidDiagram';
import { useAppStore } from '../../../store/useAppStore';
import { canRevealSolution } from '../../../lib/cheaterMode';
import type {
  SupportedLanguage,
} from '../../../types/api';


type LoadState =
  | { kind: 'idle' }
  | { kind: 'loading' }
  | { kind: 'loaded'; markdown: string }
  | { kind: 'missing'; challengeId: string; challengeName: string; category: string }
  | { kind: 'error'; message: string };

let overviewCache: string | undefined;

const REFERENCE_LANGUAGES: Array<{
  id: SupportedLanguage;
  label: string;
  monaco: string;
  extension: string;
}> = [
  { id: 'python', label: 'Python', monaco: 'python', extension: 'py' },
  { id: 'javascript', label: 'JavaScript', monaco: 'javascript', extension: 'js' },
  { id: 'sql', label: 'SQL', monaco: 'sql', extension: 'sql' },
  { id: 'bash', label: 'Bash', monaco: 'shell', extension: 'sh' },
];

export function ReferenceTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const cheaterMode = useAppStore((s) => s.cheaterMode);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const [state, setState] = useState<LoadState>({ kind: 'idle' });

  const challengeId = detail?.id ?? null;
  const challengeName = detail?.name ?? null;
  const category = detail?.category ?? null;

  const load = useCallback(async (which: 'overview' | 'by-id', id?: string) => {
    setState({ kind: 'loading' });
    try {
      if (which === 'overview') {
        if (overviewCache !== undefined) {
          setState({ kind: 'loaded', markdown: overviewCache });
          return;
        }
        const text = await apiText('/docs/overview');
        overviewCache = text;
        setState({ kind: 'loaded', markdown: text });
      } else {
        if (!id) {
          setState({ kind: 'idle' });
          return;
        }
        try {
          const text = await apiText(`/docs/by-id/${encodeURIComponent(id)}`);
          setState({ kind: 'loaded', markdown: text });
        } catch (e) {
          if (e instanceof ApiError && e.status === 404) {
            setState({
              kind: 'missing',
              challengeId: id,
              challengeName: '?',
              category: '?',
            });
            return;
          }
          throw e;
        }
      }
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      setState({ kind: 'error', message });
    }
  }, []);

  useEffect(() => {
    if (!challengeId) {
      void load('overview');
      return;
    }
    setState({ kind: 'loading' });
    void load('by-id', challengeId).then(() => {
      if (challengeName && category) {
        setState((prev) =>
          prev.kind === 'missing'
            ? { ...prev, challengeName, category }
            : prev
        );
      }
    });
  }, [challengeId, challengeName, category, load]);

  if (state.kind === 'idle' || state.kind === 'loading') {
    return (
      <div className="flex min-h-64 items-center justify-center p-8 text-sm text-coden-muted">
        <div className="flex flex-col items-center gap-2">
          <div className="h-6 w-6 animate-spin rounded-full border-2 border-coden-accent border-t-transparent" />
          <span>Loading reference documentation...</span>
        </div>
      </div>
    );
  }

  if (state.kind === 'error') {
    return (
      <div className="flex flex-col items-center justify-center gap-3 p-8 text-xs">
        <div className="text-red-400 font-semibold text-sm">Failed to load documentation</div>
        <pre className="text-coden-muted whitespace-pre-wrap max-w-lg rounded border border-coden-border bg-coden-bg p-3">{state.message}</pre>
        <button
          type="button"
          onClick={() => challengeId ? void load('by-id', challengeId) : void load('overview')}
          className="mt-2 px-4 py-1.5 text-xs font-semibold rounded-lg border border-coden-border bg-coden-surface hover:bg-coden-surface-elevated transition-colors text-coden-text"
        >
          Retry
        </button>
      </div>
    );
  }

  if (state.kind === 'missing') {
    const issueTitle = encodeURIComponent(`Docs: add reference for ${state.challengeId}`);
    const issueBody = encodeURIComponent(
      `The reference doc for **${state.challengeId}** (\`${state.challengeName}\`, category: ${state.category}) doesn't exist yet.\n\n` +
      `Please complete the canonical package document at \`dsa/leetcode/<frontend_id:04d>_<slug>/reference/\`.`,
    );
    return (
      <div className="flex flex-col items-center justify-center gap-3 p-8 text-xs text-coden-muted">
        <div className="text-base font-semibold text-coden-text">
          No reference documentation for <code className="text-coden-accent">{state.challengeId}</code>
        </div>
        <div className="text-sm max-w-md text-center text-coden-muted">
          {state.challengeName} &middot; {state.category}
        </div>
        <a
          href={`https://github.com/dawei7/code_n/issues/new?title=${issueTitle}&body=${issueBody}`}
          target="_blank"
          rel="noreferrer"
          className="mt-3 px-4 py-2 text-xs font-semibold rounded-lg border border-coden-accent text-coden-accent hover:bg-coden-accent hover:text-coden-accentContrast transition-colors"
        >
          Suggest this doc on GitHub →
        </a>
      </div>
    );
  }

  // Loaded: render the markdown and canonical solution section.
  const markdown = state.markdown;
  const solutionUnlocked = challengeId
    ? canRevealSolution(completed.includes(challengeId), cheaterMode)
    : false;

  return (
    <div className="coden-reading-container">
      {/* Challenge Header Bar */}
      {detail && <ChallengeHeaderBar detail={detail} challengeId={challengeId ?? ''} />}

      {/* Main Documentation Body */}
      <article className="prose prose-sm max-w-none text-coden-text
                          prose-headings:text-coden-text prose-headings:tracking-tight
                          prose-h2:text-lg prose-h2:font-bold prose-h2:mt-8 prose-h2:mb-3 prose-h2:border-b prose-h2:border-coden-border prose-h2:pb-2
                          prose-h3:text-base prose-h3:font-semibold prose-h3:mt-5 prose-h3:mb-2
                          prose-p:leading-7 prose-p:my-3.5 prose-p:text-coden-text
                          prose-li:my-1 prose-li:text-coden-text
                          prose-strong:text-coden-text prose-strong:font-semibold
                          prose-em:text-coden-text
                          prose-hr:border-coden-border prose-hr:my-6
                          prose-blockquote:text-coden-text prose-blockquote:border-coden-accent prose-blockquote:bg-coden-surface-elevated/40 prose-blockquote:rounded-r-lg prose-blockquote:py-1 prose-blockquote:px-4
                          prose-a:text-coden-accent prose-a:font-medium hover:prose-a:underline
                          prose-code:text-coden-accent prose-code:font-mono
                          prose-code:before:content-none prose-code:after:content-none
                          prose-table:my-4 prose-th:text-left">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeRaw, rehypeKatex]}
          components={{
            h1: ({ node, ...props }) => (
              <h1 {...props} className="text-xl font-bold mt-0 mb-4 text-coden-text" />
            ),
            h2: ({ node, ...props }) => (
              <h2 {...props} className="text-lg font-bold mt-8 mb-3 pb-2 border-b border-coden-border text-coden-text" />
            ),
            h3: ({ node, ...props }) => {
              const text = textFromReactNode(props.children);
              const isExample = /^Example\s+\d+/i.test(text.trim());
              return (
                <h3
                  {...props}
                  className={
                    isExample
                      ? 'text-sm font-bold uppercase tracking-wider text-coden-accent mt-6 mb-2 flex items-center gap-2'
                      : 'text-base font-semibold mt-5 mb-2 text-coden-text'
                  }
                />
              );
            },
            details: ({ node, ...props }) => <CollapsibleDetails node={node} {...props} />,
            summary: ({ node, ...props }) => (
              <summary
                {...props}
                className="cursor-pointer select-none text-sm font-semibold text-coden-accent"
              />
            ),
            a: ({ node, ...props }) => {
              const label = textFromReactNode(props.children).trim().toLowerCase();
              if (props.href?.startsWith('https://leetcode.com/problems/') && label === 'leetcode') {
                const descriptionUrl = new URL(props.href);
                const problemSlug = descriptionUrl.pathname.split('/').filter(Boolean)[1];
                descriptionUrl.pathname = `/problems/${problemSlug}/description/`;
                return (
                  <a
                    {...props}
                    href={descriptionUrl.toString()}
                    target="_blank"
                    rel="noreferrer"
                    title="Open the official LeetCode problem"
                    aria-label="Open the official LeetCode problem"
                    className="inline-flex items-center justify-center text-coden-accent hover:text-coden-text"
                  >
                    <LeetCodeIcon />
                  </a>
                );
              }
              if (props.href?.endsWith('.md')) {
                const match = props.href.match(/^([a-z]+_\d+)/);
                if (match) {
                  return (
                    <a
                      {...props}
                      href="#"
                      onClick={(e) => {
                        e.preventDefault();
                        useAppStore.getState().selectChallenge(match[1]);
                      }}
                      className="cursor-pointer text-coden-accent hover:underline"
                    />
                  );
                }
              }
              return <a {...props} target="_blank" rel="noreferrer" />;
            },
            table: ({ node, ...props }) => (
              <div className="my-4 overflow-x-auto rounded-lg border border-coden-border bg-coden-surface shadow-sm">
                <table {...props} className="my-0 w-full min-w-full table-auto border-collapse text-xs text-coden-text" />
              </div>
            ),
            th: ({ node, ...props }) => (
              <th {...props} className="border-b border-coden-border px-3 py-2.5 bg-coden-surface-elevated font-semibold text-coden-text text-left" />
            ),
            td: ({ node, ...props }) => (
              <td {...props} className="border-b border-coden-border/60 px-3 py-2 text-coden-text align-top" />
            ),
            img: ({ node, ...props }) => {
              const rawSrc = String(props.src || '');
              const src = challengeId?.startsWith('lc_')
                ? leetcodeAssetUrl(challengeId, rawSrc)
                : rawSrc;
              return (
                <img
                  {...props}
                  src={src}
                  className="mx-auto my-5 max-h-[520px] max-w-full rounded-lg border border-coden-border bg-coden-bg object-contain shadow-sm"
                />
              );
            },
            pre: ({ children, ...props }) => {
              const diagram = mermaidSourceFromPreChildren(children);
              if (diagram) return <MermaidDiagram source={diagram} />;
              return (
                <pre
                  {...props}
                  className="my-4 overflow-x-auto rounded-lg border border-coden-border bg-coden-surface-elevated p-3.5 font-mono text-xs text-coden-text shadow-sm"
                >
                  {children}
                </pre>
              );
            },
            code: ({ className, children, ...props }) => {
              const isBlock = String(children).includes('\n');
              if (isBlock) {
                return (
                  <code {...props} className={className}>
                    {children}
                  </code>
                );
              }
              return (
                <code
                  {...props}
                  className="rounded border border-coden-border/80 bg-coden-surface-elevated px-1.5 py-0.5 font-mono text-xs text-coden-accent"
                >
                  {children}
                </code>
              );
            },
          }}
        >
          {markdown}
        </ReactMarkdown>

        {/* Canonical Reference Solution Section */}
        {challengeId && (
          <CanonicalSolutionSection
            challengeId={challengeId}
            detail={detail}
            unlocked={solutionUnlocked}
          />
        )}
      </article>
    </div>
  );
}

function ChallengeHeaderBar({
  detail,
  challengeId,
}: {
  detail: any;
  challengeId: string;
}) {
  if (!detail) return null;

  const difficulty = detail.difficulty_label || 'Medium';
  const diffColor =
    difficulty.toLowerCase() === 'easy'
      ? 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border-emerald-500/30'
      : difficulty.toLowerCase() === 'hard'
      ? 'bg-rose-500/15 text-rose-600 dark:text-rose-400 border-rose-500/30'
      : 'bg-amber-500/15 text-amber-600 dark:text-amber-400 border-amber-500/30';

  const frontendId = detail.leetcode_frontend_id || detail.id?.replace(/^lc_/, '') || '';
  const category = detail.category || detail.leetcode_category || '';

  return (
    <div className="mb-6 flex flex-wrap items-center justify-between gap-3 border-b border-coden-border pb-4 pt-1">
      <div className="flex flex-wrap items-center gap-2.5">
        {frontendId && (
          <span className="rounded-md bg-coden-surface-elevated px-2 py-0.5 font-mono text-xs font-bold text-coden-muted border border-coden-border">
            #{frontendId}
          </span>
        )}
        <h1 className="text-xl font-bold text-coden-text m-0 tracking-tight">
          {detail.name || challengeId}
        </h1>
        <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold border ${diffColor}`}>
          {difficulty}
        </span>
        {category && (
          <span className="rounded-full bg-coden-surface-elevated px-2.5 py-0.5 text-xs font-medium text-coden-muted border border-coden-border">
            {category}
          </span>
        )}
        {detail.elo_rating && (
          <span className="rounded-full bg-indigo-500/15 text-indigo-600 dark:text-indigo-400 px-2.5 py-0.5 text-xs font-medium border border-indigo-500/30 font-mono">
            Elo {Math.round(detail.elo_rating)}
          </span>
        )}
      </div>

      {detail.leetcode_url && (
        <a
          href={detail.leetcode_url}
          target="_blank"
          rel="noreferrer"
          className="inline-flex items-center gap-1.5 rounded-lg border border-coden-border bg-coden-surface-elevated px-3 py-1.5 text-xs font-semibold text-coden-text hover:border-coden-accent hover:text-coden-accent transition-all shadow-sm"
          title="Open official LeetCode problem"
        >
          <LeetCodeIcon />
          <span>LeetCode</span>
          <span className="text-coden-muted text-[10px]">↗</span>
        </a>
      )}
    </div>
  );
}

function CanonicalSolutionSection({
  challengeId,
  detail,
  unlocked,
}: {
  challengeId: string;
  detail: any;
  unlocked: boolean;
}) {
  const [solutionOpen, setSolutionOpen] = useState(false);
  const theme = useAppStore((state) => state.theme);
  const [copyStatus, setCopyStatus] = useState<'idle' | 'copied' | 'failed'>('idle');

  const timeComplexity = detail?.time_complexity || detail?.solution_variant_complexity?.time || '';
  const spaceComplexity = detail?.space_complexity || detail?.solution_variant_complexity?.space || '';

  const solutionSource = detail?.optimal_source?.trim() || detail?.leetcode_optimal_source?.trim() || '';
  const language = REFERENCE_LANGUAGES.find((l) => l.id === detail?.primary_language) ?? REFERENCE_LANGUAGES[0];

  const copyCode = async () => {
    try {
      await copyCompleteCode(solutionSource);
      setCopyStatus('copied');
      setTimeout(() => setCopyStatus('idle'), 2000);
    } catch {
      setCopyStatus('failed');
    }
  };

  const lineCount = solutionSource ? solutionSource.split(/\r?\n/).length : 0;
  const editorHeight = Math.min(600, Math.max(200, lineCount * 19 + 32));

  return (
    <section className="not-prose my-6 rounded-xl border border-coden-border bg-coden-surface shadow-md overflow-hidden transition-all">
      {/* Header Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 border-b border-coden-border bg-coden-surface-elevated/70 px-4 py-3">
        <div className="flex items-center gap-2">
          <span className="flex h-6 w-6 items-center justify-center rounded-md bg-coden-accent/15 text-xs font-bold text-coden-accent">
            ★
          </span>
          <span className="font-semibold text-sm text-coden-text">
            Canonical Reference Solution
          </span>
        </div>

        {/* Complexity Badges */}
        <div className="flex flex-wrap items-center gap-2">
          {timeComplexity && (
            <span className="coden-complexity-pill" title="Time Complexity">
              <span className="text-coden-muted text-[11px] uppercase tracking-wider font-mono">Time</span>
              <span className="text-coden-accent font-semibold">{timeComplexity}</span>
            </span>
          )}
          {spaceComplexity && (
            <span className="coden-complexity-pill" title="Space Complexity">
              <span className="text-coden-muted text-[11px] uppercase tracking-wider font-mono">Space</span>
              <span className="text-coden-accent font-semibold">{spaceComplexity}</span>
            </span>
          )}
        </div>
      </div>

      {/* Verified Solution Section */}
      {solutionSource && (
        <div>
          <button
            type="button"
            disabled={!unlocked}
            onClick={() => unlocked && setSolutionOpen((v) => !v)}
            className={`flex w-full items-center justify-between px-4 py-3 text-left text-sm font-semibold transition-colors ${
              unlocked
                ? 'text-coden-text hover:bg-coden-surface-elevated/40'
                : 'text-coden-muted cursor-not-allowed opacity-75'
            }`}
          >
            <div className="flex items-center gap-2">
              {unlocked ? (
                <span className="text-xs text-coden-accent">{solutionOpen ? '▼' : '▶'}</span>
              ) : (
                <LockIcon />
              )}
              <span>Verified {language.label} Solution</span>
            </div>
            <span className="text-xs font-normal text-coden-muted">
              {unlocked
                ? (solutionOpen ? 'Click to hide code' : 'Click to view code')
                : 'Solve this challenge to unlock'}
            </span>
          </button>

          {unlocked && solutionOpen && (
            <div className="border-t border-coden-border bg-coden-bg p-4 space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-xs">
                  <span className="rounded px-2 py-1 font-mono font-medium border border-coden-border bg-coden-surface text-coden-accent">
                    {language.label}
                  </span>
                  <span className="text-coden-muted">{lineCount} lines</span>
                </div>
                <button
                  type="button"
                  onClick={() => void copyCode()}
                  className="inline-flex h-7 items-center gap-1.5 rounded border border-coden-border bg-coden-surface px-2.5 text-xs font-semibold text-coden-text transition-colors hover:border-coden-accent hover:text-coden-accent"
                >
                  <CopyIcon />
                  {copyStatus === 'copied' ? 'Copied!' : copyStatus === 'failed' ? 'Failed' : 'Copy code'}
                </button>
              </div>

              <div className="overflow-hidden rounded-lg border border-coden-border bg-coden-bg" style={{ height: editorHeight }}>
                <Editor
                  path={`reference://${challengeId}/optimal/verified.${language.extension}`}
                  height="100%"
                  language={language.monaco}
                  theme={theme === 'dark' ? 'vs-dark' : 'light'}
                  value={solutionSource}
                  options={{
                    readOnly: true,
                    domReadOnly: true,
                    contextmenu: false,
                    minimap: { enabled: false },
                    lineNumbers: 'on',
                    fontSize: 12.5,
                    fontFamily: "'Cascadia Code', 'Cascadia Mono', Consolas, 'SFMono-Regular', monospace",
                    renderLineHighlight: 'none',
                    scrollBeyondLastLine: false,
                    overviewRulerLanes: 0,
                    hideCursorInOverviewRuler: true,
                    wordWrap: 'off',
                    automaticLayout: true,
                    padding: { top: 12, bottom: 12 },
                  }}
                />
              </div>
            </div>
          )}
        </div>
      )}
    </section>
  );
}

function LeetCodeIcon() {
  return (
    <FontAwesomeIcon
      icon={faLeetcode}
      aria-hidden="true"
      className="h-4 w-4 text-[#FFA116]"
    />
  );
}

async function copyCompleteCode(source: string): Promise<void> {
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(source);
      return;
    }
  } catch {
    // Electron or browser fallback
  }

  const textarea = document.createElement('textarea');
  textarea.value = source;
  textarea.setAttribute('readonly', '');
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  const copied = document.execCommand('copy');
  textarea.remove();
  if (!copied) throw new Error('Clipboard copy failed');
}

function CopyIcon() {
  return (
    <svg
      aria-hidden="true"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      className="h-3.5 w-3.5"
    >
      <rect width="14" height="14" x="8" y="8" rx="2" />
      <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" />
    </svg>
  );
}

function LockIcon() {
  return (
    <svg
      aria-hidden="true"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      className="h-3.5 w-3.5 shrink-0 text-coden-muted"
    >
      <rect width="14" height="11" x="5" y="11" rx="2" />
      <path d="M8 11V7a4 4 0 0 1 8 0v4" />
    </svg>
  );
}

function leetcodeAssetUrl(challengeId: string, src: string): string {
  if (!src || /^(https?:|data:|\/)/i.test(src)) return src;
  const clean = src.replace(/^\.?\//, '').replace(/^assets\//, '');
  return `/api/docs/by-id/${encodeURIComponent(challengeId)}/assets/${clean}`;
}

type MarkdownAstNode = {
  type?: string;
  tagName?: string;
  value?: string;
  children?: MarkdownAstNode[];
};

function isSummaryElement(child: ReactNode): boolean {
  return (
    isValidElement(child) &&
    (
      child.type === 'summary' ||
      (child.props as { node?: MarkdownAstNode }).node?.tagName === 'summary'
    )
  );
}

function textFromAst(node?: MarkdownAstNode): string {
  if (!node) return '';
  if (typeof node.value === 'string') return node.value;
  return (node.children ?? []).map(textFromAst).join('');
}

function textFromReactNode(node: ReactNode): string {
  if (typeof node === 'string' || typeof node === 'number') return String(node);
  if (Array.isArray(node)) return node.map(textFromReactNode).join('');
  if (isValidElement(node)) {
    return textFromReactNode((node.props as { children?: ReactNode }).children);
  }
  return '';
}

function CollapsibleDetails({
  children,
  node,
}: {
  children?: ReactNode;
  node?: MarkdownAstNode;
}) {
  const childArray = Children.toArray(children);
  const summaryIndex = childArray.findIndex(isSummaryElement);
  const astSummary = node?.children?.find((child) => child.tagName === 'summary');
  const summaryText =
    summaryIndex >= 0 && isValidElement(childArray[summaryIndex])
      ? textFromReactNode((childArray[summaryIndex].props as { children?: ReactNode }).children).trim()
      : textFromAst(astSummary).trim();
  const summary = summaryText || 'Official Editorial';
  const body = summaryIndex >= 0
    ? childArray.filter((_, index) => index !== summaryIndex)
    : childArray;
  const isOfficialEditorial = summary.toLowerCase() === 'official editorial';

  return (
    <details
      className={
        isOfficialEditorial
          ? 'my-6 text-coden-text'
          : 'my-3 rounded-lg border border-coden-border bg-coden-surface-elevated/40 text-coden-text overflow-hidden'
      }
    >
      <summary
        className={
          isOfficialEditorial
            ? 'cursor-pointer select-none border-b border-coden-border pb-2 text-lg font-semibold text-coden-text hover:text-coden-accent transition-colors'
            : 'cursor-pointer select-none px-3.5 py-2.5 text-sm font-semibold text-coden-accent hover:bg-coden-border/40 transition-colors'
        }
      >
        {summary}
      </summary>
      <div
        className={
          isOfficialEditorial
            ? 'pt-4 text-sm text-coden-text'
            : 'border-t border-coden-border px-4 py-3 text-sm text-coden-text'
        }
      >
        {body}
      </div>
    </details>
  );
}
