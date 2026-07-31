## General

The output is determined by one ordered simulation. Maintain the two state variables named by the contract: `score` and `counter`, both starting at zero.

For each event:

- if it is `"W"`, increment only `counter`;
- if it is `"WD"` or `"NB"`, increment only `score` by `1`;
- otherwise it is one of the guaranteed numeric strings, so convert it to an integer and add that value to `score`.

After applying the event, test whether `counter == 10`. This order matters: the tenth `"W"` itself is processed and produces the final counter value, but nothing after it may affect either component. If the counter stays below ten, continue until the list is exhausted.

At every iteration, `score` equals exactly the total contributions of the processed prefix, while `counter` equals the number of `"W"` events in that prefix. Each branch applies the source-defined contribution of the current event, so the invariant remains true. Stopping after the tenth `"W"` selects precisely the required prefix; otherwise the entire list is the required prefix. Returning the two state variables therefore gives the requested final pair.

## Complexity detail

Let $p$ be the number of events actually processed, so $p\le n$. The scan takes $O(p)$ time and therefore $O(n)$ time in the worst case. Apart from the returned two-element list, it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Table-driven score contributions:** A mapping from all non-`"W"` tokens to their point values can replace the branch chain. It has the same $O(n)$ bound but stores a small lookup table.
- **Repeated prefix recomputation:** Recalculating the state of the complete prefix after every new event is correct but takes $O(n^2)$ time when no early cutoff occurs.
- **The tenth `"W"`:** Apply its counter increment before stopping; stopping before it would incorrectly return `9`.
- **Events after the cutoff:** Numeric events, `"WD"`, `"NB"`, and further `"W"` entries after the tenth `"W"` must all be ignored.
- **Numeric zero:** `"0"` is a numeric event that contributes zero points; it is not a symbolic no-op requiring a separate rule.
- **Missing numeric five:** The contract never supplies `"5"`; only the six listed numeric strings are legal.
- **Symbolic scoring events:** `"WD"` and `"NB"` each add exactly one point and never change the counter.
- **No `"W"` events:** Process the entire list and return a counter of zero.
