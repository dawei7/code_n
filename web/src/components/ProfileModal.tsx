import { useState, useEffect } from 'react';
import { useAppStore } from '../store/useAppStore';

interface ProfileModalProps {
  onClose: () => void;
}

export function ProfileModal({ onClose }: ProfileModalProps) {
  const progress = useAppStore((s) => s.progress);
  const challenges = useAppStore((s) => s.challenges);
  const setActiveSet = useAppStore((s) => s.setActiveSet);
  const updateSettings = useAppStore((s) => s.updateSettings);

  const [apiKey, setApiKey] = useState('');
  const [selectedSet, setSelectedSet] = useState<'gfg' | 'neetcode'>('neetcode');
  const [saving, setSaving] = useState(false);

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
      setSelectedSet((progress.active_set as 'gfg' | 'neetcode') || 'neetcode');
    }
  }, [progress]);

  const handleSave = async () => {
    setSaving(true);
    try {
      // Save Gemini key
      await updateSettings(false, progress?.leetcode_username || '', apiKey.trim());
      // Sync active set
      if (selectedSet !== progress?.active_set) {
        await setActiveSet(selectedSet);
      }
      onClose();
    } catch (e) {
      console.error('Failed to save settings:', e);
    } finally {
      setSaving(false);
    }
  };

  const solvedCount = progress?.completed ? progress.completed.length : 0;

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
                <span className="font-mono font-bold text-emerald-400 text-sm">{solvedCount} / {challenges.length}</span>
              </div>
            </div>
          </div>

          {/* Active Set Configuration */}
          <div className="space-y-2">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">
              Selected Algorithm Set
            </h3>
            <div className="grid grid-cols-2 gap-3 mt-1">
              <button
                type="button"
                onClick={() => setSelectedSet('neetcode')}
                className={`p-3 rounded-xl border text-left transition-all ${
                  selectedSet === 'neetcode'
                    ? 'bg-indigo-950/40 border-indigo-500 text-white shadow-sm'
                    : 'bg-slate-950/40 border-slate-850 text-slate-400 hover:border-slate-800 hover:text-slate-300'
                }`}
              >
                <div className="font-bold text-xs">NeetCode 250</div>
                <div className="text-[10px] text-slate-500 mt-0.5 leading-snug">
                  Curated core challenges with roadmap & dependency locking.
                </div>
              </button>

              <button
                type="button"
                onClick={() => setSelectedSet('gfg')}
                className={`p-3 rounded-xl border text-left transition-all ${
                  selectedSet === 'gfg'
                    ? 'bg-indigo-950/40 border-indigo-500 text-white shadow-sm'
                    : 'bg-slate-950/40 border-slate-850 text-slate-400 hover:border-slate-800 hover:text-slate-300'
                }`}
              >
                <div className="font-bold text-xs">GeeksforGeeks</div>
                <div className="text-[10px] text-slate-500 mt-0.5 leading-snug">
                  260+ standard algorithms library, fully unlocked.
                </div>
              </button>
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
