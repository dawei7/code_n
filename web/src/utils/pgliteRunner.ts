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

export async function runPostgreSQLQuery(
  source: string,
  inputData: Record<string, any>
): Promise<PGliteResult> {
  const started = performance.now();
  try {
    const db = new PGlite();
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

    const columns = lastResult?.fields ? lastResult.fields.map((f: any) => f.name) : [];
    const rows = lastResult?.rows
      ? lastResult.rows.map((rowObj: Record<string, any>) => columns.map((c: string) => rowObj[c] ?? null))
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
    throw new Error(`Table "${name}" has no valid columns.`);
  }

  const columnTypes = columns.map(col => {
    const sampleVal = records.find(r => r[col] !== undefined && r[col] !== null)?.[col];
    return `${quoteIdentifier(col)} ${inferPostgresType(sampleVal)}`;
  });

  const createDDL = `CREATE TABLE ${quoteIdentifier(name)} (${columnTypes.join(', ')});`;
  await db.exec(createDDL);

  if (records.length > 0) {
    for (const rec of records) {
      const colsStr = columns.map(quoteIdentifier).join(', ');
      const valsStr = columns.map(c => formatPGValue(rec[c])).join(', ');
      const insertDML = `INSERT INTO ${quoteIdentifier(name)} (${colsStr}) VALUES (${valsStr});`;
      await db.exec(insertDML);
    }
  }
}

function inferPostgresType(val: any): string {
  if (val === null || val === undefined) return 'TEXT';
  if (typeof val === 'boolean') return 'BOOLEAN';
  if (typeof val === 'number') return Number.isInteger(val) ? 'INTEGER' : 'DOUBLE PRECISION';
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

function quoteIdentifier(name: string): string {
  return '"' + name.replace(/"/g, '""') + '"';
}

function splitSQLStatements(source: string): string[] {
  return source
    .split(';')
    .map(s => s.trim())
    .filter(s => s.length > 0);
}
