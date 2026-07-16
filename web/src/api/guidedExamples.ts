import { apiText } from './client';


export function getGuidedExample(challengeId: string): Promise<string> {
  return apiText(`/docs/by-id/${encodeURIComponent(challengeId)}/guided-example`);
}
