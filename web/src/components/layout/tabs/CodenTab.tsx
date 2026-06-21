import { useState, useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';
import { Editor } from '@monaco-editor/react';
import { useAppStore } from '../../../store/useAppStore';

export function CodenTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const open = useAppStore((s) => s.openInVSCode);
  const opening = useAppStore((s) => s.vscodeOpening);
  const lastError = useAppStore((s) => s.vscodeLastError);
  const clearVSCodeError = useAppStore((s) => s.clearVSCodeError);

  const source = useAppStore((s) => s.source);
  const activeVersion = useAppStore((s) => s.activeVersion);
  const versions = useAppStore((s) => s.versions);
  const versionNames = useAppStore((s) => s.versionNames);

  const switchVersion = useAppStore((s) => s.switchVersion);
  const resetVersion = useAppStore((s) => s.resetVersion);
  const renameVersion = useAppStore((s) => s.renameVersion);
  const saveSource = useAppStore((s) => s.saveSource);
  const modifiedVersions = useAppStore((s) => s.modifiedVersions);



  const [contextMenu, setContextMenu] = useState<{ visible: boolean; x: number; y: number; version: number | null }>({
    visible: false,
    x: 0,
    y: 0,
    version: null,
  });

  const [editingVersion, setEditingVersion] = useState<number | null>(null);
  const [editName, setEditName] = useState('');
  const [isMaximized, setIsMaximized] = useState(false);

  // Close context menu on window click
  useEffect(() => {
    const handleWindowClick = () => setContextMenu((prev) => ({ ...prev, visible: false }));
    window.addEventListener('click', handleWindowClick);
    return () => window.removeEventListener('click', handleWindowClick);
  }, []);

  // Exit focus mode on Escape
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isMaximized) {
        setIsMaximized(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isMaximized]);

  const [editorValue, setEditorValue] = useState(source);
  const saveTimeout = useRef<number | null>(null);

  // Sync external changes (e.g. from version switch or VSCode)
  useEffect(() => {
    setEditorValue(source);
  }, [source]);

  function handleEditorChange(value: string | undefined) {
    const val = value || '';
    setEditorValue(val);

    if (saveTimeout.current) {
      window.clearTimeout(saveTimeout.current);
    }
    saveTimeout.current = window.setTimeout(() => {
      void saveSource(val);
    }, 500);
  }

  async function handleOpenInVSCode() {
    clearVSCodeError();
    await open(detail);
  }

  function handleContextMenu(e: React.MouseEvent, v: number) {
    e.preventDefault();
    setContextMenu({ visible: true, x: e.clientX, y: e.clientY, version: v });
  }



  function handleStartRename(v: number) {
    setEditingVersion(v);
    setEditName(versionNames[v] || `${v}`);
  }

  function handleFinishRename(v: number) {
    if (editingVersion !== null) {
      let finalName = editName.trim();
      // enforce the "N. " prefix
      const prefix = `${v}. `;
      if (!finalName.startsWith(prefix)) {
        // If they deleted the prefix entirely, we put it back, minus any numbers they started with
        finalName = prefix + finalName.replace(/^\\d+\\.\\s*/, '');
      }
      void renameVersion(v, finalName);
    }
    setEditingVersion(null);
  }

  if (!detail) {
    return (
      <div className="flex items-center justify-center p-8 text-coden-muted">
        Select a challenge to manage its code versions.
      </div>
    );
  }

  const sortedVersions = [...versions].sort((a, b) => a - b);

  return (
    <div className="space-y-6 flex flex-col h-full relative">
      {/* Context Menu */}
      {contextMenu.visible && contextMenu.version !== null && (
        <div
          className="fixed z-50 w-40 bg-coden-surface border border-coden-border rounded-lg shadow-xl py-1 text-coden-text"
          style={{ top: contextMenu.y, left: contextMenu.x }}
          onClick={(e) => e.stopPropagation()}
        >
          <button
            className="w-full text-left px-4 py-2 text-xs hover:bg-coden-bg"
            onClick={() => {
              setContextMenu((prev) => ({ ...prev, visible: false }));
              handleStartRename(contextMenu.version!);
            }}
          >
            Rename
          </button>
          <button
            className="w-full text-left px-4 py-2 text-xs hover:bg-coden-bg text-yellow-400"
            onClick={() => {
              setContextMenu((prev) => ({ ...prev, visible: false }));
              void resetVersion(contextMenu.version!);
            }}
          >
            Reset Version
          </button>
        </div>
      )}

      {/* Header and Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-coden-inner p-4 rounded-xl shadow-inner">
        <div>
          <h2 className="text-lg font-bold text-coden-text bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-500">
            COde(n) Space
          </h2>
          <p className="text-xs text-coden-muted mt-1 max-w-sm">
            Manage your solution versions. The active version is what runs and what opens in Antigravity.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={() => setIsMaximized(true)}
            className="px-4 py-2 text-sm font-bold rounded-lg bg-coden-surface border border-coden-border text-coden-text hover:bg-gray-800 transition-colors"
          >
            Focus Mode
          </button>
          <button
            type="button"
            onClick={() => void handleOpenInVSCode()}
            disabled={opening}
            className="px-4 py-2 text-sm font-bold rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 text-white hover:from-blue-500 hover:to-indigo-500 shadow-md shadow-blue-900/20 transition-all disabled:opacity-50"
          >
            {opening ? 'Opening...' : 'Launch Antigravity'}
          </button>
        </div>
      </div>

      {lastError && (
        <div className="border border-rose-500/40 bg-rose-500/10 rounded p-3 text-xs text-rose-300">
          {lastError}
        </div>
      )}

      {/* Version Selector */}
      <div className="flex flex-col gap-2">
        <div className="text-xs font-semibold text-coden-muted uppercase tracking-wider flex justify-between items-center">
          <span>Versions (Right-click to manage)</span>
        </div>
        <div className="flex flex-wrap gap-2">
          {sortedVersions.map((v) => {
            const isActive = v === activeVersion;
            const isModified = modifiedVersions.includes(v);
            const displayName = versionNames[v] || `${v}`;

            return (
              <div
                key={v}
                onContextMenu={(e) => handleContextMenu(e, v)}
                onDoubleClick={() => handleStartRename(v)}
                className={[
                  'relative group flex items-center h-10 px-4 rounded-xl border text-sm font-medium cursor-pointer transition-all select-none',
                  isActive
                    ? 'border-indigo-500 bg-indigo-500/20 text-indigo-300 shadow-[0_0_15px_rgba(99,102,241,0.2)]'
                    : isModified
                      ? 'border-amber-500/50 bg-amber-500/10 text-amber-300 hover:border-amber-400 hover:text-amber-200'
                      : 'border-coden-border bg-coden-surface text-coden-text hover:border-coden-accent hover:text-coden-accent',
                ].join(' ')}
                onClick={() => !isActive && void switchVersion(v)}
              >
                {editingVersion === v ? (
                  <input
                    autoFocus
                    type="text"
                    value={editName}
                    onChange={(e) => setEditName(e.target.value)}
                    onBlur={() => handleFinishRename(v)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') handleFinishRename(v);
                      if (e.key === 'Escape') setEditingVersion(null);
                    }}
                    className="bg-transparent border-none outline-none text-indigo-300 min-w-[80px] w-auto text-sm font-medium"
                    onClick={(e) => e.stopPropagation()}
                  />
                ) : (
                  <span>{displayName}</span>
                )}
              </div>
            );
          })}
        </div>
      </div>



      {/* Code Preview */}
      {!isMaximized && (
        <div className="flex-1 flex flex-col min-h-0 bg-coden-inner rounded-xl border border-coden-border overflow-hidden shadow-inner">
          <div className="flex items-center justify-between px-4 py-2 bg-coden-surface border-b border-coden-border">
            <span className="text-xs font-mono text-coden-muted">
              solutions/{detail.id}.py ({versionNames[activeVersion] || `v${activeVersion}`})
            </span>
          </div>
          <div className="flex-1 overflow-hidden">
            <Editor
              height="100%"
              language="python"
              theme="vs-dark"
              value={editorValue}
              onChange={handleEditorChange}
              options={{
                minimap: { enabled: false },
                fontSize: 14,
                fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
                scrollBeyondLastLine: false,
                wordWrap: 'on',
                padding: { top: 16, bottom: 16 },
              }}
              loading={
                <div className="flex h-full items-center justify-center text-coden-muted text-sm">
                  Loading editor...
                </div>
              }
            />
          </div>
        </div>
      )}

      {/* Maximized Code Preview Portal */}
      {isMaximized && createPortal(
        <div className="fixed inset-0 z-[9999] bg-coden-bg flex flex-col">
          <div className="flex items-center justify-between px-4 py-2 bg-coden-surface border-b border-coden-border">
            <span className="text-xs font-mono text-coden-muted">
              solutions/{detail.id}.py ({versionNames[activeVersion] || `v${activeVersion}`})
            </span>
            <button
              onClick={() => setIsMaximized(false)}
              className="text-xs font-bold text-coden-text bg-red-900/40 hover:bg-red-900/60 border border-red-900/50 px-3 py-1 rounded transition-colors"
            >
              Exit Focus Mode (Esc)
            </button>
          </div>
          <div className="flex-1 overflow-hidden">
            <Editor
              height="100%"
              language="python"
              theme="vs-dark"
              value={editorValue}
              onChange={handleEditorChange}
              options={{
                minimap: { enabled: false },
                fontSize: 14,
                fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
                scrollBeyondLastLine: false,
                wordWrap: 'on',
                padding: { top: 16, bottom: 16 },
              }}
              loading={
                <div className="flex h-full items-center justify-center text-coden-muted text-sm">
                  Loading editor...
                </div>
              }
            />
          </div>
        </div>,
        document.body
      )}
    </div>
  );
}
