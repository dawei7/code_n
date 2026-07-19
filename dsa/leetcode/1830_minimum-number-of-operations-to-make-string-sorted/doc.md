# Minimum Number of Operations to Make String Sorted

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/) |
| Frontend ID | 1830 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Combinatorics, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Starting with a 0-indexed lowercase string `s`, repeatedly perform a prescribed operation until the characters are sorted in ascending order. First find the largest index $i$ with $1 \le i < \lvert s\rvert$ for which `s[i] < s[i - 1]`.

Next choose the largest $j \ge i$ such that every character from index $i$ through $j$ is smaller than `s[i - 1]`. Swap `s[i - 1]` with `s[j]`, then reverse the suffix beginning at $i$. Return how many operations are performed, modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 3000$.

**Return value**

- Return the number of prescribed operations required to reach the ascending arrangement, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `s = "cba"`
- Output: `5`

The operation visits the five preceding permutations before reaching `"abc"`.

**Example 2**

- Input: `s = "aabaa"`
- Output: `2`

The successive strings are `"aaaba"` and then `"aaaab"`.

**Example 3**

- Input: `s = "abc"`
- Output: `0`

The string is already sorted, so no operation is needed.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Recognize a previous-permutation operation**

The specified pivot, swap, and suffix reversal are exactly the standard construction of the lexicographically previous distinct permutation. Consequently, repeated operations enumerate every distinct permutation of the same multiset below `s`, in descending order, until the ascending permutation is reached. The requested operation count is therefore the zero-based lexicographic rank of `s` among its distinct permutations.

**Count smaller permutations by their first differing position**

Suppose a scan has fixed the original prefix and there are $r$ characters remaining. Let $f_c$ be the remaining frequency of character $c$, and let

$$
D = \prod_c (f_c!)^{-1}.
$$

If the next permutation places some character smaller than the current one at this position, the other $r-1$ characters can be arranged in

$$
(r-1)! \prod_c (g_c!)^{-1}
$$

distinct ways, where one chosen frequency has been decreased. For a particular smaller character $c$, replacing $(f_c!)^{-1}$ by $((f_c-1)!)^{-1}$ multiplies the expression by $f_c$. Thus, if $C$ is the total frequency of all smaller remaining characters, every smaller choice contributes together

$$
C(r-1)!D.
$$

Add this quantity for each position. These groups are disjoint because each counted permutation has a unique first position where it differs from `s`.

**Maintain the multiset denominator modulo a prime**

Precompute factorials through $n$ modulo $P=10^9+7$. Fermat's theorem gives $(n!)^{-1} \equiv (n!)^{P-2}\pmod P$; derive every smaller inverse factorial in one descending pass.

Initialize $D$ from the complete frequency table. After fixing the actual current character with frequency $f$, its frequency becomes $f-1$, and

$$
((f-1)!)^{-1} = f(f!)^{-1}.
$$

Therefore update `D = D * f` before decrementing that frequency. The accumulated rank remains correct modulo $P$, while the frequency table also supplies $C$ by summing the at most 25 smaller-letter counts.

#### Complexity detail

Factorial preprocessing, frequency construction, and the position scan are linear in $n$. Each position scans at most the fixed 26-letter alphabet, so total time is $O(n)$. The factorial and inverse-factorial arrays use $O(n)$ space; the frequency table uses $O(1)$ space because the alphabet size is fixed.

#### Alternatives and edge cases

- **Simulate previous permutations:** It follows the operation literally but may require a factorial number of steps before reaching the sorted string.
- **Recount every suffix:** The same rank formula can rebuild suffix frequencies at every position, but that repeats work and takes $O(n^2)$ time.
- **Fenwick tree over characters:** It can obtain the number of smaller remaining characters in $O(\log 26)$ time, though a 26-entry scan is simpler and still asymptotically linear.
- **All characters equal:** There is only one distinct permutation, so every positional contribution is zero.
- **Already ascending:** No smaller distinct permutation exists and the rank is zero.
- **Repeated characters:** Divide by frequency factorials; treating occurrences as distinct overcounts the answer.
- **Current character is smallest:** Its smaller-frequency total $C$ is zero at that position.
- **Large ranks:** Apply the modulus to products and the running sum; never construct the potentially enormous exact permutation count.
- **Single character:** Its only arrangement is already sorted, producing zero.

</details>
