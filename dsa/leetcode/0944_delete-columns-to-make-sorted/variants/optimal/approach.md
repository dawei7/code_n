## General

**Read the strings as a grid**

All strings have the same length, so placing one string on each row produces a rectangular grid. A column is formed by fixing one character index and reading that character from the first string down to the last string.

The task is not asking whether the rows are sorted relative to one another as complete strings. It asks whether each individual vertical column is lexicographically non-decreasing. A column must be deleted when some lower character is smaller than the character directly above it.

The solution names `m = len(strs[0])` as the number of columns, `n = len(strs)` as the number of rows, and `ans` as the number of bad columns found so far. The equal-length guarantee makes every access `strs[i][j]` valid.

**Why every column can be decided independently**

Deleting one column does not alter the vertical order inside any other column. It also does not move characters between columns. Therefore, whether column `j` is sorted depends only on the characters at index `j`.

There is no optimization involving combinations of columns. Every unsorted column must be deleted, every sorted column can remain, and the answer is simply the number of unsorted columns.

**Why adjacent comparisons are sufficient**

For fixed column `j`, the required condition is:

`strs[0][j] <= strs[1][j] <= ... <= strs[n - 1][j]`.

A sequence is non-decreasing exactly when every adjacent pair is non-decreasing. If all adjacent comparisons hold, transitivity gives the full ordering. Conversely, whenever a column is not non-decreasing, walking downward must eventually cross an adjacent boundary where the next character is smaller.

The inner loop begins at row one because row zero has no row above it. It tests `strs[i][j] < strs[i - 1][j]`. If true, the current character is smaller than the character above and the column is invalid.

**Why equality is allowed**

The order is non-decreasing, not strictly increasing. A column such as `['a', 'a', 'c']` is sorted because no value goes backward.

That is why the failure test uses strict less-than. Using `<=` would incorrectly delete columns containing equal adjacent letters.

**Why `break` is necessary**

Once the algorithm finds one descending pair, it increments `ans` and stops scanning that column.

The answer counts columns, not violations. A single column might contain several descents, but deleting it once removes all of them. Continuing to scan and incrementing again would overcount.

The early exit also saves work. No characters below the first violation can make the column sorted again.

**Detailed trace**

Consider `strs = ["cba", "daf", "ghi"]`.

- Column zero contains `c, d, g`. Both adjacent steps are non-decreasing, so it remains.
- Column one contains `b, a, h`. At the first comparison, `a < b` is true. The answer becomes one and scanning this column stops.
- Column two contains `a, f, i`. Both downward steps are non-decreasing, so it remains.

The method returns one.

For `["zyx", "wvu", "tsr"]`, each column has a descent from the first row to the second. Each contributes once, giving three.

For `["a", "b"]`, the only column reads `a, b`. It is sorted, so the result is zero.

**Why the result is correct**

Take any column counted by the algorithm. The code observed an adjacent descent, which proves that column is not sorted and must be deleted.

Now take any column not counted. The inner loop examined every adjacent pair and found no descent. Hence the entire vertical sequence is non-decreasing and does not need deletion.

The algorithm therefore counts all and only the columns that must be deleted. Because column decisions are independent, this count is the correct answer.

## Complexity detail

Let `r` be the number of strings and `c` their common length.

There are `c` outer iterations. In the worst case, every column is sorted, so all `r - 1` adjacent pairs are checked. Time is `O(rc)`. Early exits help some inputs but do not change the worst-case bound.

Only dimensions, indices, and the counter are stored. No transposed grid, sorted copy, or collection is created, so auxiliary space is `O(1)`.

The input contains `rc` characters, but input storage is not additional algorithm memory.

## Alternatives and edge cases

- **Transpose the grid:** Construct columns with `zip` and compare each with a sorted copy. This allocates tuples and lists and performs unnecessary `O(r log r)` sorting per column.
- **Compare every pair of rows:** Testing all earlier-later pairs costs `O(r^2 c)`. Adjacent comparisons already prove the complete order through transitivity.
- **Count inversions:** The inversion count is irrelevant. A bad column contributes exactly one deletion regardless of how many violations it contains.
- **One row:** Every column has one character and is automatically sorted. The inner loop is empty.
- **One column:** It is deleted exactly when at least one adjacent row pair descends.
- **Equal adjacent characters:** Equality is valid under non-decreasing order.
- **All columns sorted:** The failure branch never runs and the answer stays zero.
- **All columns unsorted:** Every column increments the answer once, so the result equals the string length.
- **Complete-row order:** Rows may be globally unordered while their individual columns satisfy this problem. Whole-string comparisons would answer a different question.
- **Equal-length guarantee:** Direct indexing depends on it. Ragged strings would require a different contract.
