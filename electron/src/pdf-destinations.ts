import {
  PDFArray,
  PDFDict,
  PDFDocument,
  PDFName,
  PDFNull,
  PDFNumber,
  PDFRef,
  PDFString,
  PDFHexString,
  rgb,
} from 'pdf-lib';


const CODEN_DESTINATION_PREFIX = 'coden-';
const CODEN_PROBLEM_DESTINATION_PREFIX = 'coden-problem-';
const CODEN_TOC_DESTINATION = 'coden-pdf-toc';


/**
 * Chromium emits correct target-page references for long-document anchors but
 * may leave their /XYZ top coordinate in document space. Acrobat rejects the
 * resulting negative values. Normalize cOde(n)'s named destinations to the top
 * of their already-correct target page without altering other links or the
 * generated outline.
 */
export async function repairInternalPdfDestinations(
  source: Uint8Array,
): Promise<Uint8Array> {
  const document = await PDFDocument.load(source, { updateMetadata: false });
  const destinations = document.catalog.lookupMaybe(PDFName.of('Dests'), PDFDict);
  if (!destinations) return source;

  const pageHeights = new Map(
    document.getPages().map((page) => [page.ref.tag, page.getHeight()]),
  );
  const pageIndexes = new Map(
    document.getPages().map((page, index) => [page.ref.tag, index]),
  );
  let firstProblemPageIndex: number | null = null;
  let repaired = 0;

  for (const [name, rawDestination] of destinations.entries()) {
    const destinationName = name.decodeText();
    if (!destinationName.startsWith(CODEN_DESTINATION_PREFIX)) continue;
    const destination = document.context.lookup(rawDestination, PDFArray);
    const pageRef = destination.get(0);
    if (!(pageRef instanceof PDFRef)) continue;
    const pageHeight = pageHeights.get(pageRef.tag);
    if (pageHeight === undefined) continue;
    if (destinationName.startsWith(CODEN_PROBLEM_DESTINATION_PREFIX)) {
      const pageIndex = pageIndexes.get(pageRef.tag);
      if (pageIndex !== undefined) {
        firstProblemPageIndex = firstProblemPageIndex === null
          ? pageIndex
          : Math.min(firstProblemPageIndex, pageIndex);
      }
    }

    destinations.set(
      name,
      document.context.obj([
        pageRef,
        PDFName.of('XYZ'),
        PDFNull,
        PDFNumber.of(pageHeight),
        PDFNull,
      ]),
    );
    repaired += 1;
  }

  // The return control is deliberately fixed so Chromium repeats it on every
  // document page. It is meaningless on the table-of-contents pages. Cover
  // the repeated fragment in the reserved top margin there and remove its link
  // annotation, while leaving every later page's control intact.
  if (firstProblemPageIndex !== null) {
    for (let pageIndex = 0; pageIndex < firstProblemPageIndex; pageIndex += 1) {
      const page = document.getPage(pageIndex);
      const controlRectangles = removeTocLinkAnnotations(document, pageIndex);
      for (const rectangle of controlRectangles) {
        const padding = 2;
        page.drawRectangle({
          x: rectangle.x - padding,
          y: rectangle.y - padding,
          width: rectangle.width + (2 * padding),
          height: rectangle.height + (2 * padding),
          color: rgb(1, 1, 1),
        });
      }
    }
  }

  if (repaired === 0) return source;
  return document.save({
    addDefaultPage: false,
    updateFieldAppearances: false,
    useObjectStreams: false,
  });
}


type PdfRectangle = { x: number; y: number; width: number; height: number };


function removeTocLinkAnnotations(
  document: PDFDocument,
  pageIndex: number,
): PdfRectangle[] {
  const page = document.getPage(pageIndex);
  const annotations = page.node.lookupMaybe(PDFName.of('Annots'), PDFArray);
  if (!annotations) return [];
  const rectangles: PdfRectangle[] = [];

  for (let index = annotations.size() - 1; index >= 0; index -= 1) {
    const annotation = document.context.lookup(annotations.get(index), PDFDict);
    const destination = annotation.get(PDFName.of('Dest'));
    if (decodeDestinationName(destination) === CODEN_TOC_DESTINATION) {
      const rectangle = annotation.lookupMaybe(PDFName.of('Rect'), PDFArray);
      if (rectangle?.size() === 4) {
        const [left, bottom, right, top] = [0, 1, 2, 3].map(
          (coordinate) => rectangle.lookup(coordinate, PDFNumber).asNumber(),
        );
        rectangles.push({
          x: Math.min(left!, right!),
          y: Math.min(bottom!, top!),
          width: Math.abs(right! - left!),
          height: Math.abs(top! - bottom!),
        });
      }
      annotations.remove(index);
    }
  }
  return rectangles;
}


function decodeDestinationName(destination: unknown): string | null {
  if (
    destination instanceof PDFName
    || destination instanceof PDFString
    || destination instanceof PDFHexString
  ) {
    return destination.decodeText();
  }
  return null;
}
