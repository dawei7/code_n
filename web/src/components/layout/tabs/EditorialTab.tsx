import { Children, isValidElement, useEffect, useState, type ReactNode } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import 'katex/dist/katex.min.css';

import { getEditorial } from '../../../api/editorials';
import { useAppStore } from '../../../store/useAppStore';
import {
  MermaidDiagram,
  mermaidSourceFromPreChildren,
} from '../../markdown/MermaidDiagram';
import { EditorialCodeBlock } from '../../markdown/EditorialCodeBlock';
import { EditorialFrame } from '../../markdown/EditorialFrame';


type LoadState =
  | { kind: 'loading' }
  | { kind: 'error'; message: string }
  | { kind: 'ready'; markdown: string };

const CACHE = new Map<string, string>();


export function EditorialTab() {
  const detail = useAppStore((state) => state.currentDetail);
  const theme = useAppStore((state) => state.theme);
  const challengeId = detail?.id ?? '';
  const [loadState, setLoadState] = useState<LoadState>({ kind: 'loading' });

  useEffect(() => {
    let cancelled = false;
    const cached = CACHE.get(challengeId);
    if (cached !== undefined) {
      setLoadState({ kind: 'ready', markdown: cached });
      return () => {
        cancelled = true;
      };
    }

    setLoadState({ kind: 'loading' });
    void getEditorial(challengeId)
      .then((markdown) => {
        if (cancelled) return;
        CACHE.set(challengeId, markdown);
        setLoadState({ kind: 'ready', markdown });
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setLoadState({
            kind: 'error',
            message: error instanceof Error ? error.message : 'The editorial could not be loaded.',
          });
        }
      });
    return () => {
      cancelled = true;
    };
  }, [challengeId]);

  if (loadState.kind === 'loading') {
    return (
      <div className="flex min-h-64 items-center justify-center p-6 text-sm text-coden-muted">
        Loading editorial...
      </div>
    );
  }

  if (loadState.kind === 'error') {
    return (
      <div role="alert" className="min-h-64 border border-coden-swap/50 p-6">
        <div className="text-sm font-semibold text-coden-text">Editorial unavailable</div>
        <div className="mt-2 text-xs text-coden-muted">{loadState.message}</div>
      </div>
    );
  }

  const markdown = loadState.markdown;

  if (!markdown.trim()) {
    return (
      <div role="status" className="flex min-h-64 items-center justify-center p-6 text-sm text-coden-muted">
        No editorial is available for this challenge.
      </div>
    );
  }

  return (
    <article className="prose prose-sm mx-auto max-w-6xl px-6 py-7 text-coden-text
                        prose-headings:text-coden-text prose-headings:scroll-mt-4
                        prose-h1:mb-4 prose-h1:text-2xl prose-h1:font-semibold
                        prose-h2:mb-3 prose-h2:mt-8 prose-h2:border-b prose-h2:border-coden-border prose-h2:pb-2 prose-h2:text-lg
                        prose-h3:mb-2 prose-h3:mt-6 prose-h3:text-base
                        prose-p:leading-7 prose-p:text-coden-text
                        prose-li:my-1 prose-li:text-coden-text
                        prose-strong:text-coden-text prose-em:text-coden-text
                        prose-a:text-coden-accent
                        prose-blockquote:border-coden-accent prose-blockquote:bg-coden-bg prose-blockquote:px-4 prose-blockquote:py-1 prose-blockquote:not-italic prose-blockquote:text-coden-text
                        prose-code:before:content-none prose-code:after:content-none prose-code:text-coden-accent
                        prose-pre:my-4 prose-pre:overflow-x-auto prose-pre:rounded prose-pre:border prose-pre:border-coden-border prose-pre:bg-coden-bg prose-pre:text-coden-text">
      <h1>{`Editorial: ${detail?.name ?? challengeId}`}</h1>
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeRaw, rehypeKatex]}
        components={{
          details: ({ node, ...props }) => (
            <details
              {...props}
              className="my-3 overflow-hidden rounded border border-coden-border bg-coden-bg/40 text-coden-text"
            />
          ),
          summary: ({ node, ...props }) => (
            <summary
              {...props}
              className="cursor-pointer select-none px-3 py-2 text-sm font-semibold text-coden-accent hover:bg-coden-border/40"
            />
          ),
          a: ({ node, ...props }) => <a {...props} target="_blank" rel="noreferrer" />,
          iframe: ({ node, ...props }) => (
            <EditorialFrame
              {...props}
              leetcodeUrl={detail?.leetcode_url ?? ''}
            />
          ),
          img: ({ node, ...props }) => (
            <img
              {...props}
              src={editorialAssetUrl(challengeId, String(props.src || ''))}
              className="mx-auto my-5 max-h-[560px] max-w-full rounded border border-coden-border bg-coden-bg object-contain"
            />
          ),
          pre: ({ children, ...props }) => {
            const diagram = mermaidSourceFromPreChildren(children);
            if (diagram) return <MermaidDiagram source={diagram} />;
            const codeBlock = editorialCodeFromPreChildren(children);
            if (codeBlock) {
              return (
                <EditorialCodeBlock
                  challengeId={challengeId}
                  language={codeBlock.language}
                  source={codeBlock.source}
                  theme={theme}
                />
              );
            }
            return <pre {...props}>{children}</pre>;
          },
          table: ({ node, ...props }) => (
            <div className="my-4 overflow-x-auto">
              <table
                {...props}
                className="my-0 min-w-full table-auto border-collapse text-sm"
              />
            </div>
          ),
          th: ({ node, ...props }) => (
            <th
              {...props}
              className="border border-coden-border bg-coden-bg px-3 py-2 text-left font-semibold text-coden-text"
            />
          ),
          td: ({ node, ...props }) => (
            <td
              {...props}
              className="border border-coden-border px-3 py-2 align-top text-coden-text"
            />
          ),
        }}
      >
        {markdown}
      </ReactMarkdown>
    </article>
  );
}


function editorialCodeFromPreChildren(children: ReactNode): { language: string; source: string } | null {
  const codeElement = Children.toArray(children).find((child) => (
    isValidElement(child) && child.type === 'code'
  ));
  if (!isValidElement<{ className?: string; children?: ReactNode }>(codeElement)) return null;

  const className = codeElement.props.className ?? '';
  const language = /(?:^|\s)language-([^\s]+)/.exec(className)?.[1] ?? '';
  const source = reactNodeText(codeElement.props.children).replace(/\r?\n$/, '');
  if (!source) return null;
  return { language, source };
}


function reactNodeText(node: ReactNode): string {
  if (typeof node === 'string' || typeof node === 'number') return String(node);
  if (Array.isArray(node)) return node.map(reactNodeText).join('');
  if (isValidElement<{ children?: ReactNode }>(node)) return reactNodeText(node.props.children);
  return '';
}


function editorialAssetUrl(challengeId: string, src: string): string {
  if (!src || /^(?:[a-z]+:|\/|#)/i.test(src)) return src;
  const relative = src.replace(/^\.\//, '').replace(/^assets\//, '');
  const encoded = relative.split('/').map(encodeURIComponent).join('/');
  return `/api/docs/by-id/${encodeURIComponent(challengeId)}/assets/${encoded}`;
}
