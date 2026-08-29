import fs from 'node:fs';
import path from 'node:path';
import katex from '../web/node_modules/katex/dist/katex.mjs';

const LEETCODE_ROOT = path.resolve('dsa/leetcode');

function checkContent(content, filename) {
  const issues = [];
  const lines = content.split('\n');

  let inCodeBlock = false;
  let inDisplayMath = false;
  let displayMathBuffer = [];
  let displayMathStart = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineNum = i + 1;

    if (line.trim().startsWith('```')) {
      inCodeBlock = !inCodeBlock;
      continue;
    }
    if (inCodeBlock) continue;

    if (line.trim().startsWith('|') && line.includes('$$')) {
      issues.push({ line: lineNum, type: 'display_math_in_table', detail: line });
    }

    const trimmed = line.trim();
    if (trimmed.startsWith('$$') && trimmed.endsWith('$$') && trimmed.length >= 4 && trimmed !== '$$') {
      const expr = trimmed.slice(2, -2).trim();
      try {
        katex.renderToString(expr, { displayMode: true, throwOnError: true, strict: 'warn' });
      } catch (err) {
        issues.push({ line: lineNum, type: 'katex_error', math: expr, detail: err.message });
      }
    } else if (trimmed === '$$') {
      if (!inDisplayMath) {
        inDisplayMath = true;
        displayMathStart = lineNum;
        displayMathBuffer = [];
      } else {
        inDisplayMath = false;
        const expr = displayMathBuffer.join('\n').trim();
        try {
          katex.renderToString(expr, { displayMode: true, throwOnError: true, strict: 'warn' });
        } catch (err) {
          issues.push({ line: displayMathStart, type: 'katex_error', math: expr, detail: err.message });
        }
        displayMathBuffer = [];
      }
    } else if (inDisplayMath) {
      displayMathBuffer.push(line);
    }
  }

  if (inDisplayMath) {
    issues.push({ line: displayMathStart, type: 'unclosed_display_math', detail: `Unclosed $$ at line ${displayMathStart}` });
  }

  let cleanText = content;
  cleanText = cleanText.replace(/```[\s\S]*?```/g, '');
  cleanText = cleanText.replace(/`[^`\n]+?`/g, '');
  cleanText = cleanText.replace(/\$\$[\s\S]*?\$\$/g, '');

  const unescapedDollars = (cleanText.match(/(?<!\\)\$/g) || []).length;
  if (unescapedDollars % 2 !== 0) {
    issues.push({ line: 0, type: 'unclosed_inline_math', detail: `Odd dollar count (${unescapedDollars})` });
  }

  const inlineRegex = /(?<!\\)\$([^\$\n]+?)(?<!\\)\$/g;
  let match;
  while ((match = inlineRegex.exec(cleanText)) !== null) {
    const expr = match[1].trim();
    if (!expr) continue;
    try {
      katex.renderToString(expr, { displayMode: false, throwOnError: true, strict: 'warn' });
    } catch (err) {
      issues.push({ line: 0, type: 'katex_error', math: expr, detail: err.message });
    }
  }

  return issues;
}

async function main() {
  const dirs = fs.readdirSync(LEETCODE_ROOT, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name)
    .sort();

  console.log(`Auditing all reference/ and approach.md files across ${dirs.length} packages...`);

  let totalFiles = 0;
  let errorCount = 0;

  for (const dir of dirs) {
    const pkgDir = path.join(LEETCODE_ROOT, dir);
    const filesToCheck = [
      path.join(pkgDir, 'approach.md'),
      path.join(pkgDir, 'reference', 'description.md'),
      path.join(pkgDir, 'reference', 'contract.md'),
      path.join(pkgDir, 'reference', 'examples.md'),
      path.join(pkgDir, 'reference', 'constraints.md'),
    ];

    for (const f of filesToCheck) {
      if (!fs.existsSync(f)) continue;
      totalFiles++;
      const content = fs.readFileSync(f, 'utf-8');
      const issues = checkContent(content, f);
      if (issues.length > 0) {
        errorCount++;
        console.log(`[${dir}/${path.relative(pkgDir, f)}] (${issues.length} issues):`);
        for (const iss of issues) {
          console.log(`  - ${iss.type}: ${iss.detail || iss.math}`);
        }
      }
    }
  }

  console.log(`\nComplete: Audited ${totalFiles} markdown files across reference and approaches. Found ${errorCount} files with issues.`);
}

main().catch(console.error);
