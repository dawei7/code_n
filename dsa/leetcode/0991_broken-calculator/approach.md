## General

**Reverse the problem so that multiplication becomes division**

Working forward from `startValue` gives two choices: double the display or subtract one. A locally attractive choice can be misleading because an optimal route may deliberately overshoot the target and then subtract.

Working backward from `target` makes the structure much clearer. The inverse operations are:

- if the current target is even, divide it by two to undo a forward doubling;
- add one to undo a forward subtraction.

The reverse operations have the same cost as their forward counterparts, and reversing an operation sequence preserves its length. Therefore, the minimum number of forward operations equals the minimum number of reverse operations needed to reach `startValue`.

**Odd targets force the next reverse move**

If the current reverse target is odd, it cannot have been produced by doubling an integer: twice any integer is even. Therefore, the final forward operation leading to this odd value must have been subtraction from the next larger even value.

The only useful reverse step is consequently

`target += 1`.

The bit test `target & 1` is nonzero exactly when `target` is odd. Adding one makes it even, allowing a division on a later iteration.

For example, to reason backward from five, the algorithm must first go to six. In forward order, this corresponds to reaching six and then subtracting one to obtain five.

**Even targets should be halved immediately**

When the reverse target is even and still greater than `startValue`, halving makes the largest possible useful reduction in one operation:

`target >>= 1`

is integer division by two for these positive values.

Why is adding one first not better? Starting from an even value `y`, additions must occur in pairs before another division is possible: one addition makes `y + 1` odd, and a second makes `y + 2` even. Two additions followed by division reach

`(y + 2) / 2 = y / 2 + 1`

in three operations. Halving immediately reaches `y / 2` in one operation; if the extra one is genuinely useful, one later addition reaches `y / 2 + 1` in a total of two operations. Thus postponing the division cannot improve the route.

More generally, additions before an available halving can be moved after that halving with no worse destination and fewer or equal operations. An optimal reverse path therefore always halves an even target while it remains above the start.

**Count every reverse operation**

Each loop iteration performs exactly one inverse calculator operation, either add one or divide by two. Variable `ans` is incremented once afterward.

The loop condition is `while startValue < target`. As long as the reverse target exceeds the desired start, halving can rapidly shrink it, with forced increments used only to make odd values divisible.

An odd iteration raises the target by one temporarily, but the following even iteration halves it. Across those two operations, any odd target `y > 1` becomes `(y + 1) / 2`, which is strictly smaller than `y`. Progress is therefore guaranteed.

**Finish with direct increments once the reverse target is small enough**

Eventually `target <= startValue`. From that point, the best reverse operation is simply to add one until reaching `startValue`. This requires

`startValue - target`

operations, which the code adds to `ans` in one arithmetic step.

Halving at or below `startValue` would move farther downward and create more required additions. In forward direction, when `startValue >= target`, directly subtracting one `startValue - target` times is optimal. Doubling would first increase the value and then require even more subtractions.

This explains why the main loop stops at “less than or equal,” not only at exact equality.

**Trace `startValue = 3` and `target = 10`**

Work backward:

- Ten is even and above three, so divide to five. One operation.
- Five is odd, so add one to obtain six. Two operations.
- Six is even, so divide to three. Three operations.

The values now match, so the final difference is zero. Reversing these steps gives the forward sequence

`3 -> 6 -> 5 -> 10`:

double, subtract one, double.

**Trace an intentional forward decrement before doubling**

For `startValue = 5` and `target = 8`:

- Reverse eight to four by halving once.
- Four is now below five, so add the final difference of one.

The answer is two. Reversing the route gives `5 -> 4 -> 8`. This shows why a forward strategy that always doubles whenever below the target would miss the best sequence.

**Why the greedy reverse choices are globally optimal**

At an odd target above the start, division is illegal, so every valid reverse path must begin with an addition. The algorithm's choice is forced.

At an even target above the start, the exchange argument shows that any path delaying division with additions can be transformed into one that divides immediately and uses no more operations. Therefore, an optimal path exists with the algorithm's halving choice.

Once the target is no greater than the start, direct additions are optimal because division only increases the remaining distance and reverse subtraction is not an allowed operation. Applying these facts at every state proves that the counted reverse sequence has minimum length. Reversing it yields a minimum-length legal forward sequence.

**Why breadth-first search is unnecessary**

The display values can be as large as one billion, and forward transitions can grow beyond the target. A graph search would need artificial bounds and could visit many integers. The reverse parity rule reduces the value geometrically and makes the optimal next action deterministic.

## Complexity detail

Let `T` be the original target value.

An even loop iteration halves the current target. An odd iteration is followed by an even halving unless the loop terminates, so within at most two iterations the value falls from `y` to roughly `y / 2`. There are `O(\log T)` halvings before the target becomes no greater than `startValue`. The final difference is added arithmetically rather than executed as a loop, so total running time is `O(\log T)`.

The method stores only `ans` and the two integer values. It uses no recursion, collection, or path reconstruction, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Forward breadth-first search:** It can find a shortest sequence but explores many display values and needs a safe search bound, making it far less efficient.
- **Forward greedy doubling:** Doubling whenever below the target fails when decrementing first enables an exact or cheaper later doubling, as in five to eight.
- **Recursive reverse solution:** Apply the same odd/even recurrence recursively. It is concise but uses `O(\log T)` call-stack space instead of constant space.
- **Target already equal to start:** The loop is skipped, the difference is zero, and the answer is zero.
- **Target below start:** Only forward decrements are useful; the method returns `startValue - target` directly.
- **Odd target above start:** The increment is mandatory because no integer doubling can produce an odd result.
- **Power-of-two relationship:** Repeated halving reaches the start with no odd corrections when the target is the start multiplied by a power of two.
- **Temporary increase:** Adding one to an odd reverse target may exceed the original target by one, but it enables the forced halving and guarantees progress over the pair of steps.
- **Positive-value guarantee:** Bit shifting and parity reasoning use positive integers throughout; the stated constraints ensure this.
- **Large final difference:** It is counted with one subtraction expression rather than simulated, so a large `startValue - target` does not increase runtime.
- **Bit operations:** `target & 1` and `target >>= 1` are exact integer parity and division operations here; they introduce no rounding.
