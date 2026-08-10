## General

A strobogrammatic string must agree with itself after a 180-degree rotation. Rotation reverses positions, so digits must be chosen in mirrored pairs. The only legal outside-to-inside pairs are

```text
"00", "11", "69", "88", "96"
```

The pair's order is significant: a left `6` becomes the right `9`, while a left `9` becomes the right `6`. The pairs `00`, `11`, and `88` use digits that rotate into themselves.

Instead of choosing all $n$ positions independently and later filtering invalid strings, the exact solution generates only valid structures. It first generates every valid inner string of length `u - 2`, then wraps each inner string with every mirrored pair allowed at the current depth.

**The helper's precise promise**

`dfs(u)` returns all strobogrammatic strings of length `u` that may be used as the current inner portion of the final length-`n` number. Inner portions are allowed to begin with `0`; only the outermost digit of the final number is forbidden from being zero.

That distinction explains why the helper needs access to the original `n` through its closure. At an internal level, `u != n`, so wrapping with `"0" + v + "0"` is allowed. At the outermost level, `u == n`, so `00` is skipped to prevent a leading zero.

**Why construction begins at the center**

Every recursive call decreases the remaining length by two, corresponding to reserving one position at each end. The parity never changes, so there are two base cases.

- For `u == 0`, return `['']`. The empty string acts as the neutral center of an even-length number. Wrapping it with `11`, for example, produces `11`.
- For `u == 1`, return `['0', '1', '8']`. An odd-length number has one center position that maps to itself, and only these three digits do so.

The empty-string base case is especially important. If the recursion instead began with only the valid two-digit numbers, it would omit `00` as an inner block and could never generate valid values such as `1001` or `6009`.

**How each recursive level expands the inner results**

For every inner string `v`, the loop always creates four wrappers:

```text
"1" + v + "1"
"8" + v + "8"
"6" + v + "9"
"9" + v + "6"
```

It deliberately leaves `00` out of that tuple and appends it separately only when `u != n`. This layout makes it impossible to accidentally generate a final number with a leading zero while still permitting zeros at internal mirrored positions.

For `n = 2`, `dfs(0)` produces `['']`. The outer `dfs(2)` wraps the empty center with the four nonzero pairs, yielding `['11', '88', '69', '96']`. The `00` pair is skipped because `u == n`.

For `n = 4`, recursion first computes `dfs(2)` as an **inner** level. Here `u = 2` differs from the final `n = 4`, so it includes `['11', '88', '69', '96', '00']`. The outer level wraps each of those five centers with four nonzero pairs. This includes values such as `1001`, whose inner `00` is necessary even though an outer leading zero would be invalid.

**Odd-length example**

For `n = 3`, `dfs(1)` returns the three legal centers `0`, `1`, and `8`. Wrapping each center with four nonzero outer pairs creates twelve results:

```text
101, 111, 181
808, 818, 888
609, 619, 689
906, 916, 986
```

The order follows the exact nested loops rather than numeric order, which is acceptable because the contract permits any order.

**Why every generated string is valid**

The base strings are strobogrammatic: the empty string is trivially symmetric, and each one-digit base rotates into itself. Assume an inner string `v` is strobogrammatic. Wrapping it with one of the allowed pairs places two digits that rotate into each other and swap positions, while the interior still rotates into itself. The resulting longer string is therefore strobogrammatic. At the outermost level, excluding `00` also ensures the string represents an actual $n$-digit number without a leading zero.

**Why no valid number is missed**

Take any valid length-`u` strobogrammatic string. Its first and last digits must form one of the five allowed pairs. Removing those digits leaves a strobogrammatic inner string of length `u - 2`, which appears in the recursive result by the same reasoning. If `u` is the full requested length, the first digit cannot be zero, so the outer pair is one of the four always generated. If `u` is internal, `00` is also generated. Thus the loops reconstruct every valid string. Because its outer pair and inner string uniquely identify it, no string is generated twice.

The recursion is not doing branching recursive calls. Each `dfs(u)` calls `dfs(u - 2)` exactly once, then expands the returned list. Memoization is unnecessary because no length state is recomputed.

## Complexity detail

Let $h=\lfloor n/2\rfloor$, the number of mirrored position pairs. For even $n=2h$ with $h\ge1$, the outer pair has four choices and each of the remaining $h-1$ inner pairs has five choices, so the exact result count is

$$
4\cdot5^{h-1}.
$$

For odd $n=2h+1$ with $h\ge1$, there are additionally three center choices, giving

$$
3\cdot4\cdot5^{h-1}.
$$

For `n = 1`, there are simply three outputs. In asymptotic notation, the output count is $\Theta(5^{n/2})$ up to parity-dependent constants.

Each final string has length $n$, and Python string concatenation copies characters. Producing and storing the explicit output therefore takes $O(n\cdot5^{n/2})$ time and space in coarse notation. This is output-optimal up to constant factors because returning all strings already requires writing that many characters.

The recursion depth is $O(n)$ in conventional notation, more precisely $\lceil n/2\rceil$. Intermediate lists from adjacent construction levels coexist temporarily, but the geometric growth means the final level dominates their total size. The stack itself is negligible compared with the output-sized storage.

## Alternatives and edge cases

- **Backtracking into a fixed character array:** Fill mirrored positions from the outside inward and emit a copy at the center. It generates the same search space and can avoid repeatedly concatenating intermediate strings, though each completed answer still needs an $O(n)$ copy.
- **Iterative center expansion:** Start with `['']` for even `n` or `['0', '1', '8']` for odd `n`, then wrap level by level. It mirrors this recursion exactly and removes call-stack usage.
- **Generate all digit strings and filter:** Trying $10^n$ strings ignores the strong pair constraints and is exponentially much larger than generating only valid candidates.
- **`n = 1`:** Return `0`, `1`, and `8`. These are the only digits unchanged by rotation and `0` is a valid one-digit number.
- **`n = 2`:** The inner empty string is wrapped by the four nonzero pairs. `00` is excluded because it is not a two-digit number.
- **Zeros inside longer numbers:** Internal `00` pairs are necessary. Values such as `1001` are valid even though `0000` is not a valid four-digit result.
- **Leading zero:** The condition `u != n` is what distinguishes an internal layer from the final outer layer. Removing it would generate strings whose written length is `n` but whose numeric representation has fewer digits.
- **Odd center `6` or `9`:** These digits rotate into each other rather than themselves, so neither can occupy the fixed center position.
- **Pair orientation:** `69` and `96` are both valid and distinct. Pairs `66` and `99` are invalid because each digit rotates into the other digit, not itself.
- **Output ordering:** The exact code emits wrappers in the order `11`, `88`, `69`, `96`, followed by internal `00`. Sorting is unnecessary and would add work because any return order is accepted.
- **Duplicate generation:** Each result has one unique sequence of outer pairs and optional center, so different construction paths cannot produce the same string.
