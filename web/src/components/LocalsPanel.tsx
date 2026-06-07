import { useAppStore } from '../store/useAppStore';


/**
 * LocalsPanel — shows the locals snapshot at the current trace
 * frame, plus the source line that the player was on (looked up
 * from the editor source by line_no).
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

  return (
    <div className="flex-1 flex flex-col min-h-0 text-xs">
      <div className="bg-coden-bg rounded border border-coden-border px-2 py-1 mb-2 font-mono shrink-0">
        <span className="text-coden-muted">line {frame.line_no}:</span>{' '}
        <span className="text-coden-text">{line.trim() || '(empty)'}</span>
      </div>
      <div className="flex-1 overflow-y-auto font-mono bg-coden-bg rounded border border-coden-border">
        {Object.entries(frame.locals).length === 0 ? (
          <div className="text-coden-muted p-2">(no locals)</div>
        ) : (
          Object.entries(frame.locals).map(([name, value]) => (
            <div key={name} className="px-2 py-0.5 border-b border-coden-border last:border-b-0">
              <span className="text-coden-muted">{name}</span>
              <span className="text-coden-text"> = </span>
              <span className="text-coden-accent">
                {formatValue(value)}
              </span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}


function formatValue(v: unknown): string {
  if (Array.isArray(v)) {
    if (v.length <= 12) return `[${v.map(formatValue).join(', ')}]`;
    return `[${v.slice(0, 10).map(formatValue).join(', ')}, … (${v.length})]`;
  }
  if (v === null) return 'None';
  if (typeof v === 'string') return JSON.stringify(v);
  if (typeof v === 'number' || typeof v === 'boolean') return String(v);
  if (typeof v === 'object') return JSON.stringify(v).slice(0, 80);
  return String(v);
}
