import { useState, useEffect, useRef } from 'react';
import type { ReactNode } from 'react';
import { createPortal } from 'react-dom';
import { Editor } from '@monaco-editor/react';
import { useAppStore } from '../../../store/useAppStore';

type DebugStatus = 'idle' | 'starting' | 'running' | 'paused' | 'exited' | 'error';

interface DebugVariable {
  name: string;
  value: string;
  type?: string;
}

export function CodenTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const theme = useAppStore((s) => s.theme);

  const source = useAppStore((s) => s.source);
  const n = useAppStore((s) => s.n);
  const seed = useAppStore((s) => s.seed);
  const mode = useAppStore((s) => s.mode);
  const activeVersion = useAppStore((s) => s.activeVersion);
  const versionNames = useAppStore((s) => s.versionNames);

  const saveSource = useAppStore((s) => s.saveSource);
  const [isMaximized, setIsMaximized] = useState(false);

  // Exit focus mode on Escape
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isMaximized) {
        setIsMaximized(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isMaximized]);

  const [editorValue, setEditorValue] = useState(source);
  const saveTimeout = useRef<number | null>(null);
  const editorRef = useRef<any>(null);
  const monacoRef = useRef<any>(null);
  const decorationsRef = useRef<string[]>([]);
  const wsRef = useRef<WebSocket | null>(null);
  const threadIdRef = useRef<number | null>(null);
  const [breakpoints, setBreakpoints] = useState<number[]>([]);
  const [debugStatus, setDebugStatus] = useState<DebugStatus>('idle');
  const [debugCurrentLine, setDebugCurrentLine] = useState<number | null>(null);
  const [debugError, setDebugError] = useState<string | null>(null);
  const [debugReason, setDebugReason] = useState<string>('');
  const [debugLocals, setDebugLocals] = useState<DebugVariable[]>([]);
  const [debugOutput, setDebugOutput] = useState<string[]>([]);

  // Sync external changes, such as a version switch.
  useEffect(() => {
    setEditorValue(source);
  }, [source]);

  useEffect(() => {
    setBreakpoints([]);
    setDebugCurrentLine(null);
    setDebugStatus('idle');
    setDebugError(null);
    setDebugReason('');
    setDebugLocals([]);
    setDebugOutput([]);
    stopDebugSession();
  }, [detail?.id, activeVersion]);

  useEffect(() => {
    updateEditorDecorations();
  }, [breakpoints, debugCurrentLine]);

  useEffect(() => {
    return () => {
      stopDebugSession();
      if (saveTimeout.current) {
        window.clearTimeout(saveTimeout.current);
      }
    };
  }, []);

  function handleEditorChange(value: string | undefined) {
    const val = value || '';
    setEditorValue(val);

    if (saveTimeout.current) {
      window.clearTimeout(saveTimeout.current);
    }
    saveTimeout.current = window.setTimeout(() => {
      void saveSource(val);
    }, 500);
  }

  function updateEditorDecorations() {
    const editor = editorRef.current;
    const monaco = monacoRef.current;
    if (!editor || !monaco) return;
    const nextDecorations = [
      ...breakpoints.map((line) => ({
        range: new monaco.Range(line, 1, line, 1),
        options: {
          isWholeLine: false,
          glyphMarginClassName: 'coden-debug-breakpoint',
          glyphMarginHoverMessage: { value: 'Breakpoint' },
          stickiness: monaco.editor.TrackedRangeStickiness.NeverGrowsWhenTypingAtEdges,
        },
      })),
      ...(debugCurrentLine
        ? [{
            range: new monaco.Range(debugCurrentLine, 1, debugCurrentLine, 1),
            options: {
              isWholeLine: true,
              className: 'coden-debug-current-line',
              glyphMarginClassName: 'coden-debug-current-glyph',
              stickiness: monaco.editor.TrackedRangeStickiness.NeverGrowsWhenTypingAtEdges,
            },
          }]
        : []),
    ];
    decorationsRef.current = editor.deltaDecorations(decorationsRef.current, nextDecorations);
  }

  function handleEditorMount(editor: any, monaco: any) {
    editorRef.current = editor;
    monacoRef.current = monaco;
    editor.onMouseDown((event: any) => {
      const targetType = event.target?.type;
      const gutterType = monaco.editor.MouseTargetType.GUTTER_GLYPH_MARGIN;
      const lineNumberType = monaco.editor.MouseTargetType.GUTTER_LINE_NUMBERS;
      const lineNumber = event.target?.position?.lineNumber;
      if ((targetType === gutterType || targetType === lineNumberType) && typeof lineNumber === 'number') {
        toggleBreakpoint(lineNumber);
      }
    });
    updateEditorDecorations();
  }

  function toggleBreakpoint(lineNumber: number) {
    setBreakpoints((prev) => {
      const next = prev.includes(lineNumber)
        ? prev.filter((line) => line !== lineNumber)
        : [...prev, lineNumber].sort((a, b) => a - b);
      sendDebugMessage({ type: 'setBreakpoints', challengeId: detail?.id, breakpoints: next });
      return next;
    });
  }

  function sendDebugMessage(payload: Record<string, unknown>) {
    const ws = wsRef.current;
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(payload));
    }
  }

  async function startDebugSession() {
    if (!detail) return;
    if (saveTimeout.current) {
      window.clearTimeout(saveTimeout.current);
      saveTimeout.current = null;
    }
    await saveSource(editorValue);
    stopDebugSession(false);

    setDebugStatus('starting');
    setDebugError(null);
    setDebugReason('');
    setDebugCurrentLine(null);
    setDebugLocals([]);
    setDebugOutput([]);

    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const ws = new WebSocket(`${protocol}//${window.location.host}/api/debug/ws`);
    wsRef.current = ws;
    ws.onopen = () => {
      ws.send(JSON.stringify({
        type: 'start',
        challengeId: detail.id,
        n,
        seed,
        mode,
        breakpoints,
      }));
    };
    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.type === 'started') {
        setDebugStatus('running');
      } else if (msg.type === 'stopped') {
        threadIdRef.current = msg.threadId ?? null;
        setDebugStatus('paused');
        setDebugCurrentLine(typeof msg.line === 'number' ? msg.line : null);
        setDebugReason(msg.reason ?? 'paused');
        setDebugLocals(Array.isArray(msg.locals) ? msg.locals : []);
        if (typeof msg.line === 'number') {
          editorRef.current?.revealLineInCenter(msg.line);
        }
      } else if (msg.type === 'continued') {
        setDebugStatus('running');
        setDebugCurrentLine(null);
      } else if (msg.type === 'output') {
        if (msg.output) {
          setDebugOutput((prev) => [...prev.slice(-200), String(msg.output).trimEnd()]);
        }
      } else if (msg.type === 'exited') {
        setDebugStatus('exited');
        setDebugCurrentLine(null);
      } else if (msg.type === 'error') {
        setDebugStatus('error');
        setDebugError(msg.message ?? 'Debugger error');
      }
    };
    ws.onerror = () => {
      setDebugStatus('error');
      setDebugError('Debugger WebSocket failed.');
    };
    ws.onclose = () => {
      if (wsRef.current === ws) {
        wsRef.current = null;
      }
    };
  }

  function stopDebugSession(sendStop = true) {
    const ws = wsRef.current;
    if (ws) {
      if (sendStop && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({ type: 'stop' }));
      }
      ws.close();
      wsRef.current = null;
    }
    threadIdRef.current = null;
  }

  function debugCommand(type: 'continue' | 'stepOver' | 'stepIn' | 'stepOut') {
    sendDebugMessage({ type, threadId: threadIdRef.current ?? 1 });
  }

  if (!detail) {
    return (
      <div className="flex items-center justify-center p-8 text-coden-muted">
        Select a challenge to manage its code versions.
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full relative">
      {/* Code Preview */}
      {!isMaximized && (
        <div className="flex-1 flex flex-col min-h-0 bg-coden-inner rounded-xl border border-coden-border overflow-hidden shadow-inner">
          <div className="flex flex-wrap items-center justify-between gap-3 px-4 py-2 bg-coden-surface border-b border-coden-border">
            <span className="text-xs font-mono text-coden-muted">
              solutions/{detail.id}.py ({versionNames[activeVersion] || `v${activeVersion}`})
            </span>
            <div className="flex items-center gap-2">
              <DebugToolbar
                status={debugStatus}
                onStart={() => void startDebugSession()}
                onContinue={() => debugCommand('continue')}
                onStepOver={() => debugCommand('stepOver')}
                onStepIn={() => debugCommand('stepIn')}
                onStepOut={() => debugCommand('stepOut')}
                onStop={() => {
                  stopDebugSession();
                  setDebugStatus('idle');
                  setDebugCurrentLine(null);
                }}
              />
              <button
                type="button"
                onClick={() => setIsMaximized(true)}
                title="Focus mode"
                aria-label="Focus mode"
                className="h-8 w-8 text-sm font-bold rounded border border-coden-border text-coden-text hover:bg-coden-border"
              >
                ⛶
              </button>
            </div>
          </div>
          <div className="flex-1 min-h-0 grid grid-cols-1 xl:grid-cols-[minmax(0,1fr)_320px]">
            <div className="min-h-[360px] overflow-hidden">
              <Editor
                height="100%"
                language="python"
                theme={theme === 'dark' ? 'vs-dark' : 'light'}
                value={editorValue}
                onMount={handleEditorMount}
                onChange={handleEditorChange}
                options={{
                  minimap: { enabled: false },
                  fontSize: 14,
                  fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
                  scrollBeyondLastLine: false,
                  wordWrap: 'on',
                  glyphMargin: true,
                  lineDecorationsWidth: 4,
                  lineNumbersMinChars: 2,
                  padding: { top: 16, bottom: 16 },
                }}
                loading={
                  <div className="flex h-full items-center justify-center text-coden-muted text-sm">
                    Loading editor...
                  </div>
                }
              />
            </div>
            <DebugPanel
              status={debugStatus}
              reason={debugReason}
              error={debugError}
              currentLine={debugCurrentLine}
              breakpoints={breakpoints}
              locals={debugLocals}
              output={debugOutput}
            />
          </div>
        </div>
      )}

      {/* Maximized Code Preview Portal */}
      {isMaximized && createPortal(
        <div className="fixed inset-0 z-[9999] bg-coden-bg flex flex-col">
          <div className="flex flex-wrap items-center justify-between gap-3 px-4 py-2 bg-coden-surface border-b border-coden-border">
            <span className="text-xs font-mono text-coden-muted">
              solutions/{detail.id}.py ({versionNames[activeVersion] || `v${activeVersion}`})
            </span>
            <div className="flex flex-wrap items-center gap-2">
              <DebugToolbar
                status={debugStatus}
                onStart={() => void startDebugSession()}
                onContinue={() => debugCommand('continue')}
                onStepOver={() => debugCommand('stepOver')}
                onStepIn={() => debugCommand('stepIn')}
                onStepOut={() => debugCommand('stepOut')}
                onStop={() => {
                  stopDebugSession();
                  setDebugStatus('idle');
                  setDebugCurrentLine(null);
                }}
              />
              <button
                onClick={() => setIsMaximized(false)}
                className="h-8 px-3 text-xs font-bold text-coden-text bg-red-900/40 hover:bg-red-900/60 border border-red-900/50 rounded transition-colors"
              >
                Exit Focus
              </button>
            </div>
          </div>
          <div className="flex-1 min-h-0 grid grid-cols-1 xl:grid-cols-[minmax(0,1fr)_340px]">
            <div className="overflow-hidden">
              <Editor
                height="100%"
                language="python"
                theme={theme === 'dark' ? 'vs-dark' : 'light'}
                value={editorValue}
                onMount={handleEditorMount}
                onChange={handleEditorChange}
                options={{
                  minimap: { enabled: false },
                  fontSize: 14,
                  fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
                  scrollBeyondLastLine: false,
                  wordWrap: 'on',
                  glyphMargin: true,
                  lineDecorationsWidth: 4,
                  lineNumbersMinChars: 2,
                  padding: { top: 16, bottom: 16 },
                }}
                loading={
                  <div className="flex h-full items-center justify-center text-coden-muted text-sm">
                    Loading editor...
                  </div>
                }
              />
            </div>
            <DebugPanel
              status={debugStatus}
              reason={debugReason}
              error={debugError}
              currentLine={debugCurrentLine}
              breakpoints={breakpoints}
              locals={debugLocals}
              output={debugOutput}
            />
          </div>
        </div>,
        document.body
      )}
    </div>
  );
}

function DebugToolbar({
  status,
  onStart,
  onContinue,
  onStepOver,
  onStepIn,
  onStepOut,
  onStop,
}: {
  status: DebugStatus;
  onStart: () => void;
  onContinue: () => void;
  onStepOver: () => void;
  onStepIn: () => void;
  onStepOut: () => void;
  onStop: () => void;
}) {
  const paused = status === 'paused';
  const active = status === 'starting' || status === 'running' || status === 'paused';
  return (
    <div className="flex items-center gap-1">
      <button
        type="button"
        onClick={onStart}
        disabled={status === 'starting' || status === 'running'}
        className="h-8 px-3 text-xs font-bold rounded bg-emerald-600 text-white hover:bg-emerald-500 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {active ? 'Restart Debug' : 'Debug'}
      </button>
      <button
        type="button"
        onClick={onContinue}
        title="Continue"
        aria-label="Continue"
        disabled={!paused}
        className="h-8 w-8 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-40"
      >
        ▶
      </button>
      <button
        type="button"
        onClick={onStepOver}
        title="Step over"
        aria-label="Step over"
        disabled={!paused}
        className="h-8 w-8 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-40"
      >
        ↷
      </button>
      <button
        type="button"
        onClick={onStepIn}
        title="Step in"
        aria-label="Step in"
        disabled={!paused}
        className="h-8 w-8 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-40"
      >
        ↓
      </button>
      <button
        type="button"
        onClick={onStepOut}
        title="Step out"
        aria-label="Step out"
        disabled={!paused}
        className="h-8 w-8 text-sm rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-40"
      >
        ↑
      </button>
      <button
        type="button"
        onClick={onStop}
        title="Stop"
        aria-label="Stop"
        disabled={!active}
        className="h-8 w-8 text-sm rounded border border-rose-500/40 text-rose-300 hover:bg-rose-500/10 disabled:opacity-40"
      >
        ■
      </button>
    </div>
  );
}

function DebugPanel({
  status,
  reason,
  error,
  currentLine,
  breakpoints,
  locals,
  output,
}: {
  status: DebugStatus;
  reason: string;
  error: string | null;
  currentLine: number | null;
  breakpoints: number[];
  locals: DebugVariable[];
  output: string[];
}) {
  return (
    <aside className="min-h-0 border-t xl:border-t-0 xl:border-l border-coden-border bg-coden-surface flex flex-col">
      <div className="p-3 border-b border-coden-border">
        <div className="flex items-center justify-between gap-2">
          <div className="text-xs uppercase font-semibold text-coden-muted">Debugger</div>
          <span className={debugStatusClass(status)}>
            {status}
          </span>
        </div>
        <div className="mt-2 text-xs text-coden-muted">
          {status === 'paused' && currentLine
            ? `Paused at line ${currentLine}${reason ? ` (${reason})` : ''}`
            : 'Click the editor gutter to set breakpoints.'}
        </div>
        {error && (
          <div className="mt-2 rounded border border-rose-500/40 bg-rose-500/10 p-2 text-xs text-rose-300">
            {error}
          </div>
        )}
      </div>
      <div className="min-h-0 flex-1 overflow-y-auto p-3 space-y-4">
        <DebugSection title="Breakpoints">
          {breakpoints.length ? (
            <div className="flex flex-wrap gap-1">
              {breakpoints.map((line) => (
                <span key={line} className="rounded bg-rose-500/15 px-2 py-1 text-xs text-rose-200">
                  {line}
                </span>
              ))}
            </div>
          ) : (
            <EmptyDebugText>No breakpoints</EmptyDebugText>
          )}
        </DebugSection>
        <DebugSection title="Locals">
          {locals.length ? (
            <div className="space-y-1">
              {locals.map((variable) => (
                <LocalVariable key={variable.name} variable={variable} />
              ))}
            </div>
          ) : (
            <EmptyDebugText>No locals yet</EmptyDebugText>
          )}
        </DebugSection>
        <DebugSection title="Output">
          {output.length ? (
            <pre className="max-h-52 overflow-auto whitespace-pre-wrap rounded bg-coden-inner p-2 text-[11px] text-coden-text">
{output.join('\n')}
            </pre>
          ) : (
            <EmptyDebugText>No output yet</EmptyDebugText>
          )}
        </DebugSection>
      </div>
    </aside>
  );
}

function LocalVariable({ variable }: { variable: DebugVariable }) {
  const [expanded, setExpanded] = useState(false);
  const children = splitTopLevelItems(variable.value);
  const hasChildren = children.length > 0;
  return (
    <div className="rounded bg-coden-inner text-xs overflow-hidden">
      <button
        type="button"
        onClick={() => hasChildren && setExpanded((v) => !v)}
        className="w-full flex items-baseline gap-2 p-2 text-left hover:bg-coden-border/40"
      >
        <span className="w-3 text-coden-muted">{hasChildren ? (expanded ? '▾' : '▸') : ''}</span>
        <span className="font-mono text-coden-accent">{variable.name}</span>
        {variable.type && <span className="ml-auto text-[10px] text-coden-muted">{variable.type}</span>}
      </button>
      <div className="px-2 pb-2 pl-7 break-words font-mono text-[11px] text-coden-text">
        {compactValue(variable.value)}
      </div>
      {expanded && (
        <div className="border-t border-coden-border/50 px-2 py-1">
          {children.map((item, index) => (
            <div key={`${index}-${item}`} className="grid grid-cols-[42px_minmax(0,1fr)] gap-2 py-1 text-[11px]">
              <span className="font-mono text-coden-muted text-right">{index}</span>
              <span className="font-mono text-coden-text break-words">{item}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function compactValue(value: string): string {
  const trimmed = value.trim();
  if (trimmed.length <= 160) return trimmed;
  return `${trimmed.slice(0, 157)}...`;
}

function splitTopLevelItems(value: string): string[] {
  const trimmed = value.trim();
  const open = trimmed[0];
  const close = open === '[' ? ']' : open === '(' ? ')' : open === '{' ? '}' : '';
  if (!close || trimmed[trimmed.length - 1] !== close) return [];
  const inner = trimmed.slice(1, -1).trim();
  if (!inner) return [];
  const items: string[] = [];
  let depth = 0;
  let quote = '';
  let current = '';
  for (let i = 0; i < inner.length; i += 1) {
    const ch = inner[i]!;
    const prev = inner[i - 1];
    if (quote) {
      current += ch;
      if (ch === quote && prev !== '\\') quote = '';
      continue;
    }
    if (ch === '"' || ch === "'") {
      quote = ch;
      current += ch;
      continue;
    }
    if (ch === '[' || ch === '(' || ch === '{') depth += 1;
    if (ch === ']' || ch === ')' || ch === '}') depth -= 1;
    if (ch === ',' && depth === 0) {
      if (current.trim()) items.push(current.trim());
      current = '';
      continue;
    }
    current += ch;
  }
  if (current.trim()) items.push(current.trim());
  return items.length > 1 ? items : [];
}

function DebugSection({ title, children }: { title: string; children: ReactNode }) {
  return (
    <section>
      <div className="mb-2 text-[11px] uppercase tracking-wider text-coden-muted font-semibold">
        {title}
      </div>
      {children}
    </section>
  );
}

function EmptyDebugText({ children }: { children: ReactNode }) {
  return <div className="text-xs text-coden-muted">{children}</div>;
}

function debugStatusClass(status: DebugStatus): string {
  const base = 'rounded px-2 py-0.5 text-[11px] font-semibold uppercase';
  if (status === 'paused') return `${base} bg-amber-500/15 text-amber-300`;
  if (status === 'running' || status === 'starting') return `${base} bg-emerald-500/15 text-emerald-300`;
  if (status === 'error') return `${base} bg-rose-500/15 text-rose-300`;
  return `${base} bg-coden-inner text-coden-muted`;
}
