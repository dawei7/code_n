# Spec Generator

The spec generator is a tool for batch-adding algorithm challenges
to cOde(n) without the manual indentation / string-escape /
SPECS.extend bookkeeping that the inline approach requires.

## Why

Every new spec needs four correctly-indented things:
1. A `*_SOURCE` triple-quoted string literal whose function body
   is indented by 4 spaces INSIDE the string.
2. A `_setup_*` helper function at module scope.
3. A `_verify_*` helper function at module scope.
4. An `AlgorithmSpec(...)` call inside `SPECS.extend([...])`,
   indented by 4 spaces.

The first item is the most error-prone — getting the body
indentation wrong is silent until the spec gauntlet fails.
The generator centralises that formatting so the author can
focus on the algorithm, not the whitespace.

## Usage

1. **Write an input file** that defines `SPECS_TO_ADD = [...]`,
   a list of dicts. One dict per new spec. See
   `batch_2d_trees.py` for a working example.

2. **Run the generator** from the project root:

```bash
python -m challenges.algorithms._generator \\
    --module trees \\
    --input batch_2d_trees.py
```

The generator:
- Appends the source string + setup/verify functions to
  `challenges/algorithms/<module>.py`.
- Appends the AlgorithmSpec block(s) to that module's
  `SPECS.extend([...])` at the end.
- Writes a standalone organized optimal solution file for each
  record, preferring the matching
  `optimal_solutions/geeksforgeeks/<category>/<doc-stem>.py`
  path when the English doc already exists.
- Does **not** register new modules — that's still a one-line
  edit to `challenges/registry.py` if you're creating a new
  category file (not needed for the existing 8 categories).

3. **Run the spec gauntlet** to confirm:

```bash
.venv/Scripts/python.exe -m unittest tests.test_algorithm_spec
```

4. **Build & ship** as usual (see `feedback-rebuild-exe-after-changes.md`).

## Input format

```python
SPECS_TO_ADD = [
    {
        "id": "tree_11",
        "name": "Balanced Tree Check",
        "category": "trees",
        "difficulty": 3,
        "complexity": "O_N",  # one of O_1, O_LOG_N, O_N, O_N_LOG_N,
                              # O_N2, O_N3, O_2N, UNKNOWN
        "description": (
            "Return True iff the binary tree is height-balanced:\n"
            "for every node, the heights of its left and right\n"
            "subtrees differ by at most 1.\n"
            "...\n"
            "Source: https://www.geeksforgeeks.org/..."
        ),
        "source_url": "https://www.geeksforgeeks.org/...",
        "params": ["children", "root", "n"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        "returns": "True iff the tree is height-balanced.",
        "solve": '''
def solve(children, root, n):
    """Return True iff the binary tree is height-balanced."""
    balanced = [True]

    def height(u):
        if u == -1:
            return 0
        l = height(children[u][0])
        r = height(children[u][1])
        if abs(l - r) > 1:
            balanced[0] = False
        return 1 + max(l, r)

    height(root)
    return balanced[0]
''',
        "setup": '''
rng = random.Random(seed)
n_nodes = max(1, min(n, 12))
children = [[-1, -1] for _ in range(n_nodes)]
# ... build the tree ...
challenge._children = children
return {"children": children, "root": 0, "n": n_nodes}
''',
        "verify": '''
def walk(u):
    if u == -1:
        return 0
    l = walk(challenge._children[u][0])
    r = walk(challenge._children[u][1])
    if abs(l - r) > 1:
        return -1
    return 1 + max(l, r)
expected = walk(0) != -1
return result == expected
''',
        "samples": [
            ("children = [[1, 2], ...], root = 0, n = 5", "True"),
            ("children = [[1, -1], ...], root = 0, n = 2", "True"),
            ("children = [[1, 2], ...], root = 0, n = 5", "False"),
        ],
        "hint": "Recurse. For each node, if the two subtree heights differ by more than 1, the tree is unbalanced.",
        "parents": ["tree_04"],
        "children": ["tree_12"],
    },
    # ... more records ...
]
```

### Important notes on the `solve`, `setup`, and `verify` fields

- These are **triple-quoted strings** that contain Python code.
- The strings are inserted INTO the spec file as-is, so the
  author can write them with the natural indent of a function
  body (4 spaces from the function's `def` line).
- The generator strips the common leading whitespace from
  every line so that the function-body indent is preserved
  RELATIVE to the `def` line.
- The first line of `solve` MUST be `def solve(...):` at
  column 0 (after the generator strips the common indent).
- `setup` should NOT have a `def` line — the generator adds
  `def _setup_<id>(...):` for you.
- `verify` likewise has no `def` line — the generator adds
  `def _verify_<id>(...):` for you.
- Comments, nested defs, multi-line strings all work — just
  keep the RELATIVE indent consistent.

## Currently supported categories

The generator appends to existing module files. To target a
specific category, use the matching `--module` value:

| `--module` | File |
|---|---|
| `intro` | `challenges/algorithms/intro.py` |
| `sorting` | `challenges/algorithms/sorting.py` |
| `searching` | `challenges/algorithms/searching.py` |
| `graphs` | `challenges/algorithms/graphs.py` |
| `dynamic` | `challenges/algorithms/dynamic.py` |
| `greedy` | `challenges/algorithms/greedy.py` |
| `strings` | `challenges/algorithms/strings.py` |
| `trees` | `challenges/algorithms/trees.py` |

## Adding a new category

If you want to add a new category (e.g. `heaps`, `hashing`):

1. Create `challenges/algorithms/<new>.py` with `SPECS: list[AlgorithmSpec] = []`
   and the imports your helpers will need.
2. Edit `challenges/registry.py` to import + spread the new
   module's `SPECS` (the same pattern as the existing 8).
3. Run the generator with `--module <new>`.
