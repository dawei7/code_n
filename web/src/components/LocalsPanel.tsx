import { useMemo } from 'react';
import JsonView from '@uiw/react-json-view';
import { vscodeTheme } from '@uiw/react-json-view/vscode';
import { useAppStore } from '../store/useAppStore';


/**
 * LocalsPanel — shows the locals snapshot at the current trace
 * frame as a native, drillable data structure view.
 *
 * Uses @uiw/react-json-view to render the locals. Each local
 * variable is a top-level node; lists / dicts / sets (which the
 * server normalizes to arrays) can be expanded/collapsed to drill
 * in. The component is a single <JsonView> rooted at the locals
 * object so the variable names are the top-level keys (sorted in
 * insertion order: data, n, end, i for sort_01).
 *
 * The player's input is a plain list / dict (no TrackedList /
 * TrackedValue wrapper — those were removed in v0.8.5). What
 * we see here is a faithful representation of the player's
 * actual Python state at this frame.
 */
export function LocalsPanel() {
  const source = useAppStore((s) => s.source);
  const runResult = useAppStore((s) => s.runResult);
  const opIndex = useAppStore((s) => s.opIndex);

  // Compute the frame for the current step. The user-visible
  // position is opIndex (the slider index); the frame at this
  // position is just trace[opIndex] (clamped to the bounds). The
  // trace is already sorted by frame_index, so the frame the
  // slider "is on" is the most recent one captured at or
  // before the slider position.
  //
  // NB: this useMemo MUST be called on every render, regardless
  // of whether runResult exists. Putting it after the !runResult
  // early-return causes React's "Rendered fewer hooks than
  // expected" error (because the first render skips the hook
  // and the second render doesn't).
  const frame = useMemo(() => {
    if (!runResult) return undefined;
    const trace = runResult.trace;
    if (trace.length === 0) return undefined;
    const idx = Math.max(0, Math.min(opIndex, trace.length - 1));
    return trace[idx];
  }, [runResult, opIndex]);

  if (!runResult) {
    return <div className="text-xs text-coden-muted">Run the code to inspect locals.</div>;
  }
  if (!frame) {
    return <div className="text-xs text-coden-muted">No frame at this step.</div>;
  }

  const sourceLines = source.split('\n');
  const line = sourceLines[frame.line_no - 1] ?? '';

  // Light theme tweaks on top of the bundled "vscode" dark theme.
  const themed = {
    ...vscodeTheme,
    '--w-rjv-font-family': 'JetBrains Mono, Menlo, Monaco, monospace',
    '--w-rjv-font-size': '12px',
    '--w-rjv-line-color': '#94a3b8',          // slate-400
    '--w-rjv-key-string': '#34d399',          // coden-accent for keys
    '--w-rjv-background-color': '#0f172a',   // coden-surface
  } as Record<string, string>;

  return (
    <div className="flex-1 flex flex-col min-h-0 text-xs">
      <div className="bg-coden-bg rounded border border-coden-border px-2 py-1 mb-2 font-mono shrink-0">
        <span className="text-coden-muted">line {frame.line_no}:</span>{' '}
        <span className="text-coden-text">{line.trim() || '(empty)'}</span>
      </div>
      <div className="flex-1 overflow-auto bg-coden-bg rounded border border-coden-border">
        {Object.keys(frame.locals).length === 0 ? (
          <div className="text-coden-muted p-2">(no locals)</div>
        ) : (
          <JsonView
            value={frame.locals}
            collapsed={2}        // expand variables; collapse deeper nested levels
            displayDataTypes={false}
            displayObjectSize={true}
            enableClipboard={true}
            style={themed}
            className="p-2"
          />
        )}
      </div>
    </div>
  );
}
