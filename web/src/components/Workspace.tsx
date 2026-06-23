import { useEffect, useState } from 'react';
import { useAppStore, Topic } from '../store/useAppStore';
import { ResultTab } from './layout/tabs/ResultTab';
import { ComplexityAnalysis } from './ComplexityAnalysis';
import { ReferenceTab } from './layout/tabs/ReferenceTab';
import { MathematicalTab } from './layout/tabs/MathematicalTab';
import { CodenTab } from './layout/tabs/CodenTab';
import { CareerPathTab } from './layout/tabs/CareerPathTab';

export function Workspace() {
  const detail = useAppStore((s) => s.currentDetail);
  const language = useAppStore((s) => s.language);
  const activeSet = useAppStore((s) => s.activeSet);
  const activeTopic = useAppStore((s) => s.activeTopic);
  const setActiveTopic = useAppStore((s) => s.setActiveTopic);
  const activeVersion = useAppStore((s) => s.activeVersion);
  const versions = useAppStore((s) => s.versions);
  const versionNames = useAppStore((s) => s.versionNames);
  const modifiedVersions = useAppStore((s) => s.modifiedVersions);
  const switchVersion = useAppStore((s) => s.switchVersion);
  const resetVersion = useAppStore((s) => s.resetVersion);
  const renameVersion = useAppStore((s) => s.renameVersion);
  const [contextMenu, setContextMenu] = useState<{ visible: boolean; x: number; y: number; version: number | null }>(
    {
      visible: false,
      x: 0,
      y: 0,
      version: null,
    },
  );
  const [editingVersion, setEditingVersion] = useState<number | null>(null);
  const [editName, setEditName] = useState('');

  useEffect(() => {
    const handleWindowClick = () => setContextMenu((prev) => ({ ...prev, visible: false }));
    window.addEventListener('click', handleWindowClick);
    return () => window.removeEventListener('click', handleWindowClick);
  }, []);

  if (!detail) {
    if (activeSet === 'neetcode') {
      return (
        <div className="flex-1 flex flex-col min-h-0 bg-coden-bg p-6 overflow-y-auto">
          <CareerPathTab onSelectCodenTab={() => setActiveTopic('coden')} />
        </div>
      );
    }

    return (
      <div className="flex-1 flex flex-col items-center justify-center min-h-0 bg-coden-bg p-6 text-coden-muted text-center space-y-3 select-none">
        <span className="text-4xl">⌘</span>
        <h3 className="text-lg font-bold text-coden-text">Welcome to cOde(n)</h3>
        <p className="text-xs max-w-sm leading-relaxed text-coden-muted font-mono">
          You are practicing with the <strong>GeeksforGeeks Library</strong>.
          All 260+ challenges are unlocked. Select any challenge from the left sidebar to start practicing.
        </p>
      </div>
    );
  }

  const topics: { id: Topic; label: string; title: string; className?: string }[] = [
    { id: 'reference', label: '≡', title: language === 'en' ? 'Reference' : 'Referenz', className: 'font-serif text-lg' },
    { id: 'mathematical', label: 'π', title: language === 'en' ? 'Mathematical' : 'Mathematische Grundlagen' },
    { id: 'complexity', label: 'O', title: 'Complexity Analysis', className: 'font-serif italic text-lg' },
    { id: 'coden', label: '</>', title: 'cOde(n)', className: 'font-mono text-sm tracking-tight' },
    ...(activeSet === 'neetcode'
      ? [{ id: 'career_path' as Topic, label: '∴', title: 'Career Path', className: 'font-serif text-lg' }]
      : []),
  ];
  const sortedVersions = [...versions].filter((v) => v >= 1 && v <= 3).sort((a, b) => a - b);

  function handleContextMenu(e: React.MouseEvent, version: number) {
    e.preventDefault();
    setContextMenu({ visible: true, x: e.clientX, y: e.clientY, version });
  }

  function handleStartRename(version: number) {
    setEditingVersion(version);
    setEditName(versionNames[version] || `${version}`);
  }

  function handleFinishRename(version: number) {
    if (editingVersion !== null) {
      const finalName = editName.trim() || `${version}`;
      void renameVersion(version, finalName);
    }
    setEditingVersion(null);
  }

  return (
    <div className="flex-1 flex flex-col min-h-0 bg-coden-bg">
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
            className="w-full text-left px-4 py-2 text-xs hover:bg-coden-bg text-yellow-500"
            onClick={() => {
              setContextMenu((prev) => ({ ...prev, visible: false }));
              void resetVersion(contextMenu.version!);
            }}
          >
            Reset Version
          </button>
        </div>
      )}

      <div className="flex items-center gap-3 px-4 pt-2 border-b border-coden-border bg-coden-surface/60">
        <div className="flex items-center gap-1 pb-2">
          {sortedVersions.map((v) => {
            const isActive = v === activeVersion;
            const isModified = modifiedVersions.includes(v);
            return (
              <button
                key={v}
                type="button"
                onContextMenu={(e) => handleContextMenu(e, v)}
                onDoubleClick={() => handleStartRename(v)}
                onClick={() => !isActive && void switchVersion(v)}
                className={[
                  'h-7 min-w-7 px-2 rounded border text-xs font-semibold transition-colors tabular-nums',
                  isActive
                    ? 'border-coden-accent bg-coden-accent/20 text-coden-accent'
                    : isModified
                      ? 'border-amber-500/50 bg-amber-500/10 text-amber-500 hover:border-amber-400'
                      : 'border-coden-border bg-coden-surface text-coden-text hover:border-coden-accent',
                ].join(' ')}
                title={versionNames[v] || `Version ${v}`}
              >
                {editingVersion === v ? (
                  <input
                    autoFocus
                    value={editName}
                    onChange={(e) => setEditName(e.target.value)}
                    onBlur={() => handleFinishRename(v)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') handleFinishRename(v);
                      if (e.key === 'Escape') setEditingVersion(null);
                    }}
                    className="w-16 bg-transparent outline-none text-coden-accent"
                    onClick={(e) => e.stopPropagation()}
                  />
                ) : (
                  v
                )}
              </button>
            );
          })}
        </div>
        <div className="mb-2 h-6 border-l border-coden-border" />
        {topics.map((t) => (
          <button
            key={t.id}
            onClick={() => setActiveTopic(t.id)}
            title={t.title}
            aria-label={t.title}
            className={[
              'h-9 min-w-9 px-2 pb-2 text-base font-semibold border-b-2 transition-colors',
              activeTopic === t.id
                ? 'border-coden-accent text-coden-text'
                : 'border-transparent text-coden-muted hover:text-coden-text hover:border-coden-border',
              t.className ?? '',
            ].join(' ')}
          >
            {t.label}
          </button>
        ))}
      </div>

      <div className={activeTopic === 'coden' ? 'flex-1 flex flex-col min-h-0 p-3' : 'flex-1 overflow-y-auto p-4'}>
        {activeTopic === 'coden' ? (
          <div className="flex-1 bg-coden-surface rounded-xl shadow-lg flex flex-col min-h-0 overflow-hidden">
            <CodenTab />
          </div>
        ) : (
          <div className="w-full pb-24">
            {activeTopic === 'reference' && (
              <div className="bg-coden-surface rounded-lg p-6 shadow-lg">
                <ReferenceTab />
              </div>
            )}

            {activeTopic === 'mathematical' && (
              <div className="bg-coden-surface rounded-lg p-6 shadow-lg">
                <MathematicalTab />
              </div>
            )}

            {activeTopic === 'complexity' && (
              <div className="flex flex-col gap-6">
                <div className="bg-coden-surface rounded-lg shadow-lg p-2">
                  <ResultTab />
                </div>
                <div className="bg-coden-surface rounded-lg p-6 shadow-lg">
                  <ComplexityAnalysis />
                </div>
              </div>
            )}

            {activeTopic === 'career_path' && (
              <div className="bg-coden-surface rounded-lg p-6 shadow-lg">
                <CareerPathTab onSelectCodenTab={() => setActiveTopic('coden')} />
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
