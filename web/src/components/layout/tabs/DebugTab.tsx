/**
 * DebugTab — the real Python debugger surface in cOde(n).
 *
 * Three columns:
 *   * **Source** — read-only view of the player's code with
 *     the currently-paused line highlighted in accent color.
 *     Click the gutter to toggle a breakpoint (the click is
 *     forwarded to ``useAppStore.toggleBreakpoint`` and the
 *     new breakpoint set is pushed over the WebSocket by the
 *     ``useDebugSession`` hook in AppShell).
 *   * **Locals** — JSON tree of the local variables at the
 *     current frame. DAP gives us each variable as
 *     ``{name, value, type, scope}``; we render that.
 *   * **Controls** — the standard debugger controls:
 *     `[▶ Continue] [⤵ Step over] [⤴ Step in] [⤴ Step out] [⏹ Stop]`
 *
 * Top bar: a status pill that reflects ``debugStatus``
 * (idle / starting / running / paused / exited / error).
 *
 * The tab is driven entirely by the store; the WebSocket
 * lifecycle is owned by ``useDebugSession`` in AppShell so
 * the transport bar's "Debug" button and this tab share
 * the same connection.
 */
import { useEffect, useMemo } from 'react';
import { useAppStore } from '../../../store/useAppStore';
import { useDebugSession } from '../../../hooks/useDebugSession';


const STATUS_LABEL: Record<string, string> = {
  idle: 'No debug session',
  starting: 'Starting debugger…',
  running: 'Running…',
  paused: 'Paused',
  exited: 'Exited',
  error: 'Error',
};

const STATUS_COLOR: Record<string, string> = {
  idle: 'bg-coden-border text-coden-muted',
  starting: 'bg-amber-500/20 text-amber-400',
  running: 'bg-coden-accent/20 text-coden-accent',
  paused: 'bg-coden-accent/30 text-coden-text border border-coden-accent',
  exited: 'bg-coden-border text-coden-muted',
  error: 'bg-red-500/20 text-red-400',
};


export function DebugTab() {
  const source = useAppStore((s) => s.source);
  const breakpoints = useAppStore((s) => s.breakpoints);
  const toggleBreakpoint = useAppStore((s) => s.toggleBreakpoint);
  const debugStatus = useAppStore((s) => s.debugStatus);
  const debugCurrentLine = useAppStore((s) => s.debugCurrentLine);
  const debugLocals = useAppStore((s) => s.debugLocals);
  const debugStoppedReason = useAppStore((s) => s.debugStoppedReason);
  const debugError = useAppStore((s) => s.debugError);
  const currentDetail = useAppStore((s) => s.currentDetail);
  const n = useAppStore((s) => s.n);
  const seed = useAppStore((s) => s.seed);

  // We share the same singleton hook instance that
  // AppShell instantiates — it's at module scope, so the
  // call here is cheap and gives us the same methods.
  const session = useDebugSession();

  // Push breakpoint changes to the server whenever the set
  // changes. The hook's setBreakpoints dedupes against
  // the last value it sent, so calling it on every
  // keystroke is fine.
  useEffect(() => {
    if (debugStatus === 'idle' || debugStatus === 'exited' || debugStatus === 'error') {
      return;
    }
    session.setBreakpoints(Array.from(breakpoints));
    // We don't include `session` in deps; the hook's
    // setBreakpoints is stable across renders.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [breakpoints, debugStatus]);

  // -- Locals: parse DAP variables and group by scope -----------
  const localsByScope = useMemo(() => {
    const groups: Record<string, { name: string; value: string; type: string }[]> = {};
    for (const v of debugLocals) {
      const scope = v.scope || 'Locals';
      if (!groups[scope]) groups[scope] = [];
      groups[scope].push({
        name: v.name,
        value: v.value,
        type: v.type,
      });
    }
    return groups;
  }, [debugLocals]);

  // -- Source lines (memoized; source is small enough that
  // splitting per render is fine, but this lets us avoid
  // redoing it on unrelated re-renders).
  const sourceLines = useMemo(() => source.split('\n'), [source]);

  const isPaused = debugStatus === 'paused';
  const isRunning = debugStatus === 'running';
  const isStopped = debugStatus === 'exited' || debugStatus === 'error' || debugStatus === 'idle';
  const hasSession = !isStopped;

  return (
    <div className="h-full flex flex-col bg-coden-bg min-h-0">
      {/* Status bar */}
      <div className="h-9 px-3 py-1.5 text-xs border-b border-coden-border bg-coden-surface flex items-center justify-between gap-3 shrink-0">
        <div className="flex items-center gap-2 min-w-0">
          <span
            className={[
              'px-2 py-0.5 rounded font-semibold shrink-0',
              STATUS_COLOR[debugStatus] ?? 'bg-coden-border text-coden-muted',
            ].join(' ')}
            title={debugError || ''}
          >
            {STATUS_LABEL[debugStatus] ?? debugStatus}
          </span>
          {debugCurrentLine !== null && isPaused && (
            <span className="text-coden-muted font-mono">
              ⏸ line {debugCurrentLine} ({debugStoppedReason || 'breakpoint'})
            </span>
          )}
          {currentDetail && (
            <span className="text-coden-muted font-mono truncate">
              {currentDetail.id} · n={n}{seed !== null ? ` · seed=${seed}` : ''}
            </span>
          )}
        </div>
        {debugError && (
          <span className="text-red-400 truncate" title={debugError}>
            {debugError}
          </span>
        )}
      </div>

      {/* Three-column body */}
      <div className="flex-1 min-h-0 grid grid-cols-1 md:grid-cols-[1fr_1fr] lg:grid-cols-[2fr_1fr_1fr]">
        {/* Source column */}
        <div className="border-r border-coden-border overflow-y-auto bg-coden-bg">
          <div className="text-[10px] uppercase text-coden-muted font-semibold px-3 py-1.5 border-b border-coden-border bg-coden-surface sticky top-0">
            Source
          </div>
          {sourceLines.length === 0 ? (
            <div className="p-3 text-xs text-coden-muted">
              No source loaded. Pick a challenge and write some code first.
            </div>
          ) : (
            <div className="font-mono text-xs">
              {sourceLines.map((text, i) => {
                const lineNo = i + 1;
                const hasBp = breakpoints.has(lineNo);
                const isCurrent = debugCurrentLine === lineNo;
                return (
                  <div
                    key={lineNo}
                    data-line-no={lineNo}
                    className={[
                      'px-2 py-0.5 flex gap-2 items-start',
                      isCurrent
                        ? 'bg-coden-accent/15 border-l-2 border-coden-accent'
                        : 'border-l-2 border-transparent hover:bg-coden-surface/40',
                    ].join(' ')}
                  >
                    {/* Gutter: click to toggle breakpoint */}
                    <button
                      type="button"
                      data-gutter="true"
                      onClick={() => toggleBreakpoint(lineNo)}
                      title={hasBp ? 'Remove breakpoint' : 'Set breakpoint'}
                      className={[
                        'shrink-0 w-5 text-center select-none cursor-pointer',
                        hasBp
                          ? 'text-red-400 hover:text-red-300'
                          : 'text-coden-muted/40 hover:text-coden-muted',
                      ].join(' ')}
                    >
                      {hasBp ? '●' : ' '}
                    </button>
                    {/* Line number */}
                    <span
                      className={[
                        'shrink-0 w-8 text-right tabular-nums select-none',
                        isCurrent ? 'text-coden-accent font-semibold' : 'text-coden-muted',
                      ].join(' ')}
                    >
                      {lineNo}
                    </span>
                    {/* Source text */}
                    <span className="text-coden-text whitespace-pre min-w-0 flex-1">
                      {text || ' '}
                    </span>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* Locals column */}
        <div className="border-r border-coden-border overflow-y-auto bg-coden-surface/30">
          <div className="text-[10px] uppercase text-coden-muted font-semibold px-3 py-1.5 border-b border-coden-border bg-coden-surface sticky top-0">
            Locals {isPaused && <span className="text-coden-muted/60 normal-case font-normal">({debugLocals.length})</span>}
          </div>
          {!isPaused ? (
            <div className="p-3 text-xs text-coden-muted">
              {isRunning
                ? 'Execution is running; locals will appear at the next pause.'
                : hasSession
                ? 'Waiting for the first stop event…'
                : 'Click "Debug" in the transport bar to start a session.'}
            </div>
          ) : debugLocals.length === 0 ? (
            <div className="p-3 text-xs text-coden-muted">
              No locals in this frame.
            </div>
          ) : (
            <div className="p-2 space-y-3">
              {Object.entries(localsByScope).map(([scope, vars]) => (
                <div key={scope}>
                  <div className="text-[10px] uppercase text-coden-muted font-semibold mb-1">
                    {scope}
                  </div>
                  <ul className="space-y-0.5">
                    {vars.map((v) => (
                      <li key={v.name} className="font-mono text-xs flex gap-2">
                        <span className="text-coden-accent shrink-0">{v.name}</span>
                        <span className="text-coden-muted shrink-0">=</span>
                        <span className="text-coden-text break-all">{v.value}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Controls column */}
        <div className="bg-coden-surface/20">
          <div className="text-[10px] uppercase text-coden-muted font-semibold px-3 py-1.5 border-b border-coden-border bg-coden-surface">
            Controls
          </div>
          <div className="p-3 space-y-2">
            <ControlButton
              label="▶ Continue"
              hint="Resume execution until the next breakpoint or end of solve()."
              onClick={session.continueExec}
              disabled={!isPaused}
            />
            <ControlButton
              label="⤵ Step over"
              hint="Advance one line at this level; functions are executed without entering."
              onClick={session.stepOver}
              disabled={!isPaused}
            />
            <ControlButton
              label="⤴ Step in"
              hint="Advance one line; if a function is called, pause at its first line."
              onClick={session.stepIn}
              disabled={!isPaused}
            />
            <ControlButton
              label="⤴ Step out"
              hint="Run until the current function returns."
              onClick={session.stepOut}
              disabled={!isPaused}
            />
            <div className="pt-2 border-t border-coden-border">
              <ControlButton
                label="⏹ Stop session"
                hint="Close the debug session and kill the worker."
                onClick={session.stop}
                disabled={isStopped}
                variant="danger"
              />
            </div>
            <div className="pt-3 text-[10px] text-coden-muted space-y-1">
              <div className="font-semibold text-coden-muted/80 uppercase">Tip</div>
              <p>
                Click the red dot in the source gutter (or the gutter
                itself) to set / clear a breakpoint. The next time you
                click <span className="text-coden-text">▶ Continue</span>,
                execution pauses at every breakpoint.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}


function ControlButton({
  label,
  hint,
  onClick,
  disabled,
  variant,
}: {
  label: string;
  hint: string;
  onClick: () => void;
  disabled: boolean;
  variant?: 'danger';
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      title={hint}
      className={[
        'w-full px-3 py-2 text-sm rounded font-semibold text-left',
        'disabled:opacity-40 disabled:cursor-not-allowed',
        variant === 'danger'
          ? 'border border-red-500/60 text-red-300 hover:bg-red-500/15'
          : 'bg-coden-accent text-coden-bg hover:opacity-90',
      ].join(' ')}
    >
      {label}
    </button>
  );
}
