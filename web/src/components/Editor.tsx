import MonacoEditor, { OnMount } from '@monaco-editor/react';
import { useAppStore } from '../store/useAppStore';


/**
 * Editor — Monaco wrapper. Dark theme to match the rest of the
 * app, Python language for syntax highlighting, read-only when a
 * run is in progress so the player can't edit mid-execute.
 */
export function Editor() {
  const source = useAppStore((s) => s.source);
  const setSource = useAppStore((s) => s.setSource);
  const isRunning = useAppStore((s) => s.isRunning);

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
    <div className="h-full border border-coden-border rounded overflow-hidden">
      <MonacoEditor
        height="100%"
        language="python"
        value={source}
        onChange={(v) => setSource(v ?? '')}
        onMount={onMount}
        theme="coden-dark"
        options={{
          minimap: { enabled: false },
          fontSize: 13,
          fontFamily: 'JetBrains Mono, Menlo, Monaco, monospace',
          tabSize: 4,
          insertSpaces: true,
          lineNumbers: 'on',
          renderLineHighlight: 'line',
          scrollBeyondLastLine: false,
          automaticLayout: true,
          readOnly: isRunning,
          wordWrap: 'on',
        }}
      />
    </div>
  );
}
