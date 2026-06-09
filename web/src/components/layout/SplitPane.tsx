/**
 * SplitPane.tsx — recursive container that lays out children
 * either side-by-side (direction='row') or stacked (direction='col')
 * with a Splitter between every pair. Each child's flexBasis is
 * driven by the corresponding entry in `node.sizes` (a fraction).
 *
 * Inline flexBasis is written on the child wrappers so the
 * Splitter's rAF drag can update the DOM without round-tripping
 * through React on every frame. The store commit happens on
 * pointerup.
 */
import type { LayoutNode } from './tree-ops';
import { Splitter } from './Splitter';
import { Pane } from './Pane';


interface SplitPaneProps {
  node: LayoutNode;
}


export function SplitPane({ node }: SplitPaneProps) {
  // Leaf nodes are rendered by the Pane component, not here.
  if (node.kind === 'leaf') {
    return <Pane leaf={node} />;
  }

  const isRow = node.direction === 'row';

  return (
    <div
      className={[
        'flex w-full h-full',
        isRow ? 'flex-row' : 'flex-col',
      ].join(' ')}
    >
      {node.children.map((child, i) => {
        const size = node.sizes[i] ?? 1 / node.children.length;
        // IMPORTANT: do not collapse the basis to 0 — a fully-
        // shrunken child would clip its content. Sizes are
        // clamped to [0.1, 0.9] by the store.
        return (
          <div
            key={child.id}
            className="min-w-0 min-h-0 overflow-hidden flex flex-col"
            style={{ flexBasis: `${size * 100}%`, flexGrow: 0, flexShrink: 1 }}
          >
            {child.kind === 'split' ? (
              <SplitPane node={child} />
            ) : (
              <Pane leaf={child} />
            )}
          </div>
        );
      })}
      {/* Render a Splitter between every pair. */}
      {node.children.length > 1 &&
        node.children.slice(0, -1).map((_, i) => {
          const leftSize = node.sizes[i] ?? 0.5;
          return (
            <Splitter
              key={`split-${node.id}-${i}`}
              splitId={node.id}
              direction={node.direction}
              index={i}
              leftSize={leftSize}
            />
          );
        })}
    </div>
  );
}
