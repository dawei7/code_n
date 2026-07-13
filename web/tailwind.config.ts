import type { Config } from 'tailwindcss';
import typography from '@tailwindcss/typography';

// Dark-only theme. Slate for surfaces, emerald for "passed" / sorted,
// rose for errors / swapped, amber for compare highlights.
const config: Config = {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: [
          'Segoe UI',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          'sans-serif',
        ],
        mono: [
          'Cascadia Code',
          'Cascadia Mono',
          'Consolas',
          'SFMono-Regular',
          'Menlo',
          'Monaco',
          'monospace',
        ],
      },
      colors: {
        coden: {
          bg: 'var(--coden-bg)',
          surface: 'var(--coden-surface)',
          surfaceElevated: 'var(--coden-surface-elevated)',
          border: 'var(--coden-border)',
          muted: 'var(--coden-muted)',
          text: 'var(--coden-text)',
          accent: 'var(--coden-accent)',
          accentContrast: 'var(--coden-accent-contrast)',
          compare: 'var(--coden-compare)',
          swap: 'var(--coden-swap)',
          read: 'var(--coden-read)',
          inner: 'var(--coden-inner)',
        },
      },
    },
  },
  plugins: [typography],
};

export default config;
