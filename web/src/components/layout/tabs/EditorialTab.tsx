import { Children, isValidElement, useEffect, useState, useMemo, type ReactNode } from 'react';
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

  const tocHeadings = useMemo(() => {
    if (loadState.kind !== 'ready') return [];
    return extractTocHeadings(loadState.markdown);
  }, [loadState]);

  const estimatedReadTime = useMemo(() => {
    if (loadState.kind !== 'ready') return 3;
    const words = loadState.markdown.split(/\s+/).length;
    return Math.max(1, Math.round(words / 200));
  }, [loadState]);

  if (loadState.kind === 'loading') {
    return (
      <div className="flex min-h-64 items-center justify-center p-8 text-sm text-coden-muted">
        <div className="flex flex-col items-center gap-2">
          <div className="h-6 w-6 animate-spin rounded-full border-2 border-coden-accent border-t-transparent" />
          <span>Loading editorial...</span>
        </div>
      </div>
    );
  }

  if (loadState.kind === 'error') {
    return (
      <div role="alert" className="min-h-64 rounded-xl border border-coden-border bg-coden-surface p-6 shadow-sm">
        <div className="text-sm font-semibold text-red-400">Editorial unavailable</div>
        <div className="mt-2 text-xs text-coden-muted">{loadState.message}</div>
      </div>
    );
  }

  const markdown = loadState.markdown;

  if (!markdown.trim()) {
    return (
      <div role="status" className="flex min-h-64 items-center justify-center p-8 text-sm text-coden-muted">
        No editorial is available for this challenge.
      </div>
    );
  }

  const scrollToHeading = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <div className="coden-reading-container">
      {/* Editorial Header Banner */}
      <div className="coden-hero-banner">
        <div className="flex flex-wrap items-center justify-between gap-3 border-b border-coden-border/70 pb-3.5 mb-3.5">
          <div className="flex items-center gap-2.5">
            <span className="flex h-8 w-8 items-center justify-center rounded-xl bg-amber-500/15 text-sm font-bold text-amber-500 shadow-xs">
              📖
            </span>
            <div>
              <h1 className="text-xl font-extrabold text-coden-text m-0 tracking-tight">
                {`Editorial: ${detail?.name ?? challengeId}`}
              </h1>
              <span className="text-xs text-coden-muted">In-depth mathematical & algorithmic walkthrough</span>
            </div>
          </div>
          <span className="inline-flex items-center gap-1.5 rounded-full bg-amber-500/15 text-amber-600 dark:text-amber-400 px-3 py-1 text-xs font-semibold border border-amber-500/30 font-mono">
            <span>⏱️</span> ~{estimatedReadTime} min read
          </span>
        </div>

        {/* Quick Jump Navigation */}
        {tocHeadings.length > 1 && (
          <div className="flex flex-wrap items-center gap-2 pt-0.5">
            <span className="text-xs font-semibold text-coden-muted mr-1">Sections:</span>
            {tocHeadings.map((h, idx) => (
              <button
                key={h.id}
                type="button"
                onClick={() => scrollToHeading(h.id)}
                className="group inline-flex items-center gap-1.5 rounded-full border border-coden-border bg-coden-surface px-3 py-1 text-xs font-semibold text-coden-text hover:border-amber-500 hover:text-amber-500 hover:shadow-xs transition-all"
              >
                <span className="flex h-4 w-4 items-center justify-center rounded-full bg-amber-500/20 text-[10px] font-bold text-amber-500 group-hover:bg-amber-500 group-hover:text-white transition-colors">
                  {idx + 1}
                </span>
                <span>{h.title}</span>
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Main Editorial Article */}
      <article className="prose prose-sm max-w-none text-coden-text
                          prose-headings:text-coden-text prose-headings:scroll-mt-6
                          prose-h2:text-lg prose-h2:font-bold prose-h2:mt-8 prose-h2:mb-3 prose-h2:border-b prose-h2:border-coden-border prose-h2:pb-2
                          prose-h3:text-base prose-h3:font-semibold prose-h3:mt-6 prose-h3:mb-2
                          prose-p:leading-7 prose-p:my-3.5 prose-p:text-coden-text
                          prose-li:my-1 prose-li:text-coden-text
                          prose-strong:text-coden-text prose-strong:font-semibold
                          prose-em:text-coden-text
                          prose-a:text-coden-accent prose-a:font-medium hover:prose-a:underline
                          prose-blockquote:text-coden-text prose-blockquote:border-coden-accent prose-blockquote:bg-coden-surface-elevated/40 prose-blockquote:rounded-r-lg prose-blockquote:py-1 prose-blockquote:px-4
                          prose-code:before:content-none prose-code:after:content-none prose-code:text-coden-accent prose-code:font-mono
                          prose-pre:my-4 prose-pre:overflow-x-auto prose-pre:rounded-lg prose-pre:border prose-pre:border-coden-border prose-pre:bg-coden-surface-elevated prose-pre:text-coden-text">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeRaw, rehypeKatex]}
          components={{
            h2: ({ node, ...props }) => {
              const title = textFromReactNode(props.children);
              const id = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              const approachMatch = /^Approach\s+(\d+|[A-Za-z]+)[:\-]?\s*(.*)$/i.exec(title.trim());
              return (
                <div id={id} className="mt-10 mb-4">
                  {approachMatch ? (
                    <div className="flex items-center gap-3 border-b border-coden-border pb-2.5">
                      <span className="coden-step-badge bg-gradient-to-r from-amber-500 to-indigo-500 text-white">
                        Approach {approachMatch[1]}
                      </span>
                      <h2 {...props} className="text-lg font-bold text-coden-text m-0 border-0 p-0">
                        {approachMatch[2] || `Approach ${approachMatch[1]}`}
                      </h2>
                    </div>
                  ) : (
                    <h2 {...props} className="text-lg font-bold text-coden-text border-b border-coden-border pb-2.5" />
                  )}
                </div>
              );
            },
            h3: ({ node, ...props }) => (
              <h3 {...props} className="text-base font-semibold mt-6 mb-2 text-coden-text" />
            ),
            blockquote: ({ children }) => {
              const rawText = textFromReactNode(children).trim();
              let calloutClass = 'coden-callout-note';
              let badge = 'NOTE';
              if (/^\[!TIP\]/i.test(rawText) || /^Tip:/i.test(rawText)) {
                calloutClass = 'coden-callout-tip';
                badge = 'TIP';
              } else if (/^\[!WARNING\]/i.test(rawText) || /^Warning:/i.test(rawText)) {
                calloutClass = 'coden-callout-warning';
                badge = 'WARNING';
              } else if (/^\[!IMPORTANT\]/i.test(rawText) || /^Important:/i.test(rawText)) {
                calloutClass = 'coden-callout-important';
                badge = 'IMPORTANT';
              } else if (/^\[!CAUTION\]/i.test(rawText) || /^Caution:/i.test(rawText)) {
                calloutClass = 'coden-callout-caution';
                badge = 'CAUTION';
              }
              return (
                <div className={`coden-callout ${calloutClass} not-prose text-sm text-coden-text my-4`}>
                  <div className="text-[11px] font-bold tracking-wider text-amber-500 mb-1 uppercase">
                    {badge}
                  </div>
                  <div>{children}</div>
                </div>
              );
            },
            details: ({ node, ...props }) => (
              <details
                {...props}
                className="my-4 overflow-hidden rounded-lg border border-coden-border bg-coden-surface-elevated/40 text-coden-text"
              />
            ),
            summary: ({ node, ...props }) => (
              <summary
                {...props}
                className="cursor-pointer select-none px-4 py-2.5 text-sm font-semibold text-coden-accent hover:bg-coden-border/40 transition-colors"
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
                className="mx-auto my-6 max-h-[560px] max-w-full rounded-lg border border-coden-border bg-coden-bg object-contain shadow-sm"
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
              return <pre {...props} className="my-4 overflow-x-auto rounded-lg border border-coden-border bg-coden-surface-elevated p-3.5 text-xs text-coden-text">{children}</pre>;
            },
            code: ({ className, children, ...props }) => {
              const isBlock = String(children).includes('\n');
              if (isBlock) {
                return <code {...props} className={className}>{children}</code>;
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
            table: ({ node, ...props }) => (
              <div className="my-4 overflow-x-auto rounded-lg border border-coden-border bg-coden-surface shadow-sm">
                <table
                  {...props}
                  className="my-0 w-full min-w-full table-auto border-collapse text-xs text-coden-text"
                />
              </div>
            ),
            th: ({ node, ...props }) => (
              <th
                {...props}
                className="border-b border-coden-border px-3 py-2.5 bg-coden-surface-elevated font-semibold text-coden-text text-left"
              />
            ),
            td: ({ node, ...props }) => (
              <td
                {...props}
                className="border-b border-coden-border/60 px-3 py-2 text-coden-text align-top"
              />
            ),
          }}
        >
          {markdown}
        </ReactMarkdown>
      </article>
    </div>
  );
}

function extractTocHeadings(markdown: string): Array<{ id: string; title: string }> {
  const headings: Array<{ id: string; title: string }> = [];
  const lines = markdown.split(/\r?\n/);
  for (const line of lines) {
    const match = /^##\s+(.+)$/.exec(line);
    if (match) {
      const title = match[1].replace(/[*_`]/g, '').trim();
      const id = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
      if (id) {
        headings.push({ id, title });
      }
    }
  }
  return headings;
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

function textFromReactNode(node: ReactNode): string {
  return reactNodeText(node);
}

function editorialAssetUrl(challengeId: string, src: string): string {
  if (!src || /^(?:[a-z]+:|\/|#)/i.test(src)) return src;
  const relative = src.replace(/^\.\//, '').replace(/^assets\//, '');
  const encoded = relative.split('/').map(encodeURIComponent).join('/');
  return `/api/docs/by-id/${encodeURIComponent(challengeId)}/assets/${encoded}`;
}
