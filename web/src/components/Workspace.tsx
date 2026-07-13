import { useEffect } from 'react';
import { useAppStore, Topic } from '../store/useAppStore';
import { ComplexityAnalysis } from './ComplexityAnalysis';
import { ReferenceTab } from './layout/tabs/ReferenceTab';
import { CodenTab } from './layout/tabs/CodenTab';
import { AITutorTab } from './layout/tabs/AITutorTab';
import { CareerPathTab } from './layout/tabs/CareerPathTab';
import { getAlgorithmSetLabel, getAlgorithmSetOption } from '../lib/algorithmSets';

export function Workspace() {
  const detail = useAppStore((s) => s.currentDetail);
  const language = useAppStore((s) => s.language);
  const activeSet = useAppStore((s) => s.activeSet);
  const activeTopic = useAppStore((s) => s.activeTopic);
  const setActiveTopic = useAppStore((s) => s.setActiveTopic);
  const paneFontScales = useAppStore((s) => s.paneFontScales);
  const activeSetOption = getAlgorithmSetOption(activeSet);

  useEffect(() => {
    if (!activeSetOption.hasCareerPath && activeTopic === 'career_path') {
      setActiveTopic('reference');
    }
  }, [activeSetOption.hasCareerPath, activeTopic, setActiveTopic]);

  if (!detail) {
    if (activeSetOption.hasCareerPath) {
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
          You are practicing with the <strong>{getAlgorithmSetLabel(activeSet)}</strong> dataset.
          Select any available challenge from the left sidebar to start practicing.
        </p>
      </div>
    );
  }

  const topics: { id: Topic; label: string; title: string; className?: string }[] = [
    { id: 'reference', label: '≡', title: language === 'en' ? 'Reference' : 'Referenz', className: 'font-serif text-lg' },
    { id: 'complexity', label: 'O', title: 'Runtime Analysis', className: 'font-serif italic text-lg' },
    { id: 'coden', label: '</>', title: 'cOde(n)', className: 'font-mono text-sm tracking-tight' },
    { id: 'ai', label: 'AI', title: 'AI Tutor', className: 'font-mono text-xs tracking-tight' },
    ...(activeSetOption.hasCareerPath
      ? [{ id: 'career_path' as Topic, label: '∴', title: 'Career Path', className: 'font-serif text-lg' }]
      : []),
  ];
  const workspaceFontScope = `workspace:${activeTopic}`;
  const workspaceFontScale = paneFontScales[workspaceFontScope] ?? 1;
  const isCodenWorkspace = activeTopic === 'coden';

  return (
    <div className="flex-1 flex flex-col min-h-0 bg-coden-bg">
      <div className="flex items-center gap-1 px-4 pt-2 border-b border-coden-border bg-coden-surface/60">
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
        <div
          data-font-scope={workspaceFontScope}
          // Monaco performs its own coordinate-sensitive layout. CSS zoom on
          // an ancestor makes its caret and gutter hit targets drift away
          // from the rendered lines, so CodenTab applies this scale through
          // Monaco's fontSize option instead.
          style={isCodenWorkspace ? undefined : { zoom: workspaceFontScale }}
          className={isCodenWorkspace ? 'flex-1 flex flex-col min-h-0' : 'w-full'}
        >
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

            {activeTopic === 'complexity' && (
              <div className="bg-coden-surface rounded-xl p-6 shadow-lg">
                <ComplexityAnalysis />
              </div>
            )}

            {activeTopic === 'ai' && (
              <AITutorTab />
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
    </div>
  );
}
