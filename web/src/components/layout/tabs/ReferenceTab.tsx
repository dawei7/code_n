/**
 * ReferenceTab — renders the per-algorithm markdown documentation
 * for the currently-selected challenge.
 *
 * Fetches the doc from the server's `/api/docs/by-id/{id}` endpoint
 * (with `/api/docs/overview` for the general overview, shown when
 * no challenge is selected). The fetched markdown is rendered with
 * `react-markdown` + `remark-gfm` (so tables, task lists, and
 * autolinks work).
 *
 * States:
 *  - no challenge selected  →  render the overview doc
 *  - loading                →  skeleton placeholder
 *  - no doc yet             →  friendly empty state with a
 *                              "Contribute on GitHub" link that
 *                              opens a pre-filled issue
 *  - error                  →  inline error with retry button
 *  - loaded                 →  rendered markdown
 *
 * The tab is lazy-loaded by the registry.
 */
import { Children, isValidElement, useEffect, useState, useCallback } from 'react';
import type { ReactNode } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import 'katex/dist/katex.min.css';

import { useAppStore } from '../../../store/useAppStore';


type LoadState =
  | { kind: 'idle' }
  | { kind: 'loading' }
  | { kind: 'loaded'; markdown: string }
  | { kind: 'missing'; challengeId: string; challengeName: string; category: string }
  | { kind: 'error'; message: string };

type LeetCodeQuestion = {
  frontend_id: string;
  title: string;
  slug: string;
};


const CACHE: Map<string, string> = new Map();
const LEETCODE_CACHE: Map<string, LeetCodeQuestion | null> = new Map();
let OVERVIEW_CACHE: string | null = null;


export function ReferenceTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const language = useAppStore((s) => s.language);
  const activeSet = useAppStore((s) => s.activeSet);
  const [state, setState] = useState<LoadState>({ kind: 'idle' });
  const [leetcodeQuestion, setLeetcodeQuestion] = useState<LeetCodeQuestion | null>(null);

  const challengeId = detail?.id ?? null;
  const challengeName = detail?.name ?? null;
  const category = detail?.category ?? null;
  const shouldShowLeetcodeReference = activeSet === 'neetcode' && !!detail?.leetcode_url;

  const load = useCallback(async (which: 'overview' | 'by-id', id?: string) => {
    setState({ kind: 'loading' });
    try {
      if (which === 'overview') {
        if (OVERVIEW_CACHE !== null) {
          setState({ kind: 'loaded', markdown: OVERVIEW_CACHE });
          return;
        }
        const res = await fetch(`/api/docs/overview?lang=${language}`);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const text = await res.text();
        OVERVIEW_CACHE = text;
        setState({ kind: 'loaded', markdown: text });
      } else {
        if (!id) {
          setState({ kind: 'idle' });
          return;
        }
        const cached = CACHE.get(id);
        if (cached !== undefined) {
          setState({ kind: 'loaded', markdown: cached });
          return;
        }
        const res = await fetch(`/api/docs/by-id/${encodeURIComponent(id)}?lang=${language}`);
        if (res.status === 404) {
          setState({
            kind: 'missing',
            challengeId: id,
            challengeName: '?',
            category: '?',
          });
          return;
        }
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const text = await res.text();
        CACHE.set(id, text);
        setState({ kind: 'loaded', markdown: text });
      }
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      setState({ kind: 'error', message });
    }
  }, [language]);

  useEffect(() => {
    if (!challengeId) {
      // No challenge → render the overview
      void load('overview');
      return;
    }
    // Challenge changed → drop the previous state and re-fetch.
    setState({ kind: 'loading' });
    CACHE.delete('__last_loaded__'); // force a refetch when the user clicks Retry
    void load('by-id', challengeId).then(() => {
      // If the load completed with a 404, the state is already 'missing'.
      // Enrich it with the current challenge's name + category.
      if (challengeName && category) {
        setState((prev) =>
          prev.kind === 'missing'
            ? { ...prev, challengeName, category }
            : prev
        );
      }
    });
  }, [challengeId, challengeName, category, language, load]);

  useEffect(() => {
    const slug = detail?.leetcode_slug;
    if (!shouldShowLeetcodeReference || !slug) {
      setLeetcodeQuestion(null);
      return;
    }

    const cached = LEETCODE_CACHE.get(slug);
    if (cached !== undefined) {
      setLeetcodeQuestion(cached);
      return;
    }

    let cancelled = false;
    void fetch(`/api/leetcode/questions/${encodeURIComponent(slug)}`)
      .then((res) => (res.ok ? res.json() : null))
      .then((payload: LeetCodeQuestion | null) => {
        if (cancelled) return;
        LEETCODE_CACHE.set(slug, payload);
        setLeetcodeQuestion(payload);
      })
      .catch(() => {
        if (cancelled) return;
        LEETCODE_CACHE.set(slug, null);
        setLeetcodeQuestion(null);
      });

    return () => {
      cancelled = true;
    };
  }, [detail?.leetcode_slug, shouldShowLeetcodeReference]);

  if (state.kind === 'idle' || state.kind === 'loading') {
    return (
      <div className="flex items-center justify-center text-xs text-coden-muted">
        Loading reference…
      </div>
    );
  }

  if (state.kind === 'error') {
    return (
      <div className="flex flex-col items-center justify-center gap-2 text-xs">
        <div className="text-red-400">Failed to load doc:</div>
        <pre className="text-coden-muted whitespace-pre-wrap">{state.message}</pre>
        <button
          type="button"
          onClick={() => challengeId ? void load('by-id', challengeId) : void load('overview')}
          className="mt-2 px-3 py-1 text-sm rounded border border-coden-border hover:bg-coden-surface"
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
      `Please add one at \`docs/algorithms/${state.category}/${state.challengeId}_<slug>.md\` using the template at \`docs/_template.md\`.`,
    );
    return (
      <div className="flex flex-col items-center justify-center gap-3 text-xs text-coden-muted">
        <div className="text-base font-semibold text-coden-text">
          No reference doc yet for <code className="text-coden-accent">{state.challengeId}</code>
        </div>
        <div className="text-sm max-w-md text-center">
          {state.challengeName} &middot; {state.category}
        </div>
        <a
          href={`https://github.com/dawei7/code_n/issues/new?title=${issueTitle}&body=${issueBody}`}
          target="_blank"
          rel="noreferrer"
          className="mt-2 px-3 py-1.5 text-sm rounded border border-coden-accent text-coden-accent hover:bg-coden-accent hover:text-coden-bg"
        >
          Suggest this doc on GitHub →
        </a>
      </div>
    );
  }

  // Loaded: render the markdown.
  const markdown = shouldShowLeetcodeReference
    ? removeGeeksforGeeksReference(state.markdown)
    : state.markdown;
  const officialEditorial = splitCodeChefOfficialEditorial(markdown);

  return (
    <div>
      {shouldShowLeetcodeReference && detail && (
        <LeetCodeReference detail={detail} question={leetcodeQuestion} />
      )}
      <article className="prose prose-sm max-w-none p-4 text-coden-text
                          prose-headings:text-coden-text
                          prose-p:text-coden-text
                          prose-li:text-coden-text
                          prose-strong:text-coden-text
                          prose-em:text-coden-text
                          prose-hr:border-coden-border
                          prose-blockquote:text-coden-text
                          prose-blockquote:border-coden-accent
                          prose-a:text-coden-accent
                          prose-code:text-coden-accent
                          prose-code:before:content-none
                          prose-code:after:content-none
                          prose-table:my-2
                          prose-th:text-left">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeRaw, rehypeKatex]}
          components={{
            h1: ({ node, ...props }) => (
              <h1 {...props} className="text-xl font-semibold mt-0 mb-4 text-coden-text" />
            ),
            h2: ({ node, ...props }) => (
              <h2 {...props} className="text-lg font-semibold mt-6 mb-3 text-coden-text" />
            ),
            h3: ({ node, ...props }) => (
              <h3 {...props} className="text-base font-semibold mt-4 mb-2 text-coden-text" />
            ),
            details: ({ node, ...props }) => <CollapsibleDetails node={node} {...props} />,
            summary: ({ node, ...props }) => (
              <summary
                {...props}
                className="cursor-pointer select-none text-sm font-semibold text-coden-accent"
              />
            ),
            a: ({ node, ...props }) => {
              if (props.href?.endsWith('.md')) {
                // Extract the challenge ID (e.g. "dp_02_climbing-stairs.md" -> "dp_02")
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
              <table {...props} className="border-collapse border border-coden-border text-xs text-coden-text" />
            ),
            th: ({ node, ...props }) => (
              <th {...props} className="border border-coden-border px-2 py-1 bg-coden-bg text-coden-text font-semibold" />
            ),
            td: ({ node, ...props }) => (
              <td {...props} className="border border-coden-border px-2 py-1 text-coden-text" />
            ),
            pre: ({ children, ...props }) => (
              <pre
                {...props}
                className="bg-white border border-slate-300 rounded p-3 text-xs text-slate-950 shadow-sm overflow-x-auto my-3 dark:bg-coden-bg dark:border-coden-border dark:text-coden-text"
              >
                {children}
              </pre>
            ),
            code: ({ className, children, ...props }) => {
              // Heuristic for inline vs block: the code inside a <pre>
              // always contains newlines; inline code never does. The
              // AST `node` prop is no longer reliable in react-markdown v9,
              // so we use the children-string check instead.
              const isBlock = String(children).includes('\n');
              if (isBlock) {
                // Inside a <pre>. Just pass through with the language
                // className (e.g. "language-python"); the <pre> handles
                // background + padding.
                return (
                  <code {...props} className={className}>
                    {children}
                  </code>
                );
              }
              // Inline code (e.g. `foo` in a sentence). Style as a chip.
              return (
                <code
                  {...props}
                  className="bg-sky-50 border border-sky-200 rounded px-1 py-0.5 text-sky-800 text-xs dark:bg-coden-bg dark:border-coden-border dark:text-coden-accent"
                >
                  {children}
                </code>
              );
            },
          }}
        >
          {officialEditorial?.before ?? markdown}
        </ReactMarkdown>
        {officialEditorial && (
          <OfficialEditorialSection markdown={officialEditorial.editorial} />
        )}
      </article>
    </div>
  );
}

function removeGeeksforGeeksReference(markdown: string): string {
  return markdown
    .replace(/\n?##\s+GeeksforGeeks Reference\s*\n[\s\S]*?(?=\n##\s+|\n#\s+|$)/gi, '\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

type OfficialEditorialSplit = {
  before: string;
  editorial: string;
};

function splitCodeChefOfficialEditorial(markdown: string): OfficialEditorialSplit | null {
  const match = markdown.match(
    /<details\s+class="codechef-official-editorial">\s*<summary>\s*Official Editorial\s*<\/summary>\s*([\s\S]*?)\s*<\/details>/i,
  );
  if (!match || match.index === undefined) return null;
  return {
    before: markdown.slice(0, match.index).trim(),
    editorial: match[1].trim(),
  };
}

function OfficialEditorialSection({ markdown }: { markdown: string }) {
  const [open, setOpen] = useState(false);

  return (
    <section className="my-6 text-coden-text">
      <button
        type="button"
        onClick={() => setOpen((value) => !value)}
        className="flex w-full items-center gap-2 border-b border-coden-border pb-2 text-left text-lg font-semibold text-coden-text hover:text-coden-accent transition-colors"
        aria-expanded={open}
      >
        <span className="text-[10px]">{open ? '▼' : '▶'}</span>
        <span>Official Editorial</span>
      </button>
      {open && (
        <div className="pt-4 text-sm text-coden-text">
          <ReactMarkdown
            remarkPlugins={[remarkGfm, remarkMath]}
            rehypePlugins={[rehypeRaw, rehypeKatex]}
            components={{
              pre: ({ children, ...props }) => (
                <pre
                  {...props}
                  className="bg-white border border-slate-300 rounded p-3 text-xs text-slate-950 shadow-sm overflow-x-auto my-3 dark:bg-coden-bg dark:border-coden-border dark:text-coden-text"
                >
                  {children}
                </pre>
              ),
              code: ({ className, children, ...props }) => {
                const isBlock = String(children).includes('\n');
                return isBlock ? (
                  <code {...props} className={className}>
                    {children}
                  </code>
                ) : (
                  <code
                    {...props}
                    className="bg-sky-50 border border-sky-200 rounded px-1 py-0.5 text-sky-800 text-xs dark:bg-coden-bg dark:border-coden-border dark:text-coden-accent"
                  >
                    {children}
                  </code>
                );
              },
            }}
          >
            {markdown}
          </ReactMarkdown>
        </div>
      )}
    </section>
  );
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
          : 'my-3 rounded border border-coden-border bg-coden-bg/40 text-coden-text'
      }
    >
      <summary
        className={
          isOfficialEditorial
            ? 'cursor-pointer select-none border-b border-coden-border pb-2 text-lg font-semibold text-coden-text hover:text-coden-accent transition-colors'
            : 'cursor-pointer select-none px-3 py-2 text-sm font-semibold text-coden-accent hover:bg-coden-border/40 transition-colors'
        }
      >
        {summary}
      </summary>
      <div
        className={
          isOfficialEditorial
            ? 'pt-4 text-sm text-coden-text'
            : 'border-t border-coden-border px-3 py-2 text-sm text-coden-text'
        }
      >
        {body}
      </div>
    </details>
  );
}

function LeetCodeReference({
  detail,
  question,
}: {
  detail: NonNullable<ReturnType<typeof useAppStore.getState>['currentDetail']>;
  question: LeetCodeQuestion | null;
}) {
  const title = question?.title || detail.leetcode_title || detail.name;
  const idPrefix = question?.frontend_id ? `${question.frontend_id}. ` : '';

  return (
    <section className="mx-4 mt-4 rounded-lg border border-coden-border bg-coden-bg p-4 shadow-sm">
      <div className="text-xs uppercase tracking-wide text-coden-muted font-semibold">
        LeetCode Reference
      </div>
      <a
        href={detail.leetcode_url}
        target="_blank"
        rel="noreferrer"
        className="mt-1 inline-flex items-center gap-1 text-sm font-semibold text-coden-accent hover:underline"
      >
        {idPrefix}{title} ↗
      </a>
    </section>
  );
}
