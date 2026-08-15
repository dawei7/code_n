import { PGlite } from '@electric-sql/pglite';

export interface PGliteResult {
  ok: boolean;
  value?: {
    columns: string[];
    rows: any[][];
  };
  stdout: string;
  stderr: string;
  runtime_ms: number;
  error_message: string;
}

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
CREATE OR REPLACE FUNCTION date_format(d date, fmt text) RETURNS text AS $$
BEGIN
  RETURN TO_CHAR(d, REPLACE(REPLACE(REPLACE(fmt, '%Y', 'YYYY'), '%m', 'MM'), '%d', 'DD'));
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION date_format(d timestamp, fmt text) RETURNS text AS $$
BEGIN
  RETURN TO_CHAR(d, REPLACE(REPLACE(REPLACE(fmt, '%Y', 'YYYY'), '%m', 'MM'), '%d', 'DD'));
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION instr(str text, sub text) RETURNS integer AS $$ SELECT POSITION(sub IN str); $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION subdate(d date, n integer) RETURNS date AS $$ SELECT (d - n); $$ LANGUAGE sql;
CREATE OR REPLACE FUNCTION subdate(d timestamp, n integer) RETURNS timestamp AS $$ SELECT (d - (n || ' day')::interval); $$ LANGUAGE sql;
`;

export async function runPostgreSQLQuery(
  source: string,
  inputData: Record<string, any>
): Promise<PGliteResult> {
  const started = performance.now();
  try {
    const db = new PGlite();
    await db.exec(POSTGRES_PREAMBLE);
    const tables = inputData.tables || inputData;

    if (!tables || typeof tables !== 'object' || Object.keys(tables).length === 0) {
      return {
        ok: false,
        stdout: '',
        stderr: '',
        runtime_ms: 0,
        error_message: 'SQL input must contain a non-empty "tables" object.'
      };
    }

    // Create & Seed Tables in PostgreSQL WASM
    for (const [tableName, rawRows] of Object.entries(tables)) {
      await createPGliteTable(db, tableName, rawRows);
    }

    // Clean and split SQL statements
    const statements = splitSQLStatements(source);
    if (statements.length === 0) {
      return {
        ok: false,
        stdout: '',
        stderr: '',
        runtime_ms: performance.now() - started,
        error_message: 'SQL source contains no statements.'
      };
    }

    let lastResult: any = null;
    for (const stmt of statements) {
      lastResult = await db.query(stmt);
    }

    if ((!lastResult?.fields || lastResult.fields.length === 0) && Object.keys(tables).length > 0) {
      const firstTable = Object.keys(tables)[0];
      lastResult = await db.query(`SELECT * FROM ${firstTable} ORDER BY 1;`);
    }

    const columns = lastResult?.fields ? lastResult.fields.map((f: any) => f.name) : [];
    const rows = lastResult?.rows
      ? lastResult.rows.map((rowObj: Record<string, any>) => columns.map((c: string) => {
          const val = rowObj[c];
          if (val === null || val === undefined) return null;
          if (val instanceof Date) return val.toISOString().split('T')[0];
          return val;
        }))
      : [];

    const runtime_ms = performance.now() - started;
    const value = { columns, rows };
    return {
      ok: true,
      value,
      stdout: JSON.stringify(value, null, 2),
      stderr: '',
      runtime_ms,
      error_message: ''
    };
  } catch (err: any) {
    return {
      ok: false,
      stdout: '',
      stderr: String(err?.message || err),
      runtime_ms: performance.now() - started,
      error_message: `PostgreSQL Error: ${err?.message || err}`
    };
  }
}

async function createPGliteTable(db: PGlite, name: string, rawRows: any): Promise<void> {
  let records: Record<string, any>[] = [];
  let columns: string[] = [];

  if (typeof rawRows === 'object' && rawRows !== null && Array.isArray(rawRows.rows)) {
    columns = (rawRows.columns || []).map(String);
    records = rawRows.rows.map((row: any[]) => {
      const rec: Record<string, any> = {};
      columns.forEach((col, idx) => {
        rec[col] = row[idx];
      });
      return rec;
    });
  } else if (Array.isArray(rawRows)) {
    records = rawRows.filter(r => typeof r === 'object' && r !== null);
    records.forEach(rec => {
      Object.keys(rec).forEach(col => {
        if (!columns.includes(col)) columns.push(col);
      });
    });
  }

  if (columns.length === 0) {
    columns = ['id'];
  }

  const columnTypes = columns.map(col => {
    const sampleVal = records.find(r => r[col] !== undefined && r[col] !== null)?.[col];
    return `${col} ${inferPostgresType(col, sampleVal)}`;
  });

  const createDDL = `CREATE TABLE ${name} (${columnTypes.join(', ')});`;
  await db.exec(createDDL);

  if (records.length > 0) {
    for (const rec of records) {
      const colsStr = columns.join(', ');
      const valsStr = columns.map(c => formatPGValue(rec[c])).join(', ');
      const insertDML = `INSERT INTO ${name} (${colsStr}) VALUES (${valsStr});`;
      await db.exec(insertDML);
    }
  }
}

function inferPostgresType(col: string, val: any): string {
  const lower = col.toLowerCase();
  if (val === null || val === undefined) {
    if (lower.endsWith('_id') || lower === 'id' || lower.includes('salary') || lower.includes('amount') || lower.includes('count')) {
      return 'BIGINT';
    }
    return 'TEXT';
  }
  if (typeof val === 'boolean') return 'BOOLEAN';
  if (typeof val === 'number') return Number.isInteger(val) ? 'BIGINT' : 'DOUBLE PRECISION';
  if (typeof val === 'string') {
    if (/^\d{4}-\d{2}-\d{2}(\s|T)\d{2}:\d{2}:\d{2}/.test(val)) return 'TIMESTAMP';
    if (/^\d{4}-\d{2}-\d{2}$/.test(val)) return 'DATE';
  }
  return 'TEXT';
}

function formatPGValue(val: any): string {
  if (val === null || val === undefined) return 'NULL';
  if (typeof val === 'boolean') return val ? 'TRUE' : 'FALSE';
  if (typeof val === 'number') return String(val);
  const str = String(val).replace(/'/g, "''");
  return `'${str}'`;
}

function splitSQLStatements(source: string): string[] {
  const statements: string[] = [];
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
