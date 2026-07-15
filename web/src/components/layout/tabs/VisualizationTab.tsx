import { useEffect, useState } from 'react';

import { getVisualization } from '../../../api/visualizations';
import { useAppStore } from '../../../store/useAppStore';
import type { VisualizationDefinition } from '../../../types/api';
import { VisualizationPlayer } from '../../visualization/VisualizationPlayer';

type LoadState =
  | { kind: 'loading' }
  | { kind: 'error'; message: string }
  | { kind: 'ready'; definition: VisualizationDefinition };

export function VisualizationTab() {
  const challengeId = useAppStore((state) => state.currentDetail?.id ?? '');
  const [loadState, setLoadState] = useState<LoadState>({ kind: 'loading' });

  useEffect(() => {
    let cancelled = false;
    setLoadState({ kind: 'loading' });
    void getVisualization(challengeId)
      .then((definition) => {
        if (!cancelled) setLoadState({ kind: 'ready', definition });
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setLoadState({
            kind: 'error',
            message: error instanceof Error ? error.message : 'The visual walkthrough could not be loaded.',
          });
        }
      });
    return () => {
      cancelled = true;
    };
  }, [challengeId]);

  if (loadState.kind === 'loading') {
    return (
      <div className="flex min-h-64 items-center justify-center rounded-xl border border-coden-border bg-coden-surface text-sm text-coden-muted">
        Loading visual walkthrough...
      </div>
    );
  }

  if (loadState.kind === 'error') {
    return (
      <div role="alert" className="rounded-xl border border-coden-swap/50 bg-coden-surface p-6">
        <div className="text-sm font-semibold text-coden-text">Visual walkthrough unavailable</div>
        <div className="mt-2 text-xs text-coden-muted">{loadState.message}</div>
      </div>
    );
  }

  return (
    <VisualizationPlayer
      key={loadState.definition.challenge_id}
      definition={loadState.definition}
    />
  );
}
