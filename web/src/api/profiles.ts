import { apiGet, apiPost, apiDelete } from './client';
import type { ProfilesResponse } from '../types/api';

export function listProfiles(): Promise<ProfilesResponse> {
  return apiGet<ProfilesResponse>('/profiles');
}

export function createProfile(
  name: string,
  careerMode: boolean,
  leetcodeUsername: string,
): Promise<ProfilesResponse> {
  return apiPost<ProfilesResponse>('/profiles', {
    name,
    career_mode: careerMode,
    leetcode_username: leetcodeUsername,
  });
}

export function selectProfile(name: string): Promise<ProfilesResponse> {
  return apiPost<ProfilesResponse>(`/profiles/${encodeURIComponent(name)}/select`, {});
}

export function deleteProfile(name: string): Promise<ProfilesResponse> {
  return apiDelete<ProfilesResponse>(`/profiles/${encodeURIComponent(name)}`);
}
