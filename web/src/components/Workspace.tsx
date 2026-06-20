import { useState } from 'react';
import { useAppStore } from '../store/useAppStore';
import { ResultTab } from './layout/tabs/ResultTab';
import { ComplexityAnalysis } from './ComplexityAnalysis';
import { ReferenceTab } from './layout/tabs/ReferenceTab';
import { MathematicalTab } from './layout/tabs/MathematicalTab';
import { CodenTab } from './layout/tabs/CodenTab';

type Topic = 'reference' | 'mathematical' | 'complexity' | 'coden';

export function Workspace() {
  const detail = useAppStore((s) => s.currentDetail);
  const language = useAppStore((s) => s.language);
  const [activeTopic, setActiveTopic] = useState<Topic>('reference');

  if (!detail) {
    return (
      <div className="flex-1 flex items-center justify-center text-coden-muted">
        Select a challenge from the sidebar to begin.
      </div>
    );
  }

  const topics: { id: Topic; label: string }[] = [
    { id: 'reference', label: language === 'en' ? 'Reference' : 'Referenz' },
    { id: 'mathematical', label: language === 'en' ? 'Mathematical' : 'Mathematische Grundlagen' },
    { id: 'complexity', label: 'Complexity Analysis' },
    { id: 'coden', label: 'COde(n)' },
  ];

  return (
    <div className="flex-1 flex flex-col min-h-0 bg-coden-bg">
      {/* Sub-navigation for topics */}
      <div className="flex items-center gap-6 px-6 pt-4 border-b border-coden-border">
        {topics.map((t) => (
          <button
            key={t.id}
            onClick={() => setActiveTopic(t.id)}
            className={[
              'pb-3 text-sm font-semibold border-b-2 transition-colors',
              activeTopic === t.id
                ? 'border-coden-accent text-coden-text'
                : 'border-transparent text-coden-muted hover:text-coden-text hover:border-coden-border',
            ].join(' ')}
          >
            {t.label}
          </button>
        ))}
      </div>

      {/* Content Area */}
      <div className={activeTopic === 'coden' ? "flex-1 flex flex-col min-h-0 p-6" : "flex-1 overflow-y-auto p-6"}>
        {activeTopic === 'coden' ? (
          <div className="flex-1 bg-coden-surface rounded-xl p-6 shadow-lg flex flex-col min-h-0">
            <CodenTab />
          </div>
        ) : (
          <div className="w-full pb-24">
            {activeTopic === 'reference' && (
              <div className="bg-coden-surface rounded-xl p-6 shadow-lg">
                <ReferenceTab />
              </div>
            )}

            {activeTopic === 'mathematical' && (
              <div className="bg-coden-surface rounded-xl p-6 shadow-lg">
                <MathematicalTab />
              </div>
            )}

            {activeTopic === 'complexity' && (
              <div className="flex flex-col gap-6">
                <div className="bg-coden-surface rounded-xl shadow-lg p-2">
                  <ResultTab />
                </div>
                <div className="bg-coden-surface rounded-xl p-6 shadow-lg">
                  <ComplexityAnalysis />
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
