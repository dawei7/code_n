// Validates that every math span in the documentation corpus parses with the
// same KaTeX build the app renders with.
//
// A Guided Example is only as good as its mathematics: an undefined control
// sequence such as `\leftouterjoin` or an unbalanced group renders as a red
// error box in the app, no matter how good the surrounding prose is. This gate
// renders every inline and display span and reports each file that fails.
//
// Usage:
//   node scripts/test-math-docs.mjs                     # guided examples
//   node scripts/test-math-docs.mjs 0001_two-sum ...    # selected packages
//   node scripts/test-math-docs.mjs --all-docs          # every Markdown file
//
// The default scope is the Guided Example corpus, because that is the surface
// this project authors. `--all-docs` widens it to every Markdown file in the
// corpus, which also covers the Reference documents; that wider scope currently
// reports a large pre-existing defect set in `reference/editorial.md` and the
// `reference/raw/` archives, which use `$` for currency and provider snippets
// rather than for mathematics. Those files are outside this gate's scope and
// need their own repair pass, so the default scope is the one that can stay
// green as an authoring gate.
//
// Targets are resolved against the working directory first and then against the
// corpus root, so a bare package name works.
import { readdir, readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import katex from 'katex';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const corpusRoot = path.resolve(scriptDir, '../../dsa/leetcode');
const GUIDE_FILENAME = 'guided_example.md';

// `\$` is an escaped literal dollar (money amounts such as `$\$5$`, which render
// as "$5"), so it must not be mistaken for a math delimiter.
const ESCAPED_DOLLAR = '\uE000';

const rawArgs = process.argv.slice(2);
const allDocs = rawArgs.includes('--all-docs');
const args = rawArgs.filter((arg) => !arg.startsWith('--'));
const findMarkdownFiles = (root) => collectMarkdownFiles(root, allDocs);

let markdownFiles = [];
if (args.length > 0) {
  for (const arg of args) {
    const resolved = path.isAbsolute(arg) ? arg : path.resolve(process.cwd(), arg);
    const found = await collectTargets(resolved);
    if (found !== null) {
      markdownFiles.push(...found);
      continue;
    }
    const fallback = path.resolve(corpusRoot, arg);
    const fallbackFound = await collectTargets(fallback);
    if (fallbackFound !== null) {
      markdownFiles.push(...fallbackFound);
      continue;
    }
    console.error(
      `No Markdown file or directory found for '${arg}'.\n` +
      `Tried '${resolved}' and '${fallback}'.\n` +
      `Paths are resolved against the corpus root (${corpusRoot}), so pass a ` +
      `package name such as '0001_two-sum' or an absolute path.`,
    );
    process.exit(1);
  }
} else {
  markdownFiles = await findMarkdownFiles(corpusRoot);
}

let spanCount = 0;
const failures = [];
for (const markdownPath of markdownFiles) {
  const markdown = await readFile(markdownPath, 'utf8');
  const spans = extractMathSpans(markdown);
  for (const [index, span] of spans.entries()) {
    spanCount += 1;
    try {
      katex.renderToString(span.tex, {
        displayMode: span.displayMode,
        throwOnError: true,
        strict: false,
      });
    } catch (error) {
      const message = error instanceof Error ? error.message.split('\n')[0] : String(error);
      failures.push(
        `${path.relative(corpusRoot, markdownPath)}#span-${index + 1}: ${message}\n` +
        `    ${span.tex.trim().replace(/\s+/g, ' ').slice(0, 160)}`,
      );
    }
  }
}

// Report every failing span rather than only the first: a corpus-wide gate is far
// more useful as a complete work list than as a fail-fast probe.
if (failures.length > 0) {
  console.error(`Math spans that fail to render: ${failures.length}`);
  for (const failure of failures) console.error(`  ${failure}`);
  process.exit(1);
}

if (spanCount === 0) {
  console.log(`No math spans found across ${markdownFiles.length} Markdown files.`);
} else {
  console.log(
    `Validated ${spanCount} math spans across ${markdownFiles.length} Markdown files.`,
  );
}

async function collectTargets(candidate) {
  try {
    const info = await stat(candidate);
    if (info.isDirectory()) return await collectMarkdownFiles(candidate, allDocs);
    if (info.isFile() && candidate.endsWith('.md')) {
      // An explicitly named file is always checked, even in the default scope.
      return [candidate];
    }
    return null;
  } catch {
    return null;
  }
}

async function collectMarkdownFiles(root, everyDocument) {
  const result = [];
  const entries = await readdir(root, { withFileTypes: true });
  for (const entry of entries) {
    const entryPath = path.join(root, entry.name);
    if (entry.isDirectory()) {
      result.push(...await collectMarkdownFiles(entryPath, everyDocument));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      if (everyDocument || entry.name === GUIDE_FILENAME) result.push(entryPath);
    }
  }
  return result;
}

/**
 * Blank out fenced blocks and inline code so their `$` never opens a span, then
 * collect display spans before inline spans so `$$...$$` is not read as two
 * empty inline spans.
 */
function extractMathSpans(markdown) {
  const masked = markdown
    .replace(/```[\s\S]*?```/g, (match) => match.replace(/[^\n]/g, ' '))
    .replace(/~~~[\s\S]*?~~~/g, (match) => match.replace(/[^\n]/g, ' '))
    .replace(/`[^`\n]*`/g, (match) => match.replace(/[^\n]/g, ' '))
    .replace(/\\\$/g, ESCAPED_DOLLAR);
  const restore = (tex) => tex.split(ESCAPED_DOLLAR).join('\\$');
  const spans = [];
  const display = /\$\$([\s\S]+?)\$\$/g;
  let match;
  while ((match = display.exec(masked)) !== null) {
    spans.push({ tex: restore(match[1]), displayMode: true });
  }
  const remainder = masked.replace(/\$\$[\s\S]+?\$\$/g, (block) => block.replace(/[^\n]/g, ' '));
  const inline = /\$([^$\n]+?)\$/g;
  while ((match = inline.exec(remainder)) !== null) {
    spans.push({ tex: restore(match[1]), displayMode: false });
  }
  return spans;
}