## General

The solution counts how many rows have contributed each value. Two input guarantees make a simple global counter sufficient: every row is strictly increasing, so a value appears at most once in a row, and rows themselves are processed in order from top to bottom.

**Accumulate one occurrence per row automatically**

`cnt = Counter()` maps values to the number of occurrences processed so far. The nested loops visit each row and then each value `x` in that row, incrementing `cnt[x]`.

Ordinarily, a raw occurrence count would not prove that a value occurs in distinct rows. One row containing the same value several times could inflate the count. Strictly increasing rows rule this out: within a row, every value occurs at most once. Therefore, after processing some number of rows, `cnt[x]` is exactly the number of processed rows containing `x`.

**Return when the count reaches the row count**

Immediately after incrementing, the code tests

`if cnt[x] == len(mat): return x`.

Let $m$ be the number of rows. A count of $m$ cannot occur before every row has been processed for that value. Because each of the $m$ rows can contribute at most one, equality proves that `x` appears in all rows.

For $m>1$, no count can reach $m$ until the nested loop is processing the final row. The first $m-1$ rows supply at most $m-1$ occurrences. While scanning the final row, values appear in strictly increasing order. Therefore, the first value whose count reaches $m$ is the smallest value common to every row.

This early-return ordering is subtle. A hash counter by itself has no sorted iteration order that would identify the smallest key. The method does not iterate over counter keys; it relies on the final row’s sorted order to encounter common candidates from smallest to largest.

For a one-row matrix, every value is common to all one rows. The first value in that strictly increasing row immediately reaches count one, and it is also the row’s smallest value, so the same logic works without a special case.

**Following a small matrix**

For rows `[1, 2, 3]`, `[2, 3, 4]`, and `[2, 3, 5]`, the first row gives counts one for 1, 2, and 3. The second raises 2 and 3 to two. In the final row, value 2 is encountered first and its count becomes three, equal to the number of rows. The method returns 2 before examining 3, correctly choosing the smaller common element.

If no value occurs in all rows, no count reaches $m$. Both loops finish and the function returns `-1`.

**Why every possible outcome is correct**

Whenever the function returns a value, strict uniqueness within each row proves that its $m$ counted occurrences came from $m$ different rows. It is genuinely common.

Any common value receives one increment in each row, so its count will reach $m$ when the final row visits it. Thus a common value cannot be missed. Since the final row is increasing, the earliest common value that reaches the threshold is smaller than every later common value. If no threshold is reached, no value was present in all rows, making `-1` correct.

The approach does not use the within-row sorted order to accelerate counting through binary search; it uses ordering only for uniqueness and smallest-value early return. Every matrix entry may still be examined in the worst case.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns.

The nested loops inspect at most $mn$ entries. Each `Counter` increment and lookup is expected $O(1)$ hash-map work, so expected time complexity is $O(mn)$. Early return can reduce actual work when a small common value is found.

Let $u$ be the number of distinct matrix values processed before return. The exact `Counter` uses $O(u)$ auxiliary space, with $u\leq mn$. The value domain is constrained to integers from one through 10,000, so $u\leq 10{,}000$. If that fixed domain bound is treated as a constant, space is conventionally written $O(1)$; as a data-dependent description of the actual allocation, it is $O(u)$.

The method returns one integer and creates no output collection.

## Alternatives and edge cases

- **Fixed frequency array:** Allocate 10,001 integer slots indexed by value. This replaces hashing with direct access and makes the bounded-domain constant space explicit.
- **One pointer per row:** Repeatedly advance smaller row values toward the current maximum until all pointers agree or a row ends. This achieves $O(mn)$ time and $O(m)$ pointer space without value-domain storage.
- **Binary search candidates from the first row:** For each first-row value, search every other row. This uses constant extra space but costs up to $O(mn\log n)$ time.
- **One row:** The first element is common to all rows and is returned immediately.
- **One column:** A value is common only if every row’s sole entry is equal. Counts capture this directly.
- **No common element:** No count reaches the number of rows, so the final result is `-1`.
- **Several common elements:** They reach the threshold while the last row is scanned in increasing order; the smallest is returned first.
- **Strict row ordering:** It prevents one row from contributing the same value twice. With merely non-decreasing rows, the algorithm would need to skip duplicates within each row.
- **Counter order is irrelevant:** The algorithm never depends on hash-key iteration order. Smallest selection comes from final-row traversal order.
- **Expected hash performance:** The $O(mn)$ statement assumes expected constant-time `Counter` operations, which is the standard model for Python dictionaries.
