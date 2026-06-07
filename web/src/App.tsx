import { AppShell } from './components/AppShell';
import { EditorView } from './components/EditorView';


/**
 * Top-level React entry.
 *
 * Routes by URL query:
 *   - `?view=editor` → EditorView (used by the pop-out window
 *     spawned by the Electron main process)
 *   - default       → AppShell (the main three-pane UI)
 *
 * The query-param routing keeps the EditorView independent of
 * the Zustand store used by the main window — it has its own
 * minimal state for challenge selection + source editing.
 */
export default function App() {
  const params = new URLSearchParams(window.location.search);
  if (params.get('view') === 'editor') {
    return <EditorView />;
  }
  return <AppShell />;
}
