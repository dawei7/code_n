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
  SolutionImplementationDetail,
  SolutionVariantDetail,
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
  const [selectedVariantId, setSelectedVariantId] = useState('');

  const challengeId = detail?.id ?? null;
  const challengeName = detail?.name ?? null;
  const category = detail?.category ?? null;

  useEffect(() => {
    setSelectedVariantId(detail?.default_solution_variant ?? '');
  }, [challengeId, detail?.default_solution_variant]);

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
        // Problem documents are authored while the app is running. Fetch them
        // whenever a challenge is opened so edits do not remain hidden behind
        // a process-wide cache keyed only by challenge ID.
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
      // No challenge: render the overview.
      void load('overview');
      return;
    }
    // Challenge changed: drop the previous state and re-fetch.
    setState({ kind: 'loading' });
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
      <div className="flex items-center justify-center text-xs text-coden-muted">
        Loading reference...
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
      `Please complete the canonical package document at \`dsa/leetcode/<frontend_id:04d>_<slug>/doc.md\`.`,
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
          className="mt-2 px-3 py-1.5 text-sm rounded border border-coden-accent text-coden-accent hover:bg-coden-accent hover:text-coden-accentContrast"
        >
          Suggest this doc on GitHub →
        </a>
      </div>
    );
  }

  // Loaded: render the markdown.
  const markdown = state.markdown;
  const { mainMarkdown, approachMarkdown } = splitApproachSection(markdown);
  const solutionVariants = challengeId ? detail?.solution_variants ?? [] : [];
  const selectedVariant = solutionVariants.find(({ id }) => id === selectedVariantId)
    ?? solutionVariants.find(({ id }) => id === detail?.default_solution_variant)
    ?? solutionVariants[0];
  const solutionSource = challengeId ? detail?.optimal_source?.trim() ?? '' : '';
  const solutionSources: Partial<Record<SupportedLanguage, string>> = {
    ...(detail?.optimal_sources ?? {}),
  };
  if (solutionSource && detail?.primary_language && !solutionSources[detail.primary_language]?.trim()) {
    solutionSources[detail.primary_language] = solutionSource;
  }
  const leetcodeSolutionSource = challengeId ? detail?.leetcode_optimal_source?.trim() ?? '' : '';
  const leetcodeSolutionSources: Partial<Record<SupportedLanguage, string>> = {
    ...(detail?.leetcode_optimal_sources ?? {}),
  };
  if (
    leetcodeSolutionSource
    && detail?.primary_language
    && !leetcodeSolutionSources[detail.primary_language]?.trim()
  ) {
    leetcodeSolutionSources[detail.primary_language] = leetcodeSolutionSource;
  }
  const hasSolution = REFERENCE_LANGUAGES.some(({ id }) => (
    Boolean(solutionSources[id]?.trim()) && Boolean(leetcodeSolutionSources[id]?.trim())
  ));
  const solutionUnlocked = challengeId
    ? canRevealSolution(completed.includes(challengeId), cheaterMode)
    : false;
  return (
    <div>
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
                    title="Open the official LeetCode description using your LeetCode Focus Mode setting"
                    aria-label="Open the official LeetCode description using your LeetCode Focus Mode setting"
                    className="inline-flex items-center justify-center text-coden-accent hover:text-coden-text"
                  >
                    <LeetCodeIcon />
                  </a>
                );
              }
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
            img: ({ node, ...props }) => {
              const rawSrc = String(props.src || '');
              const src = challengeId?.startsWith('lc_')
                ? leetcodeAssetUrl(challengeId, rawSrc)
                : rawSrc;
              return (
                <img
                  {...props}
                  src={src}
                  className="my-4 max-h-[520px] max-w-full rounded-md border border-coden-border bg-coden-bg object-contain"
                />
              );
            },
            pre: ({ children, ...props }) => {
              const diagram = mermaidSourceFromPreChildren(children);
              if (diagram) return <MermaidDiagram source={diagram} />;
              return (
                <pre
                  {...props}
                  className="bg-white border border-slate-300 rounded p-3 text-xs text-slate-950 shadow-sm overflow-x-auto my-3 dark:bg-coden-bg dark:border-coden-border dark:text-coden-text"
                >
                  {children}
                </pre>
              );
            },
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
          {mainMarkdown}
        </ReactMarkdown>
        {selectedVariant && (
          <SolutionVariantPanel
            challengeId={challengeId ?? ''}
            variants={solutionVariants}
            selectedVariant={selectedVariant}
            onSelect={setSelectedVariantId}
            unlocked={solutionUnlocked}
            effectiveElo={detail?.solution_variant_effective_elo ?? null}
            eloSource={detail?.solution_variant_elo_source ?? ''}
            simplifiedEloCeiling={detail?.simplified_solution_elo_ceiling ?? null}
          />
        )}
        {!selectedVariant && approachMarkdown && (
          <ApproachDisclosure
            key={challengeId ?? 'overview'}
            markdown={approachMarkdown}
          />
        )}
        {!selectedVariant && hasSolution && challengeId && (
          <SolutionDisclosure
            key={`solution:${challengeId}`}
            challengeId={challengeId}
            variantId="optimal"
            sources={solutionSources}
            leetcodeSources={leetcodeSolutionSources}
            unlocked={solutionUnlocked}
          />
        )}
      </article>
    </div>
  );
}

function SolutionVariantPanel({
  challengeId,
  variants,
  selectedVariant,
  onSelect,
  unlocked,
  effectiveElo,
  eloSource,
  simplifiedEloCeiling,
}: {
  challengeId: string;
  variants: SolutionVariantDetail[];
  selectedVariant: SolutionVariantDetail;
  onSelect: (variantId: string) => void;
  unlocked: boolean;
  effectiveElo: number | null;
  eloSource: string;
  simplifiedEloCeiling: number | null;
}) {
  const eloLabel = eloSource === 'elo_rating' ? 'Real Elo' : 'Estimated Elo';
  return (
    <section className="not-prose my-5">
      <div
        data-pdf-exclude="true"
        role="tablist"
        aria-label="Solution approach"
        className="flex gap-1 border-b border-coden-border"
      >
        {variants.map((variant) => {
          const selected = variant.id === selectedVariant.id;
          return (
            <button
              key={variant.id}
              id={`solution-variant-tab-${variant.id}`}
              type="button"
              role="tab"
              aria-selected={selected}
              aria-controls={`solution-variant-panel-${variant.id}`}
              onClick={() => onSelect(variant.id)}
              className={`-mb-px rounded-t border px-4 py-2 text-sm font-semibold transition-colors ${
                selected
                  ? 'border-coden-border border-b-coden-surface bg-coden-surface text-coden-accent'
                  : 'border-transparent text-coden-muted hover:border-coden-border hover:text-coden-text'
              }`}
            >
              {variant.label}
            </button>
          );
        })}
      </div>
      <div
        id={`solution-variant-panel-${selectedVariant.id}`}
        role="tabpanel"
        aria-labelledby={`solution-variant-tab-${selectedVariant.id}`}
        className="rounded-b border border-t-0 border-coden-border bg-coden-surface/40 p-3"
      >
        <p className="m-0 text-sm leading-6 text-coden-text">{selectedVariant.summary}</p>
        <VariantRequiredComplexity variant={selectedVariant} />
        {selectedVariant.kind === 'simplified'
          && effectiveElo !== null
          && simplifiedEloCeiling !== null && (
            <p className="mt-2 text-xs text-coden-muted">
              {eloLabel}: {Math.round(effectiveElo)} ≤ {Math.round(simplifiedEloCeiling)}
            </p>
        )}
        {selectedVariant.approach_markdown && (
          <ApproachDisclosure
            key={`approach:${challengeId}:${selectedVariant.id}`}
            markdown={selectedVariant.approach_markdown}
          />
        )}
        <SolutionDisclosure
          key={`solution:${challengeId}:${selectedVariant.id}`}
          challengeId={challengeId}
          variantId={selectedVariant.id}
          sources={selectedVariant.sources}
          leetcodeSources={selectedVariant.leetcode_sources}
          implementations={selectedVariant.implementations}
          unlocked={unlocked}
        />
      </div>
    </section>
  );
}

function VariantRequiredComplexity({ variant }: { variant: SolutionVariantDetail }) {
  const markdown = [
    '### Required Complexity',
    '',
    `- **Time:** $${variant.time_complexity}$`,
    `- **Space:** $${variant.space_complexity}$`,
  ].join('\n');
  return (
    <div className="prose prose-sm mt-4 max-w-none text-coden-text prose-headings:text-coden-text prose-li:text-coden-text prose-strong:text-coden-text">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeRaw, rehypeKatex]}
      >
        {markdown}
      </ReactMarkdown>
    </div>
  );
}

function LeetCodeIcon() {
  return (
    <FontAwesomeIcon
      icon={faLeetcode}
      aria-hidden="true"
      className="h-5 w-5 text-[#FFA116]"
    />
  );
}

function splitApproachSection(markdown: string): {
  mainMarkdown: string;
  approachMarkdown: string | null;
} {
  const opening = /<details>\s*<summary>\s*Approach\s*<\/summary>\s*/i.exec(markdown);
  if (!opening || opening.index === undefined) {
    return { mainMarkdown: markdown, approachMarkdown: null };
  }
  const bodyStart = opening.index + opening[0].length;
  const bodyEnd = markdown.indexOf('</details>', bodyStart);
  if (bodyEnd === -1) {
    return { mainMarkdown: markdown, approachMarkdown: null };
  }
  return {
    mainMarkdown: `${markdown.slice(0, opening.index)}${markdown.slice(bodyEnd + '</details>'.length)}`.trim(),
    approachMarkdown: markdown.slice(bodyStart, bodyEnd).trim(),
  };
}

function ApproachDisclosure({ markdown }: { markdown: string }) {
  const [open, setOpen] = useState(false);
  return (
    <section className="not-prose my-4 overflow-hidden rounded border border-coden-border bg-coden-bg/40">
      <button
        data-pdf-exclude="true"
        type="button"
        aria-expanded={open}
        onClick={() => setOpen((current) => !current)}
        className="flex w-full items-center gap-2 px-3 py-2 text-left text-sm font-semibold text-coden-accent hover:bg-coden-border/40 transition-colors"
      >
        <span aria-hidden="true" className="w-3 text-xs">{open ? '▼' : '▶'}</span>
        <span>Approach</span>
      </button>
      <div className={`${open ? '' : 'hidden'} coden-pdf-disclosure-content overflow-x-auto border-t border-coden-border px-4 py-3 text-sm text-coden-text`}>
          <ReactMarkdown
            remarkPlugins={[remarkGfm, remarkMath]}
            rehypePlugins={[rehypeRaw, rehypeKatex]}
            components={{
              h2: ({ node, ...props }) => (
                <h2
                  {...props}
                  className="mb-2 mt-6 first:mt-0 text-sm font-semibold text-coden-text"
                />
              ),
              h4: ({ node, ...props }) => (
                <h4
                  {...props}
                  className="mb-2 mt-6 first:mt-0 text-sm font-semibold text-coden-text"
                />
              ),
              p: ({ node, ...props }) => (
                <p {...props} className="my-2 leading-6 text-coden-text" />
              ),
              ol: ({ node, ...props }) => (
                <ol {...props} className="my-3 list-decimal space-y-1 pl-6 text-coden-text" />
              ),
              ul: ({ node, ...props }) => (
                <ul {...props} className="my-3 list-disc space-y-1.5 pl-6 text-coden-text" />
              ),
              li: ({ node, ...props }) => (
                <li {...props} className="pl-1 leading-6 text-coden-text" />
              ),
              table: ({ node, ...props }) => (
                <table
                  {...props}
                  className="my-4 w-full min-w-[640px] border-collapse text-left text-xs text-coden-text"
                />
              ),
              th: ({ node, ...props }) => (
                <th
                  {...props}
                  className="border border-coden-border bg-coden-bg px-3 py-2 font-semibold text-coden-text"
                />
              ),
              td: ({ node, ...props }) => (
                <td {...props} className="border border-coden-border px-3 py-2 text-coden-text" />
              ),
              pre: ({ children, ...props }) => {
                const diagram = mermaidSourceFromPreChildren(children);
                if (diagram) return <MermaidDiagram source={diagram} />;
                return (
                  <pre
                    {...props}
                    className="my-3 overflow-x-auto rounded border border-coden-border bg-coden-bg p-3 text-xs text-coden-text"
                  >
                    {children}
                  </pre>
                );
              },
              code: ({ className, children, ...props }) => {
                const isBlock = String(children).includes('\n');
                return isBlock ? (
                  <code {...props} className={className}>{children}</code>
                ) : (
                  <code
                    {...props}
                    className="rounded border border-coden-border bg-coden-bg px-1 py-0.5 font-mono text-xs text-coden-accent"
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
    </section>
  );
}

function SolutionDisclosure({
  challengeId,
  variantId,
  sources,
  leetcodeSources,
  implementations = [],
  unlocked,
}: {
  challengeId: string;
  variantId: string;
  sources: Partial<Record<SupportedLanguage, string>>;
  leetcodeSources: Partial<Record<SupportedLanguage, string>>;
  implementations?: SolutionImplementationDetail[];
  unlocked: boolean;
}) {
  const [open, setOpen] = useState(false);
  const theme = useAppStore((state) => state.theme);
  const resolvedImplementations: SolutionImplementationDetail[] = implementations.length > 0
    ? implementations
    : [{
        id: 'solution-1',
        label: 'Verified LeetCode submission',
        sources,
        leetcode_sources: leetcodeSources,
      }];
  const panels = resolvedImplementations.flatMap((implementation) => {
    const language = REFERENCE_LANGUAGES.find(({ id }) => (
      Boolean(implementation.sources[id]?.trim())
      || Boolean(implementation.leetcode_sources[id]?.trim())
    ));
    if (!language) return [];
    const codenSource = implementation.sources[language.id]?.trim() ?? '';
    const leetcodeSource = implementation.leetcode_sources[language.id]?.trim() ?? '';
    return [{
      id: implementation.id,
      label: implementation.label,
      language,
      source: leetcodeSource || codenSource,
      sourceKind: leetcodeSource ? 'leetcode' as const : 'coden' as const,
    }];
  });
  const disclosureLabel = panels.length > 1 ? 'Solutions' : 'Solution';

  useEffect(() => {
    if (!unlocked) setOpen(false);
  }, [unlocked]);

  return (
    <section
      data-pdf-exclude="true"
      className={`not-prose my-4 overflow-hidden rounded border transition-colors ${
        unlocked
          ? 'border-coden-border bg-coden-bg/40'
          : 'border-coden-border/60 bg-coden-border/20 opacity-60'
      }`}
    >
      <button
        data-pdf-exclude="true"
        type="button"
        aria-expanded={unlocked ? open : false}
        aria-disabled={!unlocked}
        disabled={!unlocked}
        title={unlocked ? `Show the ${disclosureLabel.toLowerCase()}` : 'Solve this challenge successfully to unlock the solution'}
        onClick={() => setOpen((current) => !current)}
        className={`flex w-full items-center gap-2 px-3 py-2 text-left text-sm font-semibold transition-colors ${
          unlocked
            ? 'text-coden-accent hover:bg-coden-border/40'
            : 'cursor-not-allowed text-coden-muted'
        }`}
      >
        {unlocked ? (
          <span aria-hidden="true" className="w-3 text-xs">{open ? '▼' : '▶'}</span>
        ) : (
          <LockIcon />
        )}
        <span>{disclosureLabel}</span>
        {!unlocked && <span className="ml-auto text-xs font-normal">Solve to unlock</span>}
      </button>
      {unlocked && open && panels.length > 0 && (
        <div className="coden-screen-only space-y-5 border-t border-coden-border px-4 py-4 text-sm text-coden-text">
          {panels.map((panel) => (
            <VerifiedCodePanel
              key={panel.id}
              challengeId={challengeId}
              variantId={variantId}
              sourceId={panel.id}
              sourceKind={panel.sourceKind}
              label={panel.label}
              language={panel.language}
              source={panel.source}
              theme={theme}
            />
          ))}
        </div>
      )}
    </section>
  );
}

function VerifiedCodePanel({
  challengeId,
  variantId,
  sourceId,
  sourceKind,
  label,
  language,
  source,
  theme,
}: {
  challengeId: string;
  variantId: string;
  sourceId: string;
  sourceKind: 'coden' | 'leetcode';
  label: string;
  language: (typeof REFERENCE_LANGUAGES)[number];
  source: string;
  theme: 'light' | 'dark';
}) {
  const [copyStatus, setCopyStatus] = useState<'idle' | 'copied' | 'failed'>('idle');
  const editorHeight = Math.min(640, Math.max(260, source.split(/\r?\n/).length * 19 + 32));

  const copyCode = async () => {
    try {
      await copyCompleteCode(source);
      setCopyStatus('copied');
    } catch {
      setCopyStatus('failed');
    }
  };

  return (
    <section aria-label={`${label} in ${language.label}`}>
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <div
          className="rounded border border-coden-border bg-coden-bg px-2.5 py-1.5 text-xs font-semibold text-coden-text"
        >
          {label} &middot; {language.label}
        </div>
        <button
          type="button"
          onClick={() => void copyCode()}
          className="inline-flex h-8 items-center gap-1.5 rounded border border-coden-border bg-coden-bg px-3 text-xs font-semibold text-coden-text transition-colors hover:border-coden-accent hover:text-coden-accent focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-coden-accent"
          aria-label={`Copy the complete ${label} code`}
          title="Copy the complete code"
        >
          <CopyIcon />
          {copyStatus === 'copied' ? 'Copied' : copyStatus === 'failed' ? 'Copy failed' : 'Copy code'}
        </button>
      </div>
      <div className="overflow-hidden rounded border border-coden-border bg-coden-bg" style={{ height: editorHeight }}>
        <Editor
          path={`reference://${challengeId}/${variantId}/${sourceId}/${sourceKind}.${language.extension}`}
          height="100%"
          language={language.monaco}
          theme={theme === 'dark' ? 'vs-dark' : 'light'}
          value={source}
          options={{
            readOnly: true,
            domReadOnly: true,
            contextmenu: false,
            minimap: { enabled: false },
            folding: true,
            glyphMargin: false,
            lineNumbersMinChars: 3,
            fontSize: 13,
            fontFamily: "'Cascadia Code', 'Cascadia Mono', Consolas, 'SFMono-Regular', monospace",
            renderLineHighlight: 'none',
            scrollBeyondLastLine: false,
            overviewRulerLanes: 0,
            hideCursorInOverviewRuler: true,
            wordWrap: 'off',
            automaticLayout: true,
            padding: { top: 14, bottom: 14 },
            ariaLabel: `Read-only ${label} in ${language.label}`,
          }}
          loading={
            <div className="flex h-full items-center justify-center text-xs text-coden-muted">
              Loading code editor...
            </div>
          }
        />
      </div>
    </section>
  );
}

async function copyCompleteCode(source: string): Promise<void> {
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(source);
      return;
    }
  } catch {
    // Electron or browser clipboard permission can be unavailable; use the
    // selection-based fallback below so the convenience action still works.
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
      className="h-3.5 w-3.5 shrink-0"
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
