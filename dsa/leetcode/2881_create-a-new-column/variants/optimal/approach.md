## General

**Operate on the entire salary column as one labeled vector.** A pandas DataFrame column is a Series: a one-dimensional array of values paired with row-index labels. The expression `employees['salary']` selects that Series. Multiplying it by scalar two applies the arithmetic to every salary:

`employees['salary'] * 2`.

The result is another Series with the same index labels and one doubled value per employee.

**Assignment creates the new column.** The left side `employees['bonus']` names a column. Since `bonus` is not already present in the stated schema, assigning the doubled Series creates it. pandas aligns the right-hand Series to the DataFrame's index labels before storing values, so every bonus remains attached to the employee whose salary generated it.

The full statement is:

`employees['bonus'] = employees['salary'] * 2`.

Afterward, the source returns `employees`. The original columns remain in their existing order, and the newly created column is appended after them, producing `name`, `salary`, and `bonus`.

**Why vectorized arithmetic is the right abstraction.** A manual loop might read every row, calculate a bonus, and write it back. pandas already stores the salary values in a column-oriented representation and supplies elementwise numeric operations implemented by the underlying array system. Expressing the transformation once is shorter, clearer, and usually faster than executing Python code once per row.

Vectorized does not mean the work disappears. Every salary still has to be multiplied. It means that pandas performs the repeated operation as a Series computation rather than requiring the solution to manage row iteration and index positions.
Take an employee at index label $\ell$ with salary $s$. Series multiplication produces value $2s$ at the same label $\ell$. Assignment aligns that label with row $\ell$ in `employees` and stores $2s$ in its `bonus` cell. The code does not alter the row's `name` or `salary`. Applying this argument to every row proves that the new column contains exactly doubled salaries and all original data is preserved.

For Piper's salary `4548`, the Series operation yields `9096`. Grace's `28150` yields `56300`. These calculations occur independently, so row order does not affect the result.

**The function mutates its input DataFrame.** This implementation does not call `copy` and does not construct a replacement DataFrame before assignment. The `employees` object supplied by the caller gains a `bonus` column. Returning it makes the modified table the function result. This side effect matches the simple challenge workflow, but it matters in reusable code: another reference to the same DataFrame can observe the added column.

If a `bonus` column already existed despite the stated input schema, the assignment would replace its values instead of adding a second column with the same name. pandas column selection by a unique label treats assignment as create-or-overwrite.

**Index alignment protects row identity.** Both the salary Series and the destination DataFrame originate from the same object, so their indexes match exactly. pandas alignment makes the intent robust even with nonconsecutive labels such as `10, 20, 30`. The computation does not assume a default zero-based index.

**Data type behavior.** With integer salaries, multiplying by integer two normally yields an integer Series of a compatible width. Fixed-width numeric dtypes can overflow if values exceed their representable range, but the task's valid data is expected to fit pandas' inferred or supplied type. Missing salaries would propagate as missing bonuses; the stated schema presents integer salary data rather than asking for missing-value treatment.

**Column creation preserves rectangular shape.** The row count does not change: one bonus value is produced for every existing row. The column count increases from two to three. This makes the transformation different from appending a bonus record as a new row, which would corrupt the table's meaning.

## Complexity detail

Let $n$ be the number of employees. The vectorized multiplication processes $n$ salary values and assignment stores $n$ bonus values, so time is $O(n)$. The result Series and new DataFrame column require $O(n)$ additional storage. The manifest's $O(n)$ time and $O(n)$ space accurately describe the exact implementation.

The Python function itself uses no explicit loop or growing helper collection, but pandas must allocate the computed column. Complexity measures underlying work and storage, not merely the number of source-code lines.

## Alternatives and edge cases

- **`assign` method:** `employees.assign(bonus=employees['salary'] * 2)` returns a transformed DataFrame and is convenient in method chains, but the exact source deliberately mutates `employees`.
- **Row-wise `apply`:** Applying a lambda per value is more flexible but adds Python-level overhead for simple scalar multiplication.
- **Manual loop:** It is verbose, slower in pandas, and risks confusing positional and label indexes.
- **Empty DataFrame:** Assignment creates an empty `bonus` column with no rows, preserving the requested schema.
- **Custom row index:** Series alignment keeps doubled values attached to the correct labels.
- **Existing `bonus` column:** It would be overwritten, not duplicated.
- **Missing salary:** Standard numeric multiplication propagates missingness; this problem does not request filling it.
- **Input mutation:** Callers needing the original unchanged should copy first, because this source modifies the provided object.
