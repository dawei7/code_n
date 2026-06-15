/**
 * useDebugSession — React hook that owns the lifecycle of one
 * debug session: it starts the session (POST /api/debug/sessions),
 * opens the WebSocket, drives the play/step state, and tears
 * down on stop.
 *
 * The hook is the SOLE owner of the WebSocket — the UI
 * components (DebugTab, the transport bar's Debug button)
 * just call its methods. All protocol logic (message types,
 * JSON encoding) lives here.
 *
 * Singleton model: the WebSocket and the controller's state
 * are kept at MODULE scope, not in a per-call closure. The
 * hook just returns the same object no matter how many times
 * it's called. This is important because both the transport
 * bar's "Debug" button and the DebugTab itself need to talk
 * to the same WebSocket; if each had its own hook instance,
 * the second caller would have a stale, empty view of the
 * world.
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
      const res = await fetch('/api/debug/sessions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(args),
      });
      if (!res.ok) {
        const detail = await res.text();
        throw new Error(`debug session start failed: ${res.status} ${detail}`);
      }
      const body = await res.json() as { session_id: string; ws_url: string };
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
