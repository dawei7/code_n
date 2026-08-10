## General

**“First” means current row order.** The task does not ask for the three smallest employee identifiers or any other sorted subset. It asks for the first three rows as the DataFrame is presently ordered. pandas provides `DataFrame.head(n)` specifically for this prefix-selection operation.

The exact solution is `employees.head(3)`. Argument three says that at most row positions zero, one, and two in the current ordering should be returned. No explicit sorting, filtering condition, or loop is needed.

**What `head` preserves.** The returned object remains a DataFrame. It keeps every input column in the same order, including `employee_id`, `name`, `department`, and `salary`. It also preserves the selected rows' original index labels. If the input index happened to be `[10, 20, 30, ...]`, the result's index would remain `[10, 20, 30]` rather than being automatically reset to zero through two.

Values and dtypes are not transformed. Integer salary values stay salaries; object-valued names and departments stay in their columns. The method only changes which row positions are exposed in the result.

**Why “at most” three matters.** `head(3)` behaves safely when the DataFrame has fewer than three rows. With two rows it returns both; with no rows it returns an empty DataFrame carrying the same columns. It never invents placeholder records to reach a length of three. Under ordinary examples with at least three employees, it returns exactly three.
Let the ordered input rows be $R_0,R_1,\ldots,R_{r-1}$. The required output is

$$
R_0,R_1,R_2
$$

when $r\ge3$, or all available rows when $r<3$. By pandas' definition, `head(3)` returns the first $\min(3,r)$ rows. It therefore returns exactly this sequence and no later row. Since it retains all columns, the result satisfies the complete table contract.

In the example, Bob, Alice, and Tatiana are the first three records. Annabelle is fourth, so the method stops before that row. It does not matter that employee identifiers `3`, `90`, and `9` are not numerically sorted; row position, not identifier value, defines the prefix.

**Why bracket slicing is less expressive.** `employees.iloc[:3]` or even `employees[:3]` can also select a prefix. `head(3)` states the intention in library vocabulary and avoids ambiguity between label-based and positional slicing. A reader immediately knows this is a preview-sized prefix.

**Returned object versus input mutation.** The source does not call an in-place method and does not delete later rows from `employees`. It returns a DataFrame representing the requested slice. pandas' internal memory sharing or copying can vary with version and copy-on-write behavior, so callers should reason about it as a returned table, not depend on undocumented buffer aliasing.

**Why no full scan is needed.** The DataFrame already has ordered row storage and index metadata. Selecting a fixed prefix can be described by a slice boundary. pandas does not need to test all later rows against a predicate, because their contents cannot change whether they are among the first three.

This is a small task, but it reinforces the distinction among three common DataFrame operations: `head` selects by position, boolean indexing selects by a condition, and `sort_values` changes order according to data. Only the first is requested here.

**The default argument is not enough.** Calling `employees.head()` without an argument would return five rows by default. Supplying `3` is therefore essential rather than decorative. The method name captures the prefix operation, while its argument captures the exact output limit required by this problem.

## Complexity detail

Relative to the number $r$ of input rows, selecting a fixed three-row prefix is $O(1)$. The result contains at most three rows. With the contract's fixed four columns, its size is also constant, so additional result space is $O(1)$ with respect to $r$.

In a generalized DataFrame with variable column count $c$, constructing result metadata or materializing the selected cells may be described as $O(c)$ time and space because there are up to $3c$ cells. Here the schema fixes $c=4$, so the manifest's $O(1)$ time and space are appropriate. The complexity does not include creation of the already supplied input DataFrame.

## Alternatives and edge cases

- **`iloc[:3]`:** This is also positional and correct, but `head(3)` communicates “first rows” more directly.
- **`employees[:3]`:** It often works as row slicing, yet explicit `head` avoids indexing-semantics ambiguity.
- **Sorting by identifier first:** That would change the meaning of “first” and produce the wrong output when input order differs from identifier order.
- **Fewer than three rows:** `head(3)` returns every available row without error.
- **Empty DataFrame:** It returns an empty DataFrame with the original column schema.
- **Custom index labels:** Labels are preserved; the method selects by position and does not reset the index.
- **Duplicate index labels:** They do not affect positional prefix selection.
- **All columns retained:** The task asks to display rows, not project a subset of columns, so no column selection should be added.
