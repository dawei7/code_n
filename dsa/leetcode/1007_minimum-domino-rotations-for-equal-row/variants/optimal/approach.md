## General

**Only two target values can possibly work**

Suppose one row can be made uniform with value `x`. At domino zero, the final chosen row must show `x`. Rotation can expose only `tops[0]` or `bottoms[0]` at that position.

Therefore, `x` must be one of those two values. No other domino number needs to be tried as a global target.

The solution evaluates both candidates with helper `f` and takes the smaller valid rotation count.

**A candidate must appear on every domino**

For target `x`, each domino pair `(a, b)` must contain `x` on at least one side. If

`x not in (a, b)`,

neither leaving that domino nor rotating it can place `x` into either uniform row at this position. The candidate is impossible, so `f` returns `inf` immediately.

This condition checks feasibility for making either the top row or the bottom row uniform at the same time. If every domino contains `x` somewhere, at least one side can expose it after an appropriate rotation.

**Count how many positions already match each row**

For every feasible domino:

- `cnt1 += a == x` counts positions whose top already equals `x`;
- `cnt2 += b == x` counts positions whose bottom already equals `x`.

In Python, a Boolean used in arithmetic contributes one for true and zero for false.

To make the entire top row equal `x`, every position whose top is not `x` must be rotated. Since feasibility proved the bottom contains `x` at those positions, each such rotation works. The required count is:

`len(tops) - cnt1`.

Similarly, making the bottom row uniform requires:

`len(tops) - cnt2`

rotations.

The cheaper orientation is

`len(tops) - max(cnt1, cnt2)`,

which is algebraically the minimum of those two rotation counts.

**Dominoes with the same value on both sides**

If `a == b == x`, the domino contributes to both `cnt1` and `cnt2`. It already displays the target in either row and never needs rotation.

Rotating it would make no visible difference, so excluding it from required rotations is correct.

**Trace the first example with target two**

The pairs are:

`(2,5), (1,2), (2,6), (4,2), (2,3), (2,2)`.

Every pair contains two, so the candidate is feasible.

Four top positions already contain two: indices zero, two, four, and five. Therefore, making tops uniform requires `6 - 4 = 2` rotations, at indices one and three.

Three bottom positions contain two, so making bottoms uniform would require three rotations. Helper `f(2)` returns two.

The other first-domino candidate, five, fails because later dominoes contain no five. Taking the minimum returns two.

**Why checking the first domino is sufficient**

Every uniform row must choose one face from every domino, including the first. The first domino has only two faces, so a feasible uniform value cannot lie outside its pair.

Trying `tops[0]` and `bottoms[0]` therefore covers every possible solution. If both fail, no third value can rescue the configuration.

This reduces what might look like six possible target checks to at most two full scans.

**Why the counted rotations are minimal for one target**

Consider making tops equal `x`. A position with `tops[i] != x` must be rotated; there is no alternative operation that changes a different domino and fixes this position. A position already showing `x` on top needs no rotation.

Thus `N - cnt1` is not merely a construction cost—it is a forced lower bound and an achievable cost. It is exactly minimal. The same reasoning gives `N - cnt2` for bottoms, and their minimum is optimal for target `x`.

**Why the final answer is globally minimal**

Any valid final configuration uses one of the two first-domino values. Helper `f` returns the exact minimum for each feasible candidate and infinity for an infeasible one. Taking their minimum therefore compares every possible target and row orientation.

If both results are infinite, the code maps infinity to `-1`. Otherwise, the finite minimum is the global optimum.

**Use infinity as an impossibility sentinel**

Returning `inf` lets the outer `min` combine feasible and infeasible candidates naturally. A finite rotation count always wins over infinity.

The final conditional

`return -1 if ans == inf else ans`

converts the internal sentinel to the API's required impossibility value.

If `tops[0] == bottoms[0]`, the same candidate is evaluated twice. This harmless duplication does not affect correctness or the linear bound.

## Complexity detail

Let `N` be the number of dominoes.

Helper `f` scans all pairs at most once. It is called twice, so the total work is at most `2N` plus constants, which is `O(N)` time.

Only counters, candidate values, and loop variables are stored. Auxiliary space is `O(1)`.

The method does not rotate or copy the input arrays; it computes the minimum count analytically.

## Alternatives and edge cases

- **Try all six domino values:** Check feasibility and rotations for values one through six. This remains linear because six is fixed, but the first-domino observation reduces unnecessary scans.
- **Count frequencies separately without pair feasibility:** Large top or bottom counts are insufficient if some domino lacks the target entirely. Each pair must be checked.
- **Physically simulate rotations:** Once a target row is chosen, simulation can construct it, but the problem asks only for the count and every required position is directly identifiable.
- **Both first faces equal:** The same candidate is checked twice; the result remains correct.
- **Target appears on both sides of a domino:** That position contributes to both already-correct counts and needs no rotation.
- **Candidate missing from one pair:** It is impossible for both row orientations, so the helper returns immediately.
- **Top already uniform:** For its target, `cnt1 = N` and the result is zero.
- **Bottom already uniform:** Symmetrically, `cnt2 = N` gives zero.
- **Both candidates feasible:** The algorithm compares their best top/bottom rotation counts and returns the smaller.
- **Unique minimum not required:** Different rotation plans may use the same minimum number; only the numeric count is returned.
- **Input preservation:** The paired arrays are read-only and retain their original orientation.
