import { useState, useEffect, useRef } from 'react';
import type { CSSProperties, MouseEvent as ReactMouseEvent, ReactNode } from 'react';
import { createPortal } from 'react-dom';
import { Editor } from '@monaco-editor/react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGolang } from '@fortawesome/free-brands-svg-icons/faGolang';
import { faJava } from '@fortawesome/free-brands-svg-icons/faJava';
import { faJs } from '@fortawesome/free-brands-svg-icons/faJs';
import { faPython } from '@fortawesome/free-brands-svg-icons/faPython';
import { MAX_DEBUG_CASES, useAppStore } from '../../../store/useAppStore';
import type { UserTestCase } from '../../../store/useAppStore';
import { debugApi } from '../../../api/debug';
import type { DebugCapability, RunCaseResult, SupportedLanguage, TestCaseSummary } from '../../../types/api';
import { formatCaseValue } from '../../../lib/formatCaseValue';

type DebugStatus = 'idle' | 'starting' | 'running' | 'paused' | 'exited' | 'error';

interface DebugVariable {
  name: string;
  value: string;
  type?: string;
  variablesReference?: number;
  evaluateName?: string;
  indexedVariables?: number;
  namedVariables?: number;
}

interface DebugStackFrame {
  id: number;
  name: string;
  line?: number;
  column?: number;
  path?: string;
  sourceName?: string;
  userCode?: boolean;
}

interface DebugBreakpointState {
  line: number;
  requestedLine: number;
  verified: boolean;
  message?: string;
}

interface DebugWatch {
  id: string;
  expression: string;
  value: string;
  type?: string;
  variablesReference?: number;
  pending?: boolean;
  error?: string;
}

interface DebugException {
  exceptionId?: string;
  description?: string;
  breakMode?: string;
  details?: unknown;
}

interface DebugContext {
  challengeId: string;
  challengeName: string;
  language: SupportedLanguage;
  languageLabel: string;
  mode: string;
  selectedCaseIds?: string[];
  solutionPath: string;
  breakpointPath?: string;
  adapter?: string;
  inputs: Record<string, string>;
}

interface DebugErrorDetail {
  message: string;
  detail?: string;
  phase?: string;
  adapter?: string;
}

const languageOptions: Array<{ id: SupportedLanguage; label: string; monaco: string; extension: string }> = [
  { id: 'python', label: 'Python', monaco: 'python', extension: 'py' },
  { id: 'cpp', label: 'C++', monaco: 'cpp', extension: 'cpp' },
  { id: 'java', label: 'Java', monaco: 'java', extension: 'java' },
  { id: 'csharp', label: 'C#', monaco: 'csharp', extension: 'cs' },
  { id: 'javascript', label: 'JavaScript', monaco: 'javascript', extension: 'js' },
  { id: 'go', label: 'Go', monaco: 'go', extension: 'go' },
  { id: 'kotlin', label: 'Kotlin', monaco: 'kotlin', extension: 'kt' },
  { id: 'sql', label: 'SQL', monaco: 'sql', extension: 'sql' },
  { id: 'bash', label: 'Bash', monaco: 'shell', extension: 'sh' },
];

function languageMeta(language: SupportedLanguage) {
  return languageOptions.find((item) => item.id === language) ?? languageOptions[0]!;
}

function LanguageIcon({ language, teal = false }: { language: SupportedLanguage; teal?: boolean }) {
  if (language === 'python') return <FontAwesomeIcon icon={faPython} className={`h-4 w-4 ${teal ? 'text-coden-accent' : 'text-[#3776AB]'}`} aria-hidden="true" />;
  if (language === 'java') return <FontAwesomeIcon icon={faJava} className={`h-4 w-4 ${teal ? 'text-coden-accent' : 'text-[#E76F00]'}`} aria-hidden="true" />;
  if (language === 'javascript') return <FontAwesomeIcon icon={faJs} className={`h-4 w-4 ${teal ? 'text-coden-accent' : 'text-[#F7DF1E]'}`} aria-hidden="true" />;
  if (language === 'go') return <FontAwesomeIcon icon={faGolang} className={`h-5 w-5 ${teal ? 'text-coden-accent' : 'text-[#00ADD8]'}`} aria-hidden="true" />;
  if (language === 'cpp') return <span className={`text-[11px] font-black tracking-[-0.08em] ${teal ? 'text-coden-accent' : 'text-[#659AD2]'}`} aria-hidden="true">C++</span>;
  if (language === 'csharp') return <span className={`text-[11px] font-black tracking-[-0.08em] ${teal ? 'text-coden-accent' : 'text-[#9B4F96]'}`} aria-hidden="true">C#</span>;
  if (language === 'kotlin') return <span className={`${teal ? 'text-coden-accent' : 'bg-gradient-to-br from-[#7F52FF] via-[#C711E1] to-[#F88909] bg-clip-text text-transparent'} text-sm font-black`} aria-hidden="true">K</span>;
  if (language === 'sql') {
    return (
      <svg viewBox="0 0 24 24" className={`h-4 w-4 ${teal ? 'text-coden-accent' : 'text-[#4479A1]'}`} fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
        <ellipse cx="12" cy="5" rx="7" ry="3" />
        <path d="M5 5v6c0 1.7 3.1 3 7 3s7-1.3 7-3V5" />
        <path d="M5 11v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6" />
      </svg>
    );
  }
  return <span className={`font-mono text-[11px] font-black ${teal ? 'text-coden-accent' : 'text-[#4EAA25]'}`} aria-hidden="true">&gt;_</span>;
}

function LanguageSelector({
  value,
  options,
  onChange,
}: {
  value: SupportedLanguage;
  options: typeof languageOptions;
  onChange: (language: SupportedLanguage) => void;
}) {
  const [open, setOpen] = useState(false);
  const rootRef = useRef<HTMLDivElement>(null);
  const active = languageMeta(value);

  useEffect(() => {
    if (!open) return;
    const closeOutside = (event: PointerEvent) => {
      if (!rootRef.current?.contains(event.target as Node)) setOpen(false);
    };
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setOpen(false);
    };
    document.addEventListener('pointerdown', closeOutside);
    window.addEventListener('keydown', closeOnEscape);
    return () => {
      document.removeEventListener('pointerdown', closeOutside);
      window.removeEventListener('keydown', closeOnEscape);
    };
  }, [open]);

  return (
    <div ref={rootRef} className="relative">
      <button
        type="button"
        onClick={() => setOpen((current) => !current)}
        className={`flex h-8 w-9 items-center justify-center rounded border border-coden-border px-0 shadow-sm transition-colors hover:bg-coden-border/70 focus-visible:border-coden-accent focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-coden-accent/40 ${open ? 'bg-coden-border/70' : 'bg-coden-inner'}`}
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-label={`Solution language: ${active.label}`}
      >
        <span className="flex h-5 w-5 items-center justify-center"><LanguageIcon language={value} teal /></span>
      </button>
      {open && (
        <div
          role="listbox"
          aria-label="Solution languages"
          className="absolute left-0 top-full z-[80] mt-1 w-16 overflow-hidden rounded-md border border-coden-border bg-coden-surface p-1.5 shadow-2xl"
        >
          {options.map((option) => {
            const selected = option.id === value;
            return (
              <button
                key={option.id}
                type="button"
                role="option"
                aria-selected={selected}
                aria-label={option.label}
                title={option.label}
                onClick={() => {
                  setOpen(false);
                  if (!selected) onChange(option.id);
                }}
                className={`flex h-9 w-full items-center justify-center gap-1 rounded px-1 transition-colors ${selected ? 'bg-coden-border' : 'hover:bg-coden-inner'}`}
              >
                <span className="flex h-4 w-4 shrink-0 items-center justify-center text-coden-accent">
                  {selected && <svg viewBox="0 0 16 16" className="h-3.5 w-3.5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="m3 8 3 3 7-7" /></svg>}
                </span>
                <span className="flex h-5 w-5 shrink-0 items-center justify-center"><LanguageIcon language={option.id} teal /></span>
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}

function codenLanguageOptions(supportedLanguages: string[] | undefined) {
  const functionLanguages = languageOptions.filter((item) => item.id !== 'sql' && item.id !== 'bash');
  if (!supportedLanguages || supportedLanguages.length === 0) return functionLanguages;
  const supported = new Set(supportedLanguages);
  const options = languageOptions.filter((item) => supported.has(item.id));
  return options.length > 0 ? options : languageOptions;
}

function clamp(value: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, value));
}

function startPixelResize(
  event: ReactMouseEvent,
  options: {
    axis: 'x' | 'y';
    current: number;
    min: number;
    max: number;
    multiplier: 1 | -1;
    storageKey?: string;
    cursor: string;
    onChange: (value: number) => void;
    onCommit?: (value: number) => void;
  },
) {
  event.preventDefault();
  const start = options.axis === 'x' ? event.clientX : event.clientY;
  const previousCursor = document.body.style.cursor;
  const previousSelect = document.body.style.userSelect;
  document.body.style.cursor = options.cursor;
  document.body.style.userSelect = 'none';
  let latest = options.current;

  const handleMove = (moveEvent: MouseEvent) => {
    const current = options.axis === 'x' ? moveEvent.clientX : moveEvent.clientY;
    const next = clamp(options.current + (current - start) * options.multiplier, options.min, options.max);
    latest = next;
    options.onChange(next);
    if (options.storageKey) window.localStorage.setItem(options.storageKey, String(Math.round(next)));
  };
  const handleUp = () => {
    document.body.style.cursor = previousCursor;
    document.body.style.userSelect = previousSelect;
    window.removeEventListener('mousemove', handleMove);
    window.removeEventListener('mouseup', handleUp);
    options.onCommit?.(latest);
  };
  window.addEventListener('mousemove', handleMove);
  window.addEventListener('mouseup', handleUp);
}

function startPercentResize(
  event: ReactMouseEvent,
  container: HTMLElement | null,
  storageKey: string,
  onChange: (value: number) => void,
) {
  if (!container) return;
  event.preventDefault();
  const previousCursor = document.body.style.cursor;
  const previousSelect = document.body.style.userSelect;
  document.body.style.cursor = 'col-resize';
  document.body.style.userSelect = 'none';

  const handleMove = (moveEvent: MouseEvent) => {
    const rect = container.getBoundingClientRect();
    if (rect.width <= 0) return;
    const next = clamp(((moveEvent.clientX - rect.left) / rect.width) * 100, 28, 72);
    onChange(next);
    window.localStorage.setItem(storageKey, String(Math.round(next)));
  };
  const handleUp = () => {
    document.body.style.cursor = previousCursor;
    document.body.style.userSelect = previousSelect;
    window.removeEventListener('mousemove', handleMove);
    window.removeEventListener('mouseup', handleUp);
  };
  window.addEventListener('mousemove', handleMove);
  window.addEventListener('mouseup', handleUp);
}

export function CodenTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const theme = useAppStore((s) => s.theme);

  const source = useAppStore((s) => s.source);
  const codeLanguage = useAppStore((s) => s.codeLanguage);
  const setMode = useAppStore((s) => s.setMode);
  const selectedCaseIds = useAppStore((s) => s.selectedCaseIds);
  const setSelectedCaseIds = useAppStore((s) => s.setSelectedCaseIds);
  const run = useAppStore((s) => s.run);
  const runResult = useAppStore((s) => s.runResult);
  const isRunning = useAppStore((s) => s.isRunning);
  const userCases = useAppStore((s) => s.userCases);
  const addUserCase = useAppStore((s) => s.addUserCase);
  const updateUserCase = useAppStore((s) => s.updateUserCase);
  const deleteUserCase = useAppStore((s) => s.deleteUserCase);
  const runError = useAppStore((s) => s.error);
  const activeVersion = useAppStore((s) => s.activeVersion);
  const versions = useAppStore((s) => s.versions);
  const versionNames = useAppStore((s) => s.versionNames);
  const modifiedVersions = useAppStore((s) => s.modifiedVersions);
  const switchVersion = useAppStore((s) => s.switchVersion);
  const renameVersion = useAppStore((s) => s.renameVersion);
  const resetVersion = useAppStore((s) => s.resetVersion);

  const saveSource = useAppStore((s) => s.saveSource);
  const setCodeLanguage = useAppStore((s) => s.setCodeLanguage);
  const [isMaximized, setIsMaximized] = useState(false);
  const [workspacePanel, setWorkspacePanel] = useState<'cases' | 'debugger'>('cases');
  const [resetRequest, setResetRequest] = useState<number | null>(null);

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
  const frameIdRef = useRef<number | null>(null);
  const variableRequestsRef = useRef(new Map<string, (variables: DebugVariable[]) => void>());
  const watchCounterRef = useRef(0);
  const debugWatchesRef = useRef<DebugWatch[]>([]);
  const [breakpoints, setBreakpoints] = useState<number[]>([]);
  const [debugBreakpointStates, setDebugBreakpointStates] = useState<DebugBreakpointState[]>([]);
  const [debugStatus, setDebugStatus] = useState<DebugStatus>('idle');
  const [debugCurrentLine, setDebugCurrentLine] = useState<number | null>(null);
  const [debugError, setDebugError] = useState<string | null>(null);
  const [debugErrorDetail, setDebugErrorDetail] = useState<DebugErrorDetail | null>(null);
  const [debugReason, setDebugReason] = useState<string>('');
  const [debugLocals, setDebugLocals] = useState<DebugVariable[]>([]);
  const [debugFrames, setDebugFrames] = useState<DebugStackFrame[]>([]);
  const [debugFrameId, setDebugFrameId] = useState<number | null>(null);
  const [debugWatches, setDebugWatches] = useState<DebugWatch[]>([]);
  const [debugException, setDebugException] = useState<DebugException | null>(null);
  const [debugOutput, setDebugOutput] = useState<string[]>([]);
  const [debugContext, setDebugContext] = useState<DebugContext | null>(null);
  const [debugCapabilities, setDebugCapabilities] = useState<Record<SupportedLanguage, DebugCapability> | null>(null);
  const [debugCapabilitiesLoaded, setDebugCapabilitiesLoaded] = useState(false);
  const activeDebugCapability = debugCapabilities?.[codeLanguage] ?? null;
  const runnableInCoden = detail?.runnable_in_coden !== false;
  const runtimeUnavailableReason = runnableInCoden
    ? ''
    : `${detail?.leetcode_category_title || 'This LeetCode category'} is tracked for LeetCode subsets and tags, but it is not runnable in cOde(n) yet.`;
  const selectableLanguageOptions = runnableInCoden ? codenLanguageOptions(detail?.supported_languages) : languageOptions;
  const paneFontScales = useAppStore((s) => s.paneFontScales);
  const paneSizes = useAppStore((s) => s.paneSizes);
  const setPaneSize = useAppStore((s) => s.setPaneSize);
  const savePaneSizesToBackend = useAppStore((s) => s.savePaneSizesToBackend);
  const debugPanelWidth = clamp(paneSizes['coden.debugPanelWidth'] ?? 400, 320, 720);
  const codenFontScale = paneFontScales['workspace:coden'] ?? 1;
  const editorFontSize = Math.round(14 * codenFontScale * 10) / 10;
  const setDebugPanelWidth = (width: number) => setPaneSize('coden.debugPanelWidth', width);
  const editorLayoutStyle = { '--debug-panel-width': `${debugPanelWidth}px` } as CSSProperties;

  useEffect(() => {
    debugWatchesRef.current = debugWatches;
  }, [debugWatches]);

  // Sync external changes, such as a version switch.
  useEffect(() => {
    setEditorValue(source);
  }, [source]);

  useEffect(() => {
    setBreakpoints([]);
    setDebugBreakpointStates([]);
    setDebugCurrentLine(null);
    setDebugStatus('idle');
    setDebugError(null);
    setDebugErrorDetail(null);
    setDebugReason('');
    setDebugLocals([]);
    setDebugFrames([]);
    setDebugFrameId(null);
    frameIdRef.current = null;
    setDebugException(null);
    setDebugOutput([]);
    setDebugContext(null);
    setWorkspacePanel('cases');
    stopDebugSession();
  }, [detail?.id, activeVersion, codeLanguage]);

  useEffect(() => {
    updateEditorDecorations();
  }, [breakpoints, debugBreakpointStates, debugCurrentLine]);

  useEffect(() => {
    return () => {
      stopDebugSession();
      if (saveTimeout.current) {
        window.clearTimeout(saveTimeout.current);
      }
    };
  }, []);

  useEffect(() => {
    let active = true;
    debugApi.getCapabilities()
      .then((response) => {
        if (active) {
          setDebugCapabilities(response.languages);
          setDebugCapabilitiesLoaded(true);
        }
      })
      .catch(() => {
        if (active) {
          setDebugCapabilities(null);
          setDebugCapabilitiesLoaded(true);
        }
      });
    return () => {
      active = false;
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

  async function handleSwitchVersion(version: number) {
    if (version === activeVersion) return;
    if (saveTimeout.current) {
      window.clearTimeout(saveTimeout.current);
      saveTimeout.current = null;
      await saveSource(editorValue);
    }
    await switchVersion(version);
  }

  async function resetSolutionVersion(version: number) {
    if (version === activeVersion && saveTimeout.current) {
      window.clearTimeout(saveTimeout.current);
      saveTimeout.current = null;
    }
    await resetVersion(version);
  }

  async function handleRealRun() {
    if (saveTimeout.current) {
      window.clearTimeout(saveTimeout.current);
      saveTimeout.current = null;
      await saveSource(editorValue);
    }
    setMode('real_test');
    await run();
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
          glyphMarginClassName: debugBreakpointStates.find((item) => item.requestedLine === line && !item.verified)
            ? 'coden-debug-breakpoint coden-debug-breakpoint-unverified'
            : 'coden-debug-breakpoint',
          glyphMarginHoverMessage: {
            value: debugBreakpointStates.find((item) => item.requestedLine === line)?.message || `Breakpoint at line ${line}`,
          },
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

  function setEditorDebugError(line: number | null, message?: string) {
    const editor = editorRef.current;
    const monaco = monacoRef.current;
    if (!editor || !monaco) return;
    const model = editor.getModel();
    if (!model) return;
    const markers = line && message ? [{
      startLineNumber: line,
      startColumn: 1,
      endLineNumber: line,
      endColumn: Math.max(2, model.getLineMaxColumn(line)),
      message,
      severity: monaco.MarkerSeverity.Error,
      source: 'debugger',
    }] : [];
    monaco.editor.setModelMarkers(model, 'coden-debugger', markers);
  }

  function handleEditorMount(editor: any, monaco: any) {
    editorRef.current = editor;
    monacoRef.current = monaco;
    editor.onMouseDown((event: any) => {
      const targetType = event.target?.type;
      const gutterType = monaco.editor.MouseTargetType.GUTTER_GLYPH_MARGIN;
      const lineNumberType = monaco.editor.MouseTargetType.GUTTER_LINE_NUMBERS;
      const lineDecorationsType = monaco.editor.MouseTargetType.GUTTER_LINE_DECORATIONS;
      const lineNumber = event.target?.position?.lineNumber ?? event.target?.range?.startLineNumber;
      if (
        (targetType === gutterType || targetType === lineNumberType || targetType === lineDecorationsType)
        && typeof lineNumber === 'number'
      ) {
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
      sendDebugMessage({ type: 'setBreakpoints', challengeId: detail?.id, language: codeLanguage, breakpoints: next });
      setDebugBreakpointStates((states) => [
        ...states.filter((item) => next.includes(item.requestedLine)),
        ...next.filter((line) => !states.some((item) => item.requestedLine === line)).map((line) => ({
          line,
          requestedLine: line,
          verified: false,
          message: 'Waiting for the debugger to verify this breakpoint.',
        })),
      ]);
      return next;
    });
  }

  function sendDebugMessage(payload: Record<string, unknown>) {
    const ws = wsRef.current;
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(payload));
    }
  }

  function requestDebugVariables(variablesReference: number): Promise<DebugVariable[]> {
    if (!variablesReference) return Promise.resolve([]);
    return new Promise((resolve) => {
      const requestId = `variables-${Date.now()}-${Math.random().toString(36).slice(2)}`;
      variableRequestsRef.current.set(requestId, resolve);
      sendDebugMessage({ type: 'variables', variablesReference, requestId });
      window.setTimeout(() => {
        const pending = variableRequestsRef.current.get(requestId);
        if (pending) {
          variableRequestsRef.current.delete(requestId);
          pending([]);
        }
      }, 3000);
    });
  }

  function evaluateDebugWatches(frameId: number | null = frameIdRef.current) {
    if (!frameId) return;
    const watches = debugWatchesRef.current;
    setDebugWatches((current) => current.map((watch) => ({ ...watch, pending: true, error: undefined })));
    watches.forEach((watch) => {
      sendDebugMessage({ type: 'evaluate', expression: watch.expression, frameId, requestId: watch.id });
    });
  }

  function addDebugWatch(expression: string) {
    const trimmed = expression.trim();
    if (!trimmed || debugWatchesRef.current.some((watch) => watch.expression === trimmed)) return;
    const watch: DebugWatch = {
      id: `watch-${Date.now()}-${watchCounterRef.current += 1}`,
      expression: trimmed,
      value: '',
      pending: debugStatus === 'paused',
    };
    const next = [...debugWatchesRef.current, watch];
    debugWatchesRef.current = next;
    setDebugWatches(next);
    if (debugStatus === 'paused' && frameIdRef.current) {
      sendDebugMessage({ type: 'evaluate', expression: trimmed, frameId: frameIdRef.current, requestId: watch.id });
    }
  }

  function removeDebugWatch(id: string) {
    setDebugWatches((current) => current.filter((watch) => watch.id !== id));
  }

  function selectDebugFrame(frame: DebugStackFrame) {
    frameIdRef.current = frame.id;
    setDebugFrameId(frame.id);
    setDebugCurrentLine(typeof frame.line === 'number' ? frame.line : null);
    sendDebugMessage({ type: 'selectFrame', frameId: frame.id });
  }

  async function startDebugSession() {
    if (!detail) return;
    const visibleCaseIds = new Set([
      ...detail.test_cases.map((testCase) => testCase.id),
      ...userCases.map((testCase) => testCase.id),
    ]);
    const debugCaseId = selectedCaseIds.find((caseId) => visibleCaseIds.has(caseId))
      || detail.test_cases[0]?.id
      || userCases[0]?.id;
    if (!debugCaseId) {
      setDebugStatus('error');
      setDebugError('Select or create one visible case before starting Debug.');
      setDebugErrorDetail({ message: 'Debug requires exactly one visible or custom case.', phase: 'input' });
      return;
    }
    setMode('practice');
    setSelectedCaseIds([debugCaseId]);
    setWorkspacePanel('debugger');
    if (!runnableInCoden) {
      setDebugStatus('error');
      setDebugError(runtimeUnavailableReason);
      setDebugErrorDetail({ message: runtimeUnavailableReason, phase: 'runtime' });
      return;
    }
    if (activeDebugCapability && !activeDebugCapability.available) {
      setDebugStatus('error');
      setDebugError(activeDebugCapability.message);
      return;
    }
    if (saveTimeout.current) {
      window.clearTimeout(saveTimeout.current);
      saveTimeout.current = null;
    }
    await saveSource(editorValue);
    stopDebugSession(false);

    setDebugStatus('starting');
    setDebugError(null);
    setDebugErrorDetail(null);
    setDebugReason('');
    setDebugCurrentLine(null);
    setDebugLocals([]);
    setDebugFrames([]);
    setDebugFrameId(null);
    frameIdRef.current = null;
    setDebugException(null);
    setEditorDebugError(null);
    setDebugOutput([]);
    setDebugContext(null);

    let customInput: Record<string, unknown> | null = null;
    const selectedUserCase = userCases.find((testCase) => testCase.id === debugCaseId);
    if (selectedUserCase) {
      try {
        const parsed = JSON.parse(selectedUserCase.input);
        if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
          throw new Error('Custom input must be a JSON object matching solve(...) parameters.');
        }
        customInput = parsed as Record<string, unknown>;
      } catch (e) {
        setDebugStatus('error');
        setDebugError((e as Error).message);
        setDebugErrorDetail({ message: (e as Error).message, phase: 'input' });
        return;
      }
    }

    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const ws = new WebSocket(`${protocol}//${window.location.host}/api/debug/ws`);
    wsRef.current = ws;
    ws.onopen = () => {
      ws.send(JSON.stringify({
        type: 'start',
        challengeId: detail.id,
        mode: 'practice',
        language: codeLanguage,
        breakpoints,
        caseIds: [debugCaseId],
        customInput,
      }));
    };
    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.type === 'started') {
        setDebugStatus('running');
      } else if (msg.type === 'context') {
        setDebugContext(msg as DebugContext);
      } else if (msg.type === 'stopped') {
        threadIdRef.current = msg.threadId ?? null;
        frameIdRef.current = msg.frameId ?? null;
        setDebugStatus('paused');
        setDebugCurrentLine(typeof msg.line === 'number' ? msg.line : null);
        setDebugReason(msg.reason ?? 'paused');
        setDebugLocals(Array.isArray(msg.locals) ? msg.locals : []);
        setDebugFrames(Array.isArray(msg.frames) ? msg.frames : []);
        setDebugFrameId(typeof msg.frameId === 'number' ? msg.frameId : null);
        setDebugException(msg.exception ?? null);
        setEditorDebugError(
          typeof msg.line === 'number' && msg.exception ? msg.line : null,
          msg.exception?.description || msg.exception?.exceptionId,
        );
        window.setTimeout(() => evaluateDebugWatches(msg.frameId ?? null), 0);
        if (typeof msg.line === 'number') {
          editorRef.current?.revealLineInCenter(msg.line);
        }
      } else if (msg.type === 'continued') {
        setDebugStatus('running');
        setDebugCurrentLine(null);
        setDebugException(null);
        setEditorDebugError(null);
        setDebugLocals([]);
      } else if (msg.type === 'breakpoints') {
        setDebugBreakpointStates(Array.isArray(msg.breakpoints) ? msg.breakpoints : []);
      } else if (msg.type === 'frame') {
        frameIdRef.current = typeof msg.frameId === 'number' ? msg.frameId : frameIdRef.current;
        setDebugFrameId(frameIdRef.current);
        setDebugLocals(Array.isArray(msg.locals) ? msg.locals : []);
        window.setTimeout(() => evaluateDebugWatches(frameIdRef.current), 0);
      } else if (msg.type === 'variables') {
        const resolve = variableRequestsRef.current.get(String(msg.requestId));
        if (resolve) {
          variableRequestsRef.current.delete(String(msg.requestId));
          resolve(Array.isArray(msg.variables) ? msg.variables : []);
        }
      } else if (msg.type === 'watchResult') {
        setDebugWatches((current) => current.map((watch) => watch.id === msg.requestId ? {
          ...watch,
          value: String(msg.result ?? ''),
          type: String(msg.typeName ?? ''),
          variablesReference: Number(msg.variablesReference ?? 0),
          pending: false,
          error: msg.error ? String(msg.error) : undefined,
        } : watch));
      } else if (msg.type === 'output') {
        if (msg.output) {
          setDebugOutput((prev) => [...prev.slice(-200), String(msg.output).trimEnd()]);
        }
      } else if (msg.type === 'exited') {
        setDebugStatus('exited');
        setDebugCurrentLine(null);
        setDebugLocals([]);
        setEditorDebugError(null);
      } else if (msg.type === 'error') {
        setDebugStatus('error');
        const errorDetail = {
          message: msg.message ?? 'Debugger error',
          detail: msg.detail,
          phase: msg.phase,
          adapter: msg.adapter,
        };
        setDebugError(errorDetail.message);
        setDebugErrorDetail(errorDetail);
      }
    };
    ws.onerror = () => {
      setDebugStatus('error');
      setDebugError('Debugger WebSocket failed.');
      setDebugErrorDetail({ message: 'Debugger WebSocket failed.', phase: 'transport' });
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

  const debugControls = (
    <DebugToolbar
      status={debugStatus}
      unavailableReason={runtimeUnavailableReason || (activeDebugCapability && !activeDebugCapability.available ? activeDebugCapability.message : undefined)}
      installHint={activeDebugCapability?.install_hint}
      onStart={() => void startDebugSession()}
      onContinue={() => debugCommand('continue')}
      onStepOver={() => debugCommand('stepOver')}
      onStepIn={() => debugCommand('stepIn')}
      onStepOut={() => debugCommand('stepOut')}
      onStop={() => {
        stopDebugSession();
        setDebugStatus('idle');
        setDebugCurrentLine(null);
        setWorkspacePanel('cases');
      }}
    />
  );

  return (
    <div className="flex flex-col h-full relative">
      {resetRequest !== null && createPortal(
        <ResetSolutionDialog
          label={versionNames[resetRequest] || `Version ${resetRequest}`}
          onCancel={() => setResetRequest(null)}
          onConfirm={() => {
            const version = resetRequest;
            setResetRequest(null);
            void resetSolutionVersion(version);
          }}
        />,
        document.body,
      )}
      {/* Code Preview */}
      {!isMaximized && (
        <div className="flex-1 flex flex-col min-h-0 bg-coden-inner rounded-xl border border-coden-border overflow-hidden shadow-inner">
          <div
            className="flex-1 min-h-0 grid grid-cols-1 lg:grid-cols-none lg:[grid-template-columns:minmax(0,1fr)_6px_var(--debug-panel-width)]"
            style={editorLayoutStyle}
          >
            <div className="flex min-h-[360px] min-w-0 flex-col overflow-hidden">
              <div className="flex flex-wrap items-center justify-between gap-3 border-b border-coden-border bg-coden-surface px-4 py-2">
                <div className="flex min-w-0 flex-wrap items-center gap-2">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">Versions</span>
                  <EditorVersionControls
                    versions={versions}
                    activeVersion={activeVersion}
                    versionNames={versionNames}
                    modifiedVersions={modifiedVersions}
                    onSwitch={(version) => void handleSwitchVersion(version)}
                    onRename={(version, name) => void renameVersion(version, name)}
                    onReset={setResetRequest}
                  />
                  <span className="ml-1 text-[10px] font-bold uppercase tracking-wider text-coden-muted">Language</span>
                  <LanguageSelector
                    value={codeLanguage}
                    options={selectableLanguageOptions}
                    onChange={(language) => void setCodeLanguage(language)}
                  />
                </div>
                <div className="flex shrink-0 items-center gap-2">
                  <EditorRunControls
                    isRunning={isRunning}
                    disabledReason={runtimeUnavailableReason}
                    onRun={() => void handleRealRun()}
                    onReset={() => setResetRequest(activeVersion)}
                  />
                  <FocusModeButton onClick={() => setIsMaximized(true)} />
                </div>
              </div>
              <div className="min-h-0 flex-1 overflow-hidden">
                <Editor
                height="100%"
                language={languageMeta(codeLanguage).monaco}
                theme={theme === 'dark' ? 'vs-dark' : 'light'}
                value={editorValue}
                onMount={handleEditorMount}
                onChange={handleEditorChange}
                options={{
                  minimap: { enabled: false },
                  fontSize: editorFontSize,
                  fontFamily: "'Cascadia Code', 'Cascadia Mono', Consolas, 'SFMono-Regular', monospace",
                  scrollBeyondLastLine: false,
                  wordWrap: 'on',
                  glyphMargin: true,
                  lineDecorationsWidth: 4,
                  lineNumbersMinChars: 2,
                  automaticLayout: true,
                  padding: { top: 16, bottom: 16 },
                }}
                loading={
                  <div className="flex h-full items-center justify-center text-coden-muted text-sm">
                    Loading editor...
                  </div>
                }
                />
              </div>
            </div>
            <button
              type="button"
              aria-label="Resize side workspace"
              title="Resize side workspace"
              onMouseDown={(event) => startPixelResize(event, {
                axis: 'x',
                current: debugPanelWidth,
                min: 280,
                max: 620,
                multiplier: -1,
                cursor: 'col-resize',
                onChange: setDebugPanelWidth,
                onCommit: () => void savePaneSizesToBackend(),
              })}
              className="hidden lg:block cursor-col-resize border-x border-coden-border/60 bg-coden-border/30 hover:bg-coden-accent/40"
            />
            {workspacePanel === 'debugger' ? (
              <DebuggerWorkspacePanel
                controls={debugControls}
                status={debugStatus}
                reason={debugReason}
                error={debugError}
                errorDetail={debugErrorDetail}
                currentLine={debugCurrentLine}
                breakpoints={breakpoints}
                breakpointStates={debugBreakpointStates}
                locals={debugLocals}
                frames={debugFrames}
                activeFrameId={debugFrameId}
                watches={debugWatches}
                exception={debugException}
                output={debugOutput}
                context={debugContext}
                capability={activeDebugCapability}
                capabilityLoaded={debugCapabilitiesLoaded}
                languageLabel={languageMeta(codeLanguage).label}
                onSelectFrame={selectDebugFrame}
                onAddWatch={addDebugWatch}
                onRemoveWatch={removeDebugWatch}
                onLoadVariables={requestDebugVariables}
                onRemoveBreakpoint={toggleBreakpoint}
              />
            ) : (
              <CasesWorkspacePanel
                controls={debugControls}
                systemCases={detail.test_cases}
                userCases={userCases}
                selectedCaseIds={selectedCaseIds}
                result={runResult}
                error={runError}
                disabledReason={runtimeUnavailableReason}
                environmentCategory={detail.leetcode_category}
                expectedParams={detail.params.map((param) => param.name)}
                onSelectCase={(id) => setSelectedCaseIds([id])}
                onAddUserCase={addUserCase}
                onUpdateUserCase={updateUserCase}
                onDeleteUserCase={deleteUserCase}
              />
            )}
          </div>
        </div>
      )}

      {/* Maximized Code Preview Portal */}
      {isMaximized && createPortal(
        <div className="fixed inset-0 z-[9999] overflow-hidden bg-coden-bg" data-font-scope="workspace:coden">
          <div className="flex h-full w-full flex-col">
          <div
            className="flex-1 min-h-0 grid grid-cols-1 lg:grid-cols-none lg:[grid-template-columns:minmax(0,1fr)_6px_var(--debug-panel-width)]"
            style={editorLayoutStyle}
          >
            <div className="flex min-w-0 flex-col overflow-hidden">
              <div className="flex flex-wrap items-center justify-between gap-3 border-b border-coden-border bg-coden-surface px-4 py-2">
                <div className="flex min-w-0 flex-wrap items-center gap-2">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">Versions</span>
                  <EditorVersionControls
                    versions={versions}
                    activeVersion={activeVersion}
                    versionNames={versionNames}
                    modifiedVersions={modifiedVersions}
                    onSwitch={(version) => void handleSwitchVersion(version)}
                    onRename={(version, name) => void renameVersion(version, name)}
                    onReset={setResetRequest}
                  />
                  <span className="ml-1 text-[10px] font-bold uppercase tracking-wider text-coden-muted">Language</span>
                  <LanguageSelector
                    value={codeLanguage}
                    options={selectableLanguageOptions}
                    onChange={(language) => void setCodeLanguage(language)}
                  />
                </div>
                <div className="flex shrink-0 items-center gap-2">
                  <EditorRunControls
                    isRunning={isRunning}
                    disabledReason={runtimeUnavailableReason}
                    onRun={() => void handleRealRun()}
                    onReset={() => setResetRequest(activeVersion)}
                  />
                  <FocusModeButton active onClick={() => setIsMaximized(false)} />
                </div>
              </div>
              <div className="min-h-0 flex-1 overflow-hidden">
                <Editor
                height="100%"
                language={languageMeta(codeLanguage).monaco}
                theme={theme === 'dark' ? 'vs-dark' : 'light'}
                value={editorValue}
                onMount={handleEditorMount}
                onChange={handleEditorChange}
                options={{
                  minimap: { enabled: false },
                  fontSize: editorFontSize,
                  fontFamily: "'Cascadia Code', 'Cascadia Mono', Consolas, 'SFMono-Regular', monospace",
                  scrollBeyondLastLine: false,
                  wordWrap: 'on',
                  glyphMargin: true,
                  lineDecorationsWidth: 4,
                  lineNumbersMinChars: 2,
                  automaticLayout: true,
                  padding: { top: 16, bottom: 16 },
                }}
                loading={
                  <div className="flex h-full items-center justify-center text-coden-muted text-sm">
                    Loading editor...
                  </div>
                }
                />
              </div>
            </div>
            <button
              type="button"
              aria-label="Resize side workspace"
              title="Resize side workspace"
              onMouseDown={(event) => startPixelResize(event, {
                axis: 'x',
                current: debugPanelWidth,
                min: 280,
                max: 720,
                multiplier: -1,
                cursor: 'col-resize',
                onChange: setDebugPanelWidth,
                onCommit: () => void savePaneSizesToBackend(),
              })}
              className="hidden lg:block cursor-col-resize border-x border-coden-border/60 bg-coden-border/30 hover:bg-coden-accent/40"
            />
            {workspacePanel === 'debugger' ? (
              <DebuggerWorkspacePanel
                controls={debugControls}
                status={debugStatus}
                reason={debugReason}
                error={debugError}
                errorDetail={debugErrorDetail}
                currentLine={debugCurrentLine}
                breakpoints={breakpoints}
                breakpointStates={debugBreakpointStates}
                locals={debugLocals}
                frames={debugFrames}
                activeFrameId={debugFrameId}
                watches={debugWatches}
                exception={debugException}
                output={debugOutput}
                context={debugContext}
                capability={activeDebugCapability}
                capabilityLoaded={debugCapabilitiesLoaded}
                languageLabel={languageMeta(codeLanguage).label}
                onSelectFrame={selectDebugFrame}
                onAddWatch={addDebugWatch}
                onRemoveWatch={removeDebugWatch}
                onLoadVariables={requestDebugVariables}
                onRemoveBreakpoint={toggleBreakpoint}
              />
            ) : (
              <CasesWorkspacePanel
                controls={debugControls}
                systemCases={detail.test_cases}
                userCases={userCases}
                selectedCaseIds={selectedCaseIds}
                result={runResult}
                error={runError}
                disabledReason={runtimeUnavailableReason}
                environmentCategory={detail.leetcode_category}
                expectedParams={detail.params.map((param) => param.name)}
                onSelectCase={(id) => setSelectedCaseIds([id])}
                onAddUserCase={addUserCase}
                onUpdateUserCase={updateUserCase}
                onDeleteUserCase={deleteUserCase}
              />
            )}
          </div>
          </div>
        </div>,
        document.body
      )}
    </div>
  );
}

function EditorVersionControls({
  versions,
  activeVersion,
  versionNames,
  modifiedVersions,
  onSwitch,
  onRename,
  onReset,
}: {
  versions: number[];
  activeVersion: number;
  versionNames: Record<number, string>;
  modifiedVersions: number[];
  onSwitch: (version: number) => void;
  onRename: (version: number, name: string) => void;
  onReset: (version: number) => void;
}) {
  const [editingVersion, setEditingVersion] = useState<number | null>(null);
  const [editName, setEditName] = useState('');
  const [contextMenu, setContextMenu] = useState<{ version: number; x: number; y: number } | null>(null);

  useEffect(() => {
    if (!contextMenu) return;
    const close = () => setContextMenu(null);
    window.addEventListener('click', close);
    return () => window.removeEventListener('click', close);
  }, [contextMenu]);

  const startRename = (version: number) => {
    setEditingVersion(version);
    setEditName(versionNames[version] || `Version ${version}`);
    setContextMenu(null);
  };

  const finishRename = (version: number) => {
    if (editingVersion === version) {
      onRename(version, editName.trim() || `Version ${version}`);
    }
    setEditingVersion(null);
  };

  const resetNamedVersion = (version: number) => {
    onReset(version);
    setContextMenu(null);
  };

  return (
    <div className="relative inline-flex items-center gap-1 rounded-md border border-coden-border bg-coden-inner p-1" aria-label="Solution versions">
      {[1, 2, 3].map((version) => {
        const active = version === activeVersion;
        const modified = modifiedVersions.includes(version);
        const available = versions.includes(version);
        return editingVersion === version ? (
          <input
            key={version}
            autoFocus
            value={editName}
            onChange={(event) => setEditName(event.target.value)}
            onBlur={() => finishRename(version)}
            onKeyDown={(event) => {
              if (event.key === 'Enter') finishRename(version);
              if (event.key === 'Escape') setEditingVersion(null);
            }}
            className={`h-6 w-24 rounded border border-coden-accent bg-coden-bg px-2 text-xs text-coden-text outline-none ${version > 1 ? 'relative ml-1 before:absolute before:-left-1 before:top-1 before:h-4 before:w-px before:bg-coden-border' : ''}`}
            aria-label={`Rename version ${version}`}
          />
        ) : (
          <button
            key={version}
            type="button"
            disabled={!available}
            onClick={() => !active && onSwitch(version)}
            onDoubleClick={() => startRename(version)}
            onContextMenu={(event: ReactMouseEvent) => {
              event.preventDefault();
              setContextMenu({ version, x: event.clientX, y: event.clientY });
            }}
            title={`${versionNames[version] || `Version ${version}`} · double-click to rename · right-click for options`}
            className={[
              'h-6 min-w-6 rounded px-1.5 text-xs font-semibold tabular-nums transition-colors disabled:opacity-40',
              version > 1 ? 'relative ml-1 before:absolute before:-left-1 before:top-1 before:h-4 before:w-px before:bg-coden-border' : '',
              active
                ? 'bg-coden-accent text-coden-accentContrast'
                : modified
                  ? 'bg-amber-500/15 text-amber-400 hover:bg-amber-500/25'
                  : 'text-coden-muted hover:bg-coden-border hover:text-coden-text',
            ].join(' ')}
          >
            {version}
          </button>
        );
      })}
      {contextMenu && createPortal(
        <div
          className="fixed z-[10000] w-40 rounded-md border border-coden-border bg-coden-surface py-1 text-xs text-coden-text shadow-xl"
          style={{ left: contextMenu.x, top: contextMenu.y }}
          onClick={(event) => event.stopPropagation()}
        >
          <button type="button" onClick={() => startRename(contextMenu.version)} className="w-full px-3 py-2 text-left hover:bg-coden-border">
            Rename version
          </button>
          <button type="button" onClick={() => resetNamedVersion(contextMenu.version)} className="w-full px-3 py-2 text-left font-semibold text-rose-400 hover:bg-rose-950/40">
            Reset solution
          </button>
        </div>,
        document.body,
      )}
    </div>
  );
}

function EditorRunControls({
  isRunning,
  disabledReason,
  onRun,
  onReset,
}: {
  isRunning: boolean;
  disabledReason?: string;
  onRun: () => void;
  onReset: () => void;
}) {
  return (
    <div className="inline-flex items-center overflow-hidden rounded-md border border-coden-border bg-coden-inner">
      <button
        type="button"
        onClick={onRun}
        disabled={isRunning || Boolean(disabledReason)}
        title={disabledReason || 'Run active solution against hidden real-test cases'}
        aria-label="Run active solution against real tests"
        className="h-8 w-10 bg-coden-accent text-sm font-semibold text-coden-accentContrast hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-45"
      >
        {isRunning ? '…' : '▶'}
      </button>
      <button
        type="button"
        onClick={onReset}
        disabled={isRunning}
        title="Reset active solution version to its starter code"
        aria-label="Reset active solution version"
        className="h-8 w-10 border-l border-rose-400/50 bg-rose-600 text-base font-bold text-white hover:bg-rose-500 disabled:cursor-not-allowed disabled:opacity-45"
      >
        ↻
      </button>
    </div>
  );
}

function FocusModeButton({ active = false, onClick }: { active?: boolean; onClick: () => void }) {
  const label = active ? 'Exit focus mode' : 'Enter focus mode';
  return (
    <button
      type="button"
      onClick={onClick}
      title={label}
      aria-label={label}
      aria-pressed={active}
      className={`group flex h-9 w-10 shrink-0 items-center justify-center rounded-lg border border-yellow-100/90 bg-gradient-to-br from-yellow-300 via-amber-400 to-orange-500 text-lg font-black text-amber-950 shadow-[0_0_18px_rgba(245,158,11,0.62)] transition duration-200 hover:scale-105 hover:brightness-110 hover:shadow-[0_0_26px_rgba(250,204,21,0.82)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-yellow-200 focus-visible:ring-offset-2 focus-visible:ring-offset-coden-surface ${active ? 'ring-2 ring-yellow-100/90' : ''}`}
    >
      <span aria-hidden="true" className={`drop-shadow-sm transition-transform duration-200 group-hover:scale-110 ${active ? 'text-[10px] tracking-wider' : ''}`}>
        {active ? 'ESC' : '⛶'}
      </span>
    </button>
  );
}

function ResetSolutionDialog({
  label,
  onCancel,
  onConfirm,
}: {
  label: string;
  onCancel: () => void;
  onConfirm: () => void;
}) {
  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') onCancel();
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [onCancel]);

  return (
    <div className="fixed inset-0 z-[11000] flex items-center justify-center bg-black/75 p-4" role="presentation" onMouseDown={onCancel}>
      <div
        role="alertdialog"
        aria-modal="true"
        aria-labelledby="reset-solution-title"
        className="w-full max-w-md rounded-xl border border-rose-500/60 bg-coden-surface p-5 text-coden-text shadow-2xl"
        onMouseDown={(event) => event.stopPropagation()}
      >
        <div className="mb-1 text-xs font-bold uppercase tracking-wider text-rose-400">Danger</div>
        <h2 id="reset-solution-title" className="text-base font-bold">Reset {label}?</h2>
        <p className="mt-2 text-sm leading-6 text-coden-muted">
          This replaces the current code in this version with the starter solution. This action cannot be undone.
        </p>
        <div className="mt-5 flex justify-end gap-2">
          <button
            type="button"
            autoFocus
            onClick={onCancel}
            className="h-9 rounded-md border border-coden-border px-4 text-sm font-semibold text-coden-text hover:bg-coden-border"
          >
            No
          </button>
          <button
            type="button"
            onClick={onConfirm}
            className="h-9 rounded-md bg-rose-600 px-4 text-sm font-bold text-white hover:bg-rose-500"
          >
            Yes, reset
          </button>
        </div>
      </div>
    </div>
  );
}

async function copyTextToClipboard(value: string): Promise<void> {
  if (navigator.clipboard?.writeText) {
    await navigator.clipboard.writeText(value);
    return;
  }
  const textarea = document.createElement('textarea');
  textarea.value = value;
  textarea.setAttribute('readonly', '');
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  const copied = document.execCommand('copy');
  textarea.remove();
  if (!copied) throw new Error('Clipboard copy failed.');
}

function formatJsonForCopy(value: string): string {
  try {
    return JSON.stringify(JSON.parse(value), null, 2);
  } catch {
    return value;
  }
}

function isJsonObject(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function validateRows(value: unknown, label: string): string | null {
  if (!Array.isArray(value)) return `${label} must be an array of row objects.`;
  if (value.some((row) => !isJsonObject(row))) return `Every row in ${label} must be a JSON object.`;
  return null;
}

function validateCustomCaseInput(
  input: string,
  expectedParams: string[],
  environmentCategory?: string,
): { valid: boolean; message: string } {
  let parsed: unknown;
  try {
    parsed = JSON.parse(input);
  } catch (error) {
    return { valid: false, message: `Invalid JSON: ${(error as Error).message}` };
  }
  if (!isJsonObject(parsed)) {
    return { valid: false, message: 'Input must be one JSON object, for example { "nums": [1, 2], "target": 3 }.' };
  }

  if (environmentCategory === 'shell') {
    const unexpected = Object.keys(parsed).filter((key) => key !== 'stdin' && key !== 'files');
    if (unexpected.length) return { valid: false, message: `Unexpected Bash field${unexpected.length > 1 ? 's' : ''}: ${unexpected.join(', ')}.` };
    if ('stdin' in parsed && typeof parsed.stdin !== 'string') return { valid: false, message: 'stdin must be a JSON string.' };
    if ('files' in parsed) {
      if (!isJsonObject(parsed.files)) return { valid: false, message: 'files must be an object mapping file names to text.' };
      const invalidFile = Object.entries(parsed.files).find(([, content]) => typeof content !== 'string');
      if (invalidFile) return { valid: false, message: `File ${invalidFile[0]} must contain a JSON string.` };
    }
    return { valid: true, message: 'Valid Bash fixture. stdin and files use the correct format.' };
  }

  if (environmentCategory === 'database' || environmentCategory === 'pandas') {
    if (environmentCategory === 'pandas' && 'data' in parsed) {
      const error = validateRows(parsed.data, 'data');
      return error ? { valid: false, message: error } : { valid: true, message: 'Valid pandas fixture.' };
    }
    const tables = 'tables' in parsed ? parsed.tables : parsed;
    if (!isJsonObject(tables)) return { valid: false, message: 'tables must be a JSON object.' };
    if (!Object.keys(tables).length) return { valid: false, message: 'Add at least one table fixture.' };
    for (const [name, rows] of Object.entries(tables)) {
      const error = validateRows(rows, `table ${name}`);
      if (error) return { valid: false, message: error };
    }
    return { valid: true, message: `Valid ${environmentCategory === 'database' ? 'SQL' : 'pandas'} table fixture.` };
  }

  if (expectedParams.length) {
    const keys = Object.keys(parsed);
    const missing = expectedParams.filter((name) => !Object.prototype.hasOwnProperty.call(parsed, name));
    const unexpected = keys.filter((name) => !expectedParams.includes(name));
    if (missing.length || unexpected.length) {
      const issues = [
        missing.length ? `Missing: ${missing.join(', ')}.` : '',
        unexpected.length ? `Unexpected: ${unexpected.join(', ')}.` : '',
      ].filter(Boolean);
      return { valid: false, message: issues.join(' ') };
    }
    return { valid: true, message: `Valid input. Parameters: ${expectedParams.join(', ')}.` };
  }
  return { valid: true, message: 'Valid JSON object.' };
}

function CasesWorkspacePanel({
  controls,
  systemCases,
  userCases,
  selectedCaseIds,
  result,
  error,
  disabledReason,
  environmentCategory,
  expectedParams,
  onSelectCase,
  onAddUserCase,
  onUpdateUserCase,
  onDeleteUserCase,
}: {
  controls: ReactNode;
  systemCases: TestCaseSummary[];
  userCases: UserTestCase[];
  selectedCaseIds: string[];
  result: ReturnType<typeof useAppStore.getState>['runResult'];
  error: string | null;
  disabledReason?: string;
  environmentCategory?: string;
  expectedParams: string[];
  onSelectCase: (id: string) => void;
  onAddUserCase: (initialInput?: string) => string;
  onUpdateUserCase: (id: string, patch: Partial<Pick<UserTestCase, 'name' | 'input'>>) => void;
  onDeleteUserCase: (id: string) => void;
}) {
  const [caseMessage, setCaseMessage] = useState<{ caseId: string; tone: 'success' | 'error' | 'info'; text: string } | null>(null);
  const selectedId = selectedCaseIds[0];
  const selectedSystem = systemCases.find((testCase) => testCase.id === selectedId) ?? null;
  const selectedUser = userCases.find((testCase) => testCase.id === selectedId) ?? null;
  const selectedResult = result?.case_results?.find((caseResult) => caseResult.id === selectedId);
  const resultById = new Map((result?.case_results ?? []).map((caseResult) => [caseResult.id, caseResult]));
  const visibleSystemCases = systemCases.slice(0, MAX_DEBUG_CASES);
  const visibleUserCases = userCases.slice(0, Math.max(0, MAX_DEBUG_CASES - visibleSystemCases.length));
  const canAddCase = systemCases.length + userCases.length < MAX_DEBUG_CASES;
  const addCase = () => {
    if (!canAddCase) return;
    const id = onAddUserCase(environmentFixtureExample(environmentCategory));
    if (id) onSelectCase(id);
  };
  const copyCustomInput = async (testCase: UserTestCase) => {
    try {
      await copyTextToClipboard(formatJsonForCopy(testCase.input));
      setCaseMessage({ caseId: testCase.id, tone: 'info', text: 'Input copied to the clipboard.' });
    } catch {
      setCaseMessage({ caseId: testCase.id, tone: 'error', text: 'The clipboard is unavailable. Select the input and copy it manually.' });
    }
  };
  const validateCustomInput = (testCase: UserTestCase) => {
    const validation = validateCustomCaseInput(testCase.input, expectedParams, environmentCategory);
    setCaseMessage({ caseId: testCase.id, tone: validation.valid ? 'success' : 'error', text: validation.message });
  };

  return (
    <aside className="debug-panel flex h-full min-h-0 flex-col border-t border-coden-border bg-coden-surface lg:border-l lg:border-t-0">
      <div className="shrink-0 border-b border-coden-border bg-gradient-to-br from-coden-surface to-coden-inner/70 p-3">
        <div className="flex items-center gap-2">
          <div className="flex min-w-0 flex-1 gap-1.5 overflow-x-auto py-0.5">
            {visibleSystemCases.map((testCase, index) => (
              <CaseChip key={testCase.id} label={`${index + 1}`} title={`${testCase.name} · System case`} active={testCase.id === selectedId} result={resultById.get(testCase.id)} onClick={() => onSelectCase(testCase.id)} />
            ))}
            {visibleUserCases.map((testCase, index) => (
              <CaseChip key={testCase.id} label={`${visibleSystemCases.length + index + 1}`} title={`${testCase.name} · Custom case`} custom active={testCase.id === selectedId} result={resultById.get(testCase.id)} onClick={() => onSelectCase(testCase.id)} />
            ))}
            {canAddCase && <button type="button" onClick={addCase} title="Create custom case" aria-label="Create custom case" className="flex h-9 w-9 shrink-0 items-center justify-center rounded-md border border-dashed border-coden-accent/60 text-coden-accent hover:bg-coden-accent/10"><DebugIcon name="plus" /></button>}
          </div>
          <div className="shrink-0">{controls}</div>
        </div>
        {disabledReason && <div className="mt-2 rounded-md border border-amber-500/30 bg-amber-500/10 p-2 text-[11px] text-amber-200">{disabledReason}</div>}
        {error && <div className="mt-2 rounded-md border border-rose-500/30 bg-rose-500/10 p-2 text-[11px] text-rose-200">{error}</div>}
      </div>

      <div className="min-h-0 flex-1 overflow-y-auto p-3">
        <div className="space-y-4">
            {selectedSystem ? (
              <div className="space-y-3">
                <div className="flex items-center justify-between gap-2">
                  <div>
                    <div className="text-xs font-bold text-coden-text">{selectedSystem.name}</div>
                    <div className="mt-0.5 text-[10px] text-coden-muted">System case · read only</div>
                  </div>
                  <span className="rounded-full border border-coden-border px-2 py-1 text-[9px] font-bold uppercase text-coden-muted">locked</span>
                </div>
                <CaseInspectorBlock title="Input" value={selectedSystem.input_repr} copyValue={formatJsonForCopy(selectedSystem.input_repr)} />
                <CaseInspectorBlock title="Expected" value={selectedSystem.expected_repr || '(computed by validator)'} tone="expected" />
                {selectedResult && <CaseResultCard result={selectedResult} />}
              </div>
            ) : selectedUser ? (
              <div className="space-y-3">
                <div className="flex items-center gap-2">
                  <input value={selectedUser.name} onChange={(event) => onUpdateUserCase(selectedUser.id, { name: event.target.value })} aria-label="Custom case name" className="min-w-0 flex-1 rounded-md border border-coden-border bg-coden-inner px-2.5 py-2 text-xs font-bold text-coden-text outline-none focus:border-coden-accent" />
                  <button type="button" onClick={() => onDeleteUserCase(selectedUser.id)} title="Delete custom case" aria-label="Delete custom case" className="debug-tool-button border border-rose-500/30 text-rose-400 hover:bg-rose-500/10"><DebugIcon name="trash" /></button>
                </div>
                <div>
                  <div className="mb-1.5 flex items-center justify-between gap-2">
                    <div className="text-[10px] font-bold uppercase tracking-wider text-coden-muted">JSON input</div>
                    <div className="flex items-center gap-1.5">
                      <button type="button" onClick={() => void copyCustomInput(selectedUser)} className="h-7 rounded-md border border-coden-border px-2.5 text-[10px] font-bold text-coden-text hover:bg-coden-border">Copy</button>
                      <button type="button" onClick={() => validateCustomInput(selectedUser)} className="h-7 rounded-md border border-emerald-500/40 bg-emerald-500/10 px-2.5 text-[10px] font-bold text-emerald-300 hover:bg-emerald-500/20">Validate</button>
                    </div>
                  </div>
                  <textarea
                    value={selectedUser.input}
                    onChange={(event) => {
                      onUpdateUserCase(selectedUser.id, { input: event.target.value });
                      if (caseMessage?.caseId === selectedUser.id) setCaseMessage(null);
                    }}
                    spellCheck={false}
                    className="min-h-52 w-full resize-y rounded-md border border-coden-border bg-coden-inner p-3 font-mono text-xs leading-relaxed text-coden-text outline-none focus:border-coden-accent"
                  />
                  {caseMessage?.caseId === selectedUser.id && (
                    <div className={`mt-2 rounded-md border px-2.5 py-2 text-[11px] ${caseMessage.tone === 'success' ? 'border-emerald-500/35 bg-emerald-500/10 text-emerald-200' : caseMessage.tone === 'error' ? 'border-rose-500/35 bg-rose-500/10 text-rose-200' : 'border-coden-accent/35 bg-coden-accent/10 text-coden-text'}`}>
                      {caseMessage.text}
                    </div>
                  )}
                  <div className="mt-1 text-[10px] text-coden-muted">Saved automatically on this device.</div>
                </div>
                {selectedResult ? <CaseResultCard result={selectedResult} /> : <div className="rounded-md border border-dashed border-coden-border p-3 text-[11px] text-coden-muted">Expected output is calculated by the reference solution when you run this case.</div>}
              </div>
            ) : (
                <div className="rounded-lg border border-dashed border-coden-border p-5 text-center">
                  <div className="text-sm font-semibold text-coden-text">No case selected</div>
                  <div className="mt-1 text-xs text-coden-muted">Select a system case or create your own.</div>
                  {canAddCase && <button type="button" onClick={addCase} className="mt-3 rounded-md bg-coden-accent px-3 py-2 text-xs font-bold text-coden-accentContrast">Create custom case</button>}
                </div>
            )}
        </div>
      </div>
    </aside>
  );
}

function CaseChip({ label, title, custom = false, active, result, onClick }: { label: string; title: string; custom?: boolean; active: boolean; result?: RunCaseResult; onClick: () => void }) {
  const border = result
    ? result.correct ? 'border-emerald-500/60' : 'border-rose-500/60'
    : 'border-coden-border/60';
  const fill = active
    ? 'bg-coden-accent/25'
    : 'bg-coden-inner hover:bg-coden-border/60';
  const text = custom ? 'text-amber-300' : 'text-coden-text';
  return (
    <button type="button" onClick={onClick} title={title} aria-label={title} className={`relative flex h-9 w-9 shrink-0 items-center justify-center rounded-md border p-0 text-xs font-semibold tabular-nums transition-colors ${border} ${fill} ${text}`}>
      {label}
    </button>
  );
}

function CaseInspectorBlock({ title, value, tone = 'neutral', copyValue }: { title: string; value: string; tone?: 'neutral' | 'expected'; copyValue?: string }) {
  const [copyState, setCopyState] = useState<'idle' | 'copied' | 'error'>('idle');
  useEffect(() => setCopyState('idle'), [copyValue]);
  const copy = async () => {
    if (copyValue === undefined) return;
    try {
      await copyTextToClipboard(copyValue);
      setCopyState('copied');
    } catch {
      setCopyState('error');
    }
  };
  return (
    <div className={`overflow-hidden rounded-md border ${tone === 'expected' ? 'border-emerald-500/25' : 'border-coden-border/70'} bg-coden-inner`}>
      <div className="flex items-center justify-between gap-2 border-b border-coden-border/60 px-3 py-2 text-[10px] font-bold uppercase tracking-wider text-coden-muted">
        <span>{title}</span>
        {copyValue !== undefined && (
          <button type="button" onClick={() => void copy()} className="rounded border border-coden-border px-2 py-1 text-[9px] font-bold normal-case tracking-normal text-coden-text hover:bg-coden-border">
            {copyState === 'copied' ? 'Copied' : copyState === 'error' ? 'Copy failed' : 'Copy'}
          </button>
        )}
      </div>
      <pre className="max-h-64 overflow-auto whitespace-pre-wrap break-words p-3 font-mono text-xs leading-relaxed text-coden-text">{formatCaseValue(value)}</pre>
    </div>
  );
}

function CaseResultCard({ result }: { result: RunCaseResult }) {
  return (
    <div className={`rounded-md border p-3 ${result.correct ? 'border-emerald-500/30 bg-emerald-500/10' : 'border-rose-500/30 bg-rose-500/10'}`}>
      <div className="flex items-center justify-between gap-2">
        <div className={`text-xs font-bold ${result.correct ? 'text-emerald-300' : 'text-rose-300'}`}>{result.correct ? 'Passed' : 'Failed'}</div>
        {result.runtime_user_ms != null && <div className="text-[10px] text-coden-muted">{formatMs(result.runtime_user_ms)}</div>}
      </div>
      {result.return_value_repr && <div className="mt-2"><CaseInspectorBlock title="Returned" value={result.return_value_repr} /></div>}
      {result.expected_repr && <div className="mt-2"><CaseInspectorBlock title="Expected" value={result.expected_repr} tone="expected" /></div>}
      {result.message && <div className="mt-2 text-[11px] text-coden-muted">{result.message}</div>}
    </div>
  );
}


function environmentFixtureExample(category?: string): string {
  if (category === 'database') return '{\n  "tables": {\n    "your_table": [{"id": 1, "name": "Ada"}]\n  }\n}';
  if (category === 'pandas') return '{\n  "tables": {\n    "data": [{"id": 1, "score": 95}]\n  }\n}';
  if (category === 'shell') return '{\n  "stdin": "first line\\nsecond line\\n",\n  "files": {"file.txt": "first line\\nsecond line\\n"}\n}';
  return '{\n  \n}';
}

export function EditorCaseDeck({
  cases,
  selectedCaseIds,
  result,
  mode,
  isRunning,
  onSelectCase,
  onRun,
  onRunAll,
  customCaseInput,
  onCustomInputChange,
  environmentCategory,
  disabledReason,
  height,
  paneSplit,
  onResizeHeight,
  onResizeSplit,
}: {
  cases: TestCaseSummary[];
  selectedCaseIds: string[];
  result: ReturnType<typeof useAppStore.getState>['runResult'];
  mode: string;
  isRunning: boolean;
  onSelectCase: (id: string) => void;
  onRun: () => void;
  onRunAll: () => void;
  customCaseInput: string;
  onCustomInputChange: (value: string) => void;
  environmentCategory?: string;
  disabledReason?: string;
  height: number;
  paneSplit: number;
  onResizeHeight: (event: ReactMouseEvent) => void;
  onResizeSplit: (value: number) => void;
}) {
  const [activeTab, setActiveTab] = useState<'cases' | 'output' | 'feedback' | 'submissions'>('cases');
  const splitRef = useRef<HTMLDivElement | null>(null);
  const selectedId = selectedCaseIds[0] === '__all_trial__' ? cases[0]?.id : selectedCaseIds[0];
  const selectedCase = cases.find((item) => item.id === selectedId) ?? cases[0] ?? null;
  const selectedIndex = selectedCase ? cases.findIndex((item) => item.id === selectedCase.id) : -1;
  const resultById = new Map((result?.case_results ?? []).map((caseResult) => [caseResult.id, caseResult]));
  const selectedResult = selectedCase ? resultById.get(selectedCase.id) : undefined;
  const ranAll = Boolean(result?.selected_case_ids?.includes('__all_trial__') || (result?.case_results?.length ?? 0) > 1);
  const realMode = mode === 'real_test';
  const specialEnvironment = ['database', 'pandas', 'shell'].includes(environmentCategory || '');
  const hasCustomInput = customCaseInput.trim().length > 0;
  const runDisabled = Boolean(disabledReason) || isRunning || (cases.length === 0 && !hasCustomInput);
  const splitStyle = { '--case-input-width': `${paneSplit}%` } as CSSProperties;

  return (
    <div className="relative flex shrink-0 flex-col border-t border-coden-border bg-coden-bg" style={{ height }}>
      <button
        type="button"
        aria-label="Resize test cases"
        title="Resize test cases"
        onMouseDown={onResizeHeight}
        className="absolute -top-1 left-0 right-0 z-10 h-2 cursor-row-resize bg-transparent hover:bg-coden-accent/35"
      />
      <div className="flex flex-wrap items-center justify-between gap-2 border-b border-coden-border bg-coden-surface/60 px-3 py-2">
        <div className="flex min-w-0 items-center gap-1">
          <EditorCaseTab label="Test Cases" active={activeTab === 'cases'} onClick={() => setActiveTab('cases')} />
          <EditorCaseTab label="Output" active={activeTab === 'output'} onClick={() => setActiveTab('output')} />
          <EditorCaseTab label="Feedback" active={activeTab === 'feedback'} onClick={() => setActiveTab('feedback')} />
          <EditorCaseTab label="Submissions" active={activeTab === 'submissions'} onClick={() => setActiveTab('submissions')} />
        </div>
        <div className="flex items-center gap-2">
          {realMode && (
            <span className="rounded bg-coden-accent/15 px-2 py-1 text-[10px] font-semibold uppercase text-coden-accent">
              real test
            </span>
          )}
          <button
            type="button"
            onClick={onRun}
            disabled={runDisabled}
            title={disabledReason || 'Run selected case'}
            className="h-8 rounded bg-coden-accent px-3 text-xs font-semibold text-coden-accentContrast hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {isRunning ? 'Running...' : 'Run'}
          </button>
          <button
            type="button"
            onClick={onRunAll}
            disabled={Boolean(disabledReason) || isRunning || realMode || cases.length === 0}
            title={disabledReason || 'Run all visible cases'}
            className="h-8 rounded border border-coden-border px-3 text-xs text-coden-text hover:bg-coden-border disabled:cursor-not-allowed disabled:opacity-50"
          >
            Run all
          </button>
        </div>
      </div>

      <div className="min-h-0 flex-1 overflow-y-auto p-3">
        {activeTab === 'cases' && (
          <div className="flex min-h-full flex-col gap-3">
            {disabledReason ? (
              <div className="rounded border border-amber-500/30 bg-amber-500/10 p-3 text-xs text-amber-100">
                {disabledReason}
              </div>
            ) : cases.length === 0 ? (
              specialEnvironment ? (
                <EnvironmentFixtureEditor
                  category={environmentCategory || ''}
                  value={customCaseInput}
                  onChange={onCustomInputChange}
                />
              ) : (
                <div className="rounded border border-amber-500/30 bg-amber-500/10 p-3 text-xs text-amber-100">
                  No validated test cases are authored for this challenge yet. Add a custom JSON input in the Result tab to run it locally.
                </div>
              )
            ) : (
              <>
                <div className="flex gap-1.5 overflow-x-auto pb-1">
                  {cases.map((testCase, index) => {
                    const caseResult = resultById.get(testCase.id);
                    const active = selectedCase?.id === testCase.id;
                    const resultClass = caseResult
                      ? caseResult.correct
                        ? 'border-emerald-500/50 bg-emerald-500/10 text-emerald-100'
                        : 'border-rose-500/50 bg-rose-500/10 text-rose-100'
                      : active
                        ? 'border-coden-accent bg-coden-accent/15 text-coden-text'
                        : 'border-transparent bg-coden-inner text-coden-muted hover:text-coden-text';
                    return (
                      <button
                        key={testCase.id}
                        type="button"
                        onClick={() => onSelectCase(testCase.id)}
                        disabled={realMode}
                        className={[
                          'h-9 min-w-[76px] rounded-md border px-3 text-sm font-semibold transition-colors disabled:cursor-not-allowed disabled:opacity-50',
                          active ? 'ring-1 ring-coden-accent/70' : '',
                          resultClass,
                        ].join(' ')}
                        title={testCase.name}
                      >
                        Case {index + 1}
                      </button>
                    );
                  })}
                </div>
                {selectedCase && (
                  <div
                    ref={splitRef}
                    className="grid min-h-0 flex-1 grid-cols-1 gap-3 xl:grid-cols-none xl:[grid-template-columns:minmax(0,var(--case-input-width))_6px_minmax(0,1fr)]"
                    style={splitStyle}
                  >
                    <CaseValuePane
                      title={`Case ${selectedIndex + 1} input`}
                      subtitle={selectedCase.name}
                      value={selectedCase.input_repr}
                    />
                    <button
                      type="button"
                      aria-label="Resize input and expected panes"
                      title="Resize input and expected panes"
                      onMouseDown={(event) => startPercentResize(
                        event,
                        splitRef.current,
                        'coden.casePaneSplit',
                        onResizeSplit,
                      )}
                      className="hidden xl:block cursor-col-resize rounded bg-coden-border/40 hover:bg-coden-accent/40"
                    />
                    <CaseValuePane
                      title="Expected"
                      subtitle={selectedCase.kind}
                      value={selectedCase.expected_repr || '(no expected value)'}
                      tone="expected"
                    />
                  </div>
                )}
              </>
            )}
          </div>
        )}

        {activeTab === 'output' && (
          <EditorOutputPanel result={result} selectedResult={selectedResult} ranAll={ranAll} />
        )}

        {activeTab === 'feedback' && (
          <EditorFeedbackPanel result={result} />
        )}

        {activeTab === 'submissions' && (
          <EditorSubmissionPanel result={result} />
        )}
      </div>
    </div>
  );
}

function EnvironmentFixtureEditor({ category, value, onChange }: { category: string; value: string; onChange: (value: string) => void }) {
  const config = {
    database: {
      label: 'SQL database fixture',
      body: 'Each key becomes an in-memory table. Run your query and inspect the result grid.',
      example: '{\n  "tables": {\n    "Person": [\n      {"personId": 1, "firstName": "Ada", "lastName": "Lovelace"}\n    ]\n  }\n}',
    },
    pandas: {
      label: 'Pandas DataFrame fixture',
      body: 'Each table becomes a pandas DataFrame passed to solve(...) by name.',
      example: '{\n  "tables": {\n    "data": [\n      {"id": 1, "score": 95},\n      {"id": 2, "score": 82}\n    ]\n  }\n}',
    },
    shell: {
      label: 'Bash stdin and files',
      body: 'The script receives stdin and runs beside the temporary files defined here.',
      example: '{\n  "stdin": "first line\\nsecond line\\n",\n  "files": {\n    "file.txt": "first line\\nsecond line\\n"\n  }\n}',
    },
  }[category] || { label: 'Custom fixture', body: 'Provide the runtime input as JSON.', example: '{}' };
  return (
    <div className="flex min-h-0 flex-1 flex-col rounded-lg border border-coden-accent/30 bg-coden-accent/5 p-3">
      <div className="flex items-start justify-between gap-3">
        <div>
          <div className="text-xs font-bold text-coden-text">{config.label}</div>
          <div className="mt-1 text-[11px] text-coden-muted">{config.body}</div>
        </div>
        {!value.trim() && (
          <button type="button" onClick={() => onChange(config.example)} className="shrink-0 rounded-md border border-coden-accent/40 px-2.5 py-1.5 text-[11px] font-semibold text-coden-accent hover:bg-coden-accent/10">Use example</button>
        )}
      </div>
      <textarea
        value={value}
        onChange={(event) => onChange(event.target.value)}
        spellCheck={false}
        placeholder={config.example}
        className="mt-3 min-h-32 flex-1 resize-none rounded-md border border-coden-border bg-coden-inner p-3 font-mono text-xs leading-relaxed text-coden-text outline-none focus:border-coden-accent"
      />
      <div className="mt-2 text-[10px] text-coden-muted">Fixture data stays local and is recreated for every run.</div>
    </div>
  );
}

function EditorCaseTab({
  label,
  active,
  onClick,
}: {
  label: string;
  active: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={[
        'h-8 rounded-t px-3 text-sm font-semibold',
        active
          ? 'border-b-2 border-coden-accent text-coden-text'
          : 'text-coden-muted hover:text-coden-text',
      ].join(' ')}
    >
      {label}
    </button>
  );
}

function CaseValuePane({
  title,
  subtitle,
  value,
  tone = 'neutral',
}: {
  title: string;
  subtitle?: string;
  value: string;
  tone?: 'neutral' | 'expected' | 'actual';
}) {
  const border = {
    neutral: 'border-coden-border/50',
    expected: 'border-emerald-500/25',
    actual: 'border-rose-500/25',
  }[tone];
  return (
    <div className={`flex min-h-0 min-w-0 flex-col rounded-md border ${border} bg-coden-inner`}>
      <div className="flex items-center justify-between gap-2 border-b border-coden-border/50 px-3 py-2">
        <div className="text-[10px] font-bold uppercase tracking-wide text-coden-muted">{title}</div>
        {subtitle && <div className="truncate text-[10px] text-coden-muted">{subtitle}</div>}
      </div>
      <pre className="min-h-0 flex-1 overflow-auto whitespace-pre-wrap break-words px-3 py-3 text-xs font-mono leading-relaxed text-coden-text">
{formatCaseValue(value)}
      </pre>
    </div>
  );
}

function EditorOutputPanel({
  result,
  selectedResult,
  ranAll,
}: {
  result: ReturnType<typeof useAppStore.getState>['runResult'];
  selectedResult?: RunCaseResult;
  ranAll: boolean;
}) {
  if (!result) {
    return <EditorEmptyPanel title="No output yet" body="Run a case to see the returned value here." />;
  }
  if (ranAll && result.case_results.length > 0) {
    return (
      <div className="grid grid-cols-1 gap-2 md:grid-cols-2 xl:grid-cols-3">
        {result.case_results.map((caseResult, index) => (
          <div
            key={caseResult.id}
            className={[
              'rounded-md border bg-coden-inner p-3',
              caseResult.correct ? 'border-emerald-500/25' : 'border-rose-500/25',
            ].join(' ')}
          >
            <div className="flex items-center justify-between gap-2">
              <div className="text-xs font-semibold text-coden-text">Case {index + 1}</div>
              <div className={caseResult.correct ? 'text-xs font-bold text-emerald-300' : 'text-xs font-bold text-rose-300'}>
                {caseResult.correct ? 'PASS' : 'FAIL'}
              </div>
            </div>
            <div className="mt-1 truncate text-[10px] text-coden-muted">{caseResult.name}</div>
          </div>
        ))}
      </div>
    );
  }
  return (
    <CaseValuePane
      title="Returned"
      value={selectedResult?.return_value_repr || result.return_value_repr || '(no output)'}
      tone={selectedResult && !selectedResult.correct ? 'actual' : 'neutral'}
    />
  );
}

function EditorFeedbackPanel({
  result,
}: {
  result: ReturnType<typeof useAppStore.getState>['runResult'];
}) {
  if (!result) {
    return <EditorEmptyPanel title="No feedback yet" body="Run a case to get correctness and runtime feedback." />;
  }
  return (
    <div
      className={[
        'rounded-md border px-4 py-3',
        result.passed
          ? 'border-emerald-500/30 bg-emerald-500/10'
          : result.correct
            ? 'border-amber-500/30 bg-amber-500/10'
            : 'border-rose-500/30 bg-rose-500/10',
      ].join(' ')}
    >
      <div className="text-sm font-semibold text-coden-text">
        {result.passed ? 'Accepted' : result.correct ? 'Correct but too slow' : 'Wrong answer'}
      </div>
      <div className="mt-1 text-xs text-coden-muted">{result.message}</div>
      {result.runtime_message && (
        <div className="mt-2 rounded bg-coden-inner px-3 py-2 text-xs text-coden-text">
          {result.runtime_message}
        </div>
      )}
    </div>
  );
}

function EditorSubmissionPanel({
  result,
}: {
  result: ReturnType<typeof useAppStore.getState>['runResult'];
}) {
  if (!result) {
    return <EditorEmptyPanel title="No local run yet" body="Run results will be summarized here." />;
  }
  return (
    <div className="grid grid-cols-1 gap-3 md:grid-cols-3">
      <EditorSummaryTile label="Status" value={result.passed ? 'Accepted' : result.correct ? 'Runtime failed' : 'Wrong answer'} />
      <EditorSummaryTile label="Cases" value={String(result.case_results?.length || result.selected_case_ids?.length || 1)} />
      <EditorSummaryTile label="Runtime" value={formatMs(result.runtime_user_ms)} />
    </div>
  );
}

function EditorSummaryTile({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-md border border-coden-border bg-coden-inner px-3 py-3">
      <div className="text-[10px] font-bold uppercase tracking-wide text-coden-muted">{label}</div>
      <div className="mt-1 truncate text-sm font-semibold text-coden-text">{value}</div>
    </div>
  );
}

function EditorEmptyPanel({ title, body }: { title: string; body: string }) {
  return (
    <div className="rounded-md border border-coden-border bg-coden-inner px-4 py-5">
      <div className="text-sm font-semibold text-coden-text">{title}</div>
      <div className="mt-1 text-xs text-coden-muted">{body}</div>
    </div>
  );
}

function formatMs(value: number | null | undefined): string {
  if (value === null || value === undefined) return '-';
  if (value < 10) return `${value.toFixed(2)} ms`;
  if (value < 100) return `${value.toFixed(1)} ms`;
  return `${Math.round(value).toLocaleString()} ms`;
}

function DebugToolbar({
  status,
  onStart,
  onContinue,
  onStepOver,
  onStepIn,
  onStepOut,
  onStop,
  unavailableReason,
  installHint,
}: {
  status: DebugStatus;
  unavailableReason?: string;
  installHint?: string;
  onStart: () => void;
  onContinue: () => void;
  onStepOver: () => void;
  onStepIn: () => void;
  onStepOut: () => void;
  onStop: () => void;
}) {
  const paused = status === 'paused';
  const active = status === 'starting' || status === 'running' || status === 'paused';
  const startDisabled = status === 'starting' || status === 'running' || Boolean(unavailableReason);
  const startTitle = unavailableReason
    ? [unavailableReason, installHint].filter(Boolean).join(' ')
    : active ? 'Restart debugger' : 'Start debugger';
  return (
    <div className="flex items-center gap-1 rounded-lg border border-coden-border bg-coden-inner/80 p-1 shadow-sm">
      <button
        type="button"
        onClick={onStart}
        disabled={startDisabled}
        title={startTitle}
        aria-label={active ? 'Restart debugger' : 'Start debugger'}
        className="flex h-8 w-9 items-center justify-center rounded-md bg-coden-accent p-0 text-coden-accentContrast shadow-sm transition hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-50"
      >
        <DebugIcon name="bug" />
      </button>
      {active && <>
        <button
          type="button"
          onClick={onContinue}
          title="Continue"
          aria-label="Continue"
          disabled={!paused}
          className="debug-tool-button"
        >
          <DebugIcon name="continue" />
        </button>
        <button
          type="button"
          onClick={onStepOver}
          title="Step over"
          aria-label="Step over"
          disabled={!paused}
          className="debug-tool-button"
        >
          <DebugIcon name="step-over" />
        </button>
        <button
          type="button"
          onClick={onStepIn}
          title="Step in"
          aria-label="Step in"
          disabled={!paused}
          className="debug-tool-button"
        >
          <DebugIcon name="step-in" />
        </button>
        <button
          type="button"
          onClick={onStepOut}
          title="Step out"
          aria-label="Step out"
          disabled={!paused}
          className="debug-tool-button"
        >
          <DebugIcon name="step-out" />
        </button>
        <button
          type="button"
          onClick={onStop}
          title="Stop"
          aria-label="Stop"
          className="debug-tool-button text-rose-400 hover:bg-rose-500/10"
        >
          <DebugIcon name="stop" />
        </button>
      </>}
    </div>
  );
}

type DebugIconName = 'bug' | 'cases' | 'variables' | 'stack' | 'breakpoint' | 'console' | 'continue' | 'step-over' | 'step-in' | 'step-out' | 'stop' | 'plus' | 'close' | 'trash';

function DebugIcon({ name }: { name: DebugIconName }) {
  const paths: Record<string, ReactNode> = {
    bug: <><path d="M8 2v2m8-2v2M4 9h16M5 13H2m20 0h-3M5 17H3m18 0h-2" /><rect x="6" y="4" width="12" height="17" rx="6" /><path d="M12 9v8" /></>,
    cases: <><path d="M9 3h6l1 2h3v16H5V5h3l1-2Z" /><path d="M8 10h8M8 14h8M8 18h5" /></>,
    variables: <><path d="M7 5H4v14h3M17 5h3v14h-3" /><path d="m9 9 6 6m0-6-6 6" /></>,
    stack: <><path d="m12 3 9 5-9 5-9-5 9-5Z" /><path d="m3 12 9 5 9-5M3 16l9 5 9-5" /></>,
    breakpoint: <><circle cx="12" cy="12" r="7" /><circle cx="12" cy="12" r="2.5" fill="currentColor" stroke="none" /></>,
    console: <><rect x="3" y="4" width="18" height="16" rx="2" /><path d="m7 9 3 3-3 3M13 15h4" /></>,
    continue: <path d="m7 4 12 8-12 8V4Z" />,
    'step-over': <><path d="M5 19v-4a7 7 0 0 1 7-7h7" /><path d="m15 4 4 4-4 4" /><path d="M8 19h8" /></>,
    'step-in': <><path d="M12 3v13" /><path d="m7 11 5 5 5-5" /><path d="M5 21h14" /></>,
    'step-out': <><path d="M12 21V8" /><path d="m7 13 5-5 5 5" /><path d="M5 3h14" /></>,
    stop: <rect x="6" y="6" width="12" height="12" rx="1" />,
    plus: <><path d="M12 5v14M5 12h14" /></>,
    close: <><path d="m6 6 12 12M18 6 6 18" /></>,
    trash: <><path d="M4 7h16M9 7V4h6v3m-8 0 1 14h8l1-14M10 11v6m4-6v6" /></>,
  };
  return <svg viewBox="0 0 24 24" className="h-4 w-4" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">{paths[name]}</svg>;
}

function DebuggerWorkspacePanel({
  controls,
  status,
  reason,
  error,
  errorDetail,
  currentLine,
  breakpoints,
  breakpointStates,
  locals,
  frames,
  activeFrameId,
  watches,
  exception,
  output,
  context,
  capability,
  capabilityLoaded,
  languageLabel,
  onSelectFrame,
  onAddWatch,
  onRemoveWatch,
  onLoadVariables,
  onRemoveBreakpoint,
}: {
  controls: ReactNode;
  status: DebugStatus;
  reason: string;
  error: string | null;
  errorDetail: DebugErrorDetail | null;
  currentLine: number | null;
  breakpoints: number[];
  breakpointStates: DebugBreakpointState[];
  locals: DebugVariable[];
  frames: DebugStackFrame[];
  activeFrameId: number | null;
  watches: DebugWatch[];
  exception: DebugException | null;
  output: string[];
  context: DebugContext | null;
  capability: DebugCapability | null;
  capabilityLoaded: boolean;
  languageLabel: string;
  onSelectFrame: (frame: DebugStackFrame) => void;
  onAddWatch: (expression: string) => void;
  onRemoveWatch: (id: string) => void;
  onLoadVariables: (variablesReference: number) => Promise<DebugVariable[]>;
  onRemoveBreakpoint: (line: number) => void;
}) {
  const [activeTab, setActiveTab] = useState<'variables' | 'stack' | 'breakpoints' | 'console'>('variables');
  const [watchExpression, setWatchExpression] = useState('');
  const inputEntries = Object.entries(context?.inputs ?? {});
  const visibleFrames = frames.some((frame) => frame.userCode) ? frames.filter((frame) => frame.userCode) : frames;
  const stoppedTitle = status === 'paused'
    ? reason === 'exception' ? 'Paused on exception' : 'Execution paused'
    : status === 'running' ? 'Running your solution'
      : status === 'starting' ? 'Starting debugger'
        : status === 'exited' ? 'Run finished'
          : status === 'error' ? 'Debugger needs attention'
            : 'Ready to debug';
  const submitWatch = () => {
    onAddWatch(watchExpression);
    setWatchExpression('');
  };
  return (
    <aside className="debug-panel min-h-0 border-t border-coden-border bg-coden-surface lg:border-l lg:border-t-0">
      <div className="border-b border-coden-border bg-gradient-to-br from-coden-surface to-coden-inner/70 p-4">
        <div className="flex flex-wrap items-start justify-between gap-3">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <span className={`debug-status-dot debug-status-dot-${status}`} />
              <div className="truncate text-sm font-bold text-coden-text">{stoppedTitle}</div>
            </div>
            <div className="mt-1 truncate text-[11px] text-coden-muted">
              {status === 'paused' && currentLine
                ? `Line ${currentLine}${reason ? ` - ${humanizeDebugReason(reason)}` : ''}`
                : context?.selectedCaseIds?.length
                  ? `Case ${context.selectedCaseIds.join(', ')}`
                  : 'Set a breakpoint in the gutter, then start debugging.'}
            </div>
          </div>
          <div className="flex shrink-0 items-center gap-2">
            {controls}
            <span className={debugStatusClass(status)}>{status}</span>
          </div>
        </div>
        {(error || exception) && (
          <div className="mt-3 rounded-lg border border-rose-500/40 bg-rose-500/10 p-3 text-xs text-rose-200 shadow-sm">
            <div className="flex items-start gap-2">
              <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-rose-500/20 font-bold">!</span>
              <div className="min-w-0">
                <div className="font-bold text-rose-100">{exception?.exceptionId || error || 'Runtime exception'}</div>
                {(exception?.description || (error && exception?.exceptionId)) && (
                  <div className="mt-1 whitespace-pre-wrap leading-relaxed">{exception?.description || error}</div>
                )}
              </div>
            </div>
            {errorDetail?.phase && <div className="mt-2 text-rose-200/75">Failed while {errorDetail.phase}.</div>}
            {errorDetail?.detail && errorDetail.detail !== error && (
              <pre className="mt-2 max-h-36 overflow-auto whitespace-pre-wrap rounded-md bg-coden-bg/70 p-2 font-mono text-[11px] text-rose-100">{errorDetail.detail}</pre>
            )}
            {exception?.details ? (
              <pre className="mt-2 max-h-36 overflow-auto whitespace-pre-wrap rounded-md bg-coden-bg/70 p-2 font-mono text-[11px] text-rose-100">{formatExceptionDetails(exception.details)}</pre>
            ) : null}
          </div>
        )}
      </div>
      <div className="grid grid-cols-4 border-b border-coden-border bg-coden-inner/50 px-2">
        <DebugPanelTab label="Variables" icon="variables" badge={locals.length + watches.length} active={activeTab === 'variables'} onClick={() => setActiveTab('variables')} />
        <DebugPanelTab label="Stack" icon="stack" badge={visibleFrames.length} active={activeTab === 'stack'} onClick={() => setActiveTab('stack')} />
        <DebugPanelTab label="Breakpoints" icon="breakpoint" badge={breakpoints.length} active={activeTab === 'breakpoints'} onClick={() => setActiveTab('breakpoints')} />
        <DebugPanelTab label="Console" icon="console" badge={output.length} active={activeTab === 'console'} onClick={() => setActiveTab('console')} />
      </div>
      <div className="min-h-0 flex-1 overflow-y-auto p-3">
        {activeTab === 'variables' && (
          <div className="space-y-5">
            <DebugSection title="Watch">
              <div className="flex gap-2">
                <input
                  value={watchExpression}
                  onChange={(event) => setWatchExpression(event.target.value)}
                  onKeyDown={(event) => { if (event.key === 'Enter') submitWatch(); }}
                  placeholder="Expression, e.g. left + right"
                  className="min-w-0 flex-1 rounded-md border border-coden-border bg-coden-inner px-2.5 py-2 font-mono text-xs text-coden-text outline-none focus:border-coden-accent"
                />
                <button type="button" onClick={submitWatch} title="Add watch" className="debug-tool-button border border-coden-border bg-coden-inner"><DebugIcon name="plus" /></button>
              </div>
              {watches.length > 0 && (
                <div className="mt-2 overflow-hidden rounded-md border border-coden-border/70">
                  {watches.map((watch) => (
                    <div key={watch.id} className="group border-b border-coden-border/60 bg-coden-inner/70 px-2.5 py-2 last:border-b-0">
                      <div className="flex items-center gap-2">
                        <span className="min-w-0 flex-1 truncate font-mono text-xs text-coden-accent">{watch.expression}</span>
                        <button type="button" title="Remove watch" onClick={() => onRemoveWatch(watch.id)} className="text-coden-muted opacity-60 hover:text-rose-400 group-hover:opacity-100"><DebugIcon name="close" /></button>
                      </div>
                      <div className="mt-1 break-words font-mono text-[11px] text-coden-text">{watch.pending ? 'Evaluating...' : watch.error || watch.value || 'Pause to evaluate'}</div>
                    </div>
                  ))}
                </div>
              )}
            </DebugSection>
            <DebugSection title={`Locals${activeFrameId ? ` - frame ${activeFrameId}` : ''}`}>
              {locals.length ? (
                <div className="overflow-hidden rounded-md border border-coden-border/70 bg-coden-inner/40">
                  {locals.map((variable, index) => (
                    <DebugVariableRow key={`${variable.name}-${index}`} variable={variable} depth={0} onLoadVariables={onLoadVariables} />
                  ))}
                </div>
              ) : <EmptyDebugText>{status === 'paused' ? 'No local variables in this frame.' : 'Locals appear when execution pauses.'}</EmptyDebugText>}
            </DebugSection>
          </div>
        )}
        {activeTab === 'stack' && (
          <div className="space-y-4">
            <DebugSection title="Call stack">
              {visibleFrames.length ? (
                <div className="space-y-1">
                  {visibleFrames.map((frame, index) => (
                    <button key={frame.id} type="button" onClick={() => onSelectFrame(frame)} className={`w-full rounded-md border px-3 py-2 text-left transition ${frame.id === activeFrameId ? 'border-coden-accent bg-coden-accent/10' : 'border-transparent bg-coden-inner hover:border-coden-border'}`}>
                      <div className="flex items-center gap-2">
                        <span className="w-5 text-[10px] text-coden-muted">#{index}</span>
                        <span className="min-w-0 flex-1 truncate font-mono text-xs font-semibold text-coden-text">{frame.name || '(anonymous)'}</span>
                        <span className="text-[10px] text-coden-accent">:{frame.line ?? '-'}</span>
                      </div>
                      <div className="mt-1 truncate pl-7 text-[10px] text-coden-muted" title={frame.path}>{frame.sourceName || frame.path || 'runtime'}</div>
                    </button>
                  ))}
                </div>
              ) : <EmptyDebugText>The call stack appears when execution pauses.</EmptyDebugText>}
            </DebugSection>
            <DebugSection title="Run input">
              {inputEntries.length ? inputEntries.map(([name, value]) => (
                <div key={name} className="mb-2 rounded-md border border-coden-border/60 bg-coden-inner p-2.5 last:mb-0">
                  <div className="font-mono text-[11px] font-semibold text-coden-accent">{name}</div>
                  <pre className="mt-1 max-h-32 overflow-auto whitespace-pre-wrap break-words font-mono text-[11px] text-coden-text">{value}</pre>
                </div>
              )) : <EmptyDebugText>Input values appear after the session starts.</EmptyDebugText>}
            </DebugSection>
          </div>
        )}
        {activeTab === 'breakpoints' && (
          <DebugSection title="Your breakpoints">
            {breakpoints.length ? (
              <div className="space-y-1.5">
                {breakpoints.map((line) => {
                  const state = breakpointStates.find((item) => item.requestedLine === line);
                  return (
                    <div key={line} className="flex items-center gap-3 rounded-md border border-coden-border/60 bg-coden-inner px-3 py-2">
                      <span className={`h-2.5 w-2.5 rounded-full ${state && !state.verified ? 'border-2 border-rose-400 bg-transparent' : 'bg-rose-500 shadow-[0_0_0_3px_rgba(244,63,94,.14)]'}`} />
                      <div className="min-w-0 flex-1">
                        <div className="text-xs font-semibold text-coden-text">Line {line}</div>
                        <div className="truncate text-[10px] text-coden-muted" title={state?.message}>{state?.verified ? 'Verified' : state?.message || 'Set before launch'}</div>
                      </div>
                      <button type="button" onClick={() => onRemoveBreakpoint(line)} title="Remove breakpoint" className="text-coden-muted hover:text-rose-400"><DebugIcon name="close" /></button>
                    </div>
                  );
                })}
              </div>
            ) : <EmptyDebugText>Click beside a line number to add a breakpoint.</EmptyDebugText>}
          </DebugSection>
        )}
        {activeTab === 'console' && (
          <DebugSection title="Debug console">
            {output.length ? (
              <pre className="min-h-40 overflow-auto whitespace-pre-wrap break-words rounded-md border border-coden-border/70 bg-[#0b1020] p-3 font-mono text-[11px] leading-relaxed text-slate-200">{output.join('\n')}</pre>
            ) : <EmptyDebugText>Program output and debugger messages appear here.</EmptyDebugText>}
          </DebugSection>
        )}
      </div>
      <details className="shrink-0 border-t border-coden-border bg-coden-inner/40 px-3 py-2">
        <summary className="cursor-pointer text-[11px] font-semibold text-coden-muted hover:text-coden-text">Session and runtime</summary>
        {context && (
          <div className="mt-2 space-y-1 text-xs">
            <DebugKeyValue label="Challenge" value={context.challengeName || context.challengeId} />
            <DebugKeyValue label="Language" value={context.languageLabel || languageLabel} />
            <DebugKeyValue label="Solution" value={context.solutionPath} mono />
          </div>
        )}
        <DebuggerCapability capability={capability} capabilityLoaded={capabilityLoaded} languageLabel={languageLabel} />
      </details>
    </aside>
  );
}

function DebugPanelTab({ label, icon, badge, active, onClick }: { label: string; icon: DebugIconName; badge: number; active: boolean; onClick: () => void }) {
  return (
    <button type="button" onClick={onClick} title={label} aria-label={label} aria-pressed={active} className={`relative flex min-w-0 items-center justify-center gap-1 px-1 py-2.5 transition ${active ? 'text-coden-accent' : 'text-coden-muted hover:text-coden-text'}`}>
      <DebugIcon name={icon} />
      {badge > 0 && <span className="rounded-full bg-coden-border px-1.5 py-0.5 text-[9px] font-bold text-coden-text">{badge}</span>}
      {active && <span className="absolute inset-x-1 bottom-0 h-0.5 rounded-full bg-coden-accent" />}
    </button>
  );
}

function DebugVariableRow({ variable, depth, onLoadVariables }: { variable: DebugVariable; depth: number; onLoadVariables: (variablesReference: number) => Promise<DebugVariable[]> }) {
  const [expanded, setExpanded] = useState(false);
  const [loading, setLoading] = useState(false);
  const [children, setChildren] = useState<DebugVariable[]>([]);
  const canExpand = Boolean(variable.variablesReference) || splitTopLevelItems(variable.value).length > 0;
  const toggle = async () => {
    if (!canExpand) return;
    if (!expanded && children.length === 0) {
      if (variable.variablesReference) {
        setLoading(true);
        setChildren(await onLoadVariables(variable.variablesReference));
        setLoading(false);
      } else {
        setChildren(splitTopLevelItems(variable.value).map((value, index) => ({ name: String(index), value })));
      }
    }
    setExpanded((current) => !current);
  };
  return (
    <div className="border-b border-coden-border/50 last:border-b-0">
      <button type="button" onClick={() => void toggle()} className="grid w-full grid-cols-[16px_minmax(0,1fr)_auto] items-start gap-1.5 px-2 py-2 text-left hover:bg-coden-border/30" style={{ paddingLeft: 8 + depth * 14 }}>
        <span className="pt-0.5 text-[10px] text-coden-muted">{canExpand ? expanded ? 'v' : '>' : ''}</span>
        <span className="min-w-0">
          <span className="font-mono text-xs font-semibold text-coden-accent">{variable.name}</span>
          <span className="ml-2 break-words font-mono text-[11px] text-coden-text">{compactValue(variable.value)}</span>
        </span>
        {variable.type && <span className="rounded bg-coden-border/70 px-1.5 py-0.5 text-[9px] text-coden-muted">{variable.type}</span>}
      </button>
      {expanded && (
        <div>{loading ? <div className="px-8 py-2 text-[11px] text-coden-muted">Loading...</div> : children.map((child, index) => <DebugVariableRow key={`${child.name}-${index}`} variable={child} depth={depth + 1} onLoadVariables={onLoadVariables} />)}</div>
      )}
    </div>
  );
}

function humanizeDebugReason(reason: string): string {
  return reason.replace(/([a-z])([A-Z])/g, '$1 $2').replace(/[_-]+/g, ' ').toLowerCase();
}

function formatExceptionDetails(details: unknown): string {
  if (typeof details === 'string') return details;
  try { return JSON.stringify(details, null, 2); } catch { return String(details); }
}

export function DebugPanel({
  status,
  reason,
  error,
  errorDetail,
  currentLine,
  breakpoints,
  locals,
  exception,
  output,
  context,
  capability,
  capabilityLoaded,
  languageLabel,
}: {
  status: DebugStatus;
  reason: string;
  error: string | null;
  errorDetail: DebugErrorDetail | null;
  currentLine: number | null;
  breakpoints: number[];
  locals: DebugVariable[];
  exception: DebugException | null;
  output: string[];
  context: DebugContext | null;
  capability: DebugCapability | null;
  capabilityLoaded: boolean;
  languageLabel: string;
}) {
  const inputEntries = Object.entries(context?.inputs ?? {});
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
            <div className="font-semibold">{error}</div>
            {errorDetail?.phase && (
              <div className="mt-1 text-rose-200/80">Phase: {errorDetail.phase}</div>
            )}
            {errorDetail?.adapter && (
              <div className="mt-1 break-all font-mono text-[11px] text-rose-200/80">{errorDetail.adapter}</div>
            )}
            {errorDetail?.detail && errorDetail.detail !== error && (
              <pre className="mt-2 max-h-32 overflow-auto whitespace-pre-wrap rounded bg-coden-bg/70 p-2 text-[11px] text-rose-100">
{errorDetail.detail}
              </pre>
            )}
          </div>
        )}
        <DebuggerCapability
          capability={capability}
          capabilityLoaded={capabilityLoaded}
          languageLabel={languageLabel}
        />
      </div>
      <div className="min-h-0 flex-1 overflow-y-auto p-3 space-y-4">
        <DebugSection title="Session">
          {context ? (
            <div className="space-y-1 rounded bg-coden-inner p-2 text-xs">
              <DebugKeyValue label="Challenge" value={context.challengeName || context.challengeId} />
              <DebugKeyValue label="Mode" value={context.mode} />
              {context.selectedCaseIds?.length ? (
                <DebugKeyValue label="Cases" value={context.selectedCaseIds.join(', ')} mono />
              ) : null}
              <DebugKeyValue label="Language" value={context.languageLabel || languageLabel} />
              <DebugKeyValue label="Solution" value={context.solutionPath} mono />
              {context.adapter && <DebugKeyValue label="Adapter" value={context.adapter} mono />}
            </div>
          ) : (
            <EmptyDebugText>Start debugging to load the run context.</EmptyDebugText>
          )}
        </DebugSection>
        <DebugSection title="Inputs">
          {inputEntries.length ? (
            <div className="space-y-2">
              {inputEntries.map(([name, value]) => (
                <div key={name} className="rounded bg-coden-inner p-2">
                  <div className="mb-1 font-mono text-[11px] text-coden-accent">{name}</div>
                  <pre className="max-h-32 overflow-auto whitespace-pre-wrap text-[11px] text-coden-text">
{value}
                  </pre>
                </div>
              ))}
            </div>
          ) : (
            <EmptyDebugText>No inputs yet</EmptyDebugText>
          )}
        </DebugSection>
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
        {exception && (
          <DebugSection title="Exception">
            <div className="rounded border border-rose-500/30 bg-rose-500/10 p-2 text-xs text-rose-200">
              {exception.exceptionId && <div className="font-semibold">{exception.exceptionId}</div>}
              {exception.description && <div className="mt-1">{exception.description}</div>}
              {exception.breakMode && <div className="mt-1 text-rose-200/80">Mode: {exception.breakMode}</div>}
            </div>
          </DebugSection>
        )}
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

function DebugKeyValue({
  label,
  value,
  mono = false,
}: {
  label: string;
  value: string;
  mono?: boolean;
}) {
  return (
    <div className="grid grid-cols-[72px_minmax(0,1fr)] gap-2">
      <span className="text-coden-muted">{label}</span>
      <span className={`${mono ? 'font-mono text-[11px]' : ''} truncate text-coden-text`} title={value}>
        {value}
      </span>
    </div>
  );
}

function DebuggerCapability({
  capability,
  capabilityLoaded,
  languageLabel,
}: {
  capability: DebugCapability | null;
  capabilityLoaded: boolean;
  languageLabel: string;
}) {
  if (!capability) {
    return (
      <div className="mt-2 rounded border border-coden-border bg-coden-inner p-2 text-xs text-coden-muted">
        {capabilityLoaded
          ? `${languageLabel} debugger status is unavailable.`
          : `Checking ${languageLabel} debugger tools...`}
      </div>
    );
  }

  const ready = capability.available;
  return (
    <div
      className={[
        'mt-2 rounded border p-2 text-xs',
        ready
          ? 'border-emerald-500/35 bg-emerald-500/10 text-emerald-200'
          : 'border-amber-500/35 bg-amber-500/10 text-amber-200',
      ].join(' ')}
    >
      <div className="font-semibold">
        {ready ? `${languageLabel} debugger ready` : `${languageLabel} debugger not ready`}
      </div>
      {!ready && <div className="mt-1 text-coden-text/90">{capability.message}</div>}
      {!ready && (
        <div className="mt-1 text-coden-muted">{capability.install_hint}</div>
      )}
      {ready && capability.adapter_command && (
        <div className="mt-1 break-all font-mono text-[11px] text-coden-muted">
          {capability.adapter_id}: {capability.adapter_command}
        </div>
      )}
    </div>
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
