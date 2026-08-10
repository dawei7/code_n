import type { ComponentPropsWithoutRef } from 'react';


type EditorialFrameProps = ComponentPropsWithoutRef<'iframe'> & {
  leetcodeUrl: string;
};


export function EditorialFrame({
  leetcodeUrl,
  src,
  title,
  ...props
}: EditorialFrameProps) {
  const source = typeof src === 'string' ? src : '';

  if (isRestrictedVimeoEmbed(source)) {
    const officialEditorialUrl = leetcodeEditorialUrl(leetcodeUrl);
    return (
      <aside className="not-prose my-5 flex min-h-48 flex-col items-center justify-center rounded-lg border border-coden-border bg-coden-bg px-6 py-8 text-center text-coden-text">
        <span
          aria-hidden="true"
          className="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-full border border-coden-border bg-coden-surface text-coden-accent"
        >
          <svg
            viewBox="0 0 24 24"
            className="h-6 w-6"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <rect x="3" y="5" width="18" height="14" rx="2" />
            <path d="m10 9 5 3-5 3z" />
          </svg>
        </span>
        <strong className="text-base text-coden-text">Video available on LeetCode</strong>
        <p className="mb-0 mt-2 max-w-xl text-sm leading-6 text-coden-muted">
          The publisher restricts this video to the LeetCode website, so it cannot play inside the desktop app.
        </p>
        {officialEditorialUrl && (
          <a
            href={officialEditorialUrl}
            target="_blank"
            rel="noreferrer"
            className="mt-5 inline-flex items-center rounded border border-coden-accent px-4 py-2 text-sm font-semibold text-coden-accent no-underline transition-colors hover:bg-coden-accent hover:text-coden-bg"
          >
            Watch video on LeetCode
            <span aria-hidden="true" className="ml-1.5">↗</span>
          </a>
        )}
      </aside>
    );
  }

  return (
    <div className="not-prose my-5 aspect-video w-full max-w-4xl overflow-hidden rounded-lg border border-coden-border bg-black">
      <iframe
        {...props}
        src={source}
        title={title || 'Editorial video'}
        className="h-full w-full border-0"
        allowFullScreen
      />
    </div>
  );
}


export function isRestrictedVimeoEmbed(src: string): boolean {
  try {
    return new URL(src).hostname.toLowerCase() === 'player.vimeo.com';
  } catch {
    return false;
  }
}


export function leetcodeEditorialUrl(leetcodeUrl: string): string {
  try {
    const url = new URL(leetcodeUrl);
    if (!['http:', 'https:'].includes(url.protocol) || url.hostname !== 'leetcode.com') {
      return '';
    }
    url.pathname = `${url.pathname.replace(/\/+$/, '')}/editorial/`;
    url.search = '';
    url.hash = '';
    return url.toString();
  } catch {
    return '';
  }
}
