/**
 * tabs/registry.ts — the built-in tab definitions.
 *
 * Every analysis surface the user can place in a pane is a tab.
 * The registry is the single source of truth for what tabs exist;
 * the layout store references tabs by id, and PaneContent.tsx
 * looks them up here when rendering.
 *
 * The v0.9.0 pivot removed: editor (Monaco), debug surface,
 * locals (per-step), AI report. The new tabs are:
 *   - Result: the verdict + complexity band + return value.
 *   - VSCode: the "how to debug in VSCode" reference + the
 *     Open-in-VSCode button.
 *
 * Why component references (not pre-rendered JSX)? So lazy
 * chunks stay separate. The Reference tab pulls in
 * `react-markdown` + `remark-gfm` (~80 KB gzipped) which we
 * don't want in the main bundle unless the user opens the
 * reference pane.
 */

import { lazy } from 'react';
import { DescriptionTab } from './DescriptionTab';
import { ComplexityTab } from './ComplexityTab';
import { ResultTab } from './ResultTab';
import { VSCodeTab } from './VSCodeTab';


// Reference tab: lazy. Pulls in `react-markdown` + `remark-gfm`
// (~80 KB gzipped) which we don't want in the main bundle unless
// the user actually opens the reference pane.
const ReferenceTab = lazy(() =>
  import('./ReferenceTab').then((m) => ({ default: m.ReferenceTab })),
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
   * result, complexity) are not closable. The vscode + reference
   * tabs are not closable either — they're permanent reference
   * surfaces.
   */
  closable: boolean;
}


/** Built-in tabs, in the order they appear in the default presets. */
export const BUILTIN_TABS: TabDef[] = [
  { id: 'description', label: 'Description', icon: '📋', Component: DescriptionTab, closable: false },
  { id: 'reference',   label: 'Reference',   icon: '📚', Component: ReferenceTab,   closable: false },
  { id: 'complexity',  label: 'Complexity',  icon: '🧮', Component: ComplexityTab,  closable: false },
  { id: 'result',      label: 'Result',      icon: '🎯', Component: ResultTab,      closable: false },
  { id: 'vscode',      label: 'VSCode',      icon: '⌨️',  Component: VSCodeTab,      closable: false },
];


/** Index by id for O(1) lookup at render time. */
export const TAB_INDEX: Record<string, TabDef> = Object.fromEntries(
  BUILTIN_TABS.map((t) => [t.id, t]),
);


/** Get a tab by id; returns null if unknown. */
export function getTab(id: string): TabDef | null {
  return TAB_INDEX[id] ?? null;
}
