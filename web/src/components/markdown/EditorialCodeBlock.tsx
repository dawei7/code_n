import { Editor } from '@monaco-editor/react';
import { useState } from 'react';


type EditorialCodeBlockProps = {
  challengeId: string;
  language: string;
  source: string;
  theme: 'light' | 'dark';
};

type EditorLanguage = {
  extension: string;
  label: string;
  monaco: string;
};

const EDITOR_LANGUAGES: Record<string, EditorLanguage> = {
  bash: { label: 'Bash', monaco: 'shell', extension: 'sh' },
  c: { label: 'C', monaco: 'c', extension: 'c' },
  'c#': { label: 'C#', monaco: 'csharp', extension: 'cs' },
  cpp: { label: 'C++', monaco: 'cpp', extension: 'cpp' },
  'c++': { label: 'C++', monaco: 'cpp', extension: 'cpp' },
  csharp: { label: 'C#', monaco: 'csharp', extension: 'cs' },
  cs: { label: 'C#', monaco: 'csharp', extension: 'cs' },
  css: { label: 'CSS', monaco: 'css', extension: 'css' },
  go: { label: 'Go', monaco: 'go', extension: 'go' },
  golang: { label: 'Go', monaco: 'go', extension: 'go' },
  html: { label: 'HTML', monaco: 'html', extension: 'html' },
  java: { label: 'Java', monaco: 'java', extension: 'java' },
  javascript: { label: 'JavaScript', monaco: 'javascript', extension: 'js' },
  js: { label: 'JavaScript', monaco: 'javascript', extension: 'js' },
  kotlin: { label: 'Kotlin', monaco: 'kotlin', extension: 'kt' },
  mysql: { label: 'SQL', monaco: 'sql', extension: 'sql' },
  php: { label: 'PHP', monaco: 'php', extension: 'php' },
  py: { label: 'Python', monaco: 'python', extension: 'py' },
  python: { label: 'Python', monaco: 'python', extension: 'py' },
  python3: { label: 'Python', monaco: 'python', extension: 'py' },
  r: { label: 'R', monaco: 'r', extension: 'r' },
  ruby: { label: 'Ruby', monaco: 'ruby', extension: 'rb' },
  rust: { label: 'Rust', monaco: 'rust', extension: 'rs' },
  scala: { label: 'Scala', monaco: 'scala', extension: 'scala' },
  shell: { label: 'Bash', monaco: 'shell', extension: 'sh' },
  sh: { label: 'Bash', monaco: 'shell', extension: 'sh' },
  sql: { label: 'SQL', monaco: 'sql', extension: 'sql' },
  swift: { label: 'Swift', monaco: 'swift', extension: 'swift' },
  ts: { label: 'TypeScript', monaco: 'typescript', extension: 'ts' },
  typescript: { label: 'TypeScript', monaco: 'typescript', extension: 'ts' },
};

const PLAIN_TEXT_LANGUAGES = new Set([
  '',
  'code',
  'input',
  'output',
  'plain',
  'plaintext',
  'text',
]);


export function EditorialCodeBlock({
  challengeId,
  language,
  source,
  theme,
}: EditorialCodeBlockProps) {
  const [copyStatus, setCopyStatus] = useState<'idle' | 'copied' | 'failed'>('idle');
  const languageMeta = editorialLanguage(language);
  const lineCount = source.split(/\r?\n/).length;
  const editorHeight = Math.min(640, Math.max(180, lineCount * 19 + 44));
  const sourceId = stableSourceId(`${languageMeta.monaco}\0${source}`);

  const copyCode = async () => {
    try {
      await copyCompleteCode(source);
      setCopyStatus('copied');
    } catch {
      setCopyStatus('failed');
    }
  };

  return (
    <section
      aria-label={`Read-only ${languageMeta.label} code`}
      className="not-prose my-5 overflow-hidden rounded border border-coden-border bg-coden-bg"
    >
      <div className="flex min-h-10 flex-wrap items-center justify-between gap-2 border-b border-coden-border bg-coden-bg/80 px-3 py-1.5">
        <div className="flex items-center gap-2 text-xs">
          <span className="font-semibold text-coden-text">{languageMeta.label}</span>
          <span className="text-coden-muted">Read only</span>
        </div>
        <button
          type="button"
          onClick={() => void copyCode()}
          className="inline-flex h-8 items-center gap-1.5 rounded border border-coden-border bg-coden-bg px-3 text-xs font-semibold text-coden-text transition-colors hover:border-coden-accent hover:text-coden-accent focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-coden-accent"
          aria-label={`Copy the complete ${languageMeta.label} code`}
          title="Copy the complete code"
        >
          <CopyIcon />
          {copyStatus === 'copied' ? 'Copied' : copyStatus === 'failed' ? 'Copy failed' : 'Copy code'}
        </button>
      </div>
      <div style={{ height: editorHeight }}>
        <Editor
          path={`editorial://${encodeURIComponent(challengeId)}/${sourceId}.${languageMeta.extension}`}
          height="100%"
          language={languageMeta.monaco}
          theme={theme === 'dark' ? 'vs-dark' : 'light'}
          value={source}
          options={{
            readOnly: true,
            domReadOnly: true,
            contextmenu: false,
            minimap: { enabled: false },
            folding: true,
            glyphMargin: false,
            lineDecorationsWidth: 4,
            lineNumbersMinChars: 3,
            fontSize: 13,
            fontFamily: "'Cascadia Code', 'Cascadia Mono', Consolas, 'SFMono-Regular', monospace",
            renderLineHighlight: 'none',
            scrollBeyondLastLine: false,
            overviewRulerLanes: 0,
            hideCursorInOverviewRuler: true,
            wordWrap: 'off',
            automaticLayout: true,
            padding: { top: 14, bottom: 14 },
            ariaLabel: `Read-only ${languageMeta.label} editorial code`,
          }}
          loading={
            <div className="flex h-full items-center justify-center text-xs text-coden-muted">
              Loading code editor...
            </div>
          }
        />
      </div>
    </section>
  );
}


function editorialLanguage(language: string): EditorLanguage {
  const normalized = language.trim().toLowerCase();
  if (PLAIN_TEXT_LANGUAGES.has(normalized)) {
    return { label: 'Plain text', monaco: 'plaintext', extension: 'txt' };
  }
  return EDITOR_LANGUAGES[normalized]
    ?? { label: normalized.toUpperCase(), monaco: 'plaintext', extension: 'txt' };
}


function stableSourceId(source: string): string {
  let hash = 2166136261;
  for (let index = 0; index < source.length; index += 1) {
    hash ^= source.charCodeAt(index);
    hash = Math.imul(hash, 16777619);
  }
  return (hash >>> 0).toString(36);
}


async function copyCompleteCode(source: string): Promise<void> {
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(source);
      return;
    }
  } catch {
    // Electron or browser clipboard permission can be unavailable. The
    // selection-based fallback keeps copying available in that environment.
  }

  const textarea = document.createElement('textarea');
  textarea.value = source;
  textarea.setAttribute('readonly', '');
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  const copied = document.execCommand('copy');
  textarea.remove();
  if (!copied) throw new Error('Clipboard copy failed');
}


function CopyIcon() {
  return (
    <svg
      aria-hidden="true"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      className="h-3.5 w-3.5"
    >
      <rect width="14" height="14" x="8" y="8" rx="2" />
      <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" />
    </svg>
  );
}
