import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { JSDOM } from 'jsdom';


const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const corpusRoot = path.resolve(scriptDir, '../../dsa/leetcode');
const dom = new JSDOM('<!doctype html><html><body></body></html>', {
  pretendToBeVisual: true,
});

for (const name of [
  'window',
  'document',
  'navigator',
  'Node',
  'Element',
  'HTMLElement',
  'SVGElement',
  'DOMParser',
  'DocumentFragment',
  'HTMLTemplateElement',
  'NodeFilter',
]) {
  Object.defineProperty(globalThis, name, {
    configurable: true,
    value: dom.window[name],
  });
}

const { default: mermaid } = await import('mermaid');
mermaid.initialize({
  startOnLoad: false,
  securityLevel: 'strict',
  suppressErrorRendering: true,
});
import { stat } from 'node:fs/promises';

const args = process.argv.slice(2);
let markdownFiles = [];
if (args.length > 0) {
  for (const arg of args) {
    const resolved = path.isAbsolute(arg) ? arg : path.resolve(process.cwd(), arg);
    try {
      const s = await stat(resolved);
      if (s.isDirectory()) {
        markdownFiles.push(...await findMarkdownFiles(resolved));
      } else if (s.isFile() && resolved.endsWith('.md')) {
        markdownFiles.push(resolved);
      }
    } catch {
      const fallback = path.resolve(corpusRoot, arg);
      try {
        const s2 = await stat(fallback);
        if (s2.isDirectory()) {
          markdownFiles.push(...await findMarkdownFiles(fallback));
        } else if (s2.isFile() && fallback.endsWith('.md')) {
          markdownFiles.push(fallback);
        }
      } catch {
        console.error(
          `No Markdown file or directory found for '${arg}'.\n` +
          `Tried '${resolved}' and '${fallback}'.\n` +
          `Paths are resolved against the corpus root (${corpusRoot}), so pass a ` +
          `package name such as '0001_two-sum' or an absolute path.`,
        );
        process.exit(1);
      }
    }
  }
} else {
  markdownFiles = await findMarkdownFiles(corpusRoot);
}
let diagramCount = 0;
const failures = [];
for (const markdownPath of markdownFiles) {
  const markdown = await readFile(markdownPath, 'utf8');
  const diagrams = extractMermaidDiagrams(markdown);
  for (const [index, source] of diagrams.entries()) {
    const location = `${path.relative(corpusRoot, markdownPath)}#diagram-${index + 1}`;
    if (!/^\s*accTitle\s*:/m.test(source)) {
      failures.push(`${location}: missing accTitle`);
      continue;
    }
    if (!/^\s*accDescr(?:\s*:|\s*\{)/m.test(source)) {
      failures.push(`${location}: missing accDescr`);
      continue;
    }
    try {
      await mermaid.parse(source);
    } catch (error) {
      failures.push(`${location}: ${error instanceof Error ? error.message : String(error)}`);
      continue;
    }
    diagramCount += 1;
  }
}

// Report every invalid diagram rather than only the first one: a corpus-wide
// gate is far more useful as a complete work list than as a fail-fast probe.
if (failures.length > 0) {
  console.error(`Invalid Mermaid diagrams: ${failures.length}`);
  for (const failure of failures) console.error(`  ${failure}`);
}

if (diagramCount === 0 && failures.length === 0) {
  console.log(`No fenced Mermaid diagrams found across ${markdownFiles.length} Markdown files.`);
} else {
  console.log(`Validated ${diagramCount} accessible Mermaid diagrams across ${markdownFiles.length} Markdown files.`);
}

if (failures.length > 0) {
  process.exit(1);
}


async function findMarkdownFiles(root) {
  const result = [];
  const entries = await readdir(root, { withFileTypes: true });
  for (const entry of entries) {
    const entryPath = path.join(root, entry.name);
    if (entry.isDirectory()) {
      result.push(...await findMarkdownFiles(entryPath));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      result.push(entryPath);
    }
  }
  return result;
}


function extractMermaidDiagrams(markdown) {
  return [...markdown.matchAll(/```mermaid[\t ]*\r?\n([\s\S]*?)```/g)]
    .map((match) => match[1].trim())
    .filter(Boolean);
}
