## General

**Frequency determines the unavoidable number of rows**

No row may contain the same integer twice. If a value $x$ occurs $f_x$ times in `nums`, its copies must occupy $f_x$ different rows. Therefore, every valid answer needs at least

$$
R=\max_x f_x
$$

rows. This is a lower bound: regardless of how other values are arranged, the most frequent value alone forces that many rows.

The central task is to show that exactly $R$ rows are also sufficient. The solution does so by placing the first copy of every distinct value in row zero, the second copy in row one, and in general the occurrence numbered $i+1$ in row $i$.

**Count first, then distribute**

`Counter(nums)` creates a mapping from each distinct value `x` to its frequency `v`. The answer starts as an empty list of rows.

For one mapping entry `x, v`, the inner loop visits row indices

$$
0,1,\ldots,v-1.
$$

At each index `i`:

- if row `i` does not exist yet, append a new empty row;
- append `x` to row `i`.

Thus a value occurring $v$ times appears once in each of the first $v$ rows. It can never appear twice in one row because the inner loop visits each row index only once for that value.

**Why rows are created exactly when needed**

The condition `len(ans) <= i` means the requested row index is not yet present. Since `i` grows from zero upward without gaps, appending one row makes index `i` valid immediately.

Suppose the values processed so far have maximum frequency $M$. The answer then contains exactly $M$ rows. Processing a new value with frequency $v$ creates rows only for indices already at or beyond $M$, so the new count becomes $\max(M,v)$. After every distinct value has been processed, the number of rows is exactly $\max_x f_x=R$.

The construction therefore meets the lower bound proved earlier. It is not merely valid; it uses the minimum possible number of rows.

**Why each input occurrence is used exactly once**

For each distinct value `x`, the inner loop executes exactly `cnt[x]` times and appends `x` once per execution. Therefore, the output contains exactly as many copies of `x` as the input.

Summing over all distinct values, the number of appended elements is

$$
\sum_x f_x=n.
$$

No new numerical value is invented, and no input occurrence is lost. Although identical copies are indistinguishable, their multiplicities are preserved exactly, which is the relevant meaning of containing only the elements of `nums`.

**Why every row is distinct-valued**

Fix a row index $i$. A particular value $x$ reaches row $i$ only during the single inner-loop iteration for that $x$ with loop index $i$. The outer mapping itself has one entry per distinct value. Consequently, $x$ can occur in row $i$ at most once.

Different mapping entries have different keys, so all elements appended to one row are distinct. No comparisons against existing row contents are required; the placement rule guarantees uniqueness structurally.

**Trace the first example**

For `nums = [1,3,4,1,2,3,1]`, the frequencies are:

- one occurs three times;
- three occurs twice;
- four and two occur once each.

Processing one creates rows zero, one, and two and places one in each. Processing three adds it to rows zero and one. Four and two go only to row zero. One possible result is therefore `[[1,3,4,2],[1,3],[1]]`.

There are three rows because the frequency of one is three. Fewer than three could not separate all copies of one, so the output is minimal.

When all values are distinct, every frequency is one. The only inner-loop index is zero, so the solution creates one row and places every input value into it.

**Output order and “any answer”**

The contract permits any valid arrangement. In modern Python, `Counter` preserves the order in which distinct keys first appear, so values generally occur in that order within the generated rows. Correctness does not depend on this order.

The construction does not preserve the original global sequence of occurrences, nor does the problem ask it to. It preserves the multiset of values, row distinctness, and minimum row count—the three required properties.

**A useful layered interpretation**

Imagine drawing one column for every distinct value, with its copies stacked vertically. Row zero takes the bottom copy from every nonempty column, row one takes the next copy from every column tall enough, and so on.

The height of the tallest column is the maximum frequency $R$, explaining the row lower bound visually. Each horizontal layer contains at most one copy from each column, explaining row distinctness. The code constructs exactly these horizontal layers.

## Complexity detail

Let $n$ be the length of `nums` and $d$ the number of distinct values. Building `Counter` takes expected $O(n)$ time and stores $O(d)$ entries.

Across all mapping entries, the inner loops execute $\sum_x f_x=n$ times. Row creation is constant time per new row, and each append is amortized $O(1)$. Total expected running time is therefore $O(n)$.

The returned 2D array necessarily stores all $n$ elements and uses $O(n)$ output space. The frequency mapping adds $O(d)$ auxiliary space, bounded by $O(n)$. If output storage is excluded from auxiliary-space accounting, the extra working space is $O(d)$; the manifest reports the conventional overall $O(n)$ bound.

## Alternatives and edge cases

- **Process occurrences online:** Track the count already seen for each value and put the next copy directly into the row with that index. This also runs in $O(n)$ time and avoids a separate counting pass.
- **Repeatedly build sets:** Removing one distinct copy of every remaining value per round works conceptually but may rescan data and become quadratic.
- **Sort the array:** Equal values become grouped, but sorting adds $O(n\log n)$ time and is unnecessary.
- **All values distinct:** Maximum frequency is one, so exactly one row is produced.
- **All values equal:** Every row contains one copy, and the number of rows equals $n$.
- **Several values share the maximum frequency:** They coexist once per row across all $R$ rows without conflict.
- **Unequal row lengths:** Shorter-frequency values stop appearing in later rows, which the contract explicitly allows.
- **Input order:** The output need not reproduce it; only multiplicities and row validity matter.
- **Nonempty input:** At least one mapping entry exists, so the result always contains at least one row.
- **Input preservation:** `Counter` reads `nums`, and the construction never mutates the original array.
