import fs from 'fs';
import path from 'path';
import { PGlite } from '@electric-sql/pglite';

const repoRoot = process.cwd();
const leetcodeDir = path.join(repoRoot, 'dsa', 'leetcode');

const POSTGRES_PREAMBLE = `
CREATE OR REPLACE FUNCTION if(condition boolean, true_val anyelement, false_val anyelement)
RETURNS anyelement AS $$
BEGIN
  IF condition THEN RETURN true_val; ELSE RETURN false_val; END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ifnull(val anyelement, fallback anyelement)
RETURNS anyelement AS $$
  SELECT COALESCE(val, fallback);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION datediff(d1 timestamp, d2 timestamp)
RETURNS integer AS $$
  SELECT (d1::date - d2::date);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION datediff(d1 date, d2 date)
RETURNS integer AS $$
  SELECT (d1 - d2);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION year(d timestamp) RETURNS integer AS $$ SELECT EXTRACT(YEAR FROM d)::integer; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION year(d date) RETURNS integer AS $$ SELECT EXTRACT(YEAR FROM d)::integer; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION month(d timestamp) RETURNS integer AS $$ SELECT EXTRACT(MONTH FROM d)::integer; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION month(d date) RETURNS integer AS $$ SELECT EXTRACT(MONTH FROM d)::integer; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION day(d timestamp) RETURNS integer AS $$ SELECT EXTRACT(DAY FROM d)::integer; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION day(d date) RETURNS integer AS $$ SELECT EXTRACT(DAY FROM d)::integer; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION dayofmonth(d date) RETURNS integer AS $$ SELECT EXTRACT(DAY FROM d)::integer; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION dayofweek(d date) RETURNS integer AS $$ SELECT EXTRACT(DOW FROM d)::integer + 1; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION weekday(d date) RETURNS integer AS $$ SELECT (EXTRACT(DOW FROM d)::integer + 6) % 7; $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION round(val double precision, places integer) RETURNS numeric AS $$ SELECT ROUND(val::numeric, places); $$ LANGUAGE sql;
`;

async function createPGliteTable(db, name, rawRows) {
  let columns = [];
  let rows = [];

  if (rawRows && typeof rawRows === 'object' && !Array.isArray(rawRows)) {
    columns = (rawRows.columns || []).map(String);
    rows = rawRows.rows || [];
  } else if (Array.isArray(rawRows)) {
    if (rawRows.length > 0 && typeof rawRows[0] === 'object' && !Array.isArray(rawRows[0])) {
      columns = Object.keys(rawRows[0]);
      rows = rawRows.map(r => columns.map(c => r[c]));
    }
  }

  if (columns.length === 0) {
    columns = ['id'];
    rows = [];
  }

  const colDefs = columns.map((col, idx) => {
    let sampleVal = null;
    for (const r of rows) {
      if (r && r[idx] !== null && r[idx] !== undefined) {
        sampleVal = r[idx];
        break;
      }
    }
    let type = 'TEXT';
    const lowerCol = col.toLowerCase();
    if (typeof sampleVal === 'number' || lowerCol.endsWith('id') || lowerCol === 'id' || lowerCol.includes('salary') || lowerCol.includes('amount') || lowerCol.includes('count') || lowerCol.includes('score') || lowerCol.includes('price') || lowerCol.includes('num') || lowerCol.includes('val')) {
      type = (sampleVal !== null && !Number.isInteger(sampleVal)) ? 'DOUBLE PRECISION' : 'BIGINT';
    } else if (typeof sampleVal === 'boolean') {
      type = 'BOOLEAN';
    } else if (typeof sampleVal === 'string') {
      if (/^\d{4}-\d{2}-\d{2}$/.test(sampleVal)) type = 'DATE';
      else if (/^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}/.test(sampleVal)) type = 'TIMESTAMP';
    } else if (lowerCol.endsWith('date') || lowerCol.endsWith('time') || lowerCol.includes('day') || lowerCol.includes('month') || lowerCol.includes('year')) {
      type = 'DATE';
    }
    return `${col} ${type}`;
  });

  const createQuery = `CREATE TABLE ${name} (${colDefs.join(', ')});`;
  await db.query(createQuery);

  if (rows.length > 0) {
    for (const row of rows) {
      const placeholders = columns.map((_, i) => `$${i + 1}`).join(', ');
      const insertQuery = `INSERT INTO ${name} (${columns.join(', ')}) VALUES (${placeholders});`;
      const cleanParams = row.map((v, i) => {
        if (v === undefined || v === null) return null;
        const colDef = colDefs[i] || '';
        if (colDef.endsWith('BIGINT')) {
          const n = parseInt(v, 10);
          return isNaN(n) ? null : n;
        }
        if (colDef.endsWith('DOUBLE PRECISION')) {
          const n = parseFloat(v);
          return isNaN(n) ? null : n;
        }
        return v;
      });
      await db.query(insertQuery, cleanParams);
    }
  }
}

function splitSQLStatements(source) {
  const statements = [];
  let buffer = '';
  let inSingleQuote = false;
  let inDoubleQuote = false;
  let inLineComment = false;
  let inBlockComment = false;
  let inDollarQuote = false;
  let dollarTag = '';

  for (let i = 0; i < source.length; i++) {
    const char = source[i];
    const nextChar = source[i + 1] || '';

    if (inLineComment) {
      if (char === '\n' || char === '\r') inLineComment = false;
      continue;
    }
    if (inBlockComment) {
      if (char === '*' && nextChar === '/') {
        inBlockComment = false;
        i++;
      }
      continue;
    }

    if (!inSingleQuote && !inDoubleQuote && !inDollarQuote) {
      if (char === '-' && nextChar === '-') {
        inLineComment = true;
        i++;
        continue;
      }
      if (char === '#') {
        inLineComment = true;
        continue;
      }
      if (char === '/' && nextChar === '*') {
        inBlockComment = true;
        i++;
        continue;
      }
      if (char === '$') {
        const rest = source.slice(i);
        const match = rest.match(/^\$[a-zA-Z0-9_]*\$/);
        if (match) {
          inDollarQuote = true;
          dollarTag = match[0];
          buffer += dollarTag;
          i += dollarTag.length - 1;
          continue;
        }
      }
    } else if (inDollarQuote) {
      const rest = source.slice(i);
      if (rest.startsWith(dollarTag)) {
        inDollarQuote = false;
        buffer += dollarTag;
        i += dollarTag.length - 1;
        continue;
      }
      buffer += char;
      continue;
    }

    if (char === "'" && !inDoubleQuote) {
      if (inSingleQuote && nextChar === "'") {
        buffer += "''";
        i++;
        continue;
      }
      inSingleQuote = !inSingleQuote;
      buffer += char;
      continue;
    }

    if (char === '"' && !inSingleQuote) {
      inDoubleQuote = !inDoubleQuote;
      buffer += char;
      continue;
    }

    if (char === ';' && !inSingleQuote && !inDoubleQuote && !inDollarQuote) {
      if (buffer.trim()) statements.push(buffer.trim());
      buffer = '';
      continue;
    }

    buffer += char;
  }

  if (buffer.trim()) statements.push(buffer.trim());
  return statements;
}

export async function runPostgresCase(db, source, inputData) {
  const tables = inputData.tables || inputData;

  for (const [tableName, rawRows] of Object.entries(tables)) {
    await createPGliteTable(db, tableName, rawRows);
  }

  const statements = splitSQLStatements(source);
  let lastResult = null;
  for (const stmt of statements) {
    lastResult = await db.query(stmt);
  }

  if ((!lastResult?.fields || lastResult.fields.length === 0) && Object.keys(tables).length > 0) {
    const firstTable = Object.keys(tables)[0];
    lastResult = await db.query(`SELECT * FROM ${firstTable} ORDER BY 1;`);
  }

  const columns = lastResult?.fields ? lastResult.fields.map(f => f.name) : [];
  const rows = lastResult?.rows
    ? lastResult.rows.map(rowObj => columns.map(c => rowObj[c] ?? null))
    : [];

  return { columns, rows };
}

async function main() {
  const dirs = fs.readdirSync(leetcodeDir).filter(d => !d.startsWith('_') && !d.startsWith('.'));
  const sqlDirs = [];

  for (const d of dirs) {
    const metaPath = path.join(leetcodeDir, d, 'metadata.json');
    if (!fs.existsSync(metaPath)) continue;
    const meta = JSON.parse(fs.readFileSync(metaPath, 'utf8'));
    if (meta.primary_language === 'sql' || meta.category === 'database') {
      sqlDirs.push({ dir: path.join(leetcodeDir, d), name: d, meta });
    }
  }

  console.log(`Auditing ${sqlDirs.length} SQL packages with PostgreSQL preamble...`);

  let passedCount = 0;
  let failedPackages = [];

  for (const item of sqlDirs) {
    let solPath = path.join(item.dir, 'variants', 'optimal', 'solutions', 'solution.sql');
    if (!fs.existsSync(solPath)) {
      solPath = path.join(item.dir, 'variants', 'optimal', 'solution.sql');
    }
    if (!fs.existsSync(solPath)) {
      failedPackages.push({ name: item.name, error: 'solution.sql not found' });
      continue;
    }

    let code = fs.readFileSync(solPath, 'utf8');
    const casesPath = path.join(item.dir, 'cases.json');
    if (!fs.existsSync(casesPath)) {
      failedPackages.push({ name: item.name, error: 'cases.json not found' });
      continue;
    }

    const casesData = JSON.parse(fs.readFileSync(casesPath, 'utf8'));
    let allPassed = true;
    let errDetail = null;

    for (const c of casesData.cases) {
      try {
        const db = new PGlite();
        await db.exec(POSTGRES_PREAMBLE);
        const result = await runPostgresCase(db, code, c.input);
        const expCols = c.expected?.columns || [];
        const expRows = c.expected?.rows || [];

        const colsMatch = expCols.length === result.columns.length &&
          expCols.every((col, idx) => col.toLowerCase() === result.columns[idx]?.toLowerCase());
        
        const normalize = (v) => {
          if (v === null || v === undefined) return null;
          if (typeof v === 'number') return Math.round(v * 100) / 100;
          if (typeof v === 'string') {
            if (/^\d{4}-\d{2}-\d{2}T/.test(v)) return v.split('T')[0];
            const num = Number(v);
            if (!isNaN(num) && v.trim() !== '') return Math.round(num * 100) / 100;
          }
          return String(v);
        };
        
        const normExp = expRows.map(r => r.map(normalize));
        const normGot = result.rows.map(r => r.map(normalize));
        
        // Compare sorted rows if order not specified or if exact match
        const rowsMatch = JSON.stringify(normExp) === JSON.stringify(normGot) ||
          JSON.stringify([...normExp].sort()) === JSON.stringify([...normGot].sort());
        
        if (!colsMatch || !rowsMatch) {
          allPassed = false;
          errDetail = {
            caseId: c.id,
            expected: c.expected,
            got: result
          };
          break;
        }
      } catch (err) {
        allPassed = false;
        errDetail = {
          caseId: c.id,
          error: err.message
        };
        break;
      }
    }

    if (allPassed) {
      passedCount++;
    } else {
      failedPackages.push({ name: item.name, solPath, code, detail: errDetail });
    }
  }

  console.log(`\nAudit Results:`);
  console.log(`- PostgreSQL Passed: ${passedCount} / ${sqlDirs.length}`);
  console.log(`- Failed / Need Dialect Fixes: ${failedPackages.length}`);
  
  // Categorize errors
  const errorCategories = {};
  for (const f of failedPackages) {
    const errMsg = f.detail?.error || 'Output mismatch';
    let cat = 'Other';
    if (errMsg.includes('syntax error')) cat = 'Syntax Error: ' + errMsg;
    else if (errMsg.includes('LIMIT')) cat = 'LIMIT syntax';
    else if (errMsg.includes('does not exist')) cat = 'Object does not exist: ' + errMsg;
    else if (errMsg.includes('function') && errMsg.includes('does not exist')) cat = 'Function does not exist: ' + errMsg;
    else if (errMsg === 'Output mismatch') cat = 'Output mismatch';
    else cat = errMsg;
    errorCategories[cat] = (errorCategories[cat] || 0) + 1;
  }

  console.log(`\nError Categories:`);
  for (const [cat, count] of Object.entries(errorCategories).sort((a,b) => b[1] - a[1])) {
    console.log(`  ${count}x: ${cat}`);
  }

  console.log(`\nFirst 20 failed packages:`);
  for (const f of failedPackages.slice(0, 20)) {
    console.log(`\n[${f.name}]`);
    if (f.detail?.error) console.log(`  Error: ${f.detail.error}`);
    else console.log(`  Expected: ${JSON.stringify(f.detail?.expected)}\n  Got:      ${JSON.stringify(f.detail?.got)}`);
  }
}

main().catch(console.error);
