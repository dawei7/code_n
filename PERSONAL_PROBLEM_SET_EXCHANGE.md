# Personal problem-set exchange

cOde(n) shares Personal roots through a portable JSON document. Version 1 is a
frozen interchange contract: existing field meanings and required identity
fields must not be changed or reused. Future additions must be optional, and an
incompatible representation must use a new integer `version`.

## Envelope

```json
{
  "schema": "urn:coden:personal-problem-sets:1",
  "format": "coden.personal-problem-sets",
  "version": 1,
  "exported_at": "2026-07-18T12:00:00.000Z",
  "sets": []
}
```

Readers must ignore unknown fields. They must reject an unknown `format` or
unsupported `version` instead of guessing.

Each entry in `sets` contains:

- `name`: the Personal root name.
- `description`: its optional user-authored note.
- `career_mode`: whether that root uses leaf-local sequential unlocking.
- `nodes`: an ordered list of folders and LeetCode problem references.

A folder node uses `{"type": "folder", "name": "...", "children": []}`.
A problem node uses:

```json
{
  "type": "problem",
  "provider": "leetcode",
  "canonical_id": "lc_1",
  "frontend_id": "1",
  "title_slug": "two-sum",
  "title": "Two Sum",
  "url": "https://leetcode.com/problems/two-sum/"
}
```

`frontend_id` is the primary cross-install identity. Importers then fall back
to `canonical_id` and `title_slug`. The title and URL are descriptive and make
the file useful outside cOde(n); they do not replace canonical identity.

Internal set, folder, placement, and profile IDs are deliberately excluded.
Imports generate fresh local IDs, resolve problems against the receiving
installation's canonical LeetCode corpus, ignore same-leaf duplicates, and
report unresolved problems. Imports also enforce the current five-root,
three-folder-level, and payload-size safety limits.
