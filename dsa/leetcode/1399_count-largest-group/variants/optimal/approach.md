## General

**Use digit sum as the group key**

Every integer from one through $n$ belongs to exactly one group identified by the sum of its decimal digits. `cnt` maps each digit sum to the number of processed integers with that sum.

For each loop value `i`, the code initializes `s = 0` and repeatedly:

- Adds `i % 10`, the last decimal digit, to `s`.
- Applies `i //= 10` to remove that last digit.

When `i` becomes zero, `s` is the complete digit sum. For 14, the loop adds 4, changes `i` to 1, adds 1, and finishes with group key 5. Number 5 also has key 5, so both increment the same counter.

**Why changing the loop variable is safe in Python**

The digit loop destructively reduces local variable `i` to zero. This does not alter the `range` iterator or skip future numbers. At the start of the next `for` iteration, Python assigns the next range value to `i` afresh.

In a language where loop control depends on manually incrementing the same mutable variable, one would copy it to a temporary value before extracting digits. In this exact Python code, reassignment is safe.

**Maintain the maximum online**

After calculating digit sum `s`, `cnt[s] += 1` increases that group's size. Two scalar variables summarize all group sizes seen so far:

- `mx` is the largest current group size.
- `ans` is the number of groups whose current size equals `mx`.

If the updated group becomes strictly larger than `mx`, it is now the only group at this new record size. The code sets `mx = cnt[s]` and resets `ans = 1`.

If the updated group size equals `mx`, this group has just joined the set of largest groups, so `ans += 1`.

If its size remains below `mx`, neither summary changes.

**Why equality does not count the same group twice**

A group's size increases by exactly one whenever another number joins it. At a fixed current maximum $M$, a group reaches size $M$ only once. When it does, the equality branch adds that group once.

If some group later grows from $M$ to $M+1$, the strict branch establishes a new maximum and resets the answer to one, correctly discarding all groups still at the old size. Other groups are counted again only if they later reach the new maximum $M+1$. This is not double counting; the identity of the largest groups has changed.

**Tracing `n = 13`**

Numbers 1 through 9 initially create nine groups of size one. The first group sets `mx=1, ans=1`, and each of the next eight groups reaches the same maximum, eventually making `ans=9`.

Number 10 has digit sum one, so group one grows to size two. This creates a new maximum: `mx=2, ans=1`. Number 11 grows group two to size two, so `ans=2`. Numbers 12 and 13 do the same for groups three and four. The final answer is four, matching the groups `[1,10]` through `[4,13]`.

**Why online tracking is enough**

An alternative would fill the entire counter, call `max(cnt.values())`, and scan again to count matching groups. The online method produces the same summary during the one pass. Every counter update immediately reconciles `mx` and `ans` with the new multiset of group sizes.

**Invariant and correctness**

After processing integers one through $x$, `cnt[s]` is the exact size of digit-sum group $s$ among those integers. `mx` is the maximum of these sizes, and `ans` is the number of keys attaining it.

The digit extraction computes the correct key for $x+1$, and incrementing its counter preserves the first fact. Only that one group's size changes. The three comparison cases—above, equal to, or below the old maximum—update the other facts exactly as described. By induction, the invariant holds through $x=n$, so `ans` is the requested number of largest groups.

## Complexity detail

Let $d$ be the number of decimal digits in $n$. Extracting the digits of one integer takes at most $O(d)$ time. Repeating for all $n$ integers gives $O(nd)$ time, matching the manifest. Since $d=O(\log n)$, this can also be written $O(n\log n)$ in terms of $n$ alone.

The largest possible digit sum of a $d$-digit number is $9d$, so the counter has at most $9d+1=O(d)$ keys. The remaining variables use constant space. Total auxiliary space is $O(d)$, matching the manifest.

## Alternatives and edge cases

- **Two-pass counter summary:** Build all group sizes, then find the maximum and count its occurrences. It is equally correct and slightly simpler conceptually but scans counter values twice.
- **String conversion:** Compute `sum(int(c) for c in str(x))`. It is readable but allocates temporary string and iterator objects for each number.
- **Dynamic digit-sum recurrence:** Use the relationship between $x$ and $x-1$ while handling trailing nines. It can reduce repeated digit work but is more error-prone.
- **Fixed array of group counts:** Under $n\le10^4$, digit sums are small, so an array can replace `Counter`.
- **`n = 1`:** One group has one member, so the answer is one.
- **All groups tied at size one:** Each first occurrence triggers the equality branch and increases `ans`.
- **New unique maximum:** The strict branch resets `ans` because prior groups are no longer largest.
- **Later tie at the new maximum:** The equality branch adds exactly that newly tied group.
- **Digit sum zero:** The range starts at one, so no processed number belongs to group zero.
- **Powers of ten:** Zero digits contribute nothing; for example, 100 has digit sum one.
- **Mutated `i`:** Python's `for` loop safely assigns the next range element despite the inner reduction to zero.
- **Required import:** `Counter` must be available, normally from `collections`.
