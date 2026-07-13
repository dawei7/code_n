/**
 * broadcastSync.ts — cross-window state synchronization.
 *
 * The v0.9.0 pivot removed all detached windows (the editor
 * pop-out, the debug pop-out, the detached-pane host). The
 * main window is now the only window in the app, so the
 * BroadcastChannel-based state sync is dormant: the
 * `mountBroadcastSync` function still exists so the
 * architecture isn't ripped out (a future pop-out surface
 * would just re-enable it), but there's nothing to broadcast
 * in the current UI. The channel types and helpers are kept
 * in case a future auxiliary in-app surface needs them.
 */
import { useAppStore, applyingRemoteRef } from '../store/useAppStore';
import type { AppState } from '../store/useAppStore';


const SENDER_ID = (() => {
  if (typeof crypto !== 'undefined' && 'randomUUID' in crypto) {
    return crypto.randomUUID();
  }
  return `sender-${Math.random().toString(36).slice(2)}-${Date.now()}`;
})();


const BULK_CHANNEL = 'coden-store-bulk';


interface BulkMsg {
  kind: 'snapshot';
  senderId: string;
  seq: number;
  payload: BulkPayload;
}


interface BulkPayload {
  currentDetailId: string | null;
  source: string;
  runResult: unknown;
}


let bulkChannel: BroadcastChannel | null = null;
let outSeq = 0;
let lastBroadcastSig = '';


function bulkSig(s: AppState): string {
  return JSON.stringify({
    cd: s.currentDetail?.id ?? null,
    src: s.source,
    rr: (s.runResult as { user_ast_ops?: number } | null)?.user_ast_ops ?? null,
  });
}


function postBulk(): void {
  if (!bulkChannel) return;
  const s = useAppStore.getState();
  const payload: BulkPayload = {
    currentDetailId: s.currentDetail?.id ?? null,
    source: s.source,
    runResult: s.runResult,
  };
  const msg: BulkMsg = {
    kind: 'snapshot',
    senderId: SENDER_ID,
    seq: ++outSeq,
    payload,
  };
  bulkChannel.postMessage(msg);
}


/** Mount the broadcast sync. Call once on app start, after the
 *  stores are ready. Returns a teardown function.
 *
 *  In v0.9.0 there's only one window so the channel is
 *  technically dormant — but the wiring is kept so a future
 *  detached surface can just re-enable it without rewriting
 *  the sync protocol. */
export function mountBroadcastSync(): () => void {
  if (typeof BroadcastChannel === 'undefined') {
    return () => {};
  }
  bulkChannel = new BroadcastChannel(BULK_CHANNEL);
  bulkChannel.addEventListener('message', () => {
    // No-op for now. The main window is the only consumer.
  });

  const unsubscribe = useAppStore.subscribe((state, prev) => {
    if (applyingRemoteRef.current) return;
    const sig = bulkSig(state);
    if (sig !== lastBroadcastSig) {
      const prevSig = bulkSig(prev);
      if (sig !== prevSig) {
        lastBroadcastSig = sig;
        // Schedule (debounced 200ms) — kept from the original
        // bulk-broadcast design in case a detached surface ever
        // re-emerges.
        setTimeout(postBulk, 200);
      }
    }
  });

  return () => {
    unsubscribe();
    bulkChannel?.close();
    bulkChannel = null;
  };
}


export { SENDER_ID };
