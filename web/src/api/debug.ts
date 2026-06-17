/**
 * api/debug.ts — debug session HTTP helpers.
 *
 * The server's ``POST /api/debug/sessions`` body is a Pydantic model
 * with snake_case field names (``challenge_id``). The TS call sites
 * use camelCase identifiers (``challengeId``) for consistency with
 * the rest of the frontend; this module is the boundary that
 * converts one to the other.
 *
 * Why the conversion lives here, not in the hook: the hook is
 * responsible for the session lifecycle (WS open/close, status
 * transitions, pop-out triggers). Field-name translation is
 * an API-shape concern, so it belongs next to the other
 * ``api/*.ts`` helpers (see ``run.ts``, ``solutions.ts``).
 */
import { apiPost } from './client';


/** Args the frontend hands to ``startDebugSession``. */
export interface StartSessionArgs {
  challengeId: string;
  source: string;
  n: number;
  seed: number | null;
}


/** Response body returned by the server. */
export interface StartSessionResp {
  session_id: string;
  ws_url: string;
}


/**
 * POST /api/debug/sessions.
 *
 * Starts a new debug session. The server writes the source to a
 * temp file, spawns the debug worker, connects debugpy. The
 * returned ``ws_url`` is the relative WebSocket URL the client
 * uses to drive the session (``/ws/debug/{session_id}``).
 *
 * Throws :class:`ApiError` with status 422 if the body fails
 * Pydantic validation (e.g. missing ``challenge_id``). The
 * older call site inlined a raw ``fetch`` that sent camelCase
 * and tripped this 422; this helper is the single point that
 * does the field-name translation.
 */
export function startDebugSession(args: StartSessionArgs): Promise<StartSessionResp> {
  return apiPost<StartSessionResp>('/debug/sessions', {
    challenge_id: args.challengeId,
    source: args.source,
    n: args.n,
    seed: args.seed,
  });
}
