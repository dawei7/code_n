/**
 * debugCommands — the message types for the pop-out ↔ main-window
 * command channel.
 *
 * Why a dedicated BroadcastChannel and not the existing
 * ``coden-store-bulk`` channel? ``coden-store-bulk`` carries
 * snapshot deltas (source, runResult, opIndex, ...) and is read
 * by both windows. Commands are point-to-point (pop-out → main
 * window) and would pollute the snapshot stream if they went
 * through it. Keeping them on a separate channel also makes it
 * obvious that they're session-internal traffic, not state.
 *
 * Wire format: each message is a JSON-serializable object with
 * a ``kind`` discriminator. The main window listens for these
 * and forwards to the appropriate ``useDebugSession`` method
 * on the WS.
 */

/** Name of the BroadcastChannel used for pop-out → main commands. */
export const DEBUG_CMD_CHANNEL = 'coden-debug-cmd';


/**
 * Union of all commands the pop-out debug window can send back
 * to the main window. The main window's listener maps each
 * ``kind`` to the corresponding ``useDebugSession`` method.
 */
export type DebugCommand =
  | { kind: 'continue' }
  | { kind: 'step_over' }
  | { kind: 'step_in' }
  | { kind: 'step_out' }
  | { kind: 'stop' }
  /**
   * Sent by the pop-out on mount to tell the main window
   * "I'm alive". The main window can use this to decide
   * whether to call ``popOutDebug()`` again on the next
   * ``stopped`` event (it does, per the auto-reopen UX).
   */
  | { kind: 'popout_ready' }
  /**
   * Sent by the pop-out right before it unmounts (manual
   * close). Lets the main window know the user closed it
   * so it doesn't try to call ``close()`` on a destroyed
   * window.
   */
  | { kind: 'popout_closed' };
