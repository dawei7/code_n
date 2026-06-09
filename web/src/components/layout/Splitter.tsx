/**
 * Splitter.tsx — draggable divider between two split-pane children.
 *
 * UX:
 *   - 6px wide hit zone with a 1px visible line at center.
 *   - Pointer capture on pointerdown; rAF-coalesced DOM updates
 *     during drag (no React renders for the visual move — the
 *     store commit happens on pointerup).
 *   - body cursor + user-select: none during drag.
 *   - Double-click resets the split to equal sizes.
 *   - Keyboard: Arrow keys shift 6% (Shift = 12%); Home/End set
 *     min/max on the left child. role=separator for a11y.
 */
import { useCallback, useRef } from 'react';
import { useLayoutStore } from '../../store/useLayoutStore';


interface SplitterProps {
  splitId: string;
  direction: 'row' | 'col';
  /** Index of the left child. The splitter sits between i and i+1. */
  index: number;
  /** Current size of the left child (0..1). Used for aria-valuenow. */
  leftSize: number;
  /** Flex layout of the parent (for cursor + body styles). */
}


export function Splitter({ splitId, direction, index, leftSize }: SplitterProps) {
  const resizeSplit = useLayoutStore((s) => s.resizeSplit);
  const resetSplit = useLayoutStore((s) => s.resetSplit);

  // The ref points to the left-child DOM node so we can write
  // inline style during drag without round-tripping through React.
  const containerRef = useRef<HTMLDivElement | null>(null);
  // The pointer id we're currently capturing.
  const activePointerId = useRef<number | null>(null);
  // The starting rect of the left child at drag start.
  const startRect = useRef<{ left: number; top: number; size: number } | null>(null);
  // The starting sizes[] of the split at drag start.
  const startLeftSize = useRef<number>(0);
  // The total span at drag start (used to convert pixels → fraction).
  const startTotal = useRef<number>(0);
  // rAF handle.
  const rafRef = useRef<number | null>(null);
  // Live left-size during the drag (for store commit on pointerup).
  const liveLeft = useRef<number>(0);

  // Direction-dependent helpers.
  const isRow = direction === 'row';
  const cursorClass = isRow ? 'cursor-col-resize' : 'cursor-row-resize';
  const orient = isRow ? 'vertical' : 'horizontal';
  const minPx = 6;  // visible hit zone

  const onPointerDown = useCallback((e: React.PointerEvent<HTMLDivElement>) => {
    if (e.button !== 0) return;  // only left button starts a drag
    e.preventDefault();
    const handle = e.currentTarget;
    handle.setPointerCapture(e.pointerId);
    activePointerId.current = e.pointerId;
    // Find the parent flex container (the SplitPane root) and
    // measure the left child + the total span.
    const parent = handle.parentElement;
    if (!parent) return;
    const children = Array.from(parent.children) as HTMLElement[];
    // The structure: [child-0, splitter, child-1, splitter, ...].
    // The left-child-of-this-splitter is at children[2*index].
    const leftChild = children[2 * index];
    if (!leftChild) return;
    const leftRect = leftChild.getBoundingClientRect();
    const totalRect = parent.getBoundingClientRect();
    startRect.current = {
      left: leftRect.left,
      top: leftRect.top,
      size: isRow ? leftRect.width : leftRect.height,
    };
    startLeftSize.current = leftSize;
    startTotal.current = isRow ? totalRect.width : totalRect.height;
    liveLeft.current = leftSize;
    // Body cosmetics during drag.
    document.body.style.cursor = isRow ? 'col-resize' : 'row-resize';
    document.body.style.userSelect = 'none';
  }, [index, isRow, leftSize]);

  const onPointerMove = useCallback((e: React.PointerEvent<HTMLDivElement>) => {
    if (activePointerId.current !== e.pointerId) return;
    if (!startRect.current) return;
    e.preventDefault();
    const cur = isRow ? e.clientX : e.clientY;
    const startPos = isRow ? startRect.current.left : startRect.current.top;
    const deltaPx = cur - startPos;
    const deltaFrac = deltaPx / startTotal.current;
    let next = startLeftSize.current + deltaFrac;
    // Clamp to [0.1, 0.9] visually; the store also clamps.
    if (next < 0.1) next = 0.1;
    if (next > 0.9) next = 0.9;
    liveLeft.current = next;
    // rAF-coalesce the DOM write.
    if (rafRef.current !== null) return;
    rafRef.current = requestAnimationFrame(() => {
      rafRef.current = null;
      const parent = e.currentTarget.parentElement;
      if (!parent) return;
      const leftChild = (Array.from(parent.children) as HTMLElement[])[2 * index];
      if (leftChild) {
        leftChild.style.flexBasis = `${next * 100}%`;
      }
    });
  }, [index, isRow]);

  const finishDrag = useCallback((e: React.PointerEvent<HTMLDivElement>) => {
    if (activePointerId.current !== e.pointerId) return;
    activePointerId.current = null;
    if (rafRef.current !== null) {
      cancelAnimationFrame(rafRef.current);
      rafRef.current = null;
    }
    document.body.style.cursor = '';
    document.body.style.userSelect = '';
    // Commit the new size to the store.
    const finalFrac = liveLeft.current - startLeftSize.current;
    if (Math.abs(finalFrac) > 1e-6) {
      resizeSplit(splitId, index, finalFrac);
    }
    startRect.current = null;
  }, [index, resizeSplit, splitId]);

  const onDoubleClick = useCallback(() => {
    resetSplit(splitId);
  }, [resetSplit, splitId]);

  const onKeyDown = useCallback((e: React.KeyboardEvent<HTMLDivElement>) => {
    const step = e.shiftKey ? 0.12 : 0.06;
    let delta = 0;
    if (isRow) {
      if (e.key === 'ArrowLeft') delta = -step;
      else if (e.key === 'ArrowRight') delta = step;
    } else {
      if (e.key === 'ArrowUp') delta = -step;
      else if (e.key === 'ArrowDown') delta = step;
    }
    if (e.key === 'Home') {
      // Snap left child to min.
      resizeSplit(splitId, index, leftSize - 0.1);
      e.preventDefault();
      return;
    }
    if (e.key === 'End') {
      resizeSplit(splitId, index, 0.9 - leftSize);
      e.preventDefault();
      return;
    }
    if (delta !== 0) {
      resizeSplit(splitId, index, delta);
      e.preventDefault();
    }
  }, [index, isRow, leftSize, resizeSplit, splitId]);

  // Layout: a flex column/row with the visible 1px line centered
  // and 5px transparent margins on either side for the hit zone.
  return (
    <div
      ref={containerRef}
      role="separator"
      tabIndex={0}
      aria-orientation={orient}
      aria-valuenow={Math.round(leftSize * 100)}
      aria-valuemin={10}
      aria-valuemax={90}
      onPointerDown={onPointerDown}
      onPointerMove={onPointerMove}
      onPointerUp={finishDrag}
      onPointerCancel={finishDrag}
      onDoubleClick={onDoubleClick}
      onKeyDown={onKeyDown}
      className={[
        'shrink-0 flex items-center justify-center',
        isRow ? 'w-0 mx-[3px] h-full' : 'h-0 my-[3px] w-full',
        cursorClass,
      ].join(' ')}
      style={{ minWidth: minPx, minHeight: minPx }}
      title="Drag to resize (double-click to reset)"
    >
      <div
        className={[
          isRow ? 'w-px h-full' : 'h-px w-full',
          'bg-coden-border',
        ].join(' ')}
      />
    </div>
  );
}
