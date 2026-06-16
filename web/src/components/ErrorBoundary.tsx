/**
 * ErrorBoundary — top-level catch for React render errors.
 *
 * Without this, any exception inside a child component
 * (e.g. a TypeError from a bad prop, an undefined access on
 * a new field) would unmount the entire app and leave the
 * user with the dark coden-bg color and no content — a
 * black-screen failure that's hard to debug. With this
 * boundary, the error is rendered as a visible red card
 * with the message + stack, so the user can copy the error
 * and the developer can see exactly what broke.
 *
 * Only the top-level AppShell uses this — child components
 * can still have their own boundaries if they need to
 * isolate failure to a pane.
 */
import { Component, type ErrorInfo, type ReactNode } from 'react';


interface Props {
  children: ReactNode;
}

interface State {
  error: Error | null;
}


export class ErrorBoundary extends Component<Props, State> {
  state: State = { error: null };

  static getDerivedStateFromError(error: Error): State {
    return { error };
  }

  componentDidCatch(error: Error, info: ErrorInfo): void {
    // Log to the console so the dev tools see it. The
    // visible card below is the user-facing part.
    console.error('[ErrorBoundary]', error, info);
  }

  render() {
    const { error } = this.state;
    if (!error) return this.props.children;
    return (
      <div className="h-full w-full bg-coden-bg text-coden-text p-6 overflow-auto">
        <div className="max-w-3xl mx-auto border border-red-500/60 bg-red-500/10 rounded p-4 font-mono text-xs">
          <div className="text-red-300 font-semibold mb-2">
            ⚠ cOde(n) crashed
          </div>
          <div className="text-coden-muted mb-3">
            A React component threw during render. The error
            below is what broke — please report it so we can
            fix it.
          </div>
          <div className="text-coden-text mb-3 break-words">
            <span className="text-red-300 font-semibold">
              {error.name}:
            </span>{' '}
            {error.message}
          </div>
          <pre className="text-[10px] text-coden-muted whitespace-pre-wrap break-words bg-coden-bg/60 rounded p-2 max-h-96 overflow-y-auto">
            {error.stack}
          </pre>
          <button
            type="button"
            onClick={() => this.setState({ error: null })}
            className="mt-3 px-3 py-1.5 text-xs rounded border border-coden-border text-coden-text hover:bg-coden-border"
          >
            Try to recover
          </button>
        </div>
      </div>
    );
  }
}
