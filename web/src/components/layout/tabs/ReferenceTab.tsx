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
import { useEffect, useState, useCallback } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

import { useAppStore } from '../../../store/useAppStore';


type LoadState =
  | { kind: 'idle' }
  | { kind: 'loading' }
  | { kind: 'loaded'; markdown: string }
  | { kind: 'missing'; challengeId: string; challengeName: string; category: string }
  | { kind: 'error'; message: string };


const CACHE: Map<string, string> = new Map();
let OVERVIEW_CACHE: string | null = null;


export function ReferenceTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const [state, setState] = useState<LoadState>({ kind: 'idle' });

  const challengeId = detail?.id ?? null;
  const challengeName = detail?.name ?? null;
  const category = detail?.category ?? null;

  const load = useCallback(async (which: 'overview' | 'by-id', id?: string) => {
    setState({ kind: 'loading' });
    try {
      if (which === 'overview') {
        if (OVERVIEW_CACHE !== null) {
          setState({ kind: 'loaded', markdown: OVERVIEW_CACHE });
          return;
        }
        const res = await fetch('/api/docs/overview');
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
        const res = await fetch(`/api/docs/by-id/${encodeURIComponent(id)}`);
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
  }, []);

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
  }, [challengeId, challengeName, category, load]);

  if (state.kind === 'idle' || state.kind === 'loading') {
    return (
      <div className="h-full flex items-center justify-center text-xs text-coden-muted">
        Loading reference…
      </div>
    );
  }

  if (state.kind === 'error') {
    return (
      <div className="h-full flex flex-col items-center justify-center gap-2 text-xs">
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
      <div className="h-full flex flex-col items-center justify-center gap-3 text-xs text-coden-muted">
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
  return (
    <div className="h-full overflow-y-auto">
      <article className="prose prose-invert prose-sm max-w-none p-4
                          prose-headings:text-coden-text
                          prose-a:text-coden-accent
                          prose-code:text-coden-accent
                          prose-code:before:content-none
                          prose-code:after:content-none
                          prose-table:my-2
                          prose-th:text-left">
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            a: ({ node, ...props }) => (
              <a {...props} target="_blank" rel="noreferrer" />
            ),
            table: ({ node, ...props }) => (
              <table {...props} className="border-collapse border border-coden-border text-xs" />
            ),
            th: ({ node, ...props }) => (
              <th {...props} className="border border-coden-border px-2 py-1 bg-coden-surface font-semibold" />
            ),
            td: ({ node, ...props }) => (
              <td {...props} className="border border-coden-border px-2 py-1" />
            ),
            pre: ({ children, ...props }) => (
              <pre
                {...props}
                className="bg-coden-bg border border-coden-border rounded p-3 text-xs overflow-x-auto my-3"
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
                  className="bg-coden-bg border border-coden-border rounded px-1 py-0.5 text-coden-accent text-xs"
                >
                  {children}
                </code>
              );
            },
          }}
        >
          {state.markdown}
        </ReactMarkdown>
      </article>
    </div>
  );
}
