# LeetCode Dataset

This folder is reserved for LeetCode-sourced challenge metadata and original cOde(n) writeups.

Do not copy LeetCode problem statements, editorials, or solution text here. Store stable facts such as title, slug, difficulty, tags, paid/free status, and the official URL, then write local summaries, examples, and canonical solution notes in original wording.

Canonical layout:

- `index.json`: generated metadata for free LeetCode problems.
- `<frontend_id:04d>_<slug>/`: one package per problem, with a four-digit,
  zero-padded directory prefix for numeric repository ordering.

Use `tools/import_leetcode_free_dataset.py` to refresh metadata and scaffold missing reference files.

Use `tools/materialize_leetcode_from_local_specs.py` after a metadata refresh to fill any LeetCode docs that already match local cOde(n) specs. The script writes `_materialization_report.json`, which separates completed local-spec matches from the remaining authoring queue.

Use `tools/check_leetcode_dataset.py` to generate `_completion_report.json` and see which docs are complete, materialized from local specs, or still need original authoring.

Reference documents may use the legacy monolithic `doc.md` format or the
section-authored package format piloted by `0001_two-sum`. Section mode keeps
the authored content in `reference/description.md`, `contract.md`,
`examples.md`, and `constraints.md`, plus source-native optional files such as
`follow_up.md`; the server composes those files with the metadata table into the
single Reference document shown by the app.

Package completion and source fidelity are intentionally separate. A reviewed
package adds `source_fidelity.json`, which records the live source hash,
source-section order, exact example facts and explanation presence, constraint
count, visual/table counts, and explicit review assertions. It does not store
LeetCode prose or HTML. It also hashes each reviewed local section so later
edits cannot retain a stale verified status. Run
`tools/audit_leetcode_source_fidelity.py` to review the current first-500 batch;
missing manifests remain visibly `unverified`.
