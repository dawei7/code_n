import { Children, isValidElement, useEffect, useState } from 'react';
import type { ReactNode } from 'react';
import type { Mermaid } from 'mermaid';


type RenderState =
  | { kind: 'loading' }
  | { kind: 'ready'; svg: string }
  | { kind: 'error'; message: string };

type CodeElementProps = {
  className?: string;
  children?: ReactNode;
};

let mermaidPromise: Promise<Mermaid> | null = null;
let nextDiagramId = 0;


function loadMermaid(): Promise<Mermaid> {
  if (!mermaidPromise) {
    mermaidPromise = import('mermaid').then(({ default: mermaid }) => {
      mermaid.initialize({
        startOnLoad: false,
        securityLevel: 'strict',
        suppressErrorRendering: true,
        theme: 'base',
        htmlLabels: false,
        fontFamily: '"Segoe UI", Arial, sans-serif',
        maxEdges: 500,
        maxTextSize: 100_000,
        themeVariables: {
          background: '#ffffff',
          primaryColor: '#f8fafc',
          primaryTextColor: '#0f172a',
          primaryBorderColor: '#64748b',
          secondaryColor: '#ecfeff',
          secondaryTextColor: '#0f172a',
          secondaryBorderColor: '#0f766e',
          tertiaryColor: '#fff7ed',
          tertiaryTextColor: '#0f172a',
          tertiaryBorderColor: '#c2410c',
          lineColor: '#64748b',
          edgeLabelBackground: '#ffffff',
          fontSize: '16px',
        },
        flowchart: {
          curve: 'linear',
          nodeSpacing: 48,
          rankSpacing: 68,
          padding: 6,
          useMaxWidth: true,
        },
      });
      return mermaid;
    });
  }
  return mermaidPromise;
}


export function MermaidDiagram({ source }: { source: string }) {
  const [state, setState] = useState<RenderState>({ kind: 'loading' });

  useEffect(() => {
    let cancelled = false;
    const diagramId = `coden-mermaid-${++nextDiagramId}`;
    setState({ kind: 'loading' });

    void loadMermaid()
      .then(async (mermaid) => {
        await mermaid.parse(source);
        return mermaid.render(diagramId, source);
      })
      .then(({ svg }) => {
        if (!cancelled) setState({ kind: 'ready', svg });
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setState({
            kind: 'error',
            message: conciseError(error),
          });
        }
      });

    return () => {
      cancelled = true;
    };
  }, [source]);

  if (state.kind === 'loading') {
    return (
      <figure
        className="coden-mermaid-diagram not-prose"
        data-mermaid-state="loading"
        aria-busy="true"
      >
        <div className="flex min-h-44 items-center justify-center text-sm text-slate-500">
          Rendering graph&hellip;
        </div>
      </figure>
    );
  }

  if (state.kind === 'error') {
    return (
      <figure
        className="coden-mermaid-diagram not-prose"
        data-mermaid-state="error"
        data-mermaid-error={state.message}
      >
        <div role="alert" className="text-sm text-rose-700">
          Diagram rendering failed: {state.message}
        </div>
        <pre className="mt-3 overflow-x-auto whitespace-pre-wrap text-xs text-slate-700">
          {source}
        </pre>
      </figure>
    );
  }

  return (
    <figure
      className="coden-mermaid-diagram not-prose"
      data-mermaid-state="ready"
    >
      <div
        className="coden-mermaid-diagram-svg"
        dangerouslySetInnerHTML={{ __html: state.svg }}
      />
    </figure>
  );
}


export function mermaidSourceFromPreChildren(children: ReactNode): string | null {
  const elements = Children.toArray(children);
  if (elements.length !== 1 || !isValidElement(elements[0])) return null;

  const props = elements[0].props as CodeElementProps;
  const languages = String(props.className || '').split(/\s+/);
  if (!languages.includes('language-mermaid')) return null;

  const source = String(props.children || '').trimEnd();
  return source || null;
}


export async function waitForMermaidDiagrams(
  root: HTMLElement,
  timeoutMs = 15_000,
): Promise<void> {
  const diagrams = Array.from(
    root.querySelectorAll<HTMLElement>('[data-mermaid-state]'),
  );
  await Promise.all(diagrams.map((diagram) => waitForMermaidDiagram(diagram, timeoutMs)));
}


function waitForMermaidDiagram(diagram: HTMLElement, timeoutMs: number): Promise<void> {
  const currentState = diagram.dataset.mermaidState;
  if (currentState === 'ready') return Promise.resolve();
  if (currentState === 'error') {
    return Promise.reject(new Error(diagram.dataset.mermaidError || 'A diagram failed to render.'));
  }

  return new Promise<void>((resolve, reject) => {
    let settled = false;
    let timeout = 0;
    const finish = (callback: () => void) => {
      if (settled) return;
      settled = true;
      window.clearTimeout(timeout);
      observer.disconnect();
      callback();
    };
    const inspect = () => {
      const state = diagram.dataset.mermaidState;
      if (state === 'ready') finish(resolve);
      if (state === 'error') {
        finish(() => reject(new Error(
          diagram.dataset.mermaidError || 'A diagram failed to render.',
        )));
      }
    };
    const observer = new MutationObserver(inspect);
    timeout = window.setTimeout(() => {
      finish(() => reject(new Error('Timed out while rendering a Mermaid diagram.')));
    }, timeoutMs);

    observer.observe(diagram, {
      attributes: true,
      attributeFilter: ['data-mermaid-state', 'data-mermaid-error'],
    });
    inspect();
  });
}


function conciseError(error: unknown): string {
  const message = error instanceof Error ? error.message : String(error);
  return message.replace(/\s+/g, ' ').trim().slice(0, 240) || 'Unknown Mermaid error.';
}
