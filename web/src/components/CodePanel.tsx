import { useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';


/**
 * CodePanel — read-only source view with the currently-executed
 * line marked. Lives in the second half of the right panel.
 *
 * The active line is `frame.line_no` where `frame` is the latest
 * trace frame with `op_index <= current opIndex`. This is the
 * same computation LocalsPanel uses, so the source-line marker
 * stays in sync with the highlighted op in the op log.
 *
 * Why a plain `<pre>` instead of Monaco? Monaco is heavy (we
 * already use it in the pop-out editor). For an analysis
 * surface that just needs to read the source with one line
 * marked, a plain `<pre>` with a left-border highlight is fast
 * and crisp.
 */
export function CodePanel() {
  const source = useAppStore((s) => s.source);
  const runResult = useAppStore((s) => s.runResult);
  const opIndex = useAppStore((s) => s.opIndex);

  // The active line is the frame for the current opIndex. Same
  // derivation as LocalsPanel — kept consistent on purpose.
  // MUST be called on every render (Rules of Hooks): the
  // !source / !runResult guards happen AFTER this hook.
  const activeLine = useMemo(() => {
    if (!runResult) return null;
    const trace = runResult.trace;
    let frameIdx = 0;
    for (let f = 0; f < trace.length; f++) {
      if (trace[f].op_index <= opIndex) frameIdx = f;
      else break;
    }
    return trace[frameIdx]?.line_no ?? null;
  }, [runResult, opIndex]);

  if (!source) {
    return (
      <div className="bg-coden-surface border border-coden-border rounded p-3 h-full flex items-center justify-center text-xs text-coden-muted">
        Open the editor and save code, or click Run to load the starter template.
      </div>
    );
  }

  const lines = source.split('\n');
  const activeIdx = activeLine !== null ? activeLine - 1 : -1;

  return (
    <div className="bg-coden-surface border border-coden-border rounded p-2 h-full flex flex-col overflow-hidden">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0 flex items-center justify-between">
        <span>Source</span>
        {activeLine !== null && (
          <span className="text-coden-accent normal-case font-mono">
            ▶ line {activeLine} active
          </span>
        )}
      </div>
      <div className="flex-1 overflow-auto font-mono text-xs bg-coden-bg rounded border border-coden-border">
        {lines.map((text, i) => {
          const isActive = i === activeIdx;
          return (
            <div
              key={i}
              className={[
                'px-2 py-0.5 flex gap-2 transition-colors',
                isActive
                  ? 'bg-coden-accent/20 border-l-2 border-coden-accent'
                  : 'border-l-2 border-transparent',
              ].join(' ')}
            >
              <span
                className={[
                  'shrink-0 w-8 text-right tabular-nums select-none',
                  isActive ? 'text-coden-accent font-semibold' : 'text-coden-muted',
                ].join(' ')}
              >
                {i + 1}
              </span>
              <span className={isActive ? 'text-coden-text' : 'text-coden-text'}>
                {text || ' '}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
