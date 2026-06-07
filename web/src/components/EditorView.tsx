import { useEffect, useState, useCallback } from 'react';
import MonacoEditor, { OnMount } from '@monaco-editor/react';
import * as challengesApi from '../api/challenges';
import * as solutionsApi from '../api/solutions';
import type { ChallengeSummary } from '../types/api';


/**
 * EditorView — full-window Monaco editor for a single challenge.
 *
 * Loaded when the URL has ``?view=editor``. Used by the pop-out
 * window (a separate BrowserWindow spawned by the Electron main
 * process) so the user can drag the editor to a second monitor
 * and edit at full width.
 *
 * State management is local (no Zustand store) because this
 * window is independent of the main window's challenge list. The
 * user picks a challenge from the dropdown; the source loads
 * from the server (or the starter if no saved source exists) and
 * is saved with Ctrl+S or the Save button. The main window sees
 * the saved source on its next re-select of the same challenge.
 */
export function EditorView() {
  const [challenges, setChallenges] = useState<ChallengeSummary[]>([]);
  const [challengeId, setChallengeId] = useState<string>('');
  const [source, setSource] = useState<string>('');
  const [savedSource, setSavedSource] = useState<string>('');  // for dirty-detection
  const [saving, setSaving] = useState(false);
  const [status, setStatus] = useState<string>('');
  const [loaded, setLoaded] = useState(false);

  // Load challenge list on mount.
  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const list = await challengesApi.listChallenges();
        if (cancelled) return;
        setChallenges(list);
        // Default to the first challenge the user had selected via
        // the URL (?id=...) or the first sort challenge, falling
        // back to the first item.
        const params = new URLSearchParams(window.location.search);
        const fromUrl = params.get('id');
        const initial = fromUrl && list.find((c) => c.id === fromUrl)
          ? fromUrl
          : (list.find((c) => c.id === 'sort_01')?.id ?? list[0]?.id ?? '');
        setChallengeId(initial);
      } catch (e) {
        setStatus(`Failed to load challenges: ${(e as Error).message}`);
      }
    })();
    return () => { cancelled = true; };
  }, []);

  // Load the source for the selected challenge.
  useEffect(() => {
    if (!challengeId) return;
    let cancelled = false;
    (async () => {
      try {
        const saved = await solutionsApi.getSolution(challengeId);
        if (cancelled) return;
        if (saved.exists) {
          setSource(saved.source);
          setSavedSource(saved.source);
        } else {
          // No saved source — fall back to the starter template.
          const detail = await challengesApi.getChallenge(challengeId);
          if (cancelled) return;
          setSource(detail.starter_source);
          setSavedSource(detail.starter_source);
        }
        setLoaded(true);
        setStatus(`Loaded ${challengeId}`);
      } catch (e) {
        setStatus(`Failed to load ${challengeId}: ${(e as Error).message}`);
      }
    })();
    return () => { cancelled = true; };
  }, [challengeId]);

  const dirty = source !== savedSource;

  const save = useCallback(async () => {
    if (!challengeId) return;
    setSaving(true);
    try {
      await solutionsApi.putSolution(challengeId, source);
      setSavedSource(source);
      setStatus(`Saved ${challengeId}`);
    } catch (e) {
      setStatus(`Save failed: ${(e as Error).message}`);
    } finally {
      setSaving(false);
    }
  }, [challengeId, source]);

  // Ctrl+S to save.
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        void save();
      }
    }
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [save]);

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

  const current = challenges.find((c) => c.id === challengeId);

  return (
    <div className="h-full flex flex-col bg-coden-bg text-coden-text font-sans">
      <header className="h-12 flex items-center justify-between px-4 border-b border-coden-border bg-coden-surface shrink-0">
        <div className="flex items-center gap-3">
          <span className="text-xl">⚙️</span>
          <h1 className="text-lg font-semibold">cOde(n) editor</h1>
          <span className="text-xs text-coden-muted">pop-out window</span>
        </div>
        <div className="flex items-center gap-2">
          <select
            value={challengeId}
            onChange={(e) => setChallengeId(e.target.value)}
            className="bg-coden-bg border border-coden-border rounded px-2 py-1 text-sm font-mono"
          >
            {challenges.map((c) => (
              <option key={c.id} value={c.id}>{c.id} — {c.name}</option>
            ))}
          </select>
          <button
            type="button"
            onClick={save}
            disabled={!dirty || saving}
            className="px-3 py-1 text-sm rounded bg-coden-accent text-coden-bg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
            title="Save (Ctrl/Cmd+S)"
          >
            {saving ? 'Saving…' : '💾 Save'}
          </button>
          {dirty && (
            <span className="text-xs text-amber-400">● unsaved</span>
          )}
        </div>
      </header>
      {current && (
        <div className="px-4 py-1 text-xs text-coden-muted border-b border-coden-border bg-coden-surface">
          {current.name} · {current.category} · difficulty {current.difficulty}/10 · required {current.required_complexity}
        </div>
      )}
      <div className="flex-1 min-h-0">
        {loaded ? (
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
            }}
          />
        ) : (
          <div className="h-full flex items-center justify-center text-coden-muted">
            {status || 'Loading…'}
          </div>
        )}
      </div>
      <footer className="h-6 px-4 flex items-center justify-between text-xs text-coden-muted border-t border-coden-border bg-coden-surface shrink-0">
        <span>{status}</span>
        <span>Ctrl+S to save</span>
      </footer>
    </div>
  );
}
