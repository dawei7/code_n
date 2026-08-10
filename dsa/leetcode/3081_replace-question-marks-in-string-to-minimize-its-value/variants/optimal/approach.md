## General

**Rewrite string value in terms of final frequencies.** If a letter appears $f$ times, its occurrences contribute:

$$
0+1+\cdots+(f-1)=\binom f2.
$$

Therefore the total string value depends only on how many times each letter appears, not on their positions. Adding one new occurrence to a letter currently appearing $f$ times increases value by exactly $f$.

This marginal-cost view determines which letters should replace question marks.

**Initialize a min-heap of letter costs.** `Counter(s)` counts fixed characters; the counter also has a `'?'` entry, but heap construction reads only `ascii_lowercase`.

Each heap entry is `(cnt[c], c)`. Python tuple ordering chooses the smallest frequency first and, on a frequency tie, the lexicographically smallest letter.

**Choose the replacement multiset greedily.** For every question mark, inspect heap minimum $(v,c)$. Appending $c$ costs $v$ additional value. After choosing it, that letter's frequency becomes $v+1$, so `heapreplace` removes the old minimum and inserts the updated pair in one operation.

Choosing the smallest current marginal cost is optimal because all future costs for a letter rise one at a time. If a solution chose a higher-cost letter while a lower-cost one remained available, exchanging that assignment could not increase and would usually decrease total value.

The result is a balanced distribution over letters relative to fixed frequencies.

**Separate value minimization from lexical minimization.** The heap produces the correct multiset of replacement letters, but the order in which it selected tied letters is not necessarily the lexicographically smallest placement in the original string.

Since total value depends only on final frequencies, the selected letters may be permuted among question-mark positions without changing value. The source sorts list `t`, then fills question marks from left to right. Placing the smallest available replacement at the earliest differing position gives the lexicographically smallest completed string.

**A trace.** For `"a?a?"`, fixed counts have a twice and every other letter zero. The two cheapest replacement letters are b and c. Sorting gives `["b","c"]`, and assigning in question-mark order produces `"abac"`.

For `"???"`, heap selects a, b, c because all start at zero and tuple ties choose letters. Sorted placement produces `"abc"`.
Marginal-cost greedy selects a replacement frequency distribution with minimum sum of binomial costs. Any permutation has that same minimum value. Among permutations, sorted letters placed at increasing question positions minimize the first position at which outputs can differ, hence give the lexicographically smallest minimum-value string.

**Exact time differs from the manifest.** The manifest states $O(N)$ time. Heap operations are over a fixed 26 entries, so their $O(\log26)$ factor is constant. However, `t.sort()` sorts up to $N$ individual replacement characters using Python's comparison sort, giving $O(Q\log Q)$ worst-case for $Q$ question marks. Thus exact worst-case time is $O(N+Q\log Q)=O(N\log N)$, even though a 26-count reconstruction could make sorting linear.

## Complexity detail

Counting, string scanning, conversion to a character list, and joining cost $O(N)$. $Q$ fixed-size heap replacements cost $O(Q)$ under the 26-letter bound. Sorting `t` costs $O(Q\log Q)$ worst-case. Total exact time is $O(N+Q\log Q)$.

`t`, `cs`, and the returned string use $O(N)$ space. Counter and heap are bounded by the alphabet and use $O(1)$ additional entries. Input string is immutable.

## Alternatives and edge cases

- **Count selected replacements by letter:** Store 26 chosen counts, then emit letters alphabetically into question positions. This avoids `t.sort()` and achieves true $O(N)$ time.
- **Fill heap choices immediately:** It preserves minimum value but can fail the lexicographically smallest tie-break because selected letters may need reordering.
- **No question marks:** `t` is empty and joining `cs` returns the original string.
- **All question marks:** Letters are distributed as evenly as possible, with earlier alphabet letters winning equal marginal costs.
- **Heavily frequent fixed letter:** Its high marginal cost delays choosing it until other letters catch up.
- **Value depends only on counts:** This is why sorting replacement positions afterward is safe.
- **Heap tie order:** Tuple second component prefers smaller letters.
- **Question-position order:** Left-to-right assignment makes the earliest characters as small as possible.
- **Counter question-mark entry:** It is ignored when building lowercase-letter heap entries.
- **Manifest mismatch:** Exact Python sorting makes worst-case time $O(N\log N)$, not strictly linear.
- **Why heap size stays 26:** `heapreplace` updates one existing letter entry rather than adding another, so every lowercase letter has exactly one current marginal-cost record.
- **Final frequencies, not occurrence history:** A letter's total contribution $\binom f2$ is independent of which specific occurrences were fixed versus substituted.
- **Sorting only chosen characters:** Fixed letters cannot move. Lexicographic minimization permutes replacements solely among the original question-mark positions.
- **Stable earliest difference:** If two assignments use the same replacement multiset, placing its sorted sequence left to right makes the first differing question position as small as possible, which decides lexicographic order.
