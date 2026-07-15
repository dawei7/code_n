import type {
  VisualizationDefinition,
  VisualizationPhase,
  VisualizationStepBase,
  VisualizationTone,
} from '../../types/api';
import { VisualizationCodeStage } from './VisualizationCodeStage';
import { VisualizationControls } from './VisualizationControls';
import { VisualizationScene } from './rendererRegistry';
import { useVisualizationPlayback } from './useVisualizationPlayback';

export function VisualizationPlayer({ definition }: { definition: VisualizationDefinition }) {
  const playback = useVisualizationPlayback(definition.steps);
  const step = definition.steps[playback.stepIndex];
  const currentPhaseIndex = definition.phases.findIndex((phase) => phase.id === step.phase);

  return (
    <section
      aria-label={`${definition.title} interactive visual walkthrough`}
      className="coden-visual-root overflow-hidden rounded-xl border border-coden-border bg-coden-surface shadow-lg"
    >
      <VisualizationHeader definition={definition} />
      <LearningCompass definition={definition} />
      <PhaseTimeline
        phases={definition.phases}
        steps={definition.steps}
        currentPhaseIndex={currentPhaseIndex}
        onSelectStep={playback.selectStep}
      />

      <div className="grid gap-4 p-4 xl:grid-cols-[minmax(0,1.3fr)_minmax(22rem,0.7fr)]">
        <VisualizationScene
          definition={definition}
          stepIndex={playback.stepIndex}
        />
        <VisualizationCodeStage
          challengeId={definition.challenge_id}
          code={definition.code}
          activeAnchors={step.active_code}
        />
      </div>

      <Narration step={step} />

      <VisualizationControls
        current={playback.stepIndex}
        total={definition.steps.length}
        playing={playback.playing}
        speed={playback.speed}
        stepTitle={step.title}
        onPrevious={() => playback.selectStep(playback.stepIndex - 1)}
        onNext={() => playback.selectStep(playback.stepIndex + 1)}
        onTogglePlayback={playback.togglePlayback}
        onSelect={playback.selectStep}
        onSpeedChange={playback.setSpeed}
      />
    </section>
  );
}

function VisualizationHeader({ definition }: { definition: VisualizationDefinition }) {
  return (
    <header className="flex flex-col gap-3 border-b border-coden-border bg-coden-inner/60 px-5 py-4 lg:flex-row lg:items-start lg:justify-between">
      <div className="min-w-0">
        <div className="flex flex-wrap items-center gap-2">
          <h2 className="text-base font-semibold text-coden-text">{definition.title}</h2>
          <span className="rounded-full border border-coden-accent/40 bg-coden-accent/10 px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wide text-coden-accent">
            {definition.pattern}
          </span>
        </div>
        <p className="mt-1 max-w-3xl text-xs leading-relaxed text-coden-muted">{definition.summary}</p>
      </div>
      <div className="flex shrink-0 flex-wrap items-center gap-2 font-mono text-xs text-coden-text">
        <span className="rounded border border-coden-border bg-coden-bg px-2 py-1">Time {definition.complexity.time}</span>
        <span className="rounded border border-coden-border bg-coden-bg px-2 py-1">Space {definition.complexity.space}</span>
      </div>
    </header>
  );
}

function LearningCompass({ definition }: { definition: VisualizationDefinition }) {
  return (
    <div className="grid border-b border-coden-border bg-coden-bg/35 md:grid-cols-2">
      <div className="px-5 py-3 md:border-r md:border-coden-border">
        <div className="text-[9px] font-semibold uppercase tracking-wider text-coden-accent">Learning goal</div>
        <p className="mt-1 text-[11px] leading-relaxed text-coden-text">{definition.learning_objective}</p>
      </div>
      <div className="border-t border-coden-border px-5 py-3 md:border-t-0">
        <div className="text-[9px] font-semibold uppercase tracking-wider text-coden-compare">Invariant to watch</div>
        <p className="mt-1 text-[11px] leading-relaxed text-coden-text">{definition.invariant}</p>
      </div>
    </div>
  );
}

function PhaseTimeline({
  phases,
  steps,
  currentPhaseIndex,
  onSelectStep,
}: {
  phases: VisualizationPhase[];
  steps: VisualizationStepBase[];
  currentPhaseIndex: number;
  onSelectStep: (index: number) => void;
}) {
  return (
    <nav aria-label="Walkthrough phases" className="border-b border-coden-border bg-coden-surface px-4 py-3">
      <ol className="grid gap-2 sm:grid-cols-2 xl:grid-cols-4">
        {phases.map((phase, index) => {
          const firstStep = steps.findIndex((step) => step.phase === phase.id);
          const active = index === currentPhaseIndex;
          const complete = index < currentPhaseIndex;
          return (
            <li key={phase.id}>
              <button
                type="button"
                onClick={() => onSelectStep(firstStep)}
                aria-current={active ? 'step' : undefined}
                className={`flex w-full items-start gap-2 rounded-md border px-3 py-2 text-left transition-colors ${
                  active
                    ? 'border-coden-accent bg-coden-accent/10'
                    : complete
                      ? 'border-coden-border bg-coden-inner/60'
                      : 'border-transparent bg-coden-bg/40 hover:border-coden-border'
                }`}
              >
                <span className={`flex h-5 w-5 shrink-0 items-center justify-center rounded-full border font-mono text-[9px] ${
                  active || complete
                    ? 'border-coden-accent text-coden-accent'
                    : 'border-coden-border text-coden-muted'
                }`}>
                  {complete ? '✓' : index + 1}
                </span>
                <span className="min-w-0">
                  <span className="block text-[11px] font-semibold text-coden-text">{phase.title}</span>
                  <span className="mt-0.5 block text-[9px] leading-relaxed text-coden-muted">{phase.summary}</span>
                </span>
              </button>
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

function Narration({ step }: { step: VisualizationStepBase }) {
  return (
    <div className="mx-4 mb-4 overflow-hidden rounded-lg border border-coden-border bg-coden-inner/50" aria-live="polite">
      <div className="px-4 py-3">
        <div className="flex flex-wrap items-center gap-2">
          <StepBadge label={step.badge.label} tone={step.badge.tone} />
          <h3 className="text-sm font-semibold text-coden-text">{step.title}</h3>
        </div>
        <p className="mt-1 text-xs leading-relaxed text-coden-text">{step.description}</p>
      </div>
      {step.insight && (
        <div className="flex gap-2 border-t border-coden-border bg-coden-bg/50 px-4 py-2.5 text-[11px] leading-relaxed text-coden-muted">
          <span aria-hidden="true" className="font-semibold text-coden-compare">◆</span>
          <span><strong className="text-coden-text">Why it matters:</strong> {step.insight}</span>
        </div>
      )}
    </div>
  );
}

function StepBadge({ label, tone }: { label: string; tone: VisualizationTone }) {
  const toneClass: Record<VisualizationTone, string> = {
    neutral: 'border-coden-border bg-coden-bg text-coden-muted',
    active: 'border-coden-read/50 bg-coden-read/10 text-coden-read',
    attention: 'border-coden-compare/50 bg-coden-compare/10 text-coden-compare',
    success: 'border-coden-accent/40 bg-coden-accent/10 text-coden-accent',
  };
  return (
    <span className={`rounded-full border px-2 py-0.5 text-[9px] font-semibold uppercase tracking-wide ${toneClass[tone]}`}>
      {label}
    </span>
  );
}
