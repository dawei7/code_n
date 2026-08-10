## General

**Turn the displayed word into independent run-length choices.** A maximal run of $L$ equal displayed characters could have come from an intended run of any length $1$ through $L$. For example, displayed `"aaaa"` permits intended run lengths one, two, three, or four. Choices for different runs are independent because a long press never changes the character or crosses a boundary between different letters.

The source scans `word` and accumulates current run length `cur`. At a run boundary, it multiplies `ans` by `cur` when `cur > 1`. Length-one runs have one choice and do not change the product. Thus `ans` becomes the total number of possible originals of every length, modulo $10^9+7$.

**Separate one mandatory character per run from optional extras.** Every original must contain at least one character from each displayed run. The source decrements local `k` once per completed run. After the scan, this mutated value is

$$
K-R,
$$

where $K$ is the requested minimum original length and $R$ is the number of displayed runs. It is the number of additional characters, beyond the mandatory one per run, needed to reach length $K$.

A run of displayed length $L>1$ can contribute from zero through $L-1$ optional extra intended characters. The source stores capacity `L - 1` in `nums`. Length-one runs have capacity zero and need not enter the DP.

If the residual requirement is below one, even the shortest possible original—one character per run—already has length at least $K$. Every one of the `ans` possibilities is valid, so the early return is exact.

**Count and subtract originals that are still too short.** When residual `k` is positive, define `f[i][j]` as the number of ways to choose exactly $j$ optional extras from the first $i$ positive-capacity runs. Base `f[0][0] = 1` represents choosing no extras from no runs.

For current capacity $x$, a valid choice adds $q$ extras for any $0\le q\le x$. Therefore

$$
f[i][j]=\sum_{q=0}^{\min(x,j)}f[i-1][j-q].
$$

Only totals below residual `k` matter because they describe invalid originals shorter than $K$. The table has columns zero through `k - 1`.

**Use prefix sums for each range transition.** `s = list(accumulate(f[i - 1], initial=0))` creates an exclusive-style prefix array: `s[r]` is the sum of previous-row columns before $r$. The relevant previous indices are $j-\min(x,j)$ through $j$. Their sum is

`s[j + 1] - s[j - min(x, j)]`.

Adding the modulus before the remainder keeps Python's subtraction nonnegative in the intended residue system.

After all capacity runs, `sum(f[m][j] for j in range(k))` counts every original whose optional-extra total is less than the residual requirement. Subtracting these invalid choices from the all-length product leaves exactly originals of length at least the original $K$.

**Why the subtraction partitions all possibilities.** Every original corresponds uniquely to one chosen intended length for every run, equivalently one optional-extra count per run. Its total is either below the residual threshold or at least it, never both. `ans` counts the entire product space, and the DP counts precisely the below-threshold subset, so modular subtraction is correct.

**The source mutates the local parameter `k` but not caller state.** Integers are immutable bindings, so decrementing `k` only changes the method's local name. It is important, however, to interpret later table width and early-return checks as using the residual requirement, not the original argument.

**Actual storage is not compressed.** The editorial describes retaining one or two rows, but the exact source creates `m + 1` rows of length residual `k`. Since $m< K$ whenever DP is needed, this is $O(k^2)$ space in the worst case, contradicting the manifest's $O(k)$ claim.

## Complexity detail

Scanning runs costs $O(n)$. When DP is required, both the number of recorded runs and the residual threshold are $O(K)$, where original $K\le2000$. Each row builds a prefix array and fills $O(K)$ columns, for $O(K^2)$ time. Total time is $O(n+K^2)$.

The exact two-dimensional table uses $O(K^2)$ entries, and each temporary prefix array uses $O(K)$. `nums` uses $O(K)$. Peak auxiliary space is therefore $O(K^2)$, not the manifest's $O(K)$.

## Alternatives and edge cases

- **Rolling one-row DP:** Only the previous row is needed, so replacing `f` after each run reduces space to $O(K)$ and matches the manifest.
- **No minimum-length filter:** The simple product of run lengths already counts all possible originals.
- **Number of runs at least $K$:** Every original has at least one character per run, so all choices qualify and DP is skipped.
- **All characters distinct:** Every run has length one, the product is one, and the only possible original is the displayed word.
- **One long run:** Intended lengths one through its displayed length are filtered directly by $K$ through the DP.
- **Optional extra zero:** It represents choosing intended length one for that run and is included in the recurrence.
- **Modulo subtraction:** Python's final `% mod` returns the correct nonnegative residue even when invalid count is numerically larger than the stored residue.
- **Large displayed length:** Run scanning is linear and stores only one capacity per repeated run.
- **Length-one runs:** They reduce the residual requirement but do not create DP choices.
- **Run choice independence:** Adjacent different characters cannot merge because shortening a long press never changes character identity.
- **Local `k` meaning:** After scanning, it is extras still needed, not the original minimum length.
- **Manifest discrepancy:** The exact table is quadratic-space; only a rolling implementation is $O(K)$ space.
