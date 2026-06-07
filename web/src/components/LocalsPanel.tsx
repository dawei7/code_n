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
 * The tracecodec already unwraps TrackedList/TrackedValue and
 * converts sets/tuples to arrays for JSON, so what we see here
 * is a faithful (and "native") representation of the player's
 * actual Python state at this frame.
 */
export function LocalsPanel() {
  const source = useAppStore((s) => s.source);
  const runResult = useAppStore((s) => s.runResult);
  const frameIndex = useAppStore((s) => s.frameIndex);

  if (!runResult) {
    return <div className="text-xs text-coden-muted">Run the code to inspect locals.</div>;
  }

  const frame = runResult.trace[frameIndex];
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
