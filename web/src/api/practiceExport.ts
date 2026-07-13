import { apiFetch } from './client';

export interface PracticeExportEntry {
  id: string;
  path: string[];
  filename_prefix?: string;
}

export interface DownloadProgress {
  loaded: number;
  total: number | null;
  percent: number | null;
}

function downloadBlob(blob: Blob, fallbackName: string, disposition: string | null) {
  const match = /filename="?(?<name>[^";]+)"?/i.exec(disposition ?? '');
  const filename = match?.groups?.name || fallbackName;
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

async function responseToBlob(
  response: Response,
  onProgress?: (progress: DownloadProgress) => void,
): Promise<Blob> {
  const totalHeader = response.headers.get('Content-Length');
  const total = totalHeader ? Number(totalHeader) : null;
  const knownTotal = total && Number.isFinite(total) && total > 0 ? total : null;

  if (!response.body) {
    const blob = await response.blob();
    onProgress?.({
      loaded: blob.size,
      total: knownTotal ?? blob.size,
      percent: 100,
    });
    return blob;
  }

  const reader = response.body.getReader();
  const chunks: BlobPart[] = [];
  let loaded = 0;

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    if (!value) continue;
    chunks.push(value);
    loaded += value.byteLength;
    onProgress?.({
      loaded,
      total: knownTotal,
      percent: knownTotal ? Math.min(100, (loaded / knownTotal) * 100) : null,
    });
  }

  const blob = new Blob(chunks, {
    type: response.headers.get('Content-Type') ?? 'application/octet-stream',
  });
  onProgress?.({
    loaded,
    total: knownTotal ?? blob.size,
    percent: 100,
  });
  return blob;
}

export async function downloadChallengePracticeFile(
  challengeId: string,
  filenamePrefix?: string,
  onProgress?: (progress: DownloadProgress) => void,
) {
  const params = new URLSearchParams();
  if (filenamePrefix) params.set('filename_prefix', filenamePrefix);
  const suffix = params.toString() ? `?${params}` : '';
  const response = await apiFetch(`/practice-export/challenges/${encodeURIComponent(challengeId)}${suffix}`);
  downloadBlob(
    await responseToBlob(response, onProgress),
    `${challengeId}.py`,
    response.headers.get('Content-Disposition'),
  );
}

export async function downloadPracticeBundle(
  entries: PracticeExportEntry[],
  onProgress?: (progress: DownloadProgress) => void,
) {
  const response = await apiFetch('/practice-export/bundle', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ entries }),
  });
  downloadBlob(
    await responseToBlob(response, onProgress),
    'coden-practice-export.zip',
    response.headers.get('Content-Disposition'),
  );
}
