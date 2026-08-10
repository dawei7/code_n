## General

**Only missing names determine row removal.** A student row should be removed when its `name` entry is missing. Missing data in another column is irrelevant to this task. The exact solution creates a Boolean mask from that one Series:

`students['name'].notnull()`.

It then uses the mask to filter the entire DataFrame:

`students[students['name'].notnull()]`.

**What `notnull` means.** pandas recognizes several missing-value sentinels, including Python `None`, floating-point `NaN`, and pandas' nullable `NA` where supported. `notnull()` returns `False` at missing positions and `True` at values pandas considers present.

The method name is read literally: “is this value not null?” A present name such as `"Piper"` yields true and is kept. A missing `None` yields false and is removed.

An empty string `""` is ordinarily a present string, not a null marker, so this exact expression would keep it. The task speaks about missing values rather than blank-text validation, making that behavior appropriate.

**Boolean indexing keeps complete valid rows.** The mask has one Boolean per input row and the same index labels as the `name` Series. Placing it inside `students[...]` selects every row whose mask value is true. pandas returns all original columns for those rows: `student_id`, `name`, and `age`.

This is important because the code is not selecting only the non-null name Series. It uses that Series to decide which whole student records survive. The corresponding identifier and age remain attached to each retained name.
Consider any row $r$. If `name[r]` is missing according to pandas, `notnull` produces false, so Boolean indexing excludes $r$. If the name is present, the predicate produces true and the complete row is included. Therefore no row with a missing name survives and no row with a present name is removed. Since the operation retains all columns and preserves row order, the returned DataFrame is exactly the requested cleaned table.

In the example, Piper, Georgia, and Willow produce true mask entries. The row with identifier 217 and name `None` produces false. The result contains the three true rows in their original relative order.

**The exact source differs from the editorial form.** The editorial demonstrates `dropna(subset=['name'], inplace=True)`. That operation has equivalent row-selection semantics on valid input, but the checked-in source uses `notnull` plus Boolean indexing and does not mutate in place. The approach should explain the executable expression rather than substitute the editorial's API call.

**Original index labels are preserved.** If the removed row had index one, returned indexes might be `0, 2, 3`. The challenge display usually hides pandas' index, and it does not request a reset. Preserving those labels is normal filtering behavior and does not mean an extra row was retained.

**The input is not modified.** Boolean indexing returns a filtered DataFrame object. The source does not assign back into `students` and does not pass `inplace=True`. Code holding the original reference still sees the missing-name rows. This contrasts with the editorial's in-place example.

**Why filtering must inspect every row.** Even if a missing value appears early, later rows may be valid and must be returned. The algorithm cannot stop at the first null. Vectorization lets pandas perform the full scan efficiently but does not change the need to evaluate all $n$ names.

**Missingness is a semantic test, not text comparison.** Comparing names only with `None` would miss floating `NaN` and pandas `NA`. Comparing string representations such as `"None"` would be worse because it could delete a legitimate name containing those characters. `notnull` delegates recognition to pandas' dtype-aware missing-value system.

**Filtering does not repair the rejected record.** The row is removed as a whole rather than receiving a placeholder name. This matters because identifiers and ages from a nameless record must not remain in the cleaned result. The Boolean mask applies one keep-or-drop decision to all columns of that row.

## Complexity detail

Let $n$ be the number of students and $h$ the number of retained rows. `notnull` scans the name column and builds a Boolean Series in $O(n)$ time and $O(n)$ space. Applying the mask also examines $n$ decisions and creates an output containing $h$ rows. With a fixed three-column schema, total time is $O(n)$ and worst-case additional or result storage is $O(n)$.

These are the exact source's real bounds and match the manifest. The input's string payload is not transformed; rows are selected based on missingness metadata.

## Alternatives and edge cases

- **`dropna(subset=['name'])`:** This directly expresses row removal based on one column and returns a new DataFrame when `inplace` is omitted.
- **Editorial in-place version:** It changes the supplied object, unlike the protected Boolean-filter source.
- **Missing values in `age`:** They do not cause removal because the predicate examines only `name`.
- **Empty string:** It is not normally considered null and remains in the result.
- **Every name present:** All rows survive, although pandas still builds the mask and result.
- **Every name missing:** The result is an empty DataFrame with the same three columns.
- **Custom index:** Filtering preserves surviving labels and does not reset them.
- **Multiple null representations:** `notnull` handles pandas-recognized `None`, `NaN`, and nullable missing markers consistently.
