## General

**Fix the ordered character pair first.** The alphabet contains only digits $0$ through $4$. The source tries every ordered pair $(a,b)$ with $a\ne b$. For this pair, it searches for a substring of length at least $k$ where $a$ occurs an odd number of times, $b$ occurs a positive even number of times, and

$$
\operatorname{count}(a)-\operatorname{count}(b)
$$

is maximized. Trying all $20$ pairs remains a constant factor.

The string is converted once to integer list `s`, so comparisons inside all scans avoid repeated character conversion.

**Express a substring through two prefixes.** At right endpoint `r`, `curA` and `curB` are counts in prefix `s[0..r]`. A boundary after index `l` has prefix counts `preA` and `preB` for `s[0..l]`. The substring `s[l+1..r]` has counts

$$
A=\texttt{curA}-\texttt{preA},\qquad
B=\texttt{curB}-\texttt{preB}.
$$

Its objective is

$$
(\texttt{curA}-\texttt{curB})
-
(\texttt{preA}-\texttt{preB}).
$$

For fixed right counts, maximize this by choosing the eligible prefix with the smallest `preA - preB`.

**Store the best prefix separately for four parity states.** `t[pa][pb]` is the minimum prefix difference among eligible boundaries whose $a$ count has parity `pa` and $b$ count has parity `pb`.

To make $A$ odd, prefix $a$ parity must be opposite `curA` parity. To make $B$ even, prefix $b$ parity must equal `curB` parity. Therefore, the required table entry is

`t[(curA & 1) ^ 1][curB & 1]`.

Subtracting that minimum from `curA - curB` gives the best valid difference ending at `r`.

**Admit a prefix boundary only when length and positive-even feasibility hold.** Initially `l = -1` and both prefix counts are zero, representing the empty prefix before index zero.

The while condition `r - l >= k` ensures substring `l+1..r` has at least $k$ characters. The condition `curB - preB >= 2` ensures it contains at least two copies of $b$. Parity is checked later through the table lookup; requiring at least two here excludes the forbidden zero even count.

When both conditions hold, the current prefix state is inserted into `t`. Then `l` advances by one and `preA`/`preB` are updated to the new prefix. Repetition admits every boundary that has become eligible.

Once a boundary is admitted, it remains eligible for all later right endpoints: substring length only grows, and the number of $b$ occurrences cannot decrease. Thus the table can keep its minimum permanently.

**Why the moving boundary does not miss anything.** For each `r`, the loop inserts all prefix boundaries whose candidate substring is long enough and has at least two $b$s. The four parity buckets preserve exactly the additional information needed later. Any valid substring corresponds to one such admitted prefix and will be evaluated when its right endpoint is processed.

Conversely, a finite table value used by the lookup comes from a boundary satisfying length and positive-$b$ requirements. The chosen parity bucket guarantees odd $A$ and even $B$. Every computed candidate is therefore valid.

The initial answer is negative infinity because all valid differences may be negative. The input guarantees at least one qualifying configuration, so a real candidate eventually replaces it.

For example, an odd current $a$ prefix requires an even stored $a$ prefix, while an even current $b$ prefix requires an even stored $b$ prefix. Their differences produce odd $a$ and even $b$ counts inside the substring.

In the source expression `curA & 1 ^ 1`, Python evaluates bitwise AND before XOR, so it means `(curA & 1) ^ 1`: take the current parity and flip it. Writing the parentheses explicitly would be clearer, but the implemented lookup is correct.

## Complexity detail

Let $n=\lvert S\rvert$. Converting the string uses $O(n)$ time and space. There are $20$ ordered digit pairs. For each, `r` advances $n$ times and `l` advances at most $n$ times, so the scan is $O(n)$. Total time is $O(20n)=O(n)$ under the fixed alphabet.

The prefix-parity table is constant-size, but the integer list `s` stores $n$ entries. Exact auxiliary space is therefore $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Enumerate all substrings:** This takes $O(n^2)$ endpoint pairs before frequency evaluation.
- **One unordered digit pair:** The objective is directional; swapping $a$ and $b$ negates the difference and swaps parity roles, so ordered pairs are necessary.
- **Parity without positivity:** Even parity alone includes zero occurrences of $b$. The `>= 2` admission condition enforces nonzero even frequency.
- **Length exactly \(k\):** `r - l >= k` includes it because `l+1..r` has length `r-l`.
- **Other digits:** They affect substring length but not the two prefix counts, exactly as required.
- **Negative optimum:** The answer must not be initialized to zero.
- **Prefix boundary \(-1\):** It correctly represents substrings starting at index zero.
- **Persistent table minima:** An admitted boundary remains length- and count-eligible as `r` moves right.
- **Same character:** Pairs with `a == b` are skipped because one frequency cannot be both odd and positive even.
- **Fixed alphabet:** The linear-time statement includes a constant factor of $5\cdot4$.
