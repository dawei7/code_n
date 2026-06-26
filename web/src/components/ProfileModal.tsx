import { useState, useEffect, useMemo } from 'react';
import { useAppStore } from '../store/useAppStore';
import { ALGORITHM_SETS, normalizeAlgorithmSet } from '../lib/algorithmSets';
import type { AlgorithmSetId } from '../lib/algorithmSets';

interface ProfileModalProps {
  onClose: () => void;
}

export function ProfileModal({ onClose }: ProfileModalProps) {
  const progress = useAppStore((s) => s.progress);
  const challenges = useAppStore((s) => s.challenges);
  const setActiveSet = useAppStore((s) => s.setActiveSet);
  const updateSettings = useAppStore((s) => s.updateSettings);

  const [apiKey, setApiKey] = useState('');
  const [selectedSet, setSelectedSet] = useState<AlgorithmSetId>('neetcode');
  const [setQuery, setSetQuery] = useState('');
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
      setSelectedSet(normalizeAlgorithmSet(progress.active_set));
    }
  }, [progress]);

  const filteredSets = useMemo(() => {
    const query = setQuery.trim().toLowerCase();
    if (!query) return ALGORITHM_SETS;
    return ALGORITHM_SETS.filter((setOption) => (
      setOption.label.toLowerCase().includes(query) ||
      setOption.shortLabel.toLowerCase().includes(query) ||
      setOption.description.toLowerCase().includes(query)
    ));
  }, [setQuery]);

  const handleSave = async () => {
    setSaving(true);
    try {
      if (selectedSet !== progress?.active_set) {
        await setActiveSet(selectedSet);
      }
      await updateSettings(false, progress?.leetcode_username || '', apiKey.trim());
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
            <div className="flex items-center justify-between gap-3">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">
                Selected Algorithm Set
              </h3>
              <input
                type="search"
                value={setQuery}
                onChange={(e) => setSetQuery(e.target.value)}
                placeholder="Filter sets"
                className="w-36 text-[11px] bg-slate-950 border border-slate-800 rounded-lg px-2 py-1.5 text-white outline-none focus:border-indigo-500"
              />
            </div>
            <div className="mt-1 max-h-44 overflow-y-auto rounded-xl border border-slate-850 bg-slate-950/30 p-1.5 space-y-1.5">
              {filteredSets.map((setOption) => {
                const isSelected = selectedSet === setOption.id;
                return (
                  <button
                    key={setOption.id}
                    type="button"
                    onClick={() => setSelectedSet(setOption.id)}
                    className={`w-full p-3 rounded-lg border text-left transition-all flex items-center gap-3 ${
                      isSelected
                        ? 'bg-indigo-950/40 border-indigo-500 text-white shadow-sm'
                        : 'bg-slate-950/40 border-slate-850 text-slate-400 hover:border-slate-700 hover:text-slate-300'
                    }`}
                  >
                    <span
                      className={`h-4 w-4 rounded-full border flex items-center justify-center shrink-0 ${
                        isSelected ? 'border-indigo-400' : 'border-slate-700'
                      }`}
                      aria-hidden="true"
                    >
                      {isSelected && <span className="h-2 w-2 rounded-full bg-indigo-400" />}
                    </span>
                    <span className="min-w-0">
                      <span className="block font-bold text-xs">{setOption.label}</span>
                      <span className="block text-[10px] text-slate-500 mt-0.5 leading-snug">
                        {setOption.description}
                      </span>
                    </span>
                  </button>
                );
              })}
              {filteredSets.length === 0 && (
                <div className="px-3 py-5 text-center text-xs text-slate-500">
                  No matching sets.
                </div>
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
