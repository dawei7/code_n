import { useAppStore } from '../store/useAppStore';


/**
 * StatusBanner — pass/fail/error message at the top of the
 * Description tab. The v0.9.0 pivot moved the detailed
 * verdict view (the static op count, the tolerance band, the
 * return value) into a dedicated Result tab. This banner
 * is the one-line summary the user sees when they're
 * reading the description.
 */
export function StatusBanner() {
  const runResult = useAppStore((s) => s.runResult);
  const error = useAppStore((s) => s.error);

  if (error) {
    return (
      <div className="bg-rose-900/30 border border-rose-700 text-rose-200 rounded px-3 py-2 text-sm">
        <span className="font-mono">Error: {error}</span>
      </div>
    );
  }

  if (!runResult) {
    return (
      <div className="bg-coden-surface border border-coden-border text-coden-muted rounded px-3 py-2 text-sm">
        Hit <span className="font-mono text-coden-text">▶ Run</span> (or{' '}
        <span className="font-mono text-coden-text">R</span> /{' '}
        <span className="font-mono text-coden-text">F5</span>) to execute your solution.
      </div>
    );
  }

  const { passed, correct, within_threshold, message, required_complexity, runtime_user_ms, runtime_limit_ms } = runResult;

  if (passed) {
    return (
      <div className="bg-emerald-900/30 border border-emerald-700 text-emerald-200 rounded px-3 py-2 text-sm">
        <div className="flex items-baseline justify-between">
          <span className="font-semibold">PASS: {message.split('\n')[0]}</span>
          <span className="text-xs font-mono">
            required {required_complexity}
          </span>
        </div>
        {message.includes('\n') && (
          <div className="text-xs text-emerald-300 mt-1">
            {message.split('\n').slice(1).join('\n')}
          </div>
        )}
      </div>
    );
  }

  if (correct && !within_threshold) {
    return (
      <div className="bg-amber-900/30 border border-amber-700 text-amber-200 rounded px-3 py-2 text-sm">
        <span className="font-semibold">SLOW: {message}</span>
        <div className="text-xs mt-1">
          Runtime {formatMs(runtime_user_ms)}; limit {formatMs(runtime_limit_ms)}; required {required_complexity}.
        </div>
      </div>
    );
  }

  return (
    <div className="bg-rose-900/30 border border-rose-700 text-rose-200 rounded px-3 py-2 text-sm">
      <span className="font-semibold">FAIL: {message}</span>
    </div>
  );
}

function formatMs(value: number | null | undefined): string {
  if (value === null || value === undefined) return 'not measured';
  if (value < 10) return `${value.toFixed(2)} ms`;
  if (value < 100) return `${value.toFixed(1)} ms`;
  return `${Math.round(value).toLocaleString()} ms`;
}
