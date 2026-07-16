import { flushSync } from 'react-dom';
import { createRoot } from 'react-dom/client';
import 'katex/dist/katex.min.css';
import ReactMarkdown from 'react-markdown';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';

import { apiText } from '../../api/client';
import { getChallenge } from '../../api/challenges';
import { getGuidedExample } from '../../api/guidedExamples';
import type { ChallengeDetail, ChallengeSummary, SupportedLanguage } from '../../types/api';
import type { PdfSaveResult } from '../../types/electron';
import { BrandWordmark } from '../BrandWordmark';


export type PdfBundleProgress = {
  completed: number;
  total: number;
  message: string;
};

type MarkdownPdfDocument = {
  challenge: ChallengeSummary;
  kind: 'reference' | 'guided-example';
  markdown: string;
};

type SolutionPdfDocument = {
  challenge: ChallengeSummary;
  kind: 'solution';
  language: SupportedLanguage;
  languageLabel: string;
  source: string;
};

type PdfDocument = MarkdownPdfDocument | SolutionPdfDocument;

export type PdfTocNode =
  | {
      kind: 'group';
      id: string;
      label: string;
      children: PdfTocNode[];
    }
  | {
      kind: 'problem';
      challengeId: string;
      frontendId: string;
      label: string;
      difficultyLabel: string;
      eloRating: number | null;
    };

type ExportPdfBundleOptions = {
  challenges: ChallengeSummary[];
  language: 'en' | 'de';
  title: string;
  suggestedFilename: string;
  toc: PdfTocNode[];
  includeSolution: boolean;
  onProgress?: (progress: PdfBundleProgress) => void;
};


export async function exportChallengePdfBundle({
  challenges,
  language,
  title,
  suggestedFilename,
  toc,
  includeSolution,
  onProgress,
}: ExportPdfBundleOptions): Promise<PdfSaveResult> {
  const generatedAtUtc = formatUtcTimestamp(new Date());
  const orderedChallenges = uniqueChallenges(challenges);
  if (orderedChallenges.length === 0) {
    throw new Error('There are no problems in this PDF scope.');
  }

  const documents = await loadDocuments(
    orderedChallenges,
    language,
    includeSolution,
    onProgress,
  );
  if (documents.length === 0) {
    throw new Error('No Reference or Guided Example documents were available.');
  }

  document.getElementById('coden-pdf-root')?.remove();
  const host = document.createElement('div');
  host.id = 'coden-pdf-root';
  host.className = 'coden-pdf-preparing';
  host.setAttribute('inert', '');
  document.body.appendChild(host);
  document.documentElement.classList.add('coden-pdf-export-active');

  const root = createRoot(host);
  try {
    flushSync(() => {
      root.render(
        <PdfBundleDocument
          documents={documents}
          title={title}
          toc={toc.length > 0 ? toc : orderedChallenges.map(pdfTocProblem)}
          generatedAtUtc={generatedAtUtc}
        />,
      );
    });
    await preparePrintAssets(host);
    onProgress?.({
      completed: documents.length,
      total: documents.length,
      message: 'Opening Save As...',
    });

    const api = window.electronAPI;
    if (api?.saveDocumentPdf) {
      return await api.saveDocumentPdf({ suggestedFilename, title });
    }

    window.print();
    return { status: 'saved' };
  } finally {
    root.unmount();
    document.documentElement.classList.remove('coden-pdf-export-active');
    host.remove();
  }
}


export function buildPdfBundleFilename(
  scopeLabel: string,
  challenges: ChallengeSummary[],
  includeSolution: boolean,
): string {
  const solutionSuffix = includeSolution ? '-with-solution' : '';
  if (challenges.length === 1) {
    const challenge = challenges[0]!;
    const frontendId = (challenge.leetcode_frontend_id || challenge.id.replace(/^lc_/, ''))
      .replace(/\D/g, '')
      .padStart(4, '0');
    return `${frontendId}_${slug(challenge.leetcode_slug || challenge.name)}-reference-guided-example${solutionSuffix}.pdf`;
  }
  return `${slug(scopeLabel)}-references-guided-examples${includeSolution ? '-with-solutions' : ''}.pdf`;
}


function PdfBundleDocument({
  documents,
  title,
  toc,
  generatedAtUtc,
}: {
  documents: PdfDocument[];
  title: string;
  toc: PdfTocNode[];
  generatedAtUtc: string;
}) {
  const tocNumbers = buildTocNumbers(toc);

  return (
    <main className="coden-pdf-paper">
      <a
        href="#coden-pdf-toc"
        className="coden-pdf-back-to-toc"
        aria-label="Return to the table of contents"
      >
        <svg viewBox="0 0 16 16" aria-hidden="true">
          <path d="M8 13V3M4.5 6.5 8 3l3.5 3.5" />
        </svg>
        <span>Contents</span>
      </a>
      <section
        id="coden-pdf-toc"
        className="coden-pdf-document coden-pdf-toc"
      >
        <header className="coden-pdf-header">
          <div className="coden-pdf-brand"><BrandWordmark /></div>
          <div className="coden-pdf-metadata">{title}</div>
        </header>
        <article>
          <h1>Table of contents</h1>
          <div className="coden-pdf-toc-summary">
            <span>
              {`${uniqueDocumentChallenges(documents)} problem${uniqueDocumentChallenges(documents) === 1 ? '' : 's'}`}
            </span>
            <span>{`Generated ${generatedAtUtc}`}</span>
          </div>
          <PdfTocList nodes={toc} numbers={tocNumbers} />
        </article>
      </section>
      {documents.map((document) => {
        const frontendId = document.challenge.leetcode_frontend_id
          || document.challenge.id.replace(/^lc_/, '');
        const documentLabel = pdfDocumentLabel(document);
        return (
          <section
            key={`${document.challenge.id}:${document.kind}`}
            className="coden-pdf-document"
          >
            {document.kind === 'reference' && (
              <a
                id={problemAnchorId(document.challenge.id)}
                className="coden-pdf-destination"
                aria-hidden="true"
              />
            )}
            <header className="coden-pdf-header">
              <div className="coden-pdf-brand"><BrandWordmark /></div>
              <div className="coden-pdf-metadata">
                {`LeetCode ${frontendId} - ${documentLabel} - ${document.challenge.name}`}
              </div>
            </header>
            {document.kind === 'solution' ? (
              <article className="coden-pdf-solution">
                <h1>{`Solution: ${document.challenge.name}`}</h1>
                <p className="coden-pdf-solution-language">{document.languageLabel}</p>
                <pre>
                  <code
                    className="coden-pdf-solution-source"
                    data-lang={monacoLanguage(document.language)}
                  >
                    {document.source}
                  </code>
                </pre>
              </article>
            ) : (
              <article className="prose prose-sm max-w-none">
                <PdfMarkdown
                  challengeId={document.challenge.id}
                  markdown={document.markdown}
                />
              </article>
            )}
          </section>
        );
      })}
    </main>
  );
}


function pdfDocumentLabel(document: PdfDocument): string {
  if (document.kind === 'solution') return `Solution - ${document.languageLabel}`;
  if (document.kind === 'reference') return 'Reference';
  return 'Guided Example';
}


function PdfTocList({
  nodes,
  numbers,
  depth = 0,
}: {
  nodes: PdfTocNode[];
  numbers: Map<PdfTocNode, string>;
  depth?: number;
}) {
  return (
    <ul className="coden-pdf-toc-list" data-depth={depth}>
      {nodes.map((node) => node.kind === 'group' ? (
        <li key={`group:${node.id}`} className="coden-pdf-toc-group">
          <span
            className="coden-pdf-toc-group-heading"
            data-numbered={Boolean(numbers.get(node))}
          >
            {numbers.get(node) && (
              <span className="coden-pdf-toc-number">{numbers.get(node)}</span>
            )}
            <span>{node.label}</span>
          </span>
          {node.children.length > 0 && (
            <PdfTocList
              nodes={node.children}
              numbers={numbers}
              depth={depth + 1}
            />
          )}
        </li>
      ) : (
        <li key={`problem:${node.challengeId}`} className="coden-pdf-toc-problem">
          <a href={`#${problemAnchorId(node.challengeId)}`}>
            <span className="coden-pdf-toc-number">{numbers.get(node)}</span>
            <span className="coden-pdf-toc-entry">
              <span className="coden-pdf-toc-title">{node.label}</span>
              <span className="coden-pdf-toc-metadata">
                {formatTocMetadata(node)}
              </span>
            </span>
          </a>
        </li>
      ))}
    </ul>
  );
}


function PdfMarkdown({ challengeId, markdown }: { challengeId: string; markdown: string }) {
  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm, remarkMath]}
      rehypePlugins={[rehypeRaw, rehypeKatex]}
      components={{
        details: ({ node, ...props }) => <details {...props} open />,
        a: ({ node, ...props }) => <a {...props} target="_blank" rel="noreferrer" />,
        img: ({ node, ...props }) => (
          <img
            {...props}
            src={documentAssetUrl(challengeId, String(props.src || ''))}
          />
        ),
      }}
    >
      {markdown}
    </ReactMarkdown>
  );
}


async function loadDocuments(
  challenges: ChallengeSummary[],
  language: 'en' | 'de',
  includeSolution: boolean,
  onProgress?: (progress: PdfBundleProgress) => void,
): Promise<PdfDocument[]> {
  const total = challenges.length
    + challenges.reduce((count, challenge) => count + Number(challenge.has_guided_example), 0)
    + (includeSolution ? challenges.length : 0);
  const results: PdfDocument[][] = Array.from({ length: challenges.length }, () => []);
  let nextIndex = 0;
  let completed = 0;

  const report = (message: string) => {
    completed += 1;
    onProgress?.({ completed, total, message });
  };

  const worker = async () => {
    while (true) {
      const index = nextIndex;
      nextIndex += 1;
      if (index >= challenges.length) return;
      const challenge = challenges[index]!;

      const reference = await apiText(
        `/docs/by-id/${encodeURIComponent(challenge.id)}?lang=${language}`,
      );
      results[index]!.push({
        challenge,
        kind: 'reference',
        markdown: expandDetailsForPrint(reference),
      });
      report(`Loaded Reference for ${challenge.name}`);

      if (challenge.has_guided_example) {
        const guidedExample = await getGuidedExample(challenge.id);
        results[index]!.push({
          challenge,
          kind: 'guided-example',
          markdown: guidedExample,
        });
        report(`Loaded Guided Example for ${challenge.name}`);
      }

      if (includeSolution) {
        const detail = await getChallenge(challenge.id);
        const solution = selectPrimarySolution(detail);
        results[index]!.push({
          challenge,
          kind: 'solution',
          ...solution,
        });
        report(`Loaded ${solution.languageLabel} solution for ${challenge.name}`);
      }
    }
  };

  const workerCount = Math.min(4, challenges.length);
  await Promise.all(Array.from({ length: workerCount }, () => worker()));
  return results.flat();
}


function selectPrimarySolution(detail: ChallengeDetail): Pick<
  SolutionPdfDocument,
  'language' | 'languageLabel' | 'source'
> {
  const primary = supportedLanguage(detail.primary_language) ?? 'python';
  const sources = detail.optimal_sources ?? {};
  const source = (sources[primary] || (primary === 'python' ? detail.optimal_source : '')).trim();
  if (!source) {
    throw new Error(
      `${detail.name} has no authored solution in its primary language (${languageLabel(primary)}).`,
    );
  }
  return {
    language: primary,
    languageLabel: languageLabel(primary),
    source,
  };
}


function supportedLanguage(value: string): SupportedLanguage | null {
  const canonical = value.trim().toLowerCase();
  const aliases: Record<string, SupportedLanguage> = {
    python3: 'python',
    js: 'javascript',
    node: 'javascript',
    nodejs: 'javascript',
    shell: 'bash',
    sh: 'bash',
    mysql: 'sql',
  };
  const normalized = aliases[canonical] ?? canonical;
  const supported: SupportedLanguage[] = [
    'python', 'cpp', 'java', 'csharp', 'javascript', 'go', 'kotlin', 'sql', 'bash',
  ];
  return supported.includes(normalized as SupportedLanguage)
    ? normalized as SupportedLanguage
    : null;
}


function languageLabel(language: SupportedLanguage): string {
  const labels: Record<SupportedLanguage, string> = {
    python: 'Python 3',
    cpp: 'C++',
    java: 'Java',
    csharp: 'C#',
    javascript: 'JavaScript',
    go: 'Go',
    kotlin: 'Kotlin',
    sql: 'SQL',
    bash: 'Bash',
  };
  return labels[language];
}


function monacoLanguage(language: SupportedLanguage): string {
  return language === 'bash' ? 'shell' : language;
}


async function preparePrintAssets(root: HTMLElement): Promise<void> {
  await document.fonts?.ready;
  await colorizeSolutionSources(root);
  root.querySelectorAll<HTMLDetailsElement>('details').forEach((details) => {
    details.open = true;
  });
  const images = Array.from(root.querySelectorAll('img'));
  await Promise.all(images.map(waitForImage));
  root.classList.remove('coden-pdf-preparing');
  root.removeAttribute('inert');
  await new Promise<void>((resolve) => {
    requestAnimationFrame(() => requestAnimationFrame(() => resolve()));
  });
}


async function colorizeSolutionSources(root: HTMLElement): Promise<void> {
  const sources = Array.from(
    root.querySelectorAll<HTMLElement>('code.coden-pdf-solution-source'),
  );
  if (sources.length === 0) return;

  const monaco = await import('monaco-editor');
  const restoreTheme = document.documentElement.classList.contains('dark') ? 'vs-dark' : 'vs';
  try {
    for (const source of sources) {
      await monaco.editor.colorizeElement(source, { theme: 'vs', tabSize: 4 });
      source.querySelectorAll<HTMLElement>('span').forEach((token) => {
        const style = window.getComputedStyle(token);
        token.style.color = style.color;
        token.style.fontStyle = style.fontStyle;
        token.style.fontWeight = style.fontWeight;
        token.style.textDecoration = style.textDecoration;
        token.removeAttribute('class');
      });
      source.classList.remove('vs');
    }
  } finally {
    monaco.editor.setTheme(restoreTheme);
  }
}


async function waitForImage(image: HTMLImageElement): Promise<void> {
  if (!image.complete) {
    await new Promise<void>((resolve) => {
      const finish = () => resolve();
      image.addEventListener('load', finish, { once: true });
      image.addEventListener('error', finish, { once: true });
      window.setTimeout(finish, 5_000);
    });
  }
  if (typeof image.decode === 'function') {
    await image.decode().catch(() => undefined);
  }
}


function uniqueChallenges(challenges: ChallengeSummary[]): ChallengeSummary[] {
  const seen = new Set<string>();
  return challenges.filter((challenge) => {
    if (seen.has(challenge.id)) return false;
    seen.add(challenge.id);
    return true;
  });
}


function uniqueDocumentChallenges(documents: PdfDocument[]): number {
  return new Set(documents.map((document) => document.challenge.id)).size;
}


function problemAnchorId(challengeId: string): string {
  return `coden-problem-${slug(challengeId)}`;
}


function formatUtcTimestamp(value: Date): string {
  return value.toISOString().replace('T', ' ').replace(/\.\d{3}Z$/, ' UTC');
}


function pdfTocProblem(challenge: ChallengeSummary): PdfTocNode {
  return {
    kind: 'problem',
    challengeId: challenge.id,
    frontendId: challenge.leetcode_frontend_id || challenge.id.replace(/^lc_/, ''),
    label: challenge.name,
    difficultyLabel: challenge.difficulty_label,
    eloRating: challenge.elo_rating,
  };
}


function buildTocNumbers(nodes: PdfTocNode[]): Map<PdfTocNode, string> {
  const numbers = new Map<PdfTocNode, string>();
  const visit = (items: PdfTocNode[], prefix: number[], depth: number) => {
    items.forEach((item, index) => {
      if (depth === 0 && item.kind === 'group') {
        numbers.set(item, '');
        visit(item.children, [], depth + 1);
        return;
      }
      const path = [...prefix, index + 1];
      numbers.set(item, path.join('.'));
      if (item.kind === 'group') {
        visit(item.children, path, depth + 1);
      }
    });
  };
  visit(nodes, [], 0);
  return numbers;
}


function formatTocMetadata(node: Extract<PdfTocNode, { kind: 'problem' }>): string {
  const metadata = [`lc_${node.frontendId}`];
  if (node.difficultyLabel) metadata.push(node.difficultyLabel);
  if (node.eloRating !== null) metadata.push(`Elo: ${Math.round(node.eloRating)}`);
  return ` - ${metadata.join(' - ')}`;
}


function expandDetailsForPrint(markdown: string): string {
  return markdown
    .replace(
      /<details>\s*<summary>\s*([^<]+?)\s*<\/summary>/gi,
      (_, summary: string) => `\n## ${summary.trim()}\n`,
    )
    .replace(/<\/details>/gi, '');
}


function documentAssetUrl(challengeId: string, src: string): string {
  if (!src || /^(?:[a-z]+:|\/|#)/i.test(src)) return src;
  const relative = src.replace(/^\.\//, '').replace(/^assets\//, '');
  const encoded = relative.split('/').map(encodeURIComponent).join('/');
  return `/api/docs/by-id/${encodeURIComponent(challengeId)}/assets/${encoded}`;
}


function slug(value: string): string {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 100) || 'coden-problems';
}
