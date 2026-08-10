## General

**Convert rank to factorial-number-system choices**

The permutations with a fixed first digit form blocks of $(n-1)!$. A zero-based rank divided by that block size gives the index of the first digit among the remaining sorted digits. The remainder gives the rank inside the selected block.

The competitive source begins with `k - 1` because the problem supplies a one-based rank. It creates `perm = [1,2,...,n]` and initializes `fact = (n-1)!`. At each position, it selects `perm[k / fact]`, removes that digit, reduces `k` modulo the block size, and updates `fact` for the next suffix length.

**Why zero-based division is convenient**

Suppose each block has size 6. Zero-based ranks 0 through 5 belong to block index 0, ranks 6 through 11 belong to block index 1, and so on. Integer quotient `k // 6` identifies the block directly, while `k % 6` identifies the offset inside it.

This avoids a loop subtracting one block at a time. The selected block index is always valid because `k` is smaller than the number of remaining permutations and division by the suffix factorial yields a value smaller than the count of remaining digits.

**Meaning of reverse loop variable `i`**

`reversed(range(n))` produces `n-1, n-2, ..., 0`. Before selecting a position, `i` is the number of digits that will remain after that selection, and `fact` equals `i!`.

After a digit is removed, if `i > 0`, `k %= fact` keeps the within-block rank. Then `fact /= i` transforms $i!$ into $(i-1)!$, the block size needed after the next digit selection. At `i == 0`, no suffix remains and division is skipped.

**Trace for the ninth permutation of four digits**

Start with zero-based `k = 8`, remaining digits `[1,2,3,4]`, and `fact = 6`. Integer quotient $8/6=1$ selects digit 2. The remainder is 2, and the next factorial is 2.

Then $2/2=1$ selects the second remaining digit, 3. The remainder becomes 0 and the next factorial is 1. Quotients of zero select 1 and then 4, giving `"2314"`.

**Removing a digit preserves lexicographic candidates**

`perm` remains sorted after `remove(curr)` because deletion does not reorder the other elements. The next quotient therefore indexes remaining candidate digits in lexicographic order. `seq` receives each chosen digit exactly once.

The contract restricts `n` to 9, so converting each digit to a string and concatenating creates an unambiguous length-$n$ result.

**The factorial-block invariant**

Before each iteration, `seq` is the target prefix, `perm` is the sorted list of unused digits, `k` is a valid zero-based rank among permutations of `perm`, and `fact` is the number of arrangements for each possible next digit.

The quotient selects the only block containing the rank. Removing that digit fixes the next prefix position. The remainder is exactly the rank within that block, and dividing the factorial prepares the next block size. Induction carries the invariant until no digits remain, proving the final string has the requested rank.

**Python 3 incompatibility of the exact source**

The file uses `/` for `k / fact` and `/=` for `fact /= i`. In Python 2, integer operands produce integer division, which is the intended factorial-index algorithm. In Python 3, `/` produces a float. The very first `perm[k / fact]` therefore attempts to index a list with a float and raises `TypeError`.

The intended Python 3 operators are `//` and `//=`. This documentation does not modify the protected source, so the exact branch must be regarded as Python 2-targeted and non-executable unchanged under Python 3.

## Complexity detail

There are $n$ selections. Indexing is constant time, but `perm.remove(curr)` searches for and shifts elements in a list, costing $O(n)$ per selection in the worst case. Repeated immutable-string concatenation can also copy a growing prefix. Total time is $O(n^2)$, matching the manifest under intended integer-division semantics.

The remaining-digit list holds $O(n)$ integers, and the output string grows to length $n$. Other variables are scalar, so space is $O(n)$, matching the manifest. The Python 3 failure occurs before valid traversal but does not change the intended algorithmic bounds.

## Alternatives and edge cases

- **Use Python 3 floor division:** Replacing `/` with `//` and `/=` with `//=` preserves the intended integer block indices.
- **One-based block subtraction:** Scan unused digits and subtract factorial blocks until the target block is reached. It avoids division-version ambiguity and is the optimal branch's style.
- **Precompute all factorials:** Store values from $0!$ through $n!$ for direct access. This uses $O(n)$ additional space but simplifies updates.
- **Generate all permutations:** It performs factorial work and stores or visits far more results than necessary.
- **Order-statistics structure:** It can support selection and deletion faster than a Python list, but is unnecessary for $n \le 9$.
- **`k = 1`:** Zero-based rank is 0, so every quotient selects the first remaining digit.
- **`k = n!`:** The zero-based rank is the final valid index and repeatedly selects the last possible blocks.
- **`n = 1`:** `fact = 0! = 1`, index 0 is selected, and no factorial update occurs.
- **Python 3 runtime:** Float list indices cause immediate failure; this is a source compatibility defect, not a mathematical ambiguity.
- **Local state:** Rebinding `k`, `fact`, and `seq` does not mutate caller-owned objects.
