## General

**Choose the unique mismatch first**

Every valid pair of substrings differs at exactly one aligned position. If that mismatch occurs at `s[i]` and `t[j]`, then every chosen aligned character to its left and right must match.

The source turns this observation around. It examines every position pair $(i,j)$. Only when `s[i] != t[j]` does it treat that pair as the required mismatch and count all matching extensions around it.

This gives each valid substring pair a unique center of responsibility: its one differing aligned position. Pairs with zero mismatches are never counted because no unequal center exists, and pairs with two or more mismatches cannot be created by extending only through equal neighbors.

**Find the maximal matching extension to the left**

`l` starts at zero. The first while loop looks one position left of the mismatch, then two positions left, and so on:

`s[i - l - 1] == t[j - l - 1]`.

The boundary checks `i > l` and `j > l` ensure both indices remain non-negative. Each successful comparison increments `l`. When the loop stops, `l` is exactly the number of consecutive equal aligned character pairs immediately to the left of $(i,j)$.

The extension must be consecutive. A later matching character beyond another mismatch cannot be included, because a substring reaching it would contain at least two differences.

**Find the maximal matching extension to the right**

`r` is initialized alongside `l` and the second while loop checks positions one step right, two steps right, and onward. Its bounds

`i + r + 1 < m` and `j + r + 1 < n`

keep both strings in range. It increments `r` only while the corresponding characters match.

Afterward, `r` is the number of consecutive equal aligned pairs immediately to the right of the chosen mismatch.

**Why the contribution is `(l + 1) * (r + 1)`**

A counted substring pair must include positions $i$ and $j$, because those positions provide its one difference.

Its left boundary may start directly at the mismatch or include 1, 2, through `l` matching positions to the left. That gives `l + 1` choices.

Independently, its right boundary may end directly at the mismatch or include 1, 2, through `r` matching positions to the right. That gives `r + 1` choices.

Every left choice can be combined with every right choice, so the multiplication principle gives

$$
(l+1)(r+1)
$$

valid pairs centered on this mismatch.

For instance, if two matching characters are available on the left and one on the right, there are three possible starts and two possible ends, giving six substring pairs. Every resulting pair contains the central unequal characters and only equal aligned characters elsewhere.

**Why positions, not just substring text, define ways**

The loops use concrete start positions in `s` and `t`. Identical substring text occurring at different positions represents different choices and is counted separately, as the examples require. The formula counts boundary-position combinations rather than deduplicating textual values.

Likewise, the same substring in `s` can pair with several occurrences in `t`; each has a different $(i,j)$ alignment or boundaries and contributes separately.

**A short trace**

For `s = "ab"` and `t = "bb"`:

- At $(i,j)=(0,0)$, `a` differs from `b`. There is no left extension, while the following `b` characters match, so $l=0$, $r=1$, contributing $(1)(2)=2$: the one-character pair and the length-two pair.
- At $(0,1)$, `a` differs from the second `b`. Neither side can extend, contributing one more one-character pair.
- All other aligned position pairs contain equal `b` characters and are not mismatch centers.

The total is three.

**Why nothing is omitted or double-counted**

Take any pair of equal-length substrings differing in exactly one character. Let their mismatch align original positions $(i,j)$. All aligned positions between the substring's left boundary and $(i,j)$ match consecutively, so the first while loop's maximal `l` is at least that left extension length. The same is true for the right extension and `r`. The formula therefore includes that exact start/end choice.

The pair cannot be counted around another center because it has only one mismatch. Its boundaries combined with $(i,j)$ identify one term in exactly one product. Thus every valid pair is counted once.

Conversely, each product choice stays within maximal equal runs on both sides and includes the unequal center. It has exactly one differing character and is valid. This proves soundness and completeness.

## Complexity detail

Let $m=\lvert s\rvert$ and $n=\lvert t\rvert$. The nested loops examine all $mn$ position pairs.

A single mismatch can scan up to $\min(m,n)$ characters around it, so a loose per-iteration multiplication would suggest $O(mn\min(m,n))$. The aggregate work is tighter. Group position pairs by alignment diagonal, where moving left or right changes both indices together. Along one diagonal, comparisons form runs of equal pairs separated by mismatches. A maximal equal run can be scanned as a right extension only by the mismatch immediately before it and as a left extension only by the mismatch immediately after it. Therefore each equal aligned pair participates in at most two extension scans.

Across all diagonals there are exactly $mn$ aligned position pairs. The initial examination plus amortized extension work is $O(mn)$ total, matching the manifest's time bound.

The source stores only counters, indices, lengths, and the answer. It allocates no DP tables, slices, or substring objects. Its actual auxiliary space is $O(1)$, which is tighter than the manifest's conservative `O(n)` entry.

The numeric answer can be much larger than the number of position pairs because one mismatch contributes a product of extension choices, but integer addition is treated as constant time in the standard problem model.

## Alternatives and edge cases

- **Left/right dynamic-programming tables:** Precompute matching-run lengths ending before and starting after every alignment, then sum the same products at mismatches. This makes $O(mn)$ time obvious but uses $O(mn)$ space unless rows are compressed.
- **Diagonal one-pass DP:** Track the length of the current zero-mismatch and one-mismatch suffix while walking each diagonal. This achieves $O(mn)$ time and $O(1)$ extra space with more abstract state.
- **Enumerate all substring pairs:** There are quadratically many substrings in each string, producing a prohibitively large search before character comparison.
- **Equal center characters:** They cannot be the unique mismatch, so the source correctly does no extension work or addition for them.
- **One-character strings:** Every unequal character pair contributes one; equal pairs contribute zero.
- **All characters equal across both strings:** No mismatch center exists, so the answer is zero.
- **Mismatch at a boundary:** One extension length is zero, but the `+1` still represents choosing no characters on that side.
- **A second mismatch nearby:** Expansion stops before it, preventing invalid substring pairs with two differences.
- **Repeated substring text:** Different source or target positions are different choices and must all be counted.
- **Do not replace the mismatch:** The problem's replacement interpretation is equivalent to choosing two substrings with exactly one different aligned character; the source counts those position pairs directly.
- **No modulo:** The contract asks for the exact count, so the accumulating answer is not reduced.
