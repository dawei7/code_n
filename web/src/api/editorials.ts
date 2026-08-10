import { apiText } from './client';


export function getEditorial(challengeId: string): Promise<string> {
  return apiText(`/docs/by-id/${encodeURIComponent(challengeId)}/editorial`);
}
