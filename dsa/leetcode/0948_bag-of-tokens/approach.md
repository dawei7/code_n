## General

**Two resources move in opposite directions**

Playing a token face-up spends power and gains score. Playing one face-down spends score and gains power. The objective is the largest score reached at any time; not every token must be played.

After sorting, the smallest remaining token is the cheapest possible way to buy one score, and the largest remaining token is the most power obtainable by selling one score. This leads to a two-pointer greedy strategy.

Pointer `i` identifies the smallest unplayed token and `j` the largest. Tokens outside `[i, j]` have already been consumed.

**When enough power is available**

If `power >= tokens[i]`, the solution plays the smallest token face-up:

- subtract `tokens[i]` from power;
- add one to `score`;
- move `i` right.

Any face-up move always gains exactly one score. Choosing a larger affordable token would gain the same score while leaving less power for later moves. Therefore, the smallest remaining token is never worse and can only be better.

After gaining score, the code updates `ans = max(ans, score)`. This records the best score ever achieved, even if a later face-down move temporarily reduces the current score.

**When the cheapest token is unaffordable**

Because tokens are sorted, if the smallest remaining token cannot be bought, no other remaining token can be bought face-up.

If `score > 0`, the only way to make progress is to spend one score on a face-down token. Every such move loses exactly one score, so the best choice is the largest remaining token `tokens[j]` because it gives the most power for the same cost.

The code adds that value to power, subtracts one from score, and moves `j` left.

Selling a smaller token would leave no more score and strictly less or equal power, so it could not enable any sequence that selling the largest token cannot also enable.

**When the process must stop**

If the smallest token is unaffordable and `score == 0`, neither move type is legal:

- no token can be played face-up;
- face-down play requires at least one score.

The algorithm breaks. Leaving remaining tokens unused is allowed.

**Why current score and best score differ**

A face-down play deliberately reduces current score to buy power. That trade can enable several later face-up plays and a higher final score, but it can also fail to improve the previous record.

For example, the algorithm could reach score two, sell a token and fall to one, then end without buying enough new scores. Returning only current `score` would incorrectly lose the earlier maximum. Variable `ans` preserves it.

**Trace**

For `tokens = [100, 200, 300, 400]` and `power = 200`:

- Buy 100: power becomes 100, score becomes one, and `ans` becomes one.
- Token 200 is unaffordable. Sell 400: power becomes 500 and score becomes zero.
- Buy 200: power becomes 300, score becomes one.
- Buy 300: power becomes zero, score and `ans` become two.

All tokens are used and the maximum is two.

For `tokens = [100]` and power 50, the only token is unaffordable and score is zero. The loop stops and returns zero.

**Why the greedy strategy is correct**

Any face-up move can be exchanged with buying the cheapest remaining token. The exchanged move gains the same score and leaves at least as much power, so it cannot reduce future possibilities.

Whenever no face-up move is possible but score is available, any continuing strategy must make a face-down move before it can buy again. Exchanging its sold token with the largest remaining token gives at least as much power for the same one-score cost.

Applying these exchange arguments repeatedly transforms an optimal strategy into the exact choices made by the algorithm without lowering its best score. Therefore, the greedy result is optimal.

## Complexity detail

Let `n` be the number of tokens.

Sorting costs `O(n log n)`. Each loop iteration consumes exactly one token by moving `i` right or `j` left, so there are at most `n` iterations and `O(n)` work after sorting. Total time is `O(n log n)`.

The exact code sorts the input list in place. Python sorting may require `O(n)` temporary memory in the worst case, matching the manifest's `O(n)` space bound. The pointer and score state itself is `O(1)`.

## Alternatives and edge cases

- **Try every play sequence:** Each token has multiple choices, producing exponential search. Sorting exposes exchange-dominant choices.
- **Always play face-up only:** This misses beneficial score-for-power trades that can unlock several later purchases.
- **Sell the smallest token:** It sacrifices the same one score but gains less power than selling the largest remaining token.
- **Return final score:** A late trade can make final score smaller than an earlier maximum, so `ans` is necessary.
- **Empty token list:** `j = -1`, the loop never runs, and zero is returned.
- **Zero-valued tokens:** They are bought face-up for no power and increase score, so sorting places them in the best possible position.
- **One remaining token:** If affordable, buy it. If unaffordable but score is positive, the code may sell it, but `ans` preserves the previous maximum.
- **Already enough power for all tokens:** Every token is bought from smallest to largest and the answer is `n`.
- **Input mutation:** `tokens.sort()` changes token order. Use a sorted copy if the caller needs the original order.
- **Equal token values:** Their identities do not matter; every token is still consumed at most once.
