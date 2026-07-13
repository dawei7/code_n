const INLINE_LIMIT = 120;

export function formatCaseValue(value: string): string {
  const trimmed = value.trim();
  if (!trimmed) return '';
  try {
    return formatFriendlyJson(JSON.parse(trimmed));
  } catch {
    return trimmed;
  }
}

function formatFriendlyJson(value: unknown, depth = 0): string {
  const inline = formatInlineJson(value);
  if (inline.length <= INLINE_LIMIT) {
    return inline;
  }

  if (Array.isArray(value)) {
    if (value.length === 0) return '[]';
    const indent = '  '.repeat(depth);
    const childIndent = '  '.repeat(depth + 1);
    const children = value.map((item) => {
      const formatted = formatFriendlyJson(item, depth + 1);
      return `${childIndent}${formatted.replace(/\n/g, `\n${childIndent}`)}`;
    });
    return `[\n${children.join(',\n')}\n${indent}]`;
  }

  if (isPlainObject(value)) {
    const entries = Object.entries(value);
    if (entries.length === 0) return '{}';
    const indent = '  '.repeat(depth);
    const childIndent = '  '.repeat(depth + 1);
    const children = entries.map(([key, child]) => {
      const formatted = formatFriendlyJson(child, depth + 1);
      return `${childIndent}${formatObjectKey(key)}: ${formatted.replace(/\n/g, `\n${childIndent}`)}`;
    });
    return `{\n${children.join(',\n')}\n${indent}}`;
  }

  return inline;
}

function formatInlineJson(value: unknown): string {
  if (Array.isArray(value)) {
    return `[${value.map((item) => formatInlineJson(item)).join(', ')}]`;
  }
  if (isPlainObject(value)) {
    const entries = Object.entries(value);
    return `{ ${entries.map(([key, child]) => `${formatObjectKey(key)}: ${formatInlineJson(child)}`).join(', ')} }`;
  }
  return JSON.stringify(value);
}

function isPlainObject(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function formatObjectKey(key: string): string {
  return /^[A-Za-z_$][\w$]*$/.test(key) ? key : JSON.stringify(key);
}
