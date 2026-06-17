/**
 * PaneContent.tsx — given a tabId, render the right component.
 * Wraps the registry lookup in a Suspense boundary so the
 * lazy-loaded ReferenceTab (react-markdown chunk) can show a
 * placeholder while its chunk is fetching. The v0.9.0 pivot
 * removed the Monaco editor tab, so Monaco is no longer
 * pulled in by any tab.
 */
import { Suspense } from 'react';
import { getTab } from './tabs/registry';


export function PaneContent({ tabId }: { tabId: string | null }) {
  if (!tabId) {
    return (
      <div className="h-full flex items-center justify-center text-xs text-coden-muted">
        (no tab)
      </div>
    );
  }
  const def = getTab(tabId);
  if (!def) {
    return (
      <div className="h-full flex items-center justify-center text-xs text-coden-muted">
        Unknown tab: {tabId}
      </div>
    );
  }
  const Component = def.Component;
  return (
    <Suspense
      fallback={
        <div className="h-full flex items-center justify-center text-xs text-coden-muted">
          Loading {def.label}…
        </div>
      }
    >
      <Component />
    </Suspense>
  );
}
