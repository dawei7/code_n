import { useEffect } from 'react';

interface InfoModalProps {
  onClose: () => void;
}

export function InfoModal({ onClose }: InfoModalProps) {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onClose]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md">
      <div className="w-full max-w-3xl bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[85vh] text-slate-200">
        
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-950">
          <h2 className="text-base font-bold text-white flex items-center gap-2">
            📖 System Glossary & Documentation
          </h2>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors text-sm px-2.5 py-1 rounded bg-slate-800 border border-slate-700 font-bold"
            title="Close (ESC)"
          >
            ✕ ESC
          </button>
        </div>

        {/* Content */}
        <div className="flex-grow overflow-y-auto p-6 space-y-6 scrollbar-thin text-sm leading-relaxed">
          
          {/* Section 1 */}
          <section className="space-y-2">
            <h3 className="text-sm font-bold text-indigo-400 border-b border-indigo-950 pb-1 uppercase tracking-wide">
              🚀 How It Works
            </h3>
            <p>
              cOde(n) is an automated algorithm checker that evaluates implementation correctness and performance scaling. 
              Write your solutions locally in your preferred editor (VSCode, Cursor, or the Antigravity desktop app).
            </p>
            <ul className="list-disc pl-5 space-y-1 text-slate-300">
              <li><strong>Local Editing:</strong> Open challenges directly in Antigravity. The files are located in <code className="bg-slate-950 px-1 py-0.5 rounded text-indigo-300 text-xs">solutions/&lt;challenge_id&gt;.py</code>.</li>
              <li><strong>Hot-Reload Runs:</strong> Clicking the <span className="font-semibold text-white">Run</span> button reads your solution directly from disk and compiles/runs it instantly.</li>
              <li><strong>AST Op Counts:</strong> Performance is measured by counting exact operations in the Python Abstract Syntax Tree (AST) rather than raw execution wall-clock time, ensuring absolute determinism regardless of system hardware.</li>
            </ul>
          </section>

          {/* Section 2 */}
          <section className="space-y-2">
            <h3 className="text-sm font-bold text-indigo-400 border-b border-indigo-950 pb-1 uppercase tracking-wide">
              🛣️ Algorithm Sets & Career Mode
            </h3>
            <p>
              Switch between available problem sets in Settings depending on your goals:
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-2">
              <div className="bg-slate-950 p-3 rounded-lg border border-slate-850">
                <h4 className="text-xs font-bold text-white mb-1">NeetCode 250 (Career Mode)</h4>
                <p className="text-xs text-slate-400">
                  Focus on 250 core interview preparation challenges mapped directly to LeetCode. 
                  Problems within each topic are locked sequentially: solve the first challenge in a topic to unlock the next harder one.
                </p>
              </div>
              <div className="bg-slate-950 p-3 rounded-lg border border-slate-850">
                <h4 className="text-xs font-bold text-white mb-1">GeeksforGeeks Library (Free Mode)</h4>
                <p className="text-xs text-slate-400">
                  Access the complete registry of 260+ challenges covering specialized computer science topics. 
                  All challenges are fully unlocked and available for practice at any time.
                </p>
              </div>
            </div>
          </section>

          {/* Section 3 */}
          <section className="space-y-2">
            <h3 className="text-sm font-bold text-indigo-400 border-b border-indigo-950 pb-1 uppercase tracking-wide">
              🧪 Practice vs Real Test Mode
            </h3>
            <ul className="space-y-3">
              <li>
                <strong>Practice Mode:</strong> Allows you to pick the input size (<code className="text-indigo-300">n</code>) and a seed. Ideal for testing boundaries, debugging exceptions, and checking intermediate step counts.
              </li>
              <li>
                <strong>Real Test Mode:</strong> The server overrides your <code className="text-indigo-300">n</code> and generates a random seed to run a verification suite. Your solution must pass this test to be marked as completed.
              </li>
            </ul>
          </section>

          {/* Section 4 */}
          <section className="space-y-2">
            <h3 className="text-sm font-bold text-indigo-400 border-b border-indigo-950 pb-1 uppercase tracking-wide">
              🤖 Gemini AI Tutor
            </h3>
            <p>
              When your solution fails verification or throws an exception, the integrated AI Tutor uses your Gemini API Key to inspect your code, trace AST executions, and provide high-quality hints. 
              Configure your API key in the <span className="font-semibold text-white">Settings Modal</span> to enable tutoring.
            </p>
          </section>

          {/* Section 5 */}
          <section className="space-y-2">
            <h3 className="text-sm font-bold text-indigo-400 border-b border-indigo-950 pb-1 uppercase tracking-wide">
              ⌨️ Keyboard Shortcuts
            </h3>
            <div className="grid grid-cols-2 gap-2 font-mono text-xs">
              <div className="bg-slate-950 p-2 rounded flex justify-between border border-slate-850">
                <span className="text-slate-400">Run Code</span>
                <span className="text-white bg-slate-900 px-1.5 py-0.5 rounded border border-slate-800">Ctrl + Enter</span>
              </div>
              <div className="bg-slate-950 p-2 rounded flex justify-between border border-slate-850">
                <span className="text-slate-400">Close Overlay</span>
                <span className="text-white bg-slate-900 px-1.5 py-0.5 rounded border border-slate-800">Esc</span>
              </div>
            </div>
          </section>

        </div>

        {/* Footer */}
        <div className="px-6 py-4 border-t border-slate-800 bg-slate-950 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-bold transition-all"
          >
            Close Guide
          </button>
        </div>

      </div>
    </div>
  );
}
