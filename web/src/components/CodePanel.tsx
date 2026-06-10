import { useEffect, useMemo, useRef } from 'react';
import { useAppStore } from '../store/useAppStore';
import { useLayoutStore } from '../store/useLayoutStore';


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
  const moveTab = useLayoutStore((s) => s.moveTab);
  const tree = useLayoutStore((s) => s.tree);
  // The first leaf in the tree. The Source view lives in some
  // leaf, but CodePanel doesn't know which — the "✎ Edit" button
  // adds the editor tab to the first leaf, which is the most
  // predictable behaviour for a 4-pane 2×2 layout.
  const firstLeafId = useMemo(() => {
    // Walk the tree depth-first and return the first leaf's id.
    const walk = (n: import('./layout/tree-ops').LayoutNode): string | null => {
      if (n.kind === 'leaf') return n.id;
      for (const c of n.children) {
        const id = walk(c);
        if (id) return id;
      }
      return null;
    };
    return walk(tree) ?? '';
  }, [tree]);

  // === ALL HOOKS MUST BE CALLED ON EVERY RENDER ===
  // (Rules of Hooks). Early-returns go BELOW the hook block.

  // The active line is the frame for the current opIndex. Same
  // derivation as LocalsPanel — kept consistent on purpose.
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

  // Ref to the scrollable code container, used by the
  // auto-scroll effect below.
  const containerRef = useRef<HTMLDivElement>(null);

  // Lines count (derived; safe for the effect even when source
  // is empty). Computed here so the useEffect below has a
  // stable value to depend on.
  const linesLength = source ? source.split('\n').length : 0;

  // Auto-scroll the highlighted line into the center of the
  // visible area whenever the active line changes. Same
  // pédagogical intent as the OpLog auto-scroll: keep the
  // user's focus on the line being executed, even as the
  // algorithm walks through the source.
  useEffect(() => {
    if (activeLine === null) return;
    const container = containerRef.current;
    if (!container) return;
    const el = container.querySelector<HTMLElement>(`[data-line-no="${activeLine}"]`);
    if (el) {
      el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }
  }, [activeLine, linesLength]);

  // === EARLY RETURNS GO BELOW THE HOOK BLOCK ===

  if (!source) {
    return (
      <div className="bg-coden-surface border border-coden-border rounded p-3 h-full flex items-center justify-center text-xs text-coden-muted">
        Open the editor and save code, or click Run to load the starter template.
      </div>
    );
  }

  const lines = source.split('\n');
  const activeIdx = activeLine !== null ? activeLine - 1 : -1;

  // The Source view is intentionally read-only. To make editing
  // discoverable from here, we offer two affordances in the header:
  //   1. "Edit" — adds the Monaco editor tab to the first leaf
  //      (so the user can switch between Source and Editor in
  //      the same pane), AND
  //   2. "⧉" — pops the editor out into its own window
  //      (preserves the read-only Source view on the main screen).
  function handleEdit() {
    // The Source view is the same source object as the Editor.
    // Adding the Editor tab gives the user an editable surface
    // next to / above / below the Source view (depending on
    // where their leaf is). No data copy — they share state.
    moveTab('editor', null, firstLeafId);
  }
  function handlePopOutEditor() {
    const api = (window as Window).electronAPI;
    if (api?.popOutEditor) {
      void api.popOutEditor();
    } else {
      window.open(window.location.pathname + '?view=editor', '_blank');
    }
  }

  return (
    <div className="bg-coden-surface border border-coden-border rounded p-2 h-full flex flex-col overflow-hidden">
      <div className="text-xs uppercase text-coden-muted font-semibold mb-2 shrink-0 flex items-center justify-between">
        <span>Source</span>
        <div className="flex items-center gap-2 normal-case font-normal">
          {activeLine !== null && (
            <span className="text-coden-accent font-mono">
              ▶ line {activeLine} active
            </span>
          )}
          <button
            type="button"
            onClick={handleEdit}
            className="px-2 py-0.5 rounded border border-coden-border text-coden-text hover:bg-coden-border"
            title="Add the Editor tab to the first pane (so you can edit code next to this read-only Source view)"
          >
            ✎ Edit
          </button>
          <button
            type="button"
            onClick={handlePopOutEditor}
            className="px-2 py-0.5 rounded border border-coden-border text-coden-text hover:bg-coden-border"
            title="Pop the Monaco editor out into its own window"
          >
            ⧉
          </button>
        </div>
      </div>
      <div
        ref={containerRef}
        className="flex-1 overflow-auto font-mono text-xs bg-coden-bg rounded border border-coden-border"
      >
        {lines.map((text, i) => {
          const isActive = i === activeIdx;
          const lineNo = i + 1;
          return (
            <div
              key={i}
              data-line-no={lineNo}
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
                {lineNo}
              </span>
              {/* whitespace-pre preserves leading spaces and tabs so
                  Python indentation is visible. min-w-0 lets the long
                  lines wrap if the pane is narrow. */}
              <span className="text-coden-text whitespace-pre min-w-0 flex-1">
                {text || ' '}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
