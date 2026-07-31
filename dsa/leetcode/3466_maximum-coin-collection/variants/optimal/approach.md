## General

**Represent the only three useful lane histories.** A trip always begins conceptually in lane 1. After zero switches it is in lane 1, after one switch it is in lane 2, and after two switches it is back in lane 1. For the current mile, maintain:

- `no_switch`: the best nonempty trip ending here in lane 1 with zero switches;
- `one_switch`: the best nonempty trip ending here in lane 2 with exactly one switch;
- `two_switches`: the best nonempty trip ending here in lane 1 with exactly two switches.

These values summarize everything the next mile needs: current total, current lane, and switches already used. Earlier entry and switch positions no longer matter once their best total for a state is known.

**Extend or enter at the current mile.** Let `first = lane1[i]` and `second = lane2[i]`. Using only the previous mile's states, compute

```text
next_no_switch = max(first, no_switch + first)
next_one_switch = max(second, one_switch + second, no_switch + second)
next_two_switches = max(two_switches + first, one_switch + first)
```

The first state either starts a new lane-1 trip or extends one. The second can start at the current mile by switching immediately upon entry, continue in lane 2, or switch from lane 1 between the preceding and current miles. The third either stays in lane 1 after two switches or performs its second switch from lane 2. A separate restart in the third state is unnecessary: it would collect the same current `first` as a zero-switch restart while discarding future switching flexibility, so the zero-switch state dominates it.

Update the three states simultaneously; using an already updated current-mile value would incorrectly allow two lane transitions while collecting the same mile. Track the maximum over all states and all endpoints because Mario may leave after any mile and need not use every switch.

Initialize every state and the answer to an unreachable value below the smallest possible legal total. Do not initialize the answer to zero: when both lanes are negative, the nonempty-trip rule requires returning the least harmful negative choice.

## Complexity detail

Let $n$ be the common lane length. Each mile performs a fixed number of additions and comparisons, so time is $O(n)$. The three previous-state totals, three next-state totals, and the running answer use $O(1)$ auxiliary space. The result may have magnitude up to $10^{14}$, so implementations need a sufficiently wide integer type; Python integers already satisfy that requirement.

## Alternatives and edge cases

- **Enumerate entry and exit miles:** Even before trying switch positions, all contiguous intervals already require $O(n^2)$ candidates.
- **Two-dimensional table by mile and switch count:** This gives the same $O(n)$ recurrence but stores $O(n)$ values that can be compressed because only the preceding mile is needed.
- **Independent Kadane runs per lane:** They miss profitable paths whose total combines segments from both lanes.
- **Allow three useful switches:** Starting in lane 1, a third switch would create a lane-2 segment after the permitted two-switch limit.
- **Update states in place from left to right:** Letting `two_switches` consume the current-mile `one_switch` permits two switches at one mile and double-counts its value.
- **All values negative:** Mario must still travel at least one mile; zero is not a valid fallback.
- **Immediate entry switch:** A trip may begin with `lane2[i]`, represented by restarting `one_switch` at that value.
- **Exit before the array ends:** The running global maximum preserves a trip that should stop before later tolls.
- **Single mile:** The answer is `max(lane1[0], lane2[0])` because immediate switching is allowed.
