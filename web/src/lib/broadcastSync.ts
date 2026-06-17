/**
 * broadcastSync.ts — cross-window state synchronization.
 *
 * Two channels:
 *   - `coden-store-bulk`  — debounced 200ms; carries full snapshots
 *     of the engine state that changes infrequently (currentDetail,
 *     source, runResult, n, seed).
 *   - `coden-store-tick`  — debounced 50ms; carries just opIndex
 *     updates during the play loop.
 *
 * Each window has a stable `senderId` (a UUID generated on first
 * import) and a monotonic `seq` for each outgoing message. Receivers
 * drop `incoming.seq <= lastSeenSeq` from the same `senderId` to
 * break echo loops caused by React StrictMode double-mounting.
 *
 * The window that ORIGINATED a change broadcasts; receivers apply
 * via `_applyRemoteSnapshot` and do not re-broadcast (the
 * `applyingRemoteRef` ref-sentinel in useAppStore enforces this).
 */
import { useAppStore, applyingRemoteRef } from '../store/useAppStore';
import type { AppState, DebugLocal, DebugStatus } from '../store/useAppStore';
import type { RunResponse } from '../types/api';


const SENDER_ID = (() => {
  // crypto.randomUUID is available in all browsers and in
  // Electron's renderer. Fall back to a counter if not.
  if (typeof crypto !== 'undefined' && 'randomUUID' in crypto) {
    return crypto.randomUUID();
  }
  return `sender-${Math.random().toString(36).slice(2)}-${Date.now()}`;
})();


const BULK_CHANNEL = 'coden-store-bulk';
const TICK_CHANNEL = 'coden-store-tick';


interface BulkMsg {
  kind: 'snapshot';
  senderId: string;
  seq: number;
  payload: BulkPayload;
}


interface BulkPayload {
  currentDetailId: string | null;
  source: string;
  runResult: RunResponse | null;
  n: number;
  seed: number | null;
  /** Request id from the originating window so the receiver can
   *  drop stale runs if a newer run started. */
  requestId: string | null;
  // -- Debug surface state, mirrored to the popped-out window --
  // The main window owns the WS; the pop-out is a pure view
  // that reads these slices and posts commands back on
  // coden-debug-cmd. Set isn't JSON-serializable, so we ship
  // breakpoints as a sorted array and reconstruct on receive.
  breakpoints: number[];
  debugStatus: DebugStatus;
  debugCurrentLine: number | null;
  debugLocals: DebugLocal[];
  debugStoppedReason: string;
  debugError: string;
}


interface TickMsg {
  kind: 'tick';
  senderId: string;
  seq: number;
  opIndex: number;
  isPlaying: boolean;
  frameIntervalMs: number;
}


let bulkChannel: BroadcastChannel | null = null;
let tickChannel: BroadcastChannel | null = null;
let outSeq = 0;
let lastBroadcastSig = '';
let lastOpIndexBroadcast = -1;
let pendingBulk: ReturnType<typeof setTimeout> | null = null;
let pendingTick: ReturnType<typeof setTimeout> | null = null;
let activeRequestId: string | null = null;
let lastSeenSeqBySender = new Map<string, number>();


/** Compute the current bulk signature. Used to skip no-op broadcasts. */
function bulkSig(s: AppState): string {
  return JSON.stringify({
    cd: s.currentDetail?.id ?? null,
    src: s.source,
    rr: s.runResult?.stats.total ?? null,
    n: s.n,
    sd: s.seed,
    rid: activeRequestId,
    // Debug surface signature: status + breakpoints + current line +
    // stopped reason + error string. We intentionally do NOT include
    // ``debugLocals`` here — it changes on every step and would
    // flood the channel. Locals flow through the WS, not broadcast.
    ds: s.debugStatus,
    bp: Array.from(s.breakpoints).sort((a, b) => a - b),
    dl: s.debugCurrentLine,
    dr: s.debugStoppedReason,
    de: s.debugError,
  });
}


function postBulk(): void {
  if (!bulkChannel) return;
  const s = useAppStore.getState();
  const payload: BulkPayload = {
    currentDetailId: s.currentDetail?.id ?? null,
    source: s.source,
    runResult: s.runResult,
    n: s.n,
    seed: s.seed,
    requestId: activeRequestId,
    breakpoints: Array.from(s.breakpoints).sort((a, b) => a - b),
    debugStatus: s.debugStatus,
    debugCurrentLine: s.debugCurrentLine,
    debugLocals: s.debugLocals,
    debugStoppedReason: s.debugStoppedReason,
    debugError: s.debugError,
  };
  const msg: BulkMsg = {
    kind: 'snapshot',
    senderId: SENDER_ID,
    seq: ++outSeq,
    payload,
  };
  bulkChannel.postMessage(msg);
}


function postTick(): void {
  if (!tickChannel) return;
  const s = useAppStore.getState();
  const msg: TickMsg = {
    kind: 'tick',
    senderId: SENDER_ID,
    seq: ++outSeq,
    opIndex: s.opIndex,
    isPlaying: s.isPlaying,
    frameIntervalMs: s.frameIntervalMs,
  };
  tickChannel.postMessage(msg);
}


/** Schedule a bulk broadcast (debounced 200ms). */
function scheduleBulk(): void {
  if (pendingBulk !== null) return;
  pendingBulk = setTimeout(() => {
    pendingBulk = null;
    postBulk();
  }, 200);
}


/** Schedule a tick broadcast (debounced 50ms). */
function scheduleTick(): void {
  if (pendingTick !== null) return;
  pendingTick = setTimeout(() => {
    pendingTick = null;
    postTick();
  }, 50);
}


function applyBulk(msg: BulkMsg): void {
  // Echo guard: drop our own messages and any out-of-order ones.
  if (msg.senderId === SENDER_ID) return;
  const last = lastSeenSeqBySender.get(msg.senderId) ?? 0;
  if (msg.seq <= last) return;
  lastSeenSeqBySender.set(msg.senderId, msg.seq);

  const s = useAppStore.getState();
  // Conflict resolution: if we have a newer run in flight, drop.
  if (msg.payload.requestId && activeRequestId && msg.payload.requestId !== activeRequestId) {
    // No-op for now; could resolve by keeping the newer one.
  }

  // Apply via the sentinel-guarded action. setTimeout(0) breaks
  // the synchronous subscribe→setState→subscribe loop.
  setTimeout(() => {
    useAppStore.getState()._applyRemoteSnapshot({
      source: msg.payload.source,
      runResult: msg.payload.runResult,
      n: msg.payload.n,
      seed: msg.payload.seed,
      breakpoints: new Set(msg.payload.breakpoints),
      debugStatus: msg.payload.debugStatus,
      debugCurrentLine: msg.payload.debugCurrentLine,
      debugLocals: msg.payload.debugLocals,
      debugStoppedReason: msg.payload.debugStoppedReason,
      debugError: msg.payload.debugError,
    });
    // Note: we do NOT touch currentDetail from broadcast; the
    // detached window's challenge selection is driven by its
    // own URL param (paneId/tabId), not the main window's
    // selection. Sharing currentDetail would override the
    // detached window's intentional local state.
    void s;
  }, 0);
}


function applyTick(msg: TickMsg): void {
  if (msg.senderId === SENDER_ID) return;
  const last = lastSeenSeqBySender.get(msg.senderId) ?? 0;
  if (msg.seq <= last) return;
  lastSeenSeqBySender.set(msg.senderId, msg.seq);
  setTimeout(() => {
    useAppStore.getState()._applyRemoteSnapshot({
      opIndex: msg.opIndex,
      isPlaying: msg.isPlaying,
      frameIntervalMs: msg.frameIntervalMs,
    });
  }, 0);
}


/**
 * Mount the broadcast sync. Call once on app start, after the
 * stores are ready. Returns a teardown function. The main window
 * and detached pane windows both call this — the channel is
 * symmetric.
 */
export function mountBroadcastSync(): () => void {
  if (typeof BroadcastChannel === 'undefined') {
    // Unsupported (e.g., very old browser). Skip silently.
    return () => {};
  }
  bulkChannel = new BroadcastChannel(BULK_CHANNEL);
  tickChannel = new BroadcastChannel(TICK_CHANNEL);
  bulkChannel.addEventListener('message', (e) => applyBulk(e.data as BulkMsg));
  tickChannel.addEventListener('message', (e) => applyTick(e.data as TickMsg));

  // Subscribe to the app store; on changes, broadcast.
  const unsubscribe = useAppStore.subscribe((state, prev) => {
    if (applyingRemoteRef.current) return;

    // Bulk changes: only broadcast when the signature actually changes.
    const sig = bulkSig(state);
    if (sig !== lastBroadcastSig) {
      const prevSig = bulkSig(prev);
      if (sig !== prevSig) {
        lastBroadcastSig = sig;
        scheduleBulk();
      }
    }

    // Tick changes: only the opIndex/play/interval.
    if (
      state.opIndex !== lastOpIndexBroadcast ||
      state.isPlaying !== prev.isPlaying ||
      state.frameIntervalMs !== prev.frameIntervalMs
    ) {
      lastOpIndexBroadcast = state.opIndex;
      scheduleTick();
    }
  });

  return () => {
    unsubscribe();
    bulkChannel?.close();
    tickChannel?.close();
    bulkChannel = null;
    tickChannel = null;
    if (pendingBulk !== null) { clearTimeout(pendingBulk); pendingBulk = null; }
    if (pendingTick !== null) { clearTimeout(pendingTick); pendingTick = null; }
  };
}


/** Mark that a new run started. Bumps the request id used to
 *  resolve conflicts when the same run result arrives in two
 *  windows. Call from the main window's `run()` action. */
export function noteRunStarted(): string {
  activeRequestId = (typeof crypto !== 'undefined' && 'randomUUID' in crypto)
    ? crypto.randomUUID()
    : `r-${Date.now()}-${Math.random()}`;
  return activeRequestId;
}


export { SENDER_ID };
