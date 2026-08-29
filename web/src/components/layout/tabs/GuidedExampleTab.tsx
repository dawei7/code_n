import { useEffect, useState, useMemo } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import 'katex/dist/katex.min.css';

import { getGuidedExample } from '../../../api/guidedExamples';
import {
  MermaidDiagram,
  mermaidSourceFromPreChildren,
} from '../../markdown/MermaidDiagram';
import { useAppStore } from '../../../store/useAppStore';


type LoadState =
  | { kind: 'loading' }
  | { kind: 'error'; message: string }
  | { kind: 'ready'; markdown: string };

const CACHE = new Map<string, string>();


export function GuidedExampleTab() {
  const detail = useAppStore((state) => state.currentDetail);
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
    void getGuidedExample(challengeId)
      .then((markdown) => {
        if (cancelled) return;
        CACHE.set(challengeId, markdown);
        setLoadState({ kind: 'ready', markdown });
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setLoadState({
            kind: 'error',
            message: error instanceof Error ? error.message : 'The guided example could not be loaded.',
          });
        }
      });
    return () => {
      cancelled = true;
    };
  }, [challengeId]);

  const guidedSteps = useMemo(() => {
    if (loadState.kind !== 'ready') return [];
    return extractGuidedSteps(loadState.markdown);
  }, [loadState]);

  if (loadState.kind === 'loading') {
    return (
      <div className="flex min-h-64 items-center justify-center p-8 text-sm text-coden-muted">
        <div className="flex flex-col items-center gap-2">
          <div className="h-6 w-6 animate-spin rounded-full border-2 border-coden-accent border-t-transparent" />
          <span>Loading guided walkthrough...</span>
        </div>
      </div>
    );
  }

  if (loadState.kind === 'error') {
    return (
      <div role="alert" className="min-h-64 rounded-xl border border-coden-border bg-coden-surface p-6 shadow-sm">
        <div className="text-sm font-semibold text-red-400">Guided example unavailable</div>
        <div className="mt-2 text-xs text-coden-muted">{loadState.message}</div>
      </div>
    );
  }

  const scrollToStep = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <div className="coden-reading-container">
      {/* Lesson Header Banner */}
      <div className="coden-hero-banner">
        <div className="flex flex-wrap items-center justify-between gap-3 border-b border-coden-border/70 pb-3.5 mb-3.5">
          <div className="flex items-center gap-2.5">
            <span className="flex h-8 w-8 items-center justify-center rounded-xl bg-indigo-500/15 text-sm font-bold text-indigo-500 shadow-xs">
              🎓
            </span>
            <div>
              <h1 className="text-xl font-extrabold text-coden-text m-0 tracking-tight">
                {`Guided Example: ${detail?.name ?? challengeId}`}
              </h1>
              <span className="text-xs text-coden-muted">Step-by-step code-free pedagogical walkthrough of representative input</span>
            </div>
          </div>
          {guidedSteps.length > 0 && (
            <span className="inline-flex items-center gap-1 rounded-full bg-indigo-500/15 text-indigo-600 dark:text-indigo-400 px-3 py-1 text-xs font-semibold border border-indigo-500/30 font-mono">
              <span>🎯</span> {guidedSteps.length} {guidedSteps.length === 1 ? 'Step' : 'Interactive Steps'}
            </span>
          )}
        </div>

        {/* Step Jump Pills */}
        {guidedSteps.length > 1 && (
          <div className="flex flex-wrap items-center gap-2 pt-0.5">
            <span className="text-xs font-semibold text-coden-muted mr-1">Steps:</span>
            {guidedSteps.map((s, idx) => (
              <button
                key={s.id}
                type="button"
                onClick={() => scrollToStep(s.id)}
                className="group inline-flex items-center gap-1.5 rounded-full border border-coden-border bg-coden-surface px-3 py-1 text-xs font-semibold text-coden-text hover:border-indigo-500 hover:text-indigo-500 hover:shadow-xs transition-all"
              >
                <span className="flex h-4 w-4 items-center justify-center rounded-full bg-indigo-500/20 text-[10px] font-bold text-indigo-500 group-hover:bg-indigo-500 group-hover:text-white transition-colors">
                  {s.stepNumber || idx + 1}
                </span>
                <span>{s.stepNumber ? `Step ${s.stepNumber}` : s.title}</span>
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Main Walkthrough Article */}
      <article className="prose prose-base max-w-none text-coden-text text-[16px] leading-relaxed
                          prose-headings:text-coden-text prose-headings:tracking-tight
                          prose-h1:text-2xl prose-h1:font-extrabold prose-h1:mt-0 prose-h1:mb-4
                          prose-h2:text-xl prose-h2:font-bold prose-h2:mt-8 prose-h2:mb-3
                          prose-h3:text-lg prose-h3:font-semibold prose-h3:mt-6 prose-h3:mb-2
                          prose-h4:text-base prose-h4:font-semibold prose-h4:mt-4 prose-h4:mb-2
                          prose-p:text-[16px] prose-p:leading-relaxed prose-p:my-4 prose-p:text-coden-text
                          prose-li:text-[16px] prose-li:leading-relaxed prose-li:my-1.5 prose-li:text-coden-text
                          prose-strong:text-coden-text prose-strong:font-semibold
                          prose-em:text-coden-text
                          prose-hr:border-coden-border prose-hr:my-6
                          prose-a:text-coden-accent prose-a:font-medium hover:prose-a:underline
                          prose-code:text-coden-accent prose-code:font-mono
                          prose-code:before:content-none prose-code:after:content-none
                          prose-pre:my-4 prose-pre:overflow-x-auto prose-pre:rounded-lg prose-pre:border prose-pre:border-coden-border prose-pre:bg-coden-surface-elevated prose-pre:text-coden-text">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkMath]}
          rehypePlugins={[rehypeRaw, rehypeKatex]}
          components={{
            h2: ({ node, ...props }) => {
              const text = textFromReactNode(props.children);
              const id = text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
              const stepMatch = /^Step\s+(\d+|[A-Za-z]+)[:\-]?\s*(.*)$/i.exec(text.trim());
              return (
                <div id={id} className="mt-10 mb-4">
                  {stepMatch ? (
                    <div className="flex items-center gap-3 border-b border-coden-border pb-2.5">
                      <span className="coden-step-badge">Step {stepMatch[1]}</span>
                      <h2 {...props} className="text-xl font-bold text-coden-text m-0 border-0 p-0" />
                    </div>
                  ) : (
                    <h2 {...props} className="text-xl font-bold text-coden-text border-b border-coden-border pb-2.5" />
                  )}
                </div>
              );
            },
            h3: ({ node, ...props }) => (
              <h3 {...props} className="text-lg font-semibold mt-6 mb-2 text-coden-text" />
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
                  <div className="text-[11px] font-bold tracking-wider text-indigo-500 mb-1 uppercase">
                    {badge}
                  </div>
                  <div>{children}</div>
                </div>
              );
            },
            img: ({ node, ...props }) => (
              <img
                {...props}
                src={guidedExampleAssetUrl(challengeId, String(props.src || ''))}
                className="mx-auto my-6 max-h-[560px] max-w-full rounded-lg border border-coden-border bg-coden-bg object-contain shadow-sm"
              />
            ),
            pre: ({ children, ...props }) => {
              const diagram = mermaidSourceFromPreChildren(children);
              if (diagram) return <MermaidDiagram source={diagram} />;
              return (
                <pre {...props} aria-label="Worked-example diagram" className="my-4 overflow-x-auto rounded-lg border border-coden-border bg-coden-surface-elevated p-3.5 text-xs text-coden-text">
                  {children}
                </pre>
              );
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
          {loadState.markdown}
        </ReactMarkdown>
      </article>
    </div>
  );
}

function extractGuidedSteps(markdown: string): Array<{ id: string; title: string; stepNumber: string }> {
  const steps: Array<{ id: string; title: string; stepNumber: string }> = [];
  const lines = markdown.split(/\r?\n/);
  for (const line of lines) {
    const match = /^##\s+(.+)$/.exec(line);
    if (match) {
      const full = match[1].replace(/[*_`]/g, '').trim();
      const id = full.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
      const stepMatch = /^Step\s+(\d+|[A-Za-z]+)/i.exec(full);
      const stepNumber = stepMatch ? stepMatch[1] : '';
      if (id) {
        steps.push({ id, title: full, stepNumber });
      }
    }
  }
  return steps;
}

function textFromReactNode(node: any): string {
  if (typeof node === 'string' || typeof node === 'number') return String(node);
  if (Array.isArray(node)) return node.map(textFromReactNode).join('');
  if (node && typeof node === 'object' && node.props) {
    return textFromReactNode(node.props.children);
  }
  return '';
}

function guidedExampleAssetUrl(challengeId: string, src: string): string {
  if (!src || /^(?:[a-z]+:|\/|#)/i.test(src)) return src;
  const relative = src.replace(/^\.\//, '').replace(/^assets\//, '');
  const encoded = relative.split('/').map(encodeURIComponent).join('/');
  return `/api/docs/by-id/${encodeURIComponent(challengeId)}/assets/${encoded}`;
}
