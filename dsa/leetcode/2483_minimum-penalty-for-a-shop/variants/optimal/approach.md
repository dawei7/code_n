## General

**Start with the penalty for closing immediately.** If the shop closes at hour `0`, every `"Y"` lies in the closed suffix and contributes one penalty point, while no open hour exists. The initial penalty is therefore the total number of `"Y"` characters.

**Move the closing boundary one hour at a time.** When the boundary crosses a `"Y"` hour, that customer hour changes from closed to open, so its penalty disappears and the total decreases by one. When it crosses an `"N"` hour, that empty hour changes from closed to open, so it begins contributing a penalty and the total increases by one.

After processing the first $j$ characters, the running value is exactly the penalty for closing at hour $j$: all crossed `"N"` characters are penalized in the open prefix, and all uncrossed `"Y"` characters are penalized in the closed suffix. Compare this value with the best penalty seen so far. Update the answer only when the penalty is strictly smaller; leaving equal values unchanged preserves the earliest minimizing hour.

## Complexity detail

Counting the initial `"Y"` characters and moving the boundary across the string each take $O(n)$ time. The algorithm stores only the current penalty, best penalty, and best hour, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Prefix and suffix arrays:** Precomputing open-prefix `"N"` counts and closed-suffix `"Y"` counts also gives $O(n)$ time, but uses $O(n)$ auxiliary space unnecessarily.
- **Recount every closing hour:** Evaluating both sides independently for all $n+1$ boundaries is correct but takes $O(n^2)$ time.
- **Tied minimum:** Updating only on a strict improvement is essential because the contract requires the earliest hour.
- **All `"N"`:** The initial penalty is zero, so hour `0` remains the answer.
- **All `"Y"`:** The penalty decreases at every step, so hour $n$ is optimal.
- **Single hour:** Both legal boundaries are considered by the same initialization-and-update process.

