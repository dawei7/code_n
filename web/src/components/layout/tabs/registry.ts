/**
 * tabs/registry.ts — the built-in tab definitions.
 *
 * Every analysis surface the user can place in a pane is a tab.
 * The registry is the single source of truth for what tabs exist;
 * the layout store references tabs by id, and PaneContent.tsx
 * looks them up here when rendering.
 *
 * Why component references (not pre-rendered JSX)? So lazy
 * chunks stay separate. The Monaco editor (~1.5MB) is loaded
 * via React.lazy; if we held pre-rendered nodes, every import
 * would eagerly pull Monaco into the main bundle.
 */

import { lazy } from 'react';
import { DescriptionTab } from './DescriptionTab';
import { LocalsTab } from './LocalsTab';
import { StatsTab } from './StatsTab';
import { ComplexityTab } from './ComplexityTab';


// Lazy-loaded Monaco. Renders a "Loading editor..." placeholder
// while the chunk fetches. The detached-window use case also
// benefits: the main window never loads Monaco unless the user
// opens the editor tab.
const EditorTab = lazy(() => import('./EditorTab').then((m) => ({ default: m.EditorTab })));

// Reference tab: also lazy. Pulls in `react-markdown` + `remark-gfm`
// (~80 KB gzipped) which we don't want in the main bundle unless
// the user actually opens the reference pane.
const ReferenceTab = lazy(() =>
  import('./ReferenceTab').then((m) => ({ default: m.ReferenceTab })),
);

// AI Report tab: lazy because it pulls in react-markdown and
// is only relevant when AI mode is on.
const AiReportTab = lazy(() =>
  import('./AiReportTab').then((m) => ({ default: m.AiReportTab })),
);

// Debug tab: lazy. Only added to a leaf when the user
// starts a debug session; lives in its own chunk so the
// debugger UI doesn't bloat the main bundle.
const DebugTab = lazy(() =>
  import('./DebugTab').then((m) => ({ default: m.DebugTab })),
);


export interface TabDef {
  /** Stable id referenced by the layout store. */
  id: string;
  /** Display label shown in the tab bar. */
  label: string;
  /** Small unicode glyph for the tab bar. */
  icon: string;
  /** The React component that renders the tab's content. */
  Component: React.ComponentType;
  /**
   * Whether the user can fully remove this tab from the global
   * pool (VSCode "Close all"). Always-on tabs (description,
   * locals, etc.) are not closable. The editor tab IS closable
   * because it's optional and not assigned to any default leaf.
   */
  closable: boolean;
}


/** Built-in tabs, in the order they appear in the default presets. */
export const BUILTIN_TABS: TabDef[] = [
  { id: 'description', label: 'Description', icon: '📋', Component: DescriptionTab,  closable: false },
  { id: 'reference',   label: 'Reference',   icon: '📚', Component: ReferenceTab,    closable: false },
  { id: 'complexity',  label: 'Complexity',  icon: '🧮', Component: ComplexityTab,   closable: false },
  { id: 'locals',      label: 'Locals',      icon: '🔢', Component: LocalsTab,       closable: false },
  { id: 'stats',       label: 'Stats & Ops', icon: '📊', Component: StatsTab,        closable: false },
  // The AI Report tab is registered but only shown when AI
  // mode is on. The tab id is stable; visibility is gated by
  // the app store (see useVisibleTabs hook).
  { id: 'aiReport',    label: 'AI Report',   icon: '🤖', Component: AiReportTab,     closable: false },
  // The Debug tab is registered but only shown when a
  // debug session is active. Same gating pattern as the
  // AI Report tab.
  { id: 'debug',       label: 'Debug',       icon: '🐞', Component: DebugTab,        closable: true  },
  { id: 'editor',      label: 'Editor',      icon: '⌨️',  Component: EditorTab,       closable: true  },
];


/** Index by id for O(1) lookup at render time. */
export const TAB_INDEX: Record<string, TabDef> = Object.fromEntries(
  BUILTIN_TABS.map((t) => [t.id, t]),
);


/** Get a tab by id; returns null if unknown. */
export function getTab(id: string): TabDef | null {
  return TAB_INDEX[id] ?? null;
}
