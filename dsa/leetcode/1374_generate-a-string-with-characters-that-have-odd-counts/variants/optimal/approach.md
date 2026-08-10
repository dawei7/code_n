## General

**The construction depends only on whether `n` is odd or even**

The answer may be any lowercase string of length $n$ as long as every distinct character used occurs an odd number of times. There is no need to search among strings. We can choose extremely simple frequencies whose sum is $n$.

If $n$ is odd, using only `a` works. The string `'a' * n` has length $n$, and its sole distinct character occurs $n$ times. Since $n$ is odd, the requirement is satisfied.

If $n$ is even, using one character for all $n$ positions would make its frequency even and fail. Instead, split $n$ into

$$
n=(n-1)+1.
$$

When $n$ is even, $n-1$ is odd, and one is also odd. Therefore `'a' * (n - 1) + 'b'` has the correct length and gives both used characters odd frequencies.

The conditional expression in the exact code directly selects these constructions:

`'a' * n if n & 1 else 'a' * (n - 1) + 'b'`.

**Why `n & 1` detects parity**

The lowest binary bit represents the ones place. An odd integer has that bit set, so `n & 1` evaluates to one. An even integer has it clear, producing zero. Python treats one as true and zero as false, so the first branch runs precisely for odd $n$.

This is equivalent to checking `n % 2 == 1`. The bitwise form is compact, but the mathematical decision remains simply odd versus even.

**Why two letters are enough for even lengths**

The sum of an odd number of odd integers is odd, while the sum of an even number of odd integers is even. For an even target length, the construction can therefore use two odd positive counts. Choosing $n-1$ and one is the easiest such decomposition and works for every positive even $n$.

There is no requirement that all 26 letters appear, that counts differ, or that the result resemble a word. The letters `a` and `b` are arbitrary valid lowercase choices. Avoiding unnecessary characters makes both the proof and implementation smaller.

For $n=4$, the method returns `"aaab"`. Its length is four, `a` occurs three times, and `b` occurs once. The sample's `"pppz"` is different but equally valid because the problem accepts any solution.

For $n=7$, the method returns seven copies of `a`. One distinct character occurs seven times, an odd count, so this is just as valid as the sample output.

**Why the construction is correct**

There are two exhaustive cases. If $n$ is odd, the returned string contains exactly $n$ copies of `a`, so it has length $n$ and its only frequency is odd. If $n$ is even, the returned string contains $n-1$ copies of `a` and one copy of `b`. Its length is $(n-1)+1=n$, and both counts are odd because an even number minus one is odd and one is odd. Both letters are lowercase English letters.

Thus every possible valid input follows one branch whose returned string satisfies the length, alphabet, and frequency requirements. No verification loop or fallback is necessary.

**Why direct construction is optimal**

Returning a string of length $n$ necessarily creates or outputs $n$ characters. The implementation performs only the work needed to build that output. It does not count the resulting string afterward because the branch proof already guarantees its frequencies.

The expression also avoids mutable buffers and repeated one-character concatenation. Python's string repetition builds each repeated block directly, and the even branch combines only two pieces.

## Complexity detail

Constructing a length-$n$ string takes $O(n)$ time because all $n$ output characters must be produced. In the odd branch, one repeated string of length $n$ is made. In the even branch, the repeated `a` block has length $n-1$ and concatenating `b` produces length $n$. The constant-time parity test does not affect the bound.

The returned string occupies $O(n)$ space, matching the manifest. Beyond output construction and temporary string storage managed by Python, the algorithm uses only the integer input and a constant number of literals, so conceptual auxiliary state excluding the output is $O(1)$.

No algorithm can use asymptotically less than $O(n)$ output time or output space when it must return $n$ explicit characters, making the construction optimal in the relevant sense.

## Alternatives and edge cases

- **Modulo parity check:** Use `n % 2` instead of `n & 1`. It is equally correct and may be more immediately readable to beginners.
- **Always use two characters:** For odd $n$, two positive odd counts cannot sum to an odd total, so a fixed two-letter rule needs a different number of used letters in that case.
- **Use three characters for odd `n`:** Three odd counts can sum to an odd length when $n$ is large enough, but this complicates small inputs without benefit.
- **Random construction:** Generate candidates and count frequencies until one works. It is unnecessary, nondeterministic, and less efficient than a proof-driven formula.
- **`n = 1`:** The odd branch returns `"a"`, whose only count is one.
- **`n = 2`:** The even branch returns `"ab"`, giving both letters count one.
- **Largest input:** Repetition handles $n=500$ directly; no loop-depth or numeric issue appears.
- **Any valid output:** The returned string need not match the examples. `"aaab"` and `"pppz"` are both correct for four.
- **Lowercase restriction:** Both chosen literals are lowercase English letters.
- **No empty input:** The constraint $n\ge1$ ensures the even branch never tries to use a negative repetition count.
- **Frequency of unused letters:** Characters absent from the string are not considered distinct characters “in such string,” so their zero counts do not violate the requirement.
- **Immutability:** String multiplication and concatenation create the answer without mutating external data.
