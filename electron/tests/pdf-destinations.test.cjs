const assert = require('node:assert/strict');
const test = require('node:test');

const {
  PDFArray,
  PDFDict,
  PDFDocument,
  PDFName,
  PDFNumber,
} = require('pdf-lib');
const {
  repairInternalPdfDestinations,
} = require('../dist/electron/src/pdf-destinations.js');


test('normalizes cOde(n) destinations without changing unrelated destinations', async () => {
  const source = await PDFDocument.create({ updateMetadata: false });
  const tocPage = source.addPage([600, 800]);
  const targetPage = source.addPage([600, 800]);
  const destinations = PDFDict.withContext(source.context);
  destinations.set(
    PDFName.of('coden-problem-test'),
    source.context.obj([
      targetPage.ref,
      PDFName.of('XYZ'),
      PDFNumber.of(0),
      PDFNumber.of(-5000),
      PDFNumber.of(0),
    ]),
  );
  destinations.set(
    PDFName.of('external-destination'),
    source.context.obj([
      targetPage.ref,
      PDFName.of('XYZ'),
      PDFNumber.of(0),
      PDFNumber.of(-200),
      PDFNumber.of(0),
    ]),
  );
  destinations.set(
    PDFName.of('coden-pdf-toc'),
    source.context.obj([
      tocPage.ref,
      PDFName.of('XYZ'),
      PDFNumber.of(0),
      PDFNumber.of(800),
      PDFNumber.of(0),
    ]),
  );
  source.catalog.set(PDFName.of('Dests'), destinations);

  const tocLink = source.context.obj({
    Type: 'Annot',
    Subtype: 'Link',
    Rect: [500, 755, 600, 800],
    Dest: 'coden-pdf-toc',
  });
  tocPage.node.set(PDFName.of('Annots'), source.context.obj([tocLink]));
  targetPage.node.set(PDFName.of('Annots'), source.context.obj([tocLink]));

  const repairedBytes = await repairInternalPdfDestinations(await source.save());
  const repaired = await PDFDocument.load(repairedBytes, { updateMetadata: false });
  const repairedDestinations = repaired.catalog.lookup(PDFName.of('Dests'), PDFDict);
  const codenDestination = repaired.context.lookup(
    repairedDestinations.get(PDFName.of('coden-problem-test')),
    PDFArray,
  );
  const externalDestination = repaired.context.lookup(
    repairedDestinations.get(PDFName.of('external-destination')),
    PDFArray,
  );

  assert.equal(codenDestination.lookup(3, PDFNumber).asNumber(), 800);
  assert.equal(externalDestination.lookup(3, PDFNumber).asNumber(), -200);
  assert.equal(
    repaired.getPage(0).node.lookup(PDFName.of('Annots'), PDFArray).size(),
    0,
  );
  assert.equal(
    repaired.getPage(1).node.lookup(PDFName.of('Annots'), PDFArray).size(),
    1,
  );
  assert.ok(repaired.getPage(0).node.get(PDFName.of('Contents')));
});
