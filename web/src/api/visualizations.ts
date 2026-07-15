import { apiGet } from './client';
import type { VisualizationDefinition } from '../types/api';

export function getVisualization(challengeId: string): Promise<VisualizationDefinition> {
  return apiGet<VisualizationDefinition>(
    `/visualizations/${encodeURIComponent(challengeId)}`,
  );
}
