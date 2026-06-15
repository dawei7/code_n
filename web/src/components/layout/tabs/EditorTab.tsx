/**
 * EditorTab — Monaco editor embedded in a tab. Lazy-loaded so
 * panes that don't show the editor don't pay the ~1.5MB Monaco
 * cost. The detached-window editor (`?view=editor`) is a
 * separate route and still uses EditorView for the legacy
 * decoupled behavior.
 *
 * For the in-window tab, we use the same Monaco setup as the
 * existing EditorView (Python language, coden-dark theme) but
 * bind the source to the shared zustand store so the
 * detached-window sync (BroadcastChannel) flows naturally.
 *
 * The Monaco gutter is augmented with click-to-toggle
 * breakpoints. When a debug session is active, the user
 * can click the gutter to set / clear breakpoints in the
 * shared ``useAppStore.breakpoints`` set; the Debug tab
 * subscribes to that set and pushes changes to the
 * debugpy subprocess over the WebSocket.
 */
import { useEffect, useRef, useState } from 'react';
import MonacoEditor, { OnMount } from '@monaco-editor/react';
import type { editor } from 'monaco-editor';
import { useAppStore } from '../../../store/useAppStore';


export function EditorTab() {
  const source = useAppStore((s) => s.source);
  const setSource = useAppStore((s) => s.setSource);
  const isRunning = useAppStore((s) => s.isRunning);
  const saveSolution = useAppStore((s) => s.saveSolution);
  const currentDetail = useAppStore((s) => s.currentDetail);
  const breakpoints = useAppStore((s) => s.breakpoints);
  const toggleBreakpoint = useAppStore((s) => s.toggleBreakpoint);
  const [status, setStatus] = useState('');
  const editorRef = useRef<editor.IStandaloneCodeEditor | null>(null);
  const decorationsRef = useRef<editor.IEditorDecorationsCollection | null>(null);

  // Ctrl/Cmd+S to save the current source to disk.
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        void (async () => {
          try {
            await saveSolution();
            setStatus('Saved');
            setTimeout(() => setStatus(''), 1500);
          } catch (err) {
            setStatus(`Save failed: ${(err as Error).message}`);
          }
        })();
      }
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [saveSolution]);

  // Whenever the breakpoints set changes, re-apply the
  // Monaco decorations so the gutter markers stay in sync
  // with the store. We use ``deltaDecorations`` so the
  // existing decoration collection is replaced atomically
  // (Monaco's recommended pattern for fast updates).
  useEffect(() => {
    const editor = editorRef.current;
    if (!editor || !decorationsRef.current) return;
    const newDecorations: editor.IModelDeltaDecoration[] = [];
    for (const line of breakpoints) {
      newDecorations.push({
        range: { startLineNumber: line, endLineNumber: line, startColumn: 1, endColumn: 1 },
        options: {
          isWholeLine: false,
          glyphMarginClassName: 'coden-breakpoint-glyph',
          glyphMarginHoverMessage: { value: 'Breakpoint' },
          linesDecorationsClassName: 'coden-breakpoint-line',
        },
      });
    }
    decorationsRef.current.set(newDecorations);
  }, [breakpoints]);

  // The mouse-down handler converts gutter clicks into
  // breakpoint toggles. Monaco gives us the line number via
  // ``target.position.lineNumber`` when the click is on the
  // glyph margin; for the line-number gutter we have to
  // detect it via the DOM class.
  const onMount: OnMount = (ed, monaco) => {
    editorRef.current = ed;
    decorationsRef.current = ed.createDecorationsCollection([]);

    monaco.editor.defineTheme('coden-dark', {
      base: 'vs-dark',
      inherit: true,
      rules: [],
      colors: {
        'editor.background': '#0f172a',
        'editor.foreground': '#e2e8f0',
        'editorLineNumber.foreground': '#475569',
        'editorLineNumber.activeForeground': '#cbd5e1',
        'editor.lineHighlightBackground': '#1e293b',
        'editor.selectionBackground': '#334155',
      },
    });
    monaco.editor.setTheme('coden-dark');

    // Click handler for the glyph margin. Monaco doesn't
    // expose a "glyphMarginClick" event in v0.46+ (it was
    // removed in 0.46), so we listen for mousedown on the
    // DOM and check if the target is in the glyph margin.
    const dom = ed.getDomNode();
    if (dom) {
      dom.addEventListener('mousedown', (ev) => {
        const target = ev.target as HTMLElement | null;
        if (!target) return;
        // Monaco's glyph-margin class is ``.glyph-margin``.
        if (target.closest('.glyph-margin')) {
          const position = ed.getPosition();
          if (position) {
            toggleBreakpoint(position.lineNumber);
          }
        }
      });
    }
  };

  return (
    <div className="h-full flex flex-col bg-coden-bg">
      <div className="px-3 py-1.5 text-xs text-coden-muted border-b border-coden-border bg-coden-surface flex items-center justify-between shrink-0">
        <span className="font-mono">
          {currentDetail ? `${currentDetail.id} — ${currentDetail.name}` : 'no challenge'}
          {isRunning && <span className="ml-2 text-amber-400">(read-only while running)</span>}
        </span>
        <span className="text-coden-muted">{status || 'Ctrl+S to save · click ◉ in the gutter to set a breakpoint'}</span>
      </div>
      <div className="flex-1 min-h-0">
        <MonacoEditor
          height="100%"
          language="python"
          value={source}
          onChange={(v) => setSource(v ?? '')}
          onMount={onMount}
          theme="coden-dark"
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            fontFamily: 'JetBrains Mono, Menlo, Monaco, monospace',
            tabSize: 4,
            insertSpaces: true,
            lineNumbers: 'on',
            renderLineHighlight: 'line',
            scrollBeyondLastLine: false,
            automaticLayout: true,
            wordWrap: 'on',
            readOnly: isRunning,
            // The glyph margin is the small column to the LEFT
            // of the line numbers. We need it visible so the
            // user can click on it to set breakpoints.
            glyphMargin: true,
            // Reserve enough horizontal space for the breakpoint
            // glyph and the line number column.
            lineDecorationsWidth: 8,
          }}
        />
      </div>
      <style>{`
        /* The red dot that appears in the Monaco glyph
           margin on a breakpoint line. The dot is a simple
           Unicode bullet styled red via the coden-accent
           palette; we use a CSS class so Monaco can apply
           it via deltaDecorations. */
        .coden-breakpoint-glyph::before {
          content: '●';
          color: #f87171;
          font-size: 12px;
          line-height: 1;
          display: inline-block;
          transform: translateY(-1px);
        }
        .coden-breakpoint-line {
          background: rgba(248, 113, 113, 0.10);
          border-left: 2px solid #f87171;
        }
      `}</style>
    </div>
  );
}
