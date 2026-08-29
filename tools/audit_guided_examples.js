import fs from 'node:fs';
import path from 'node:path';
import katex from '../web/node_modules/katex/dist/katex.mjs';

const LEETCODE_ROOT = path.resolve('dsa/leetcode');

export function checkGuidedExample(content) {
  const issues = [];
  const lines = content.split('\n');

  // 1. Check for multiline/unclosed $$ blocks
  let inDisplayMath = false;
  let displayMathBuffer = [];
  let displayMathStart = 0;
  let inCodeBlock = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineNum = i + 1;

    if (line.trim().startsWith('```')) {
      inCodeBlock = !inCodeBlock;
      continue;
    }
    if (inCodeBlock) continue;

    // Check if line contains unescaped $$ inside a table row
    if (line.trim().startsWith('|') && line.includes('$$')) {
      issues.push({
        line: lineNum,
        type: 'display_math_in_table',
        detail: `Found '$$' inside table row: ${line.slice(0, 80)}`,
      });
    }

    // Process display math delimiter $$
    const trimmed = line.trim();
    if (trimmed.startsWith('$$') && trimmed.endsWith('$$') && trimmed.length >= 4 && trimmed !== '$$') {
      // Single line display math
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
    issues.push({
      line: displayMathStart,
      type: 'unclosed_display_math',
      detail: `Unclosed '$$' starting at line ${displayMathStart}`,
    });
  }

  // 2. Remove code blocks and full $$ ... $$ blocks to audit inline math $...$
  let cleanText = content;
  // Strip code blocks
  cleanText = cleanText.replace(/```[\s\S]*?```/g, '');
  cleanText = cleanText.replace(/`[^`\n]+?`/g, '');
  // Strip display math blocks
  cleanText = cleanText.replace(/\$\$[\s\S]*?\$\$/g, '');

  // 3. Count unescaped dollar signs
  const unescapedDollars = (cleanText.match(/(?<!\\)\$/g) || []).length;
  if (unescapedDollars % 2 !== 0) {
    issues.push({
      line: 0,
      type: 'unclosed_inline_math',
      detail: `Odd number of unescaped '$' signs (${unescapedDollars})`,
    });
  }

  // 4. Extract inline math $...$
  const inlineRegex = /(?<!\\)\$([^\$\n]+?)(?<!\\)\$/g;
  let match;
  while ((match = inlineRegex.exec(cleanText)) !== null) {
    const expr = match[1].trim();
    if (!expr) continue;
    try {
      katex.renderToString(expr, { displayMode: false, throwOnError: true, strict: 'warn' });
    } catch (err) {
      issues.push({
        line: 0,
        type: 'katex_error',
        math: expr,
        detail: err.message,
      });
    }
  }

  // 5. Check for corrupted bullet duplication: "- **- **" or "**text:** - **text:**"
  const corruptedBulletRegex = /-\s*\*\*\s*-\s*\*\*/;
  for (let i = 0; i < lines.length; i++) {
    if (corruptedBulletRegex.test(lines[i])) {
      issues.push({
        line: i + 1,
        type: 'corrupted_bullet',
        detail: lines[i].slice(0, 80),
      });
    }
  }

  return issues;
}

async function main() {
  const dirs = fs.readdirSync(LEETCODE_ROOT, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name)
    .sort();

  console.log(`Auditing ${dirs.length} packages for guided_example.md errors...`);

  let totalFiles = 0;
  let errorFiles = [];

  for (const dir of dirs) {
    const filePath = path.join(LEETCODE_ROOT, dir, 'guided_example.md');
    if (!fs.existsSync(filePath)) continue;

    totalFiles++;
    const content = fs.readFileSync(filePath, 'utf-8');
    const issues = checkGuidedExample(content);

    if (issues.length > 0) {
      errorFiles.push({ dir, issues });
    }
  }

  console.log(`\nAudit complete: Checked ${totalFiles} files. Found ${errorFiles.length} files with issues.\n`);

  for (const item of errorFiles) {
    console.log(`[${item.dir}] (${item.issues.length} issues):`);
    for (const issue of item.issues) {
      console.log(`  - Line ${issue.line} [${issue.type}]: ${issue.detail || issue.math}`);
    }
  }

  fs.writeFileSync('guided_example_errors.json', JSON.stringify(errorFiles, null, 2), 'utf-8');
  console.log(`Wrote full issue list to guided_example_errors.json`);
}

if (process.argv[1].endsWith('audit_guided_examples.js')) {
  main().catch(console.error);
}
