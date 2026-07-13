export type ThemeMode = 'light' | 'dark';

export interface RgbaColor {
  r: number;
  g: number;
  b: number;
  a: number;
}

export const DEFAULT_ACCENT_COLORS: Record<ThemeMode, string> = {
  light: '#0284c7',
  dark: '#03dac6',
};

export const ACCENT_PRESETS = [
  '#03dac6', '#06b6d4', '#0284c7', '#2563eb', '#7c3aed', '#c026d3',
  '#e11d48', '#ea580c', '#d97706', '#65a30d', '#16a34a', '#0f766e',
];

const clampByte = (value: number) => Math.max(0, Math.min(255, Math.round(value)));
const clampAlpha = (value: number) => Math.max(0, Math.min(1, value));

export function parseCssColor(value: string): RgbaColor | null {
  const input = value.trim();
  const hex = input.match(/^#([0-9a-f]{3,8})$/i);
  if (hex && [3, 4, 6, 8].includes(hex[1].length)) {
    const expanded = hex[1].length <= 4
      ? hex[1].split('').map((part) => part + part).join('')
      : hex[1];
    return {
      r: Number.parseInt(expanded.slice(0, 2), 16),
      g: Number.parseInt(expanded.slice(2, 4), 16),
      b: Number.parseInt(expanded.slice(4, 6), 16),
      a: expanded.length === 8 ? Number.parseInt(expanded.slice(6, 8), 16) / 255 : 1,
    };
  }

  const rgba = input.match(/^rgba?\(\s*([+-]?(?:\d+\.?\d*|\.\d+))\s*,\s*([+-]?(?:\d+\.?\d*|\.\d+))\s*,\s*([+-]?(?:\d+\.?\d*|\.\d+))(?:\s*,\s*([+-]?(?:\d+\.?\d*|\.\d+)))?\s*\)$/i);
  if (!rgba) return null;
  const channels = rgba.slice(1, 4).map(Number);
  const alpha = rgba[4] === undefined ? 1 : Number(rgba[4]);
  if (channels.some((channel) => !Number.isFinite(channel) || channel < 0 || channel > 255)) return null;
  if (!Number.isFinite(alpha) || alpha < 0 || alpha > 1) return null;
  return { r: clampByte(channels[0]), g: clampByte(channels[1]), b: clampByte(channels[2]), a: clampAlpha(alpha) };
}

export function colorToHex(color: RgbaColor): string {
  return `#${[color.r, color.g, color.b].map((channel) => clampByte(channel).toString(16).padStart(2, '0')).join('')}`;
}

export function formatCssColor(color: RgbaColor): string {
  if (color.a >= 0.999) return colorToHex(color);
  return `rgba(${clampByte(color.r)}, ${clampByte(color.g)}, ${clampByte(color.b)}, ${Number(clampAlpha(color.a).toFixed(3))})`;
}

export function normalizeAccentColors(value?: Partial<Record<ThemeMode, string>> | null): Record<ThemeMode, string> {
  return {
    light: formatCssColor(parseCssColor(value?.light || '') ?? parseCssColor(DEFAULT_ACCENT_COLORS.light)!),
    dark: formatCssColor(parseCssColor(value?.dark || '') ?? parseCssColor(DEFAULT_ACCENT_COLORS.dark)!),
  };
}

function composite(foreground: RgbaColor, background: RgbaColor): RgbaColor {
  const alpha = foreground.a + background.a * (1 - foreground.a);
  if (alpha <= 0) return { r: 0, g: 0, b: 0, a: 0 };
  return {
    r: (foreground.r * foreground.a + background.r * background.a * (1 - foreground.a)) / alpha,
    g: (foreground.g * foreground.a + background.g * background.a * (1 - foreground.a)) / alpha,
    b: (foreground.b * foreground.a + background.b * background.a * (1 - foreground.a)) / alpha,
    a: alpha,
  };
}

function luminance(color: RgbaColor): number {
  const linear = [color.r, color.g, color.b].map((channel) => {
    const normalized = channel / 255;
    return normalized <= 0.04045 ? normalized / 12.92 : ((normalized + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2];
}

function ratio(first: RgbaColor, second: RgbaColor): number {
  const high = Math.max(luminance(first), luminance(second));
  const low = Math.min(luminance(first), luminance(second));
  return (high + 0.05) / (low + 0.05);
}

export function themeBackground(theme: ThemeMode): RgbaColor {
  return parseCssColor(theme === 'dark' ? '#121212' : '#f8f9fa')!;
}

export function accentContrastRatio(value: string, theme: ThemeMode): number {
  const background = themeBackground(theme);
  const accent = composite(parseCssColor(value) ?? parseCssColor(DEFAULT_ACCENT_COLORS[theme])!, background);
  return ratio(accent, background);
}

export function bestAccentTextColor(value: string, theme: ThemeMode): '#000000' | '#ffffff' {
  const accent = composite(parseCssColor(value) ?? parseCssColor(DEFAULT_ACCENT_COLORS[theme])!, themeBackground(theme));
  const black = parseCssColor('#000000')!;
  const white = parseCssColor('#ffffff')!;
  return ratio(black, accent) >= ratio(white, accent) ? '#000000' : '#ffffff';
}

