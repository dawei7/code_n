import { useState, useEffect, useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';
import { challengesForAlgorithmSet } from '../lib/algorithmSets';
import type { LeetCodeSessionStatus } from '../types/electron';

interface ProfileModalProps {
  onClose: () => void;
}

export function ProfileModal({ onClose }: ProfileModalProps) {
  const progress = useAppStore((s) => s.progress);
  const challenges = useAppStore((s) => s.challenges);
  const activeSet = useAppStore((s) => s.activeSet);
  const updateSettings = useAppStore((s) => s.updateSettings);

  const [apiKey, setApiKey] = useState('');
  const [saving, setSaving] = useState(false);
  const [leetcodeSession, setLeetcodeSession] = useState('');
  const [leetcodeCsrf, setLeetcodeCsrf] = useState('');
  const [leetcodeClearance, setLeetcodeClearance] = useState('');
  const [leetcodeStatus, setLeetcodeStatus] = useState<LeetCodeSessionStatus | null>(null);
  const [checkingLeetCode, setCheckingLeetCode] = useState(false);
  const [leetcodeError, setLeetcodeError] = useState('');

  // Esc key closure
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onClose]);

  useEffect(() => {
    if (progress) {
      setApiKey(progress.gemini_api_key || '');
    }
  }, [progress]);

  const refreshLeetCodeStatus = async () => {
    if (!window.electronAPI) {
      setLeetcodeStatus({ configured: false, secureStorageAvailable: false, state: 'unavailable', message: 'LeetCode submission settings are available in the desktop app.' });
      return;
    }
    setCheckingLeetCode(true);
    setLeetcodeError('');
    try {
      setLeetcodeStatus(await window.electronAPI.getLeetCodeSessionStatus());
    } catch (error) {
      setLeetcodeError(error instanceof Error ? error.message : String(error));
    } finally {
      setCheckingLeetCode(false);
    }
  };

  const saveAndVerifyLeetCode = async (): Promise<LeetCodeSessionStatus | null> => {
    if (!window.electronAPI) {
      setLeetcodeError('LeetCode credentials require the desktop app.');
      return null;
    }
    const hasVisibleCredentials = Boolean(
      leetcodeSession.trim() || leetcodeCsrf.trim() || leetcodeClearance.trim(),
    );
    setCheckingLeetCode(true);
    setLeetcodeError('');
    try {
      if (hasVisibleCredentials) {
        if (!leetcodeSession.trim() || !leetcodeCsrf.trim()) {
          throw new Error('Both LEETCODE_SESSION and csrftoken are required.');
        }
        await window.electronAPI.saveLeetCodeCredentials({
          session: leetcodeSession,
          csrfToken: leetcodeCsrf,
          cloudflareClearance: leetcodeClearance,
        });
      }
      const status = await window.electronAPI.getLeetCodeSessionStatus();
      setLeetcodeStatus(status);
      if (status.state === 'valid') {
        // Do not retain secrets in React state after they have entered the
        // OS-encrypted Electron store.
        setLeetcodeSession('');
        setLeetcodeCsrf('');
        setLeetcodeClearance('');
      }
      return status;
    } catch (error) {
      setLeetcodeError(error instanceof Error ? error.message : String(error));
      return null;
    } finally {
      setCheckingLeetCode(false);
    }
  };

  useEffect(() => {
    void refreshLeetCodeStatus();
  }, []);

  const handleSave = async () => {
    setSaving(true);
    try {
      if (leetcodeSession.trim() || leetcodeCsrf.trim() || leetcodeClearance.trim()) {
        const status = await saveAndVerifyLeetCode();
        if (!status || status.state !== 'valid') return;
      }
      await updateSettings(false, progress?.leetcode_username || '', apiKey.trim());
      onClose();
    } catch (e) {
      console.error('Failed to save settings:', e);
    } finally {
      setSaving(false);
    }
  };

  const selectedChallenges = useMemo(
    () => challengesForAlgorithmSet(challenges, activeSet),
    [challenges, activeSet],
  );
  const selectedChallengeCount = selectedChallenges.length;
  const solvedCount = useMemo(() => {
    const completed = new Set(progress?.completed ?? []);
    return selectedChallenges.filter((challenge) => completed.has(challenge.id)).length;
  }, [progress?.completed, selectedChallenges]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md">
      <div className="w-full max-w-xl bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden flex flex-col text-slate-200">
        
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-950">
          <h2 className="text-base font-bold text-white flex items-center gap-2">
            ⚙️ App Settings & Configuration
          </h2>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors text-sm px-2.5 py-1 rounded bg-slate-800 border border-slate-700 font-bold"
            title="Cancel (ESC)"
          >
            ✕ ESC
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6">
          
          {/* User Profile Info (Static/Information - Not Clickable) */}
          <div className="p-4 bg-slate-950 rounded-xl border border-slate-850 space-y-2">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">
              User Profile
            </h3>
            <div className="grid grid-cols-2 gap-4 text-xs mt-1">
              <div>
                <span className="block text-slate-500">Username</span>
                <span className="font-mono font-bold text-white text-sm">dawei7</span>
              </div>
              <div>
                <span className="block text-slate-500">Challenges Solved</span>
                <span className="font-mono font-bold text-emerald-400 text-sm">{solvedCount} / {selectedChallengeCount}</span>
              </div>
            </div>
          </div>

          {/* Gemini API Key */}
          <div className={`space-y-3 rounded-xl border bg-slate-950/60 p-4 transition-colors ${leetcodeStatus?.state === 'valid' ? 'border-emerald-500/40' : leetcodeStatus?.state === 'expired' || leetcodeStatus?.state === 'blocked' || leetcodeError ? 'border-amber-500/40' : 'border-slate-800'}`}>
            <div className="flex items-start justify-between gap-3">
              <div>
                <h3 className="text-xs font-bold uppercase tracking-wider text-slate-300">LeetCode connection</h3>
                <p className="mt-1 text-[10px] leading-relaxed text-slate-500">
                  Used only to send reviewed package submissions after you solve a problem locally. Values are encrypted with your operating system and never stored in progress.json.
                </p>
              </div>
              <span className={`shrink-0 rounded-full border px-2 py-1 text-[9px] font-bold uppercase ${leetcodeStatus?.state === 'valid' ? 'border-emerald-500/40 text-emerald-300' : leetcodeStatus?.state === 'expired' || leetcodeStatus?.state === 'blocked' ? 'border-amber-500/40 text-amber-300' : 'border-slate-700 text-slate-400'}`}>
                {checkingLeetCode ? 'Checking' : leetcodeStatus?.state || 'Unknown'}
              </span>
            </div>
            {leetcodeStatus && (
              <div className={`text-[11px] ${leetcodeStatus.state === 'valid' ? 'text-emerald-300' : 'text-slate-400'}`}>
                {leetcodeStatus.message}
                {leetcodeStatus.username && <span className="ml-1 font-bold text-white">@{leetcodeStatus.username}{leetcodeStatus.is_premium ? ' · Premium' : ''}</span>}
              </div>
            )}
            {leetcodeError && <div className="text-[11px] font-medium text-amber-300">{leetcodeError}</div>}
            <p className="text-[10px] leading-relaxed text-slate-500">
              In a signed-in leetcode.com tab, open Developer Tools → Application → Cookies and copy the values named LEETCODE_SESSION and csrftoken. Cloudflare clearance is optional unless LeetCode blocks the connection.
            </p>
            <div className="grid gap-2">
              <input type="password" value={leetcodeSession} onChange={(event) => setLeetcodeSession(event.target.value)} placeholder="LEETCODE_SESSION (leave blank to keep saved value)" autoComplete="off" className="w-full rounded-lg border border-slate-800 bg-slate-950 px-3 py-2 font-mono text-xs text-white outline-none focus:border-coden-accent" />
              <input type="password" value={leetcodeCsrf} onChange={(event) => setLeetcodeCsrf(event.target.value)} placeholder="csrftoken" autoComplete="off" className="w-full rounded-lg border border-slate-800 bg-slate-950 px-3 py-2 font-mono text-xs text-white outline-none focus:border-coden-accent" />
              <input type="password" value={leetcodeClearance} onChange={(event) => setLeetcodeClearance(event.target.value)} placeholder="cf_clearance (optional)" autoComplete="off" className="w-full rounded-lg border border-slate-800 bg-slate-950 px-3 py-2 font-mono text-xs text-white outline-none focus:border-coden-accent" />
            </div>
            <div className="flex gap-2">
              <button type="button" onClick={() => void saveAndVerifyLeetCode()} disabled={checkingLeetCode} className="rounded-lg border border-slate-700 px-3 py-1.5 text-[10px] font-bold text-slate-300 hover:border-coden-accent disabled:opacity-50">{checkingLeetCode ? 'Verifying…' : leetcodeSession.trim() || leetcodeCsrf.trim() || leetcodeClearance.trim() ? 'Save & verify session' : 'Verify session'}</button>
              {leetcodeStatus?.configured && window.electronAPI && (
                <button type="button" onClick={async () => { setLeetcodeStatus(await window.electronAPI!.clearLeetCodeCredentials()); setLeetcodeSession(''); setLeetcodeCsrf(''); setLeetcodeClearance(''); }} className="rounded-lg border border-red-900/60 px-3 py-1.5 text-[10px] font-bold text-red-300 hover:border-red-500">Disconnect</button>
              )}
            </div>
          </div>

          {/* Gemini API Key */}
          <div className="space-y-1">
            <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">
              Gemini API Key (Google AI Studio)
            </label>
            <input
              type="password"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder="Enter Gemini API key (starts with AIzaSy...)"
              className="w-full text-xs bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-white outline-none focus:border-indigo-500 font-mono"
            />
          </div>

        </div>

        {/* Footer with Save / Cancel */}
        <div className="px-6 py-4 border-t border-slate-800 bg-slate-950 flex items-center justify-end gap-3">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 hover:bg-slate-800 text-slate-300 border border-slate-800 rounded-lg text-xs font-semibold transition-all"
          >
            Cancel
          </button>
          <button
            type="button"
            onClick={handleSave}
            disabled={saving}
            className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white rounded-lg text-xs font-bold transition-all shadow-md"
          >
            {saving ? 'Saving...' : 'Save Settings'}
          </button>
        </div>

      </div>
    </div>
  );
}
