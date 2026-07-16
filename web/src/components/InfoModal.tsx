import { useEffect } from 'react';
import { BrandWordmark } from './BrandWordmark';

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
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-md">
      <div className="w-full max-w-3xl bg-coden-surface border border-coden-border rounded-xl shadow-2xl overflow-hidden flex flex-col max-h-[85vh] text-coden-text">
        <div className="flex items-center justify-between px-6 py-4 border-b border-coden-border bg-coden-bg">
          <div>
            <h2 className="text-base font-bold text-coden-text">
              About <BrandWordmark />
            </h2>
            <p className="text-xs text-coden-muted font-mono mt-0.5">Algorithms, debugging, and complexity in one workspace</p>
          </div>
          <button
            onClick={onClose}
            className="text-coden-muted hover:text-coden-text transition-colors text-sm px-2.5 py-1 rounded bg-coden-surface border border-coden-border font-bold"
            title="Close (ESC)"
          >
            x ESC
          </button>
        </div>

        <div className="flex-grow overflow-y-auto p-6 space-y-6 scrollbar-thin text-sm leading-relaxed">
          <section className="space-y-2">
            <h3 className="text-sm font-bold text-coden-accent border-b border-coden-border pb-1 uppercase tracking-wide">
              The Goal
            </h3>
            <p>
              cOde(n) is a focused practice environment for learning algorithms by writing real code, running deterministic tests, and inspecting performance behavior directly.
              The goal is to keep the full learning loop inside one app: read the problem, implement a solution, run it, debug it, and understand whether it scales.
            </p>
            <p>
              It is built for people who want the power of an editor and debugger without switching to a separate desktop IDE while solving interview-style challenges.
            </p>
          </section>

          <section className="space-y-2">
            <h3 className="text-sm font-bold text-coden-accent border-b border-coden-border pb-1 uppercase tracking-wide">
              Why The Name <BrandWordmark />
            </h3>
            <p>
              The name combines <strong>code</strong> with <strong>O(n)</strong>, the notation used to describe algorithmic complexity.
              That is the core idea of the app: code is not only about producing the right output, but also about understanding how the solution behaves as the input grows.
            </p>
            <p>
              The capital <strong>O</strong> is intentional. It points to Big-O thinking while still reading naturally as cOde(n).
            </p>
          </section>

          <section className="space-y-2">
            <h3 className="text-sm font-bold text-coden-accent border-b border-coden-border pb-1 uppercase tracking-wide">
              What The App Does
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <InfoCard
                title="Practice"
                body="Work through NeetCode-style career paths or an unlocked algorithm library with deterministic generated inputs."
              />
              <InfoCard
                title="Debug"
                body="Set breakpoints in the built-in editor and step through supported languages with locals visible beside the solution."
              />
              <InfoCard
                title="Analyze"
                body="Compare your solution against reference behavior using calibrated runtime checks and complexity guidance."
              />
              <InfoCard
                title="Learn"
                body="Use reference notes, mathematical explanations, and result feedback to understand the underlying pattern."
              />
            </div>
          </section>

          <section className="space-y-3">
            <h3 className="text-sm font-bold text-coden-accent border-b border-coden-border pb-1 uppercase tracking-wide">
              Contact
            </h3>
            <div className="flex flex-wrap gap-2">
              <a
                href="https://github.com/dawei7"
                target="_blank"
                rel="noreferrer"
                className="px-3 py-2 rounded border border-coden-border bg-coden-bg text-coden-text hover:border-coden-accent hover:text-coden-accent transition-colors font-mono text-xs"
              >
                GitHub: dawei7
              </a>
              <a
                href="https://www.linkedin.com/in/david-schmid-56194772/"
                target="_blank"
                rel="noreferrer"
                className="px-3 py-2 rounded border border-coden-border bg-coden-bg text-coden-text hover:border-coden-accent hover:text-coden-accent transition-colors font-mono text-xs"
              >
                LinkedIn: David Schmid
              </a>
            </div>
          </section>
        </div>

        <div className="px-6 py-4 border-t border-coden-border bg-coden-bg flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-1.5 bg-coden-accent hover:opacity-90 text-coden-accentContrast rounded-lg text-xs font-bold transition-all"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}

function InfoCard({ title, body }: { title: string; body: string }) {
  return (
    <div className="bg-coden-bg p-3 rounded-lg border border-coden-border">
      <h4 className="text-xs font-bold text-coden-text mb-1">{title}</h4>
      <p className="text-xs text-coden-muted">{body}</p>
    </div>
  );
}
