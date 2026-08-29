import { useEffect, type ReactNode } from 'react';
import { useAppStore, Topic } from '../store/useAppStore';
import { ComplexityAnalysis } from './ComplexityAnalysis';
import { ReferenceTab } from './layout/tabs/ReferenceTab';
import { CodenTab } from './layout/tabs/CodenTab';
import { AITutorTab } from './layout/tabs/AITutorTab';
import { CareerPathTab } from './layout/tabs/CareerPathTab';
import { EditorialTab } from './layout/tabs/EditorialTab';
import { GuidedExampleTab } from './layout/tabs/GuidedExampleTab';
import { BrandWordmark } from './BrandWordmark';
import { getAlgorithmSetLabel, getAlgorithmSetOption } from '../lib/algorithmSets';
import { canRevealSolution } from '../lib/cheaterMode';

type WorkspaceTopic = {
  id: Topic;
  label: ReactNode;
  title: string;
  className?: string;
  disabled?: boolean;
};

export function Workspace() {
  const detail = useAppStore((s) => s.currentDetail);
  const activeSet = useAppStore((s) => s.activeSet);
  const activeTopic = useAppStore((s) => s.activeTopic);
  const setActiveTopic = useAppStore((s) => s.setActiveTopic);
  const paneFontScales = useAppStore((s) => s.paneFontScales);
  const completed = useAppStore((s) => s.progress?.completed ?? []);
  const cheaterMode = useAppStore((s) => s.cheaterMode);
  const activeSetOption = getAlgorithmSetOption(activeSet);
  const activeCustomSetId = useAppStore((s) => s.activeCustomSetId);
  const customProblemSets = useAppStore((s) => s.customProblemSets);
  const activeCustomSet = activeSet === 'custom'
    ? customProblemSets.find((set) => set.id === activeCustomSetId)
    : null;
  const hasCareerPath = activeSetOption.hasCareerPath || activeCustomSet?.career_mode === true;
  const editorialUnlocked = detail
    ? canRevealSolution(completed.includes(detail.id), cheaterMode)
    : false;

  useEffect(() => {
    if (!hasCareerPath && activeTopic === 'career_path') {
      setActiveTopic('reference');
    }
    if (activeTopic === 'guided_example' && !detail?.has_guided_example) {
      setActiveTopic('reference');
    }
    if (activeTopic === 'editorial' && !editorialUnlocked) {
      setActiveTopic('reference');
    }
  }, [
    hasCareerPath,
    activeTopic,
    detail?.has_guided_example,
    editorialUnlocked,
    setActiveTopic,
  ]);

  if (!detail) {
    if (hasCareerPath) {
      return (
        <div className="flex-1 flex flex-col min-h-0 bg-coden-bg p-6 overflow-y-auto">
          <CareerPathTab onSelectCodenTab={() => setActiveTopic('coden')} />
        </div>
      );
    }

    return (
      <div className="flex-1 flex flex-col items-center justify-center min-h-0 bg-coden-bg p-6 text-coden-muted text-center space-y-3 select-none">
        <span className="text-4xl">⌘</span>
        <h3 className="text-lg font-bold text-coden-text">
          Welcome to <BrandWordmark />
        </h3>
        <p className="text-xs max-w-sm leading-relaxed text-coden-muted font-mono">
          You are practicing with the{' '}
          <strong>{activeCustomSet?.name || getAlgorithmSetLabel(activeSet)}</strong> dataset.
          Select any available challenge from the left sidebar to start practicing.
        </p>
      </div>
    );
  }

  const topics: WorkspaceTopic[] = [
    { id: 'reference', label: '≡', title: 'Reference', className: 'font-serif text-lg' },
    ...(detail.has_guided_example
      ? [{ id: 'guided_example' as Topic, label: <ProfessorLectureIcon />, title: 'Guided Example' }]
      : []),
    {
      id: 'editorial',
      label: <EditorialIcon locked={!editorialUnlocked} />,
      title: editorialUnlocked
        ? 'Editorial'
        : 'Editorial — solve this challenge successfully to unlock',
      disabled: !editorialUnlocked,
    },
    { id: 'coden', label: '</>', title: 'cOde(n)', className: 'font-mono text-sm tracking-tight' },
    { id: 'complexity', label: 'O', title: 'Complexity Analysis', className: 'font-serif italic text-lg' },
    { id: 'ai', label: 'AI', title: 'AI Tutor', className: 'font-mono text-xs tracking-tight' },
    ...(hasCareerPath
      ? [{ id: 'career_path' as Topic, label: '∴', title: 'Career Path', className: 'font-serif text-lg' }]
      : []),
  ];
  const workspaceFontScope = `workspace:${activeTopic}`;
  const workspaceFontScale = paneFontScales[workspaceFontScope] ?? 1;
  const isCodenWorkspace = activeTopic === 'coden';
  const hasCoordinateSensitiveEditor = isCodenWorkspace;

  return (
    <div className="flex-1 flex flex-col min-h-0 bg-coden-bg">
      <div className="flex items-center gap-1 px-4 pt-2 border-b border-coden-border bg-coden-surface/60">
        {topics.map((t) => (
          <button
            key={t.id}
            onClick={() => setActiveTopic(t.id)}
            disabled={t.disabled}
            title={t.title}
            aria-label={t.title}
            aria-disabled={t.disabled || undefined}
            className={[
              'h-9 min-w-9 px-2 pb-2 text-base font-semibold border-b-2 transition-colors',
              t.disabled
                ? 'cursor-not-allowed border-transparent text-coden-muted opacity-35'
                : activeTopic === t.id
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
          style={hasCoordinateSensitiveEditor ? undefined : { zoom: workspaceFontScale }}
          className={isCodenWorkspace ? 'flex-1 flex flex-col min-h-0' : 'w-full'}
        >
          {activeTopic === 'coden' ? (
            <div className="flex-1 bg-coden-surface rounded-xl shadow-lg flex flex-col min-h-0 overflow-hidden">
              <CodenTab />
            </div>
          ) : (
            <div className="w-full pb-24">
              {activeTopic === 'reference' && (
                <div className="bg-coden-surface rounded-xl border border-coden-border shadow-md overflow-hidden">
                  <ReferenceTab />
                </div>
              )}

              {activeTopic === 'guided_example' && (
                <div className="bg-coden-surface rounded-xl border border-coden-border shadow-md overflow-hidden">
                  <GuidedExampleTab />
                </div>
              )}

              {activeTopic === 'editorial' && editorialUnlocked && (
                <div className="bg-coden-surface rounded-xl border border-coden-border shadow-md overflow-hidden">
                  <EditorialTab />
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


function EditorialIcon({ locked }: { locked: boolean }) {
  return (
    <span className="relative inline-flex h-[18px] w-[18px] items-center justify-center">
      <svg
        viewBox="0 0 24 24"
        className="h-[18px] w-[18px]"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
      >
        <path d="M6 2.5h8l4 4v15H6z" />
        <path d="M14 2.5v4h4" />
        <path d="M9 11h6M9 14.5h6M9 18h4" />
      </svg>
      {locked && (
        <svg
          viewBox="0 0 12 12"
          className="absolute -bottom-1 -right-1 h-2.5 w-2.5 fill-coden-surface"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <rect x="2" y="5" width="8" height="6" rx="1" />
          <path d="M4 5V3.75a2 2 0 0 1 4 0V5" />
        </svg>
      )}
    </span>
  );
}


function ProfessorLectureIcon() {
  return (
    <svg
      viewBox="0 0 24 24"
      className="h-[18px] w-[18px]"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.7"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      <path d="M12 3h9v11h-8" />
      <path d="M15 7h3.5M15 10h2.5" />
      <circle cx="6.5" cy="6.5" r="2.25" />
      <path d="M2.5 18v-4.75a4 4 0 0 1 8 0V18" />
      <path d="m9.5 10.75 4-2.25" />
      <path d="M1.5 20h21" />
    </svg>
  );
}
