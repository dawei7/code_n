/**
 * Thin fetch wrapper. All API calls go through `/api/*` so the
 * Vite dev proxy and the Electron production build can use the
 * same base path.
 */

export class ApiError extends Error {
  constructor(public status: number, public detail: unknown, message: string) {
    super(message);
  }
}

async function readErrorDetail(res: Response): Promise<unknown> {
  let text = '';
  try {
    text = await res.text();
  } catch {
    return null;
  }
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

export async function apiFetch(path: string, init: RequestInit = {}): Promise<Response> {
  const method = init.method?.toUpperCase() ?? 'GET';
  const res = await fetch(`/api${path}`, init);
  if (!res.ok) {
    const detail = await readErrorDetail(res);
    throw new ApiError(res.status, detail, `${method} ${path} -> ${res.status}`);
  }
  return res;
}

export async function apiGet<T>(path: string): Promise<T> {
  const res = await apiFetch(path);
  return res.json() as Promise<T>;
}

export async function apiText(path: string): Promise<string> {
  const res = await apiFetch(path);
  return res.text();
}

export async function apiPost<T>(path: string, body: unknown): Promise<T> {
  const res = await apiFetch(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return res.json() as Promise<T>;
}

export async function apiPut<T>(path: string, body: unknown): Promise<T> {
  const res = await apiFetch(path, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return res.json() as Promise<T>;
}

export async function apiDelete<T>(path: string): Promise<T> {
  const res = await apiFetch(path, {
    method: 'DELETE',
  });
  return res.json() as Promise<T>;
}
