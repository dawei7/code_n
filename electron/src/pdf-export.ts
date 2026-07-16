import { app, BrowserWindow, dialog, ipcMain } from 'electron';
import * as fs from 'node:fs';
import * as path from 'node:path';

import type {
  PdfSaveRequest,
  PdfSaveResult,
} from '../../web/src/types/electron';
import { repairInternalPdfDestinations } from './pdf-destinations';


const PDF_CHANNEL = 'pdf:save';


export function initPdfExport(getMainWindow: () => BrowserWindow | null): void {
  ipcMain.removeHandler(PDF_CHANNEL);
  ipcMain.handle(
    PDF_CHANNEL,
    async (event, rawRequest: PdfSaveRequest): Promise<PdfSaveResult> => {
      const window = getMainWindow();
      if (!window || window.isDestroyed() || event.sender !== window.webContents) {
        return { status: 'error', message: 'The PDF export window is unavailable.' };
      }

      const request = normalizeRequest(rawRequest);
      const selection = await dialog.showSaveDialog(window, {
        title: 'Save as PDF',
        defaultPath: path.join(app.getPath('documents'), request.suggestedFilename),
        buttonLabel: 'Save PDF',
        filters: [{ name: 'PDF document', extensions: ['pdf'] }],
        properties: ['createDirectory', 'showOverwriteConfirmation'],
      });
      if (selection.canceled || !selection.filePath) {
        return { status: 'cancelled' };
      }

      const outputPath = ensurePdfExtension(selection.filePath);
      const previousBackgroundColor = window.getBackgroundColor();
      try {
        // Chromium paints the physical @page margin from the BrowserWindow
        // backing color. The app window is navy in every theme, so print CSS
        // alone cannot prevent that color from becoming part of the PDF.
        window.setBackgroundColor('#ffffff');
        await event.sender.executeJavaScript(
          'new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))',
        );
        const chromiumPdf = await event.sender.printToPDF({
          pageSize: 'A4',
          printBackground: true,
          preferCSSPageSize: true,
          displayHeaderFooter: true,
          headerTemplate: '<div></div>',
          footerTemplate: footerTemplate(request.title),
          generateTaggedPDF: true,
          generateDocumentOutline: true,
        });
        const pdf = await repairInternalPdfDestinations(chromiumPdf);
        await fs.promises.writeFile(outputPath, pdf);
        return { status: 'saved', path: outputPath };
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        console.error(`[coden-electron] PDF export failed: ${message}`);
        return { status: 'error', message: `Could not save the PDF: ${message}` };
      } finally {
        if (!window.isDestroyed()) {
          window.setBackgroundColor(previousBackgroundColor);
        }
      }
    },
  );
}


function normalizeRequest(raw: PdfSaveRequest): PdfSaveRequest {
  const rawTitle = typeof raw?.title === 'string' ? raw.title.trim() : '';
  const rawFilename = typeof raw?.suggestedFilename === 'string'
    ? raw.suggestedFilename
    : '';
  return {
    title: rawTitle.slice(0, 180) || 'cOde(n) document',
    suggestedFilename: sanitizePdfFilename(rawFilename),
  };
}


function sanitizePdfFilename(value: string): string {
  const withoutExtension = value.replace(/\.pdf$/i, '');
  const safe = withoutExtension
    .replace(/[<>:"/\\|?*\u0000-\u001f]/g, '-')
    .replace(/\s+/g, ' ')
    .replace(/[. ]+$/g, '')
    .trim()
    .slice(0, 120);
  return `${safe || 'coden-document'}.pdf`;
}


function ensurePdfExtension(filePath: string): string {
  return path.extname(filePath).toLowerCase() === '.pdf'
    ? filePath
    : `${filePath}.pdf`;
}


function footerTemplate(title: string): string {
  const escapedTitle = escapeHtml(title);
  return `
    <div style="box-sizing:border-box;width:100%;padding:0 18mm;color:#64748b;font-family:Arial,sans-serif;font-size:8px;display:flex;justify-content:space-between;align-items:center;">
      <span style="max-width:75%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escapedTitle}</span>
      <span style="white-space:nowrap;"><span class="pageNumber"></span> / <span class="totalPages"></span></span>
    </div>
  `;
}


function escapeHtml(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
