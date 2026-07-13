import { apiGet } from './client';
import type { DebugCapabilitiesResponse } from '../types/api';

export function getCapabilities(): Promise<DebugCapabilitiesResponse> {
  return apiGet<DebugCapabilitiesResponse>('/debug/capabilities');
}

export const debugApi = { getCapabilities };
