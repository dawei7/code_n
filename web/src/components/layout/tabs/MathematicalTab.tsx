import { useEffect, useState, useCallback } from 'react';
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

const CACHE: Map<string, string> = new Map();

export function MathematicalTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const language = useAppStore((s) => s.language);
  const [state, setState] = useState<LoadState>({ kind: 'idle' });

  const challengeId = detail?.id ?? null;
  const challengeName = detail?.name ?? null;
  const category = detail?.category ?? null;

  const load = useCallback(async (id?: string) => {
    setState({ kind: 'loading' });
    try {
      if (!id) {
        setState({ kind: 'idle' });
        return;
      }
      const cached = CACHE.get(id);
      if (cached !== undefined) {
        setState({ kind: 'loaded', markdown: cached });
        return;
      }
      const res = await fetch(`/api/math/by-id/${encodeURIComponent(id)}?lang=${language}`);
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
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      setState({ kind: 'error', message });
    }
  }, [language]);

  useEffect(() => {
    if (!challengeId) {
      setState({ kind: 'idle' });
      return;
    }
    setState({ kind: 'loading' });
    void load(challengeId).then(() => {
      if (challengeName && category) {
        setState((prev) =>
          prev.kind === 'missing'
            ? { ...prev, challengeName, category }
            : prev
        );
      }
    });
  }, [challengeId, challengeName, category, language, load]);

  if (state.kind === 'idle' || state.kind === 'loading') {
    return (
      <div className="flex items-center justify-center text-xs text-coden-muted">
        Loading mathematical theory…
      </div>
    );
  }

  if (state.kind === 'error') {
    return (
      <div className="flex flex-col items-center justify-center gap-2 text-xs">
        <div className="text-red-400">Failed to load math doc:</div>
        <pre className="text-coden-muted whitespace-pre-wrap">{state.message}</pre>
        <button
          type="button"
          onClick={() => challengeId && load(challengeId)}
          className="mt-2 px-3 py-1 text-sm rounded border border-coden-border hover:bg-coden-surface"
        >
          Retry
        </button>
      </div>
    );
  }

  if (state.kind === 'missing') {
    const issueTitle = encodeURIComponent(`Docs: add math theory for ${state.challengeId}`);
    const issueBody = encodeURIComponent(
      `The mathematical reference doc for **${state.challengeId}** (\`${state.challengeName}\`, category: ${state.category}) doesn't exist yet.\n\n` +
      `Please add one at \`docs/mathematical/${state.category}/${state.challengeId}_<slug>.md\`.`,
    );
    return (
      <div className="flex flex-col items-center justify-center gap-3 text-xs text-coden-muted">
        <div className="text-base font-semibold text-coden-text">
          No formal mathematical documentation yet for <code className="text-coden-accent">{state.challengeId}</code>
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

  return (
    <div>
      <article className="prose prose-invert prose-sm max-w-none p-4
                          prose-headings:text-coden-text
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
            a: ({ node, ...props }) => <a {...props} target="_blank" rel="noreferrer" />,
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
              const isBlock = String(children).includes('\n');
              if (isBlock) {
                return <code {...props} className={className}>{children}</code>;
              }
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
