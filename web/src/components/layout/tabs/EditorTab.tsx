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
 */
import { useEffect, useState } from 'react';
import MonacoEditor, { OnMount } from '@monaco-editor/react';
import { useAppStore } from '../../../store/useAppStore';


export function EditorTab() {
  const source = useAppStore((s) => s.source);
  const setSource = useAppStore((s) => s.setSource);
  const isRunning = useAppStore((s) => s.isRunning);
  const saveSolution = useAppStore((s) => s.saveSolution);
  const currentDetail = useAppStore((s) => s.currentDetail);
  const [status, setStatus] = useState('');

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

  const onMount: OnMount = (_editor, monaco) => {
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
  };

  return (
    <div className="h-full flex flex-col bg-coden-bg">
      <div className="px-3 py-1.5 text-xs text-coden-muted border-b border-coden-border bg-coden-surface flex items-center justify-between shrink-0">
        <span className="font-mono">
          {currentDetail ? `${currentDetail.id} — ${currentDetail.name}` : 'no challenge'}
          {isRunning && <span className="ml-2 text-amber-400">(read-only while running)</span>}
        </span>
        <span className="text-coden-muted">{status || 'Ctrl+S to save'}</span>
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
          }}
        />
      </div>
    </div>
  );
}
