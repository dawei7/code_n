import { useEffect, useState } from 'react';

import type { VisualizationStepBase } from '../../types/api';

export type PlaybackSpeed = 0.75 | 1 | 1.5;

function isTypingTarget(target: EventTarget | null): boolean {
  if (!(target instanceof HTMLElement)) return false;
  return target.isContentEditable || ['INPUT', 'SELECT', 'TEXTAREA', 'BUTTON'].includes(target.tagName);
}

export function useVisualizationPlayback(steps: VisualizationStepBase[]) {
  const [stepIndex, setStepIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState<PlaybackSpeed>(1);
  const lastIndex = steps.length - 1;

  useEffect(() => {
    if (!playing) return undefined;
    if (stepIndex >= lastIndex) {
      setPlaying(false);
      return undefined;
    }
    const timer = window.setTimeout(() => {
      setStepIndex((current) => Math.min(current + 1, lastIndex));
    }, steps[stepIndex].duration_ms / speed);
    return () => window.clearTimeout(timer);
  }, [lastIndex, playing, speed, stepIndex, steps]);

  const selectStep = (next: number) => {
    setPlaying(false);
    setStepIndex(Math.max(0, Math.min(next, lastIndex)));
  };

  const togglePlayback = () => {
    if (playing) {
      setPlaying(false);
      return;
    }
    if (stepIndex >= lastIndex) setStepIndex(0);
    setPlaying(true);
  };

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (isTypingTarget(event.target)) return;
      if (event.key === 'ArrowLeft') {
        event.preventDefault();
        selectStep(stepIndex - 1);
      } else if (event.key === 'ArrowRight') {
        event.preventDefault();
        selectStep(stepIndex + 1);
      } else if (event.key === ' ') {
        event.preventDefault();
        togglePlayback();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  });

  return {
    stepIndex,
    playing,
    speed,
    lastIndex,
    selectStep,
    togglePlayback,
    setSpeed,
  };
}
