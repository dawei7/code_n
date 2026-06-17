/**
 * useDebugSession — React hook that owns the lifecycle of one
 * debug session: it starts the session (POST /api/debug/sessions),
 * opens the WebSocket, drives the play/step state, and tears
 * down on stop.
 *
 * The hook is the SOLE owner of the WebSocket — the UI
 * components (DebugTab, the popped-out DetachedDebugHost)
 * just call its methods (or post commands that the hook
 * forwards). All protocol logic (message types, JSON
 * encoding) lives here.
 *
 * Singleton model: the WebSocket and the controller's state
 * are kept at MODULE scope, not in a per-call closure. The
 * hook just returns the same object no matter how many times
 * it's called. The main window (AppShell) mounts the hook
 * once; the popped-out debug window (DetachedDebugHost) posts
 * commands on the ``coden-debug-cmd`` BroadcastChannel and
 * this hook forwards them to the WS.
 *
 * Pop-out lifecycle (added in v0.8.4):
 *   - The main window owns the WS.
 *   - On every 'paused' transition (i.e. a breakpoint or step
 *     pause), the main window calls
 *     ``window.electronAPI.popOutDebug(sessionId)``. Electron
 *     opens a new BrowserWindow at ``?view=debug&sessionId=...``
 *     (or focuses the existing one). The pop-out is a pure
 *     view of the main window's debug state and ships user
 *     actions back over coden-debug-cmd.
 *   - On every 'exited' / 'error' transition, the main window
 *     calls ``window.electronAPI.closeDebugPopout()`` so the
 *     pop-out disappears automatically.
 *   - If the user manually closes the pop-out mid-session, the
 *     Electron main process fires a 'pane-window-closed' event
 *     with key 'debug'; the main window's paneWindowClosed
 *     handler ignores it (no layout-store flag to clear). The
 *     next 'paused' event reopens the pop-out (auto-reopen UX).
 *
 * State machine (mirrors `debugStatus` in the store):
 *
 *   idle → starting → (running ↔ paused) → exited
 *                     ↘ error
 *
 *   * ``starting`` — POST in flight, WebSocket not open yet.
 *   * ``running``  — the user clicked Continue / Step; the
 *                    worker is executing.
 *   * ``paused``   — a stopped event arrived (initial pause,
 *                    breakpoint hit, or step completed).
 *   * ``exited``   — the worker reported solve() returned.
 *   * ``error``    — POST failed, WS dropped, or DAP error.
 */
import { useCallback, useEffect, useRef } from 'react';

import { useAppStore, DebugLocal } from '../store/useAppStore';
import { startDebugSession } from '../api/debug';
import { DEBUG_CMD_CHANNEL, type DebugCommand } from '../lib/debugCommands';


interface StartArgs {
  challengeId: string;
  source: string;
  n: number;
  seed: number | null;
}

interface WsMessage {
  type: string;
  line?: number;
  frame_id?: number;
  thread_id?: number;
  reason?: string;
  locals?: DebugLocal[];
  result?: unknown;
  passed?: boolean;
  message?: string;
  output?: string;
  stream?: string;
  // Outbound (client → server) fields:
  lines?: number[];
  mode?: 'over' | 'in' | 'out';
}


interface SessionController {
  ws: WebSocket | null;
  sessionId: string | null;
  // Per-session: the breakpoints we've sent to the server.
  // We re-send whenever it changes (idempotent on the
  // server side).
  lastBpSent: number[];
}


const controller: SessionController = {
  ws: null,
  sessionId: null,
  lastBpSent: [],
};


function reset() {
  try {
    controller.ws?.close();
  } catch {
    // ignore
  }
  controller.ws = null;
  controller.sessionId = null;
  controller.lastBpSent = [];
}


// Pure state machine reducer for the WS messages. Kept
// outside the hook so tests can call it directly.
export function reduceMessage(msg: WsMessage): Partial<{
  debugStatus: 'running' | 'paused' | 'exited' | 'error' | 'idle';
  debugCurrentLine: number | null;
  debugLocals: DebugLocal[];
  debugStoppedReason: string;
  debugError: string;
}> {
  switch (msg.type) {
    case 'stopped':
      return {
        debugStatus: 'paused',
        debugCurrentLine: msg.line ?? null,
        debugLocals: Array.isArray(msg.locals) ? msg.locals : [],
        debugStoppedReason: msg.reason ?? 'unknown',
      };
    case 'continued':
      return {
        debugStatus: 'running',
        debugCurrentLine: null,
      };
    case 'exited':
      return {
        debugStatus: 'exited',
        debugCurrentLine: null,
        debugStoppedReason: 'exited',
      };
    case 'error':
      return {
        debugStatus: 'error',
        debugError: msg.message ?? 'unknown error',
      };
    default:
      return {};
  }
}


export function useDebugSession() {
  const store = useAppStore;
  // We use a ref to track the last sent breakpoints so
  // we can dedupe updates without re-rendering.
  const lastSentRef = useRef<number[]>([]);

  // -- cleanup on unmount --------------------------------------------
  // If the AppShell unmounts (rare — only on full reload),
  // close the WS. The server's WS handler will then kill
  // the worker subprocess.
  useEffect(() => {
    return () => {
      reset();
    };
  }, []);

  // -- send helper ---------------------------------------------------
  const send = useCallback((msg: WsMessage) => {
    const ws = controller.ws;
    if (!ws || ws.readyState !== WebSocket.OPEN) {
      store.setState({ debugError: 'debug socket not connected' });
      return;
    }
    ws.send(JSON.stringify(msg));
  }, [store]);

  // -- start a session ----------------------------------------------
  const start = useCallback(async (args: StartArgs) => {
    const state = store.getState();
    if (state.debugStatus === 'starting' || state.debugStatus === 'running' || state.debugStatus === 'paused') {
      // Already in a session — don't double-start.
      return;
    }
    store.setState({
      debugStatus: 'starting',
      debugError: '',
      debugCurrentLine: null,
      debugLocals: [],
      debugStoppedReason: '',
    });
    try {
      // POST /api/debug/sessions. The api helper converts
      // ``challengeId`` to ``challenge_id`` (snake_case) before
      // sending; sending camelCase used to trip a 422 from
      // Pydantic.
      const body = await startDebugSession(args);
      controller.sessionId = body.session_id;

      const wsScheme = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const wsUrl = `${wsScheme}//${window.location.host}${body.ws_url}`;
      const ws = new WebSocket(wsUrl);
      controller.ws = ws;

      ws.onmessage = (ev) => {
        let msg: WsMessage;
        try {
          msg = JSON.parse(ev.data);
        } catch {
          return;
        }
        // We mutate the store directly so the hook caller
        // (and any subscriber) re-renders.
        store.setState(reduceMessage(msg) as Record<string, unknown>);
      };

      ws.onerror = () => {
        store.setState({
          debugStatus: 'error',
          debugError: 'WebSocket error (debug session)',
        });
      };

      ws.onclose = () => {
        controller.ws = null;
        controller.sessionId = null;
        controller.lastBpSent = [];
        const cur = store.getState();
        if (cur.debugStatus !== 'exited' && cur.debugStatus !== 'idle' && cur.debugStatus !== 'error') {
          store.setState({
            debugStatus: 'exited',
            debugStoppedReason: 'connection closed',
          });
        }
      };
    } catch (e) {
      const message = e instanceof Error ? e.message : String(e);
      store.setState({
        debugStatus: 'error',
        debugError: message,
      });
    }
  }, [store]);

  // -- send breakpoint changes --------------------------------------
  // Called by the editor gutter when the user clicks a line,
  // or by the effect in DebugTab that watches the
  // ``breakpoints`` set. We dedupe: only send when the
  // sorted set actually changes.
  const setBreakpoints = useCallback((lines: number[]) => {
    const sorted = Array.from(new Set(lines)).sort((a, b) => a - b);
    if (arraysEqual(sorted, lastSentRef.current)) return;
    lastSentRef.current = sorted;
    if (sorted.length === 0) return;
    send({ type: 'set_breakpoints', lines: sorted });
  }, [send]);

  // -- step / continue ---------------------------------------------
  const continueExec = useCallback(() => send({ type: 'continue' }), [send]);
  const stepOver = useCallback(() => send({ type: 'step', mode: 'over' }), [send]);
  const stepIn = useCallback(() => send({ type: 'step', mode: 'in' }), [send]);
  const stepOut = useCallback(() => send({ type: 'step', mode: 'out' }), [send]);

  // -- stop ---------------------------------------------------------
  const stop = useCallback(() => {
    try {
      send({ type: 'stop' });
    } catch {
      // ignore
    }
    try {
      controller.ws?.close();
    } catch {
      // ignore
    }
    reset();
    store.setState({
      debugStatus: 'exited',
      debugCurrentLine: null,
      debugLocals: [],
    });
  }, [send, store]);

  // -- pop-out on 'paused', close on 'exited' / 'error' ------------
  //
  // Subscribe to the store and trigger the Electron pop-out
  // when the session pauses. The pop-out is a pure view of
  // the store, so we don't need to pass it any state — it
  // reads everything via the existing broadcastSync infra.
  //
  // We only run this in the main window (where ``popOutDebug``
  // makes sense). The popped-out window doesn't run this effect
  // because it doesn't mount AppShell (which is where the
  // hook is).
  useEffect(() => {
    const api = (typeof window !== 'undefined' ? window.electronAPI : null);
    if (!api?.popOutDebug) {
      // Dev (browser) — no pop-out; the user still gets the
      // DebugTab in the 4-pane layout.
      return;
    }
    const unsub = useAppStore.subscribe((state, prev) => {
      if (state.debugStatus === prev.debugStatus) return;
      if (state.debugStatus === 'paused' && controller.sessionId) {
        // Fire-and-forget. If the pop-out is already open,
        // Electron just focuses it.
        void api.popOutDebug(controller.sessionId);
      } else if (
        state.debugStatus === 'exited' ||
        state.debugStatus === 'error' ||
        state.debugStatus === 'idle'
      ) {
        // Auto-close per the UX spec: the pop-out disappears
        // when the session ends.
        void api.closeDebugPopout();
      }
    });
    return unsub;
  }, []);

  // -- Listen for pop-out commands ----------------------------------
  //
  // The popped-out debug window (DetachedDebugHost) posts
  // DebugCommand messages on the coden-debug-cmd
  // BroadcastChannel. We forward each one to the WS via
  // the same send() helper the in-window controls use.
  //
  // This is the main window's only "command receiver" — the
  // pop-out has no WS of its own.
  useEffect(() => {
    if (typeof BroadcastChannel === 'undefined') return;
    const ch = new BroadcastChannel(DEBUG_CMD_CHANNEL);
    const onMessage = (ev: MessageEvent<DebugCommand>) => {
      const cmd = ev.data;
      switch (cmd.kind) {
        case 'continue': continueExec(); break;
        case 'step_over': stepOver(); break;
        case 'step_in':   stepIn(); break;
        case 'step_out':  stepOut(); break;
        case 'stop':      stop(); break;
        // popout_ready / popout_closed are informational; the
        // Electron main process already tracks the window via
        // its own detachedWindows map.
        case 'popout_ready':
        case 'popout_closed':
          break;
      }
    };
    ch.addEventListener('message', onMessage);
    return () => {
      ch.removeEventListener('message', onMessage);
      ch.close();
    };
  }, [continueExec, stepOver, stepIn, stepOut, stop]);

  return {
    start,
    stop,
    continueExec,
    stepOver,
    stepIn,
    stepOut,
    setBreakpoints,
  };
}


function arraysEqual(a: number[], b: number[]): boolean {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}
