## General

**Reduce the sentence to word lengths**

Line breaks may be inserted only between words, and every pair of adjacent words kept on one row needs exactly one space. The letters themselves never change.

The source splits the sentence and stores each word length in `nums`. It then builds prefix sums `s` with an initial zero. For a half-open word interval from `i` through `j-1`, the letters occupy

`s[j] - s[i]`

characters. There are `j-i` words and therefore `j-i-1` internal spaces. The complete row length is

`s[j] - s[i] + j - i - 1`.

**Define the dynamic-programming state**

`dfs(i)` is the minimum cost of arranging words from index `i` through the final word, assuming word `i` begins a new row.

This state is sufficient because earlier rows affect the future only through the next unplaced word. Row costs do not otherwise interact.

The `@cache` decorator memoizes each starting index. Different earlier choices that leave the same suffix reuse one computed optimum.

**Handle the free final row first**

The length of all words from `i` through `n-1` on one row is

`s[n] - s[i] + n - i - 1`.

If this is at most `k`, the whole suffix can be the last row. The problem excludes the last row from total cost, so `dfs(i)` immediately returns zero.

This base case does more than stop recursion. It makes the algorithm prefer placing every remaining fitting word on the final free row rather than charging an unnecessary earlier break.

**Try every feasible non-final first row**

If the entire suffix does not fit, at least one break is necessary. The source lets `j` range from `i+1` upward, making the next row start at `j`. The current row contains words `i` through `j-1`.

Its length `m` is computed with the prefix formula. While `m<=k`, the candidate cost is

`(k - m) ** 2 + dfs(j)`.

The first term charges unused capacity on this non-final row. The recursive term is the best arrangement of everything after it.

Once `m>k`, adding still more positive-length words and spaces cannot make the row shorter, so the loop stops.

**Why the loop requires `j<n`**

When all remaining words fit, the earlier base case has already returned zero. When they do not fit, `j=n` would describe an invalid overlength row.

Thus the transition loop needs only `j<n`, ensuring at least one word remains for the suffix and avoiding charging a row that should instead be the cost-free last row.

**Trace the first example**

For `"i love leetcode"` and `k=12`, the word lengths are one, four, and eight.

At `dfs(0)`, all three words need fifteen characters including spaces, so they do not fit. Choosing `j=1` makes row `"i"` with cost `(12-1)^2`. Choosing `j=2` makes `"i love"` of length six with cost 36.

From `dfs(2)`, `"leetcode"` fits as the final row and costs zero. The second split therefore totals 36 and beats the first arrangement.

**Why the recurrence is complete**

Any valid arrangement beginning at word `i` has a unique first break after some word `j-1`. If the row is the final row, the base case represents it. Otherwise its length is at most `k`, so the loop considers that exact `j`.

After the break, the remaining decisions form precisely subproblem `dfs(j)`. Taking the minimum over every feasible first break therefore includes every valid arrangement.

**Why the recurrence is optimal**

For each chosen first row, its squared unused-space cost is fixed. By definition, `dfs(j)` is the minimum possible remaining cost. Replacing the suffix with anything more expensive cannot improve the whole arrangement.

Taking the minimum among these optimally completed first-row choices yields the optimum for `dfs(i)`. The zero-cost base case is clearly optimal whenever the suffix fits. Induction from later suffixes proves `dfs(0)` is the global minimum.

**Every word is guaranteed placeable**

The contract guarantees each individual word length is at most `k`. Therefore whenever the suffix does not fit, the loop has at least the one-word row `j=i+1` as a feasible transition.

`ans` cannot remain infinity on valid input.

## Complexity detail

Let $W$ be the number of words. There are at most $W$ memoized states. In the worst case, each state tries $O(W)$ following break positions, so time is $O(W^2)$.

Word lengths, prefix sums, and cached results use $O(W)$ space. Recursion can also reach depth $O(W)$, so total auxiliary space remains $O(W)$. Splitting the sentence additionally materializes its words, whose total characters are bounded by the input length.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** Fill minimum suffix costs from right to left and avoid recursive call depth.
- **Greedy fullest row:** Not always optimal because squared slack can favor redistributing words across earlier rows.
- **Enumerate all line-break subsets:** Exponential; memoization collapses arrangements sharing a suffix.
- **One word:** It is the final row and costs zero.
- **Entire sentence fits:** The base case returns zero immediately.
- **Word length exactly `k`:** It forms a full row with zero slack cost even when non-final.
- **Last row slack:** Never charged, regardless of how much unused capacity remains.
- **Single spaces:** The `j-i-1` term counts exactly the internal separators.
- **No leading or trailing row spaces:** The length formula includes only spaces between words.
- **Long suffix:** The transition stops as soon as row length exceeds `k`.
- **Guaranteed word fit:** Ensures every nonterminal state has a legal first-row choice.
- **Input preservation:** The source builds lengths without modifying the sentence.
