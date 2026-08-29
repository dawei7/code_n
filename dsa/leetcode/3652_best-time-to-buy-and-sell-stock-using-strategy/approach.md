## General

**Treat profit as an independent contribution from each day**

The profit is defined directly as

`sum(strategy[i] * prices[i])`.

There is no budget limit, inventory requirement, or rule that a sale must be preceded by a purchase. Therefore this is not the usual stock-trading state-machine problem. Each day contributes independently according to its strategy value:

- Buying, represented by `-1`, contributes `-prices[i]`.
- Holding, represented by `0`, contributes zero.
- Selling, represented by `1`, contributes `prices[i]`.

The one allowed modification overwrites a length-`k` window in a completely fixed way. It does not let us choose the new action of each day independently. The first half becomes zero and the second half becomes one.

The task is therefore to evaluate the original profit and the profit produced by every possible length-`k` window, then take the maximum.

**Start from the original total**

Define the original daily contribution

`contribution[i] = strategy[i] * prices[i]`.

The source builds prefix array `s` where

`s[i]` is the sum of original contributions on indices `0` through `i - 1`.

It also builds prefix array `t` where

`t[i]` is the sum of raw prices on indices `0` through `i - 1`.

Both arrays have length `n + 1` with entry zero representing the empty prefix. Using half-open intervals, any original-profit range `[l, r)` is

`s[r] - s[l]`,

and any price sum on that range is

`t[r] - t[l]`.

Half-open indexing makes adjacent sections meet cleanly and avoids special cases at the start or end of the arrays.

The unmodified total is `s[n]`. The source initializes `ans` to this value because modification is optional. Even if every possible overwrite lowers profit, the original strategy remains a legal choice.

**Describe one candidate window precisely**

The loop variable `i` is the exclusive right endpoint of a modified window. Because the window has length `k`, it covers

`[i - k, i)`.

Since `k` is even, let `h = k / 2`. The two overwritten halves are:

- First half: `[i - k, i - h)`, set to strategy zero.
- Second half: `[i - h, i)`, set to strategy one.

Days outside `[i - k, i)` keep their original contributions.

One way to calculate the candidate is to split the entire timeline into the unchanged prefix, the zeroed first half, the forced-sale second half, and the unchanged suffix. The source uses an equivalent and more compact replacement formula.

**Remove the old window and add its new contribution**

Begin with original total `s[n]`. The original contribution of the whole selected window is

`s[i] - s[i - k]`.

Subtracting it leaves exactly the contributions outside the window:

`s[n] - (s[i] - s[i - k])`.

The new first half contributes zero, so there is nothing to add for it.

Every strategy entry in the new second half is one, so its contribution is simply the corresponding price. Its total is

`t[i] - t[i - k // 2]`.

Adding that term produces the exact candidate used by the source:

`s[n] - (s[i] - s[i - k]) + t[i] - t[i - k // 2]`.

This formula does not care whether an overwritten original action was buy, hold, or sell. Subtracting the entire old window removes all of them, and the two new halves are added from their definitions.

**Evaluate every legal window**

The exclusive endpoint `i` ranges from `k` through `n` inclusive. The first value `i = k` represents window `[0, k)`. The last value `i = n` represents window `[n - k, n)`. Every intermediate length-`k` consecutive window has exactly one exclusive endpoint in this range.

For each endpoint, the method computes the candidate in constant time and compares it with `ans`. Because it considers the no-modification result and all `n - k + 1` legal modifications, no possible choice is omitted.

The maximum is valid even when profits are negative. Initializing `ans = 0` would be wrong because zero might be unattainable: the problem permits at most one overwrite but does not permit discarding the entire original strategy. Starting with `s[n]` uses an actually feasible outcome.

**View the same formula as an additive gain**

For intuition, the modification’s gain over the original strategy is:

- On the first half, new contribution zero minus old contribution.
- On the second half, new contribution `prices[i]` minus old contribution.

Thus for a window starting at `l` with half-length `h`,

`gain(l) = -sum(contribution on [l, l+h)) + sum(prices - contribution on [l+h, l+2h))`.

The candidate is `original_profit + gain(l)`. This view explains why a modification can be harmful: replacing profitable original sales in the first half with holds loses value, and replacing an already profitable pattern may not compensate elsewhere.

The exact source chooses the full-window replacement expression because its two prefix arrays make all pieces readily available.

**Trace the first example**

For `prices = [4, 2, 8]` and `strategy = [-1, 0, 1]`, original contributions are `[-4, 0, 8]`, so `s[n] = 4`.

With `k = 2`, choose the first window `[0, 2)`, whose exclusive endpoint is `i = 2`. The old window contribution is `-4 + 0 = -4`. Removing it from the original total gives `4 - (-4) = 8`, which is the unchanged contribution of day two.

The modified second half consists of day one, whose price is two, so adding it gives ten. The first half, day zero, is set to hold and contributes zero. This matches modified strategy `[0, 1, 1]`.

For the second example, original profit is nine. Both possible overwrites reduce it. Because `ans` begins at the original total, the method correctly returns nine without forcing a modification.

**Why no stock-ownership dynamic programming is needed**

In conventional stock problems, a strategy must respect whether a share is currently held, and buying or selling changes that state. The reference explicitly removes those constraints. A sell action is feasible regardless of earlier days, and a buy action does not require budget.

Adding an ownership state would solve a different problem and might reject forced second-half sales that are expressly allowed here. The linear contribution formula is the complete objective.

**The stored source does not implement the manifest’s constant-space slide**

The manifest summary describes sliding the modification’s additive gain with boundary updates and declares `O(1)` auxiliary space. That is a valid optimization, but it is not what the exact stored source does.

The source allocates two arrays, `s` and `t`, each of length `n + 1`. Its implemented space complexity is therefore `O(n)`. The approach teaches this prefix-sum implementation faithfully and lists the rolling-gain version as an alternative rather than attributing constant space to code that does not have it.

## Complexity detail

Building `s` and `t` visits each day once, taking `O(n)` time. The endpoint loop evaluates `n - k + 1` windows, and each evaluation performs a constant number of prefix lookups and arithmetic operations. That phase is also `O(n)`, giving total time `O(n)`.

The two prefix arrays each contain `n + 1` integers, so the exact source uses `O(n)` auxiliary space. All other variables use `O(1)`.

This differs from the manifest’s `O(1)` space claim. The gain expression can indeed be maintained with two running half-window sums and constant extra storage, but that optimized implementation is not present in `solution.py`.

The absolute profit can reach roughly `n * 10^5` in magnitude. With `n = 10^5`, a 64-bit integer is appropriate in fixed-width languages. Python integers grow automatically.

## Alternatives and edge cases

- **Constant-space rolling gain:** Maintain the first-half loss and second-half replacement gain for the current window, then update them as the window shifts one day. This achieves the manifest’s `O(n)` time and `O(1)` space, but it is different from the stored prefix-array source.
- **Recompute every modified strategy:** Copying a window and summing all `n` days for each start costs `O(n^2)` and is unnecessary.
- **Prefix only the original contribution:** A second prefix or rolling sum is still needed to obtain raw prices in the forced-sale half efficiently.
- **Force exactly one modification:** The statement says at most one. Initializing with original profit preserves the option to make no change.
- **Initialize the answer to zero:** This can return an infeasible result when all legal profits are negative. Use the actual original profit.
- **Odd `k`:** The problem guarantees even `k`, so the two halves have equal length and `k // 2` is exact. Without that guarantee, the operation would need a clarified split rule.
- **`k = n`:** There is one possible window covering the whole strategy, plus the option not to modify. The loop evaluates exactly that one endpoint.
- **Modification at the start:** Endpoint `i = k` gives start index zero; prefix entry `s[0]` handles it without a branch.
- **Modification at the end:** Endpoint `i = n` includes the final day and leaves an empty unchanged suffix.
- **Original buy in the first half:** Removing its negative contribution and replacing it with zero increases profit.
- **Original sell in the first half:** Replacing it with zero loses its positive contribution, so a window can be worse than doing nothing.
- **Original action in the second half:** It is always overwritten with one. The formula removes the old contribution before adding the raw price, avoiding double counting.
- **No ownership or budget constraints:** Forced sales are legal even without prior buys. Do not introduce transaction-validity checks.
- **Negative original profit:** Prefix sums and maximum comparison work without special treatment; a beneficial modification may make it less negative or positive.
- **Input preservation:** The source builds new prefix arrays and does not modify `prices` or `strategy`.
- **Missing type import:** The stored source uses `List` without importing it. Standalone Python needs `from typing import List` unless the execution harness provides it.
