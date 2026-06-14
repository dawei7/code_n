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
          'Inter',
          'system-ui',
          '-apple-system',
          'BlinkMacSystemFont',
          'Segoe UI',
          'Roboto',
          'sans-serif',
        ],
        mono: [
          'JetBrains Mono',
          'Menlo',
          'Monaco',
          'Cascadia Code',
          'Consolas',
          'monospace',
        ],
      },
      colors: {
        coden: {
          bg: '#020617',        // slate-950
          surface: '#0f172a',   // slate-900
          border: '#1e293b',    // slate-800
          muted: '#475569',     // slate-600
          text: '#e2e8f0',      // slate-200
          accent: '#34d399',    // emerald-400
          compare: '#fbbf24',   // amber-400
          swap: '#fb7185',      // rose-400
          read: '#60a5fa',      // blue-400
        },
      },
    },
  },
  plugins: [typography],
};

export default config;
