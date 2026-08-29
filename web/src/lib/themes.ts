export type ThemeId =
  | 'obsidian-emerald'
  | 'midnight-cyber'
  | 'tokyo-night'
  | 'cyber-princess'
  | 'sakura-blossom'
  | 'nordic-frost'
  | 'solarized-sand';

export interface AppTheme {
  id: ThemeId;
  name: string;
  subtitle: string;
  mode: 'dark' | 'light';
  colors: {
    bg: string;
    surface: string;
    surfaceElevated: string;
    border: string;
    muted: string;
    text: string;
    accent: string;
    accentContrast: string;
    compare: string;
    swap: string;
    read: string;
    inner: string;
  };
  previewColors: string[];
}

export const APP_THEMES: AppTheme[] = [
  {
    id: 'obsidian-emerald',
    name: 'Obsidian Emerald',
    subtitle: 'Terminal Dark with Vivid Mint Accent',
    mode: 'dark',
    colors: {
      bg: '#0d1117',
      surface: '#161b22',
      surfaceElevated: '#21262d',
      border: '#30363d',
      muted: '#8b949e',
      text: '#f0f6fc',
      accent: '#10b981',
      accentContrast: '#000000',
      compare: '#f59e0b',
      swap: '#f43f5e',
      read: '#38bdf8',
      inner: '#090d12',
    },
    previewColors: ['#0d1117', '#161b22', '#10b981', '#f0f6fc'],
  },
  {
    id: 'midnight-cyber',
    name: 'Midnight Cyber',
    subtitle: 'Deep Indigo Canvas with Neon Cyan',
    mode: 'dark',
    colors: {
      bg: '#0b0f19',
      surface: '#111827',
      surfaceElevated: '#1f2937',
      border: '#374151',
      muted: '#9ca3af',
      text: '#f9fafb',
      accent: '#06b6d4',
      accentContrast: '#000000',
      compare: '#fbbf24',
      swap: '#ec4899',
      read: '#818cf8',
      inner: '#070a12',
    },
    previewColors: ['#0b0f19', '#111827', '#06b6d4', '#f9fafb'],
  },
  {
    id: 'tokyo-night',
    name: 'Tokyo Night',
    subtitle: 'Twilight Slate with Pastel Lavender',
    mode: 'dark',
    colors: {
      bg: '#1a1b26',
      surface: '#24283b',
      surfaceElevated: '#2f354f',
      border: '#414868',
      muted: '#7aa2f7',
      text: '#c0caf5',
      accent: '#bb9af7',
      accentContrast: '#1a1b26',
      compare: '#e0af68',
      swap: '#f7768e',
      read: '#7dcfff',
      inner: '#16161e',
    },
    previewColors: ['#1a1b26', '#24283b', '#bb9af7', '#c0caf5'],
  },
  {
    id: 'cyber-princess',
    name: 'Cyber Princess 🎀',
    subtitle: 'Deep Velvet Plum with Electric Fuchsia & Pink Glow',
    mode: 'dark',
    colors: {
      bg: '#150914',
      surface: '#241022',
      surfaceElevated: '#361933',
      border: '#52214e',
      muted: '#f472b6',
      text: '#fdf2f8',
      accent: '#ff2a8d',
      accentContrast: '#ffffff',
      compare: '#fbbf24',
      swap: '#fb7185',
      read: '#c084fc',
      inner: '#0d050c',
    },
    previewColors: ['#150914', '#241022', '#ff2a8d', '#fdf2f8'],
  },
  {
    id: 'sakura-blossom',
    name: 'Sakura Blossom 🌸',
    subtitle: 'Cotton Candy & Soft Rose with Bubblegum Pink',
    mode: 'light',
    colors: {
      bg: '#fff0f5',
      surface: '#ffffff',
      surfaceElevated: '#fce7f3',
      border: '#fbcfe8',
      muted: '#9d174d',
      text: '#500724',
      accent: '#ec4899',
      accentContrast: '#ffffff',
      compare: '#f59e0b',
      swap: '#e11d48',
      read: '#a855f7',
      inner: '#fdf2f8',
    },
    previewColors: ['#fff0f5', '#fce7f3', '#ec4899', '#500724'],
  },
  {
    id: 'nordic-frost',
    name: 'Nordic Frost',
    subtitle: 'Crisp Polar White with Glacial Blue',
    mode: 'light',
    colors: {
      bg: '#f4f6f9',
      surface: '#ffffff',
      surfaceElevated: '#e9ecef',
      border: '#d1d5db',
      muted: '#64748b',
      text: '#0f172a',
      accent: '#0284c7',
      accentContrast: '#ffffff',
      compare: '#d97706',
      swap: '#e11d48',
      read: '#2563eb',
      inner: '#e2e8f0',
    },
    previewColors: ['#f4f6f9', '#ffffff', '#0284c7', '#0f172a'],
  },
  {
    id: 'solarized-sand',
    name: 'Solarized Sand',
    subtitle: 'Warm Reading Parchment with Amber Ochre',
    mode: 'light',
    colors: {
      bg: '#fbf7ee',
      surface: '#f4efe6',
      surfaceElevated: '#e8e0d3',
      border: '#dcd3c4',
      muted: '#78716c',
      text: '#292524',
      accent: '#d97706',
      accentContrast: '#ffffff',
      compare: '#ca8a04',
      swap: '#dc2626',
      read: '#0284c7',
      inner: '#ede4d4',
    },
    previewColors: ['#fbf7ee', '#f4efe6', '#d97706', '#292524'],
  },
];

export function getTheme(id: string): AppTheme {
  return APP_THEMES.find((t) => t.id === id) ?? APP_THEMES[0];
}

export function applyThemeToDocument(theme: AppTheme): void {
  const root = document.documentElement;

  if (theme.mode === 'dark') {
    root.classList.add('dark');
  } else {
    root.classList.remove('dark');
  }

  root.style.setProperty('--coden-bg', theme.colors.bg);
  root.style.setProperty('--coden-surface', theme.colors.surface);
  root.style.setProperty('--coden-surface-elevated', theme.colors.surfaceElevated);
  root.style.setProperty('--coden-border', theme.colors.border);
  root.style.setProperty('--coden-muted', theme.colors.muted);
  root.style.setProperty('--coden-text', theme.colors.text);
  root.style.setProperty('--coden-accent', theme.colors.accent);
  root.style.setProperty('--coden-accent-contrast', theme.colors.accentContrast);
  root.style.setProperty('--coden-compare', theme.colors.compare);
  root.style.setProperty('--coden-swap', theme.colors.swap);
  root.style.setProperty('--coden-read', theme.colors.read);
  root.style.setProperty('--coden-inner', theme.colors.inner);
}
