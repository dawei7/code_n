import ReactMarkdown from 'react-markdown';
import { useMemo, useState } from 'react';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import 'katex/dist/katex.min.css';
import { useAppStore } from '../../../store/useAppStore';
import { analyzeChallenge } from '../../../api/run';
import { ApiError } from '../../../api/client';
import type { SupportedLanguage, TutorChatMessage } from '../../../types/api';


const tutorHistoryStorageKey = 'coden-ai-tutor-chat-history-v1';


interface TutorChatSession {
  id: string;
  challengeId: string;
  challengeName: string;
  language: SupportedLanguage;
  createdAt: string;
  updatedAt: string;
  messages: TutorChatMessage[];
}


function loadTutorHistory(): TutorChatSession[] {
  try {
    const raw = localStorage.getItem(tutorHistoryStorageKey);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) return [];
    return parsed.filter(isTutorChatSession);
  } catch {
    return [];
  }
}


function isTutorChatSession(value: unknown): value is TutorChatSession {
  if (!value || typeof value !== 'object') return false;
  const item = value as Partial<TutorChatSession>;
  return (
    typeof item.id === 'string'
    && typeof item.challengeId === 'string'
    && typeof item.challengeName === 'string'
    && typeof item.language === 'string'
    && typeof item.createdAt === 'string'
    && typeof item.updatedAt === 'string'
    && Array.isArray(item.messages)
  );
}


function saveTutorHistory(sessions: TutorChatSession[]): void {
  localStorage.setItem(tutorHistoryStorageKey, JSON.stringify(sessions));
}


function makeTutorSessionId(): string {
  return `tutor-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
}


function sessionLabel(session: TutorChatSession): string {
  const firstQuestion = session.messages.find((message) => message.role === 'user')?.content.trim();
  if (firstQuestion) return compactText(firstQuestion, 44);
  return `Analysis ${formatSessionDate(session.createdAt)}`;
}


function compactText(value: string, maxLength: number): string {
  const normalized = value.replace(/\s+/g, ' ').trim();
  return normalized.length <= maxLength ? normalized : `${normalized.slice(0, maxLength - 3)}...`;
}


function formatSessionDate(value: string): string {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return 'saved chat';
  return date.toLocaleString([], {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
}


function latestAssistant(messages: TutorChatMessage[]): string {
  return [...messages].reverse().find((message) => message.role === 'assistant')?.content ?? '';
}


export function AITutorTab() {
  const detail = useAppStore((s) => s.currentDetail);
  const result = useAppStore((s) => s.runResult);
  const codeLanguage = useAppStore((s) => s.codeLanguage);
  const source = useAppStore((s) => s.source);
  const progress = useAppStore((s) => s.progress);
  const aiStatus = useAppStore((s) => s.aiStatus);
  const aiMessages = useAppStore((s) => s.aiMessages);
  const aiError = useAppStore((s) => s.aiError);
  const setAiStatus = useAppStore((s) => s.setAiStatus);
  const setAiAnalysis = useAppStore((s) => s.setAiAnalysis);
  const setAiMessages = useAppStore((s) => s.setAiMessages);
  const setAiError = useAppStore((s) => s.setAiError);
  const [draft, setDraft] = useState('');
  const [tutorHistory, setTutorHistory] = useState<TutorChatSession[]>(loadTutorHistory);
  const [activeTutorSessionId, setActiveTutorSessionId] = useState<string | null>(null);

  const visibleTutorSessions = useMemo(() => {
    if (!detail) return [];
    return tutorHistory
      .filter((session) => session.challengeId === detail.id && session.language === codeLanguage)
      .sort((a, b) => Date.parse(b.updatedAt) - Date.parse(a.updatedAt));
  }, [codeLanguage, detail, tutorHistory]);

  const isLoading = aiStatus === 'loading';
  const hasMessages = aiMessages.length > 0;
  const activeSavedSessionId = visibleTutorSessions.some((session) => session.id === activeTutorSessionId)
    ? activeTutorSessionId
    : null;

  const setTutorError = (e: unknown) => {
    if (e instanceof ApiError && e.detail && typeof e.detail === 'object' && 'detail' in e.detail) {
      setAiError(String((e.detail as any).detail));
    } else {
      setAiError(e instanceof Error ? e.message : String(e));
    }
  };

  const updateTutorHistory = (updater: (sessions: TutorChatSession[]) => TutorChatSession[]) => {
    setTutorHistory((current) => {
      const next = updater(current);
      saveTutorHistory(next);
      return next;
    });
  };

  const restoreTutorSession = (sessionId: string) => {
    const session = tutorHistory.find((item) => item.id === sessionId);
    if (!session) return;
    setActiveTutorSessionId(session.id);
    setAiMessages(session.messages);
    setAiAnalysis(latestAssistant(session.messages));
    setAiStatus('loaded');
    setAiError('');
  };

  const deleteTutorSession = (sessionId: string) => {
    updateTutorHistory((sessions) => sessions.filter((session) => session.id !== sessionId));
    if (activeTutorSessionId === sessionId) {
      startNewTutorChat();
    }
  };

  const startNewTutorChat = () => {
    setActiveTutorSessionId(null);
    setAiMessages([]);
    setAiAnalysis('');
    setAiStatus('idle');
    setAiError('');
  };

  const sendQuestion = async (question: string) => {
    if (!detail) return;
    const trimmed = question.trim();
    if (!trimmed || isLoading) return;

    if (!progress?.gemini_api_key?.trim()) {
      setAiStatus('error');
      setAiError('Please configure your Gemini API Key in the Profile settings first.');
      return;
    }

    const state = useAppStore.getState();
    const previousMessages = state.aiMessages;
    const nextMessages: TutorChatMessage[] = [
      ...previousMessages,
      { role: 'user', content: trimmed },
    ];
    setAiMessages(nextMessages);
    setAiStatus('loading');
    setAiError('');

    try {
      const latestResult = state.runResult;
      const activeOptimalSource = detail.optimal_sources?.[state.codeLanguage] || detail.optimal_source;
      const res = await analyzeChallenge({
        challengeId: detail.id,
        source: state.source,
        language: state.codeLanguage,
        returned: latestResult?.return_value_repr ?? '',
        expected: latestResult?.reference_return_value_repr ?? '',
        inputs: latestResult?.setup_data_repr ?? {},
        optimalSource: activeOptimalSource,
        question: trimmed,
        messages: previousMessages,
      });
      const completedMessages: TutorChatMessage[] = [
        ...nextMessages,
        { role: 'assistant', content: res.analysis },
      ];
      const now = new Date().toISOString();
      const sessionId = activeTutorSessionId ?? makeTutorSessionId();
      setActiveTutorSessionId(sessionId);
      updateTutorHistory((sessions) => {
        const existing = sessions.find((session) => session.id === sessionId);
        const updatedSession: TutorChatSession = {
          id: sessionId,
          challengeId: detail.id,
          challengeName: detail.name,
          language: state.codeLanguage,
          createdAt: existing?.createdAt ?? now,
          updatedAt: now,
          messages: completedMessages,
        };
        return [updatedSession, ...sessions.filter((session) => session.id !== sessionId)];
      });
      setAiAnalysis(res.analysis);
      setAiMessages(completedMessages);
      setAiStatus('loaded');
    } catch (e) {
      setAiStatus('error');
      setTutorError(e);
    }
  };

  const submitDraft = () => {
    const question = draft.trim();
    if (!question || isLoading) return;
    setDraft('');
    void sendQuestion(question);
  };

  const analyzeLatestRun = () => {
    if (!result) return;
    const question = result.passed
      ? 'Please review my latest accepted solution. What should I understand about correctness, edge cases, and complexity before I move on?'
      : 'Please analyze my latest run and help me find the issue without giving me the full solution.';
    void sendQuestion(question);
  };

  if (!detail) {
    return (
      <div className="flex items-center justify-center text-xs text-coden-muted p-4">
        Pick a challenge from the left rail.
      </div>
    );
  }

  const hasCurrentSource = Boolean(source.trim());

  return (
    <div className="flex flex-col gap-4 lg:grid lg:grid-cols-[260px_minmax(0,1fr)]">
      <aside className="border border-coden-border bg-coden-surface rounded-lg p-3 min-h-[28rem]">
        <div className="flex items-center justify-between gap-3 border-b border-coden-border pb-3">
          <div className="flex items-center gap-2">
            <span className="h-7 min-w-7 rounded border border-coden-accent/50 bg-coden-accent/10 text-coden-accent font-mono text-xs font-bold flex items-center justify-center">
              AI
            </span>
            <div>
              <div className="text-xs font-semibold text-coden-text">Tutor Chats</div>
              <div className="text-[10px] text-coden-muted">{visibleTutorSessions.length} saved</div>
            </div>
          </div>
          <button
            type="button"
            onClick={startNewTutorChat}
            disabled={isLoading}
            className="px-2 py-1 text-xs rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50"
          >
            New
          </button>
        </div>
        <div className="mt-3 space-y-2 max-h-[36rem] overflow-y-auto pr-1">
          {visibleTutorSessions.length === 0 ? (
            <div className="rounded border border-coden-border/50 bg-coden-inner px-3 py-2 text-xs text-coden-muted">
              No saved chats yet.
            </div>
          ) : (
            visibleTutorSessions.map((session) => (
              <div
                key={session.id}
                className={`rounded border p-2 ${
                  session.id === activeSavedSessionId
                    ? 'border-coden-accent/60 bg-coden-accent/10'
                    : 'border-coden-border/60 bg-coden-inner'
                }`}
              >
                <button
                  type="button"
                  onClick={() => restoreTutorSession(session.id)}
                  className="w-full text-left"
                >
                  <div className="text-xs text-coden-text font-semibold truncate">
                    {sessionLabel(session)}
                  </div>
                  <div className="text-[10px] text-coden-muted mt-1">
                    {formatSessionDate(session.updatedAt)}
                  </div>
                  <div className="text-[10px] text-coden-muted mt-1">
                    {session.messages.length} messages
                  </div>
                </button>
                <button
                  type="button"
                  onClick={() => deleteTutorSession(session.id)}
                  disabled={isLoading}
                  className="mt-2 px-2 py-1 text-[10px] rounded border border-rose-500/30 text-rose-200 hover:bg-rose-500/10 disabled:opacity-50"
                >
                  Delete
                </button>
              </div>
            ))
          )}
        </div>
      </aside>

      <section className="border border-coden-border bg-coden-surface rounded-lg min-h-[28rem] flex flex-col overflow-hidden">
        <header className="flex flex-col gap-3 border-b border-coden-border p-4 sm:flex-row sm:items-center sm:justify-between">
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <span className="h-7 min-w-7 rounded border border-coden-accent/50 bg-coden-accent/10 text-coden-accent font-mono text-xs font-bold flex items-center justify-center">
                AI
              </span>
              <div className="text-sm font-semibold text-coden-text truncate">{detail.name}</div>
            </div>
            <div className="mt-1 text-[11px] text-coden-muted">
              {codeLanguage} | required {detail.required_complexity}
              {result ? ` | ${result.selected_case_ids.length || 1} case${(result.selected_case_ids.length || 1) === 1 ? '' : 's'}` : ''}
            </div>
          </div>
          <div className="flex flex-wrap gap-2">
            <button
              type="button"
              onClick={() => void sendQuestion('Can you help me understand the task and the key idea before I code?')}
              disabled={isLoading}
              className="px-3 py-1.5 text-xs rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50"
            >
              Task
            </button>
            <button
              type="button"
              onClick={() => void sendQuestion('Can you explain the optimal approach at a high level without giving me the full code?')}
              disabled={isLoading}
              className="px-3 py-1.5 text-xs rounded border border-coden-border text-coden-text hover:bg-coden-border disabled:opacity-50"
            >
              Optimal Idea
            </button>
            <button
              type="button"
              onClick={analyzeLatestRun}
              disabled={!result || isLoading || !hasCurrentSource}
              className="px-3 py-1.5 text-xs rounded bg-coden-accent text-coden-accentContrast hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Analyze Run
            </button>
          </div>
        </header>

        <div className="flex-1 min-h-0 overflow-y-auto p-4 space-y-3">
          {!hasMessages && aiStatus !== 'loading' ? (
            <div className="flex justify-start">
              <div className="max-w-[92%] rounded-lg bg-coden-inner border border-coden-border/60 px-3 py-2 text-xs text-coden-text">
                What would you like to figure out first?
              </div>
            </div>
          ) : (
            aiMessages.map((message, index) => (
              <TutorBubble
                key={`${message.role}-${index}-${message.content.slice(0, 24)}`}
                message={message}
              />
            ))
          )}
          {isLoading && (
            <div className="flex justify-start">
              <div className="rounded-lg border border-coden-accent/20 bg-coden-inner px-3 py-2 text-xs text-coden-accent flex items-center gap-2">
                <span className="w-3 h-3 rounded-full border-2 border-coden-accent border-t-transparent animate-spin"></span>
                Thinking...
              </div>
            </div>
          )}
          {aiStatus === 'error' && aiError && (
            <div className="text-xs text-rose-200 bg-rose-950/20 border border-rose-900/30 rounded-lg p-3 whitespace-pre-wrap">
              {aiError}
            </div>
          )}
        </div>

        <form
          className="border-t border-coden-border p-4 flex flex-col gap-2"
          onSubmit={(event) => {
            event.preventDefault();
            submitDraft();
          }}
        >
          <textarea
            value={draft}
            onChange={(event) => setDraft(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                submitDraft();
              }
            }}
            disabled={isLoading}
            rows={3}
            placeholder="Ask about the task, your code, the latest run, or the optimal idea..."
            className="w-full resize-none rounded border border-coden-border bg-coden-inner px-3 py-2 text-xs text-coden-text placeholder:text-coden-muted focus:outline-none focus:ring-1 focus:ring-coden-accent disabled:opacity-60"
          />
          <div className="flex justify-end">
            <button
              type="submit"
              disabled={isLoading || !draft.trim()}
              className="px-4 py-1.5 text-xs rounded bg-coden-accent text-coden-accentContrast font-semibold hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Send
            </button>
          </div>
        </form>
      </section>
    </div>
  );
}


function TutorBubble({ message }: { message: TutorChatMessage }) {
  const isUser = message.role === 'user';
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={
          isUser
            ? 'max-w-[85%] rounded-lg bg-coden-accent/25 border border-coden-accent/30 px-3 py-2 text-xs text-coden-text whitespace-pre-wrap'
            : 'max-w-[92%] rounded-lg bg-coden-inner border border-coden-border/60 px-3 py-2'
        }
      >
        {isUser ? message.content : <TutorMarkdown content={message.content} />}
      </div>
    </div>
  );
}


function TutorMarkdown({ content }: { content: string }) {
  return (
    <article className="prose prose-invert prose-xs max-w-none
                        prose-headings:text-coden-text prose-headings:font-bold prose-headings:my-2
                        prose-p:text-coden-text prose-p:leading-relaxed prose-p:my-1.5
                        prose-strong:text-coden-accent
                        prose-code:text-coden-accent prose-code:before:content-none prose-code:after:content-none
                        prose-ul:list-disc prose-ul:pl-4 prose-ul:my-2
                        prose-ol:list-decimal prose-ol:pl-4 prose-ol:my-2
                        prose-li:my-0.5">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeRaw, rehypeKatex]}
        components={{
          pre: ({ children, ...props }) => (
            <pre
              {...props}
              className="bg-coden-bg border border-coden-border rounded p-3 text-xs overflow-x-auto my-3 font-mono"
            >
              {children}
            </pre>
          ),
          code: ({ className, children, ...props }) => {
            const isBlock = String(children).includes('\n');
            if (isBlock) {
              return <code {...props} className={className}>{children}</code>;
            }
            return (
              <code
                {...props}
                className="bg-coden-bg border border-coden-border rounded px-1 py-0.5 text-coden-accent text-xs font-mono"
              >
                {children}
              </code>
            );
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </article>
  );
}
