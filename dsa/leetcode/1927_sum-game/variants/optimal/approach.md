## General

**Summarize the board instead of exploring moves**

Only four quantities affect the winner:

- `s1`: the sum of fixed digits in the first half;
- `s2`: the sum of fixed digits in the second half;
- `cnt1`: the number of question marks in the first half;
- `cnt2`: the number of question marks in the second half.

The exact solution obtains these values with slicing, `count("?")`, and generators that convert only non-question-mark characters to integers. The locations of question marks within a half do not matter because every position in that half contributes to the same sum and may receive any digit from zero through nine.

Let $D=s1-s2$. A digit placed in the first half increases $D$; a digit placed in the second half decreases it. Bob needs the final difference to be zero, while Alice needs any nonzero value.

**An odd number of moves gives Alice the last choice**

If `cnt1 + cnt2` is odd, Alice makes both the first and last moves. On the final move, exactly one question mark remains. For any fixed state before that move, at most one of the ten available digits can make the two sums equal. Alice can choose one of the other nine digits and force inequality. Therefore the first condition, `(cnt1 + cnt2) % 2 == 1`, immediately means Alice wins.

**Pair the moves when the count is even**

When the total number of question marks is even, every Alice move is followed by a Bob move, and Bob makes the last move. Imagine pairing all question-mark positions in advance:

- two positions in the first half can be paired;
- two positions in the second half can be paired;
- one position from each half can be paired.

Bob waits for Alice to fill one position of a pair, then fills its partner. If both positions are in the same half and Alice chooses $x$, Bob chooses $9-x$. Their combined contribution to that half is always $9$. If the positions are in opposite halves, Bob copies Alice's digit, so the two additions cancel in the difference between halves.

Such a pairing is always possible when the total count is even. Pair as many positions across halves as possible. All leftovers are in only one half, and their count is even because subtracting twice the number of cross pairs preserves even parity. Those leftovers can be paired within that half.

After cross-half pairs cancel, only the imbalance in the numbers of question marks matters. The net forced contribution from all same-half pairs is

$$
9\cdot\frac{cnt1-cnt2}{2}
$$

to the first-half-minus-second-half difference. Bob's complementary responses can therefore make the final difference

$$
D+9\cdot\frac{cnt1-cnt2}{2}.
$$

Bob wins exactly when this equals zero. Rearranging gives

$$
s1-s2=9\cdot\frac{cnt2-cnt1}{2}.
$$

That is precisely the equality tested by the code. The return value is true for Alice when the equality does not hold.

**Why the division is exact**

The source writes `9 * (cnt2 - cnt1) // 2`. Floor division would be suspicious if `cnt2 - cnt1` could be odd. However, this expression matters only after the total count has been found even. If `cnt1 + cnt2` is even, then `cnt1` and `cnt2` have the same parity, so their difference is even. Division by two is exact, including when the difference is negative.

Another useful form doubles everything:

$$
2(s1-s2)=9(cnt2-cnt1).
$$

It says that each question mark carries a neutral average value of $4.5$. If the current fixed-sum difference is exactly balanced by the difference in available unknown positions at that average, Bob can neutralize Alice's choices pair by pair. Otherwise Alice can preserve an imbalance under optimal play.

**Why the condition characterizes optimal play**

When the equality holds, the pairing response above is an explicit Bob strategy. Every Alice choice has a legal response: complement within the same half or copy across halves. Each completed pair has a contribution independent of Alice's chosen digit, and the equality guarantees that those forced pair contributions cancel the fixed-digit difference. Bob reaches equal final sums.

When the equality fails, the board begins with a nonzero residual after accounting for the $9$ contributed by same-half pairs and the zero contributed by cross-half pairs. Alice controls the first element completed in each response pair and can choose values that prevent Bob from repairing that residual while also answering all of Alice's possible digit choices. Equivalently, the second player has a move-by-move neutralizing strategy only at the exact balance point above. Away from that point, Alice can force the final difference to remain nonzero. Thus the concise Boolean expression completely replaces an exponential game-tree search.

For `num = "25??"`, the fixed difference is $7-0=7$, while `cnt1=0` and `cnt2=2`. Bob's balance target is $9(2-0)/2=9$, not $7$, so Alice wins. For a board with no question marks, both counts are zero and the target is zero; the method returns false exactly when the already fixed sums are equal.

## Complexity detail

Let $N$ be the length of `num`.

The solution creates half-string slices several times. Each slice has $O(N)$ total length, and each `count` or sum generator scans its slice. Although there are multiple passes, their number is constant, so time is $O(N)$.

In Python, slicing a string creates a new string. At least one half-sized temporary exists during these expressions, so the concrete implementation uses $O(N)$ peak temporary space, even though the four mathematical counters themselves require only $O(1)$ state. The manifest's $O(1)$ space describes the counting idea if implemented with one index-based pass and no slices; it is not the strict allocation bound of this exact Python source.

No recursion or game-state table is needed. Arithmetic values are at most proportional to $9N$, which is easily handled by Python integers.

## Alternatives and edge cases

- **One-pass counter implementation:** Inspect each character with its index and update the appropriate half's sum or question-mark count. This preserves $O(N)$ time while achieving true $O(1)$ auxiliary space in Python.
- **Minimax search:** Trying every question mark and all ten digits creates an exponential game tree and is infeasible for length up to $10^5$.
- **Neutral-value interpretation:** Treating each unknown as an average contribution of $4.5$ leads to the doubled equation `2 * (s1 - s2) == 9 * (cnt2 - cnt1)`. This avoids division and is algebraically equivalent.
- **Odd total question marks:** Alice owns the final move and can always avoid the single digit, if any, that would make the sums equal.
- **No question marks:** The parity is even and the target term is zero. Bob wins exactly when `s1 == s2`.
- **Question marks only in one half:** Their count must be even for Bob to have a chance. Bob pairs them within that half so every pair contributes nine; the fixed difference must match that forced total exactly.
- **Equal unknown counts:** The target is zero because all question marks can be paired across halves. Bob wins precisely when the fixed sums already match.
- **Negative count difference:** Python floor division is harmless here because the difference is even whenever this branch is relevant, so the quotient is mathematically exact.
- **Digit zero:** Zero is a legal choice. Within a same-half pair its complement is nine; across halves Bob copies zero.
- **Repeated slicing:** It does not change the linear time bound, but it does make the exact implementation's peak space linear rather than constant.
- **Return meaning:** The expression returns `True` for Alice and `False` for Bob. The equality case is negated because equality is Bob's objective.
