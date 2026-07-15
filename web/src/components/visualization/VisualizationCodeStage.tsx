import { Editor, type OnMount } from '@monaco-editor/react';
import { useCallback, useEffect, useRef } from 'react';

import { useAppStore } from '../../store/useAppStore';
import type { VisualizationCode } from '../../types/api';

type MonacoEditor = Parameters<OnMount>[0];
type MonacoApi = Parameters<OnMount>[1];

export function VisualizationCodeStage({
  challengeId,
  code,
  activeAnchors,
}: {
  challengeId: string;
  code: VisualizationCode;
  activeAnchors: string[];
}) {
  const theme = useAppStore((state) => state.theme);
  const fontScale = useAppStore((state) => state.paneFontScales['workspace:visualization'] ?? 1);
  const editorRef = useRef<MonacoEditor | null>(null);
  const monacoRef = useRef<MonacoApi | null>(null);
  const decorationsRef = useRef<string[]>([]);

  const updateDecorations = useCallback(() => {
    const editor = editorRef.current;
    const monaco = monacoRef.current;
    if (!editor || !monaco) return;
    const ranges = activeAnchors
      .map((anchor) => code.anchors[anchor])
      .filter((range) => range !== undefined);
    const decorations = ranges.map((range) => ({
      range: new monaco.Range(range.start_line, 1, range.end_line, 1),
      options: {
        isWholeLine: true,
        className: 'coden-visual-active-line',
        linesDecorationsClassName: 'coden-visual-active-glyph',
        stickiness: monaco.editor.TrackedRangeStickiness.NeverGrowsWhenTypingAtEdges,
      },
    }));
    decorationsRef.current = editor.deltaDecorations(decorationsRef.current, decorations);
    if (ranges.length > 0) {
      editor.revealLinesInCenterIfOutsideViewport(
        ranges[0].start_line,
        ranges[ranges.length - 1].end_line,
      );
    }
  }, [activeAnchors, code.anchors]);

  useEffect(() => {
    updateDecorations();
  }, [updateDecorations]);

  useEffect(() => () => {
    const editor = editorRef.current;
    if (editor) decorationsRef.current = editor.deltaDecorations(decorationsRef.current, []);
  }, []);

  const handleMount: OnMount = (editor, monaco) => {
    editorRef.current = editor;
    monacoRef.current = monaco;
    updateDecorations();
  };

  return (
    <section className="flex h-[30rem] min-h-0 flex-col overflow-hidden rounded-lg border border-coden-border bg-coden-inner xl:h-auto xl:min-h-[34rem]">
      <header className="flex items-center justify-between gap-3 border-b border-coden-border px-4 py-2">
        <div>
          <h3 className="text-xs font-semibold uppercase tracking-wide text-coden-muted">Canonical code</h3>
          <div className="mt-0.5 font-mono text-[10px] text-coden-muted">{code.source_path}</div>
        </div>
        <span className="rounded-full border border-coden-border bg-coden-bg px-2 py-0.5 text-[9px] font-semibold uppercase tracking-wide text-coden-muted">
          Read only
        </span>
      </header>
      <div className="min-h-0 flex-1" aria-label="Canonical solution with the active algorithm line highlighted">
        <Editor
          path={`visualization://${challengeId}/${code.source_path}`}
          height="100%"
          language={code.language}
          theme={theme === 'dark' ? 'vs-dark' : 'light'}
          value={code.source}
          onMount={handleMount}
          options={{
            readOnly: true,
            domReadOnly: true,
            contextmenu: false,
            minimap: { enabled: false },
            folding: false,
            glyphMargin: false,
            lineDecorationsWidth: 5,
            lineNumbersMinChars: 2,
            fontSize: Math.round(13 * fontScale),
            fontFamily: "'Cascadia Code', 'Cascadia Mono', Consolas, 'SFMono-Regular', monospace",
            renderLineHighlight: 'none',
            scrollBeyondLastLine: false,
            overviewRulerLanes: 0,
            hideCursorInOverviewRuler: true,
            wordWrap: 'on',
            automaticLayout: true,
            padding: { top: 14, bottom: 14 },
            ariaLabel: 'Canonical solution source synchronized with the current visualization step',
          }}
          loading={
            <div className="flex h-full items-center justify-center text-sm text-coden-muted">
              Loading canonical code...
            </div>
          }
        />
      </div>
      <footer className="border-t border-coden-border px-4 py-2 text-[10px] leading-relaxed text-coden-muted">
        Highlighted from semantic anchors resolved against the real package solution.
      </footer>
    </section>
  );
}
