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

const markdownFiles = await findMarkdownFiles(corpusRoot);
let diagramCount = 0;
for (const markdownPath of markdownFiles) {
  const markdown = await readFile(markdownPath, 'utf8');
  const diagrams = extractMermaidDiagrams(markdown);
  for (const [index, source] of diagrams.entries()) {
    const location = `${path.relative(corpusRoot, markdownPath)}#diagram-${index + 1}`;
    if (!/^\s*accTitle\s*:/m.test(source)) {
      throw new Error(`${location}: missing accTitle`);
    }
    if (!/^\s*accDescr(?:\s*:|\s*\{)/m.test(source)) {
      throw new Error(`${location}: missing accDescr`);
    }
    try {
      await mermaid.parse(source);
    } catch (error) {
      throw new Error(`${location}: ${error instanceof Error ? error.message : String(error)}`);
    }
    diagramCount += 1;
  }
}

if (diagramCount === 0) {
  throw new Error('No fenced Mermaid diagrams were found in the LeetCode corpus.');
}
console.log(`Validated ${diagramCount} accessible Mermaid diagrams across ${markdownFiles.length} Markdown files.`);


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
