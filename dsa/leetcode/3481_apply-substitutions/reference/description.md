## Description

The list `replacements` defines a mapping from one-letter keys to string values. A placeholder has the form `%X%`, where `X` is a mapped key. Replacement values may themselves contain placeholders, so resolving one key can depend on resolving other keys first.

Expand every placeholder recursively and return the fully substituted `text`. Every referenced key is present, replacement dependencies contain no cycle, and the returned string must contain no placeholders. A key's expansion has the same meaning wherever that key is referenced.
