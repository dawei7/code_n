## General

**Reduce the problem to assigning distinct frequencies**

`Counter(s)` obtains one positive frequency for every character present. Deleting characters can only decrease a frequency; it cannot increase one. The goal is to keep as many characters as possible while making the remaining positive frequencies distinct. A zero frequency means deleting that character completely and is ignored by the goodness rule.

The source sorts the positive frequencies in descending order. Processing large counts first is useful because a smaller count can never be increased to get out of a larger count's way. The best response is to keep each frequency as large as possible below the previous assigned one.

**Interpret `pre` as the strict upper boundary**

`pre` records the final frequency assigned to the previously processed character. The current final frequency must be strictly less than `pre`.

Initially `pre = inf`, so the largest frequency can remain unchanged.

For each original frequency `v`, three cases apply.

If `pre == 0`, no positive frequency smaller than the previous assignment exists. The current character must be deleted completely, so all `v` occurrences are added to `ans`.

If `v >= pre`, keeping `v` would duplicate or exceed the previous assigned frequency. The largest legal choice is `pre - 1`. The deletions are

$$
v-(pre-1)=v-pre+1.
$$

The source adds that amount and decrements `pre`.

If `v < pre`, the frequency is already strictly smaller, so no deletion is needed and `pre` becomes `v`.

**Why zero is treated specially**

Once `pre` reaches zero, later positive counts cannot receive a distinct non-negative frequency below it. All must become zero. Multiple characters may have frequency zero because absent characters do not count when deciding whether the string is good.

The dedicated first branch prevents setting `pre` negative and counts complete deletion directly.

**A trace**

For `"aaabbbcc"`, the positive frequencies are `[3,3,2]`.

The first 3 remains 3. The second 3 must be at most 2, costing one deletion and setting `pre=2`. The original 2 must then be at most 1, costing one more deletion. Final positive frequencies are 3, 2, and 1, with two deletions.

**Why the greedy choice is minimal**

After larger frequencies have been fixed, the current frequency cannot exceed its original `v` and must be below `pre`. The greatest legal value is therefore `min(v, pre-1)`, clamped at zero. Choosing anything smaller would delete extra characters and would not help any earlier assignment. It can only make more room for later, already smaller counts, but choosing the greatest legal value still leaves every lower non-negative frequency available.

Thus each step maximizes the retained count given the optimal prefix. Induction proves the total retained characters are maximal, so deletions are minimal.

Another exchange view reaches the same conclusion. Suppose a proposed optimal result assigns the current character a frequency lower than the greedy value while leaving that greedy value unused. Raising the character to the unused value restores some deleted occurrences without colliding with any earlier, larger assignment. That would reduce deletions, contradicting optimality. Therefore the largest legal value chosen by the source is always safe and necessary for minimum cost.

**Why descending order matters**

Processing a small original count first could reserve a frequency that a larger count also wants, then force awkward reconsideration. Descending order gives priority to values with fewer downward alternatives at the high end. Once the previous final frequency is fixed, every later original frequency is no larger, and the single boundary `pre - 1` completely describes what remains legal.

## Complexity detail

Let $n$ be the string length and $K$ the number of distinct lowercase letters. Counting takes $O(n)$ time. Sorting takes $O(K\log K)$, and the loop takes $O(K)$.

Because the alphabet fixes $K\le26$, sorting and the loop are constant-sized. Total time is $O(n)$.

The Counter and frequency list hold at most 26 entries, so auxiliary space is $O(1)$ under the fixed alphabet. This matches the manifest. For an unbounded alphabet, the general bounds would be $O(n+K\log K)$ time and $O(K)$ space.

## Alternatives and edge cases

- **Used-frequency set:** For each count, decrement until it reaches an unused positive value or zero. It is simple and still effectively linear with 26 letters, but may perform more individual decrement steps.
- **Max-heap:** Repeatedly reduce duplicate largest counts. It works but adds heap operations for a constant-sized alphabet.
- **All frequencies already distinct:** Every `v < pre` after the first, so the answer remains zero.
- **Several equal frequencies:** The sorted greedy assigns consecutive smaller values while possible.
- **Frequency reaches zero:** That character disappears and zero may be reused by any later character.
- **Single distinct character:** Its frequency is retained unchanged.
- **Lowercase-only constraint:** It is what makes Counter storage and sorting constant space relative to $n$.
- **Do not require zero frequencies to be unique:** Only characters remaining in the string participate in the rule.
- **Infinite initial boundary:** It lets the largest original frequency stay unchanged without a special first-iteration branch.
- **Frequency one collision:** One character may keep frequency 1; any later colliding character must fall to zero and disappear.
- **Deletion count formula:** In the collision branch, `v - pre + 1` is exactly `v - (pre - 1)`, the cost of lowering to the greatest permitted frequency.
