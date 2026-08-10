## General

**Separate a nested-data problem into two phases**

Each input item may contain nested objects and arrays, while a matrix needs one flat, consistent set of columns. The solution handles this mismatch in two phases:

1. flatten every input item into a map from complete leaf path to leaf value;
2. take the union of those paths, sort it, and align every flattened row to that common column order.

This separation is important. A row cannot be finalized when it is first visited because a later input item may introduce a new column that all earlier rows must also contain as an empty cell.

**What a flattened row represents**

For one input item, `flattened` is an object whose keys are column paths and whose values are terminal JSON values.

For example, a nested value conceptually shaped as an object `a` containing leaf `b` produces path `a.b`. If an array is encountered, its indices act as keys. Thus an array's element zero containing property `a` produces path `0.a`.

Only leaves become entries. Container objects and arrays determine path segments, but they do not themselves occupy matrix cells.

**Recursively visit containers and leaves**

The inner function `visit(value, path)` distinguishes a traversable container with:

`value !== null && typeof value === "object"`.

This condition needs both parts. In JavaScript, `typeof null` is `"object"` even though `null` is a terminal JSON value, not a container that should be traversed.

For a real object or array, `Object.entries(value)` produces each own enumerable key and child value. The recursive call processes the child using an extended path.

For a number, string, Boolean, or `null`, recursion stops and the solution stores:

`flattened[path] = value`.

The stored value remains unchanged. In particular, false, zero, `null`, and an actual empty string are legitimate leaf values and must not be mistaken for a missing column.

**Build paths without a leading period**

When recursion begins, `path` is the empty string. For the first key, the expression chooses that key directly:

`path === "" ? key : path + "." + key`.

At deeper levels it places a period between the prior path and the next segment.

This produces `a.b` instead of `.a.b`. The rule works equally for object property names and the string-form numeric indices returned by `Object.entries` on arrays.

**Arrays require no separate traversal branch**

JavaScript arrays are objects, and `Object.entries` enumerates their present indexed elements using keys such as `"0"`, `"1"`, and so on.

Therefore the same recursive container case naturally flattens arrays. An input item like `[{"a": null}]` reaches the leaf through segments `0` and `a`, creating column `0.a` with value `null`.

This reuse keeps object and array behavior consistent without duplicating recursion logic.

**Empty containers contribute no leaf path**

`Object.entries({})` and `Object.entries([])` are empty. The loop makes no recursive calls, and the container itself is not stored because it entered the object branch.

Therefore an empty object flattens to a row with no keys. If every input item is empty, the union of keys is empty, the header is `[]`, and every data row is also `[]`.

If only one row is empty while other rows define columns, matrix construction later fills every cell of that empty row with `""`.

**Collect the global columns**

After `arr.map` has produced all flattened row objects, the expression `rows.flatMap((row) => Object.keys(row))` gathers every leaf path from every row.

Different rows may contain the same path, so `new Set(...)` removes duplicates. Converting the set back to an array and calling `sort()` produces the required lexicographically ascending header.

The sorted `columns` array becomes the first matrix row. Because every later row iterates this exact same array, column positions are consistent throughout the matrix.

**Why sorting happens after collecting the union**

Sorting each row's own paths would not establish a shared schema. For example, one row might contain `a` and `d` while another contains `b` and `c`. Their separately sorted lists still have different meanings at each index.

The algorithm first determines the complete set `[a, b, c, d]` and sorts that one set. Only then can every row place its values under the correct header.

**Align each row with direct lookup**

For each flattened row, the algorithm maps over every global column. If the row owns that path, it emits `row[column]`. Otherwise, it emits the required missing-cell marker `""`.

The own-property test is written as:

`Object.prototype.hasOwnProperty.call(row, column)`.

This is more precise than testing truthiness. A present value may be zero, false, `null`, or `""`, all of which must be preserved. It is also safer than calling `row.hasOwnProperty(column)` directly because input-derived property names could shadow a method name and because only the object's own flattened entries should count.

**Trace rows with different schemas**

Suppose the first flattened row is conceptually `{a: 1, b: 2}` and the second is `{c: 3}`.

The union of paths is `a`, `b`, and `c`, already in sorted order. Matrix construction produces:

- header `["a", "b", "c"]`;
- first data row `[1, 2, ""]`;
- second data row `["", "", 3]`.

The empty strings are generated by absence checks, not by changing the flattened row objects.

**Trace nested and null values**

For input items shaped like `{"a":{"b":1,"c":2}}` and `{"a":{"b":3,"d":null}}`, flattening creates paths `a.b` and `a.c` for the first row, and `a.b` and `a.d` for the second.

The sorted columns are `["a.b", "a.c", "a.d"]`. The `null` under `a.d` is retained as `null` because the property exists. Only `a.c` in the second row and `a.d` in the first row become `""`.

This illustrates why checking property existence rather than the value itself is essential.

**Why the result is correct**

Recursion follows every object property and array index from an input root to every reachable leaf, appending exactly the traversed key at each level. Consequently, each leaf is stored under its complete required path, and no non-leaf creates a column.

The set of row keys is therefore exactly the union of all leaf paths. Sorting it makes the header satisfy the required order. For every row and header column, the final mapping emits the corresponding leaf value if that path exists and `""` otherwise.

These facts cover all cells and prove that the returned matrix has the required schema and contents.

**Why flatten once is efficient**

An alternative can collect paths and then repeatedly walk each original nested object to retrieve every column. That revisits common prefixes many times.

The exact solution visits the nested input once to materialize direct path lookups. Matrix construction then performs one expected constant-time own-property lookup per output cell. This matches the unavoidable need to produce all $r \times k$ data cells when there are $r$ input rows and $k$ global columns.

## Complexity detail

Let $r$ be the number of input items, $k$ the number of unique leaf paths, and $S$ the total work required to traverse the nested inputs and construct their path strings and flattened entries.

Flattening costs $O(S)$. Collecting keys is linear in the stored flattened entries. Sorting the $k$ unique columns costs $O(k\log k)$. Constructing the data portion performs one lookup for each row-column combination, costing expected $O(rk)$. Total time is $O(S+k\log k+rk)$.

The flattened rows and their path strings use $O(S)$ space. The returned matrix contains a header and $r$ rows with up to $k$ cells each, using $O(rk)$ space. The recursion additionally uses $O(d)$ call-stack space for maximum nesting depth $d$, which is covered by the traversed representation bound. Total space is $O(S+rk)$.

## Alternatives and edge cases

- **Collect paths, then traverse originals for each cell:** Correct but can repeatedly walk deep prefixes and do more work than direct flattened lookup.
- **Build columns incrementally while emitting rows:** New columns discovered late require extending and realigning earlier rows, making the logic more complicated.
- **Iterative depth-first traversal:** An explicit stack avoids recursive call-stack limits while producing the same path-to-value maps.
- **Use `Map` for flattened rows:** It avoids special object property behavior and supports direct `has` checks, at the cost of slightly different syntax.
- **Plain-object special keys:** The exact code stores paths in `{}`; a path such as `__proto__` has special legacy behavior in JavaScript. `Object.create(null)` or `Map` is more defensive when arbitrary property names must be supported.
- **Periods inside source keys:** Dot-separated path notation is ambiguous if an individual key itself contains a period. The challenge's path representation must be interpreted under its intended key semantics.
- **Null leaf:** It is preserved as `null` because the explicit null check prevents recursion into it.
- **False, zero, and empty-string leaves:** They are present values and are preserved by the own-property test.
- **Missing leaf:** Only genuine absence produces the placeholder `""`.
- **Nested arrays:** Numeric indices become ordinary path segments such as `0.a`.
- **Empty object or array:** It contributes no columns.
- **All rows empty:** The result contains one empty header followed by one empty row for every input item.
- **Different schemas per row:** The union supplies every column and missing paths are padded.
- **Duplicate paths across rows:** The set keeps one shared column.
- **Deep nesting:** Recursive code is clear, but an extremely deep structure may exceed the JavaScript call-stack limit.
- **Lexicographic order:** The header is sorted once; insertion order from objects, arrays, or the set does not determine final column position.
- **No mutation of input:** The traversal reads input structures and constructs separate flattened rows and a separate matrix.
