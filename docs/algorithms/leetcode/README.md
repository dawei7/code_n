# LeetCode Dataset

This folder is reserved for LeetCode-sourced challenge metadata and original cOde(n) writeups.

Do not copy LeetCode problem statements, editorials, or solution text here. Store stable facts such as title, slug, difficulty, tags, paid/free status, and the official URL, then write local summaries, examples, and canonical solution notes in original wording.

Suggested layout:

- `index.json`: generated metadata for free LeetCode problems.
- `{topic}/{frontend_id}_{slug}.md`: local reference docs in the same compact style as the NeetCode references.

Use `tools/import_leetcode_free_dataset.py` to refresh metadata and scaffold missing reference files.

Use `tools/materialize_leetcode_from_local_specs.py` after a metadata refresh to fill any LeetCode docs that already match local cOde(n) specs. The script writes `_materialization_report.json`, which separates completed local-spec matches from the remaining authoring queue.

Use `tools/check_leetcode_dataset.py` to generate `_completion_report.json` and see which docs are complete, materialized from local specs, or still need original authoring.
