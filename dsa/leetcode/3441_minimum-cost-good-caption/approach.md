## General

**A good caption is a sequence of runs, each of length at least three.** Changing one letter with repeated previous/next alphabet operations costs the absolute difference between its alphabet indices. If original character $x$ becomes character $c$, its cost is

$$
\lvert \operatorname{index}(x)-\operatorname{index}(c)\rvert.
$$

The source converts every input letter to an integer from $0$ through $25$ so this cost is a direct absolute value.

If $n<3$, no non-empty run can reach the minimum length, and changing letters cannot alter the caption length. The method correctly returns the empty string immediately.

**Define the suffix state after a valid run already exists.** For a letter `last` and position $i$, `dp[last][i]` is the minimum cost to complete positions $i$ through $n-1$, assuming the output immediately before $i$ already ends in a valid run of `last` containing at least three characters.

From this state there are only two legal actions.

**Extend the current run by one character.** Change `caption[i]` to `last` and continue from $i+1$ with the same last character:

`abs(values[i] - last) + dp[last][i + 1]`.

The run was already at least three characters long, so extending it preserves validity. This action also handles one or two leftover positions near the end.

**Start a different run with three characters.** If at least three positions remain, choose `char != last`, change positions $i$, $i+1$, and $i+2$ to that character, and continue at $i+3$:

`abs(values[i] - char) + abs(values[i + 1] - char) + abs(values[i + 2] - char) + dp[char][i + 3]`.

Starting with three copies immediately makes the new run valid. Requiring `char != last` is natural: choosing the same character would merely extend the existing run and is already represented more flexibly by repeated extension.

At `i == n`, the suffix is empty and costs zero, which is why the preallocated DP columns begin with zero at the terminal position. When fewer than three characters remain, switching is forbidden and only extension can reach the end.

**Find the best different next character in constant alphabet time.** A direct transition could, for each of $26$ values of `last`, scan all $26$ possible new characters. The alphabet is fixed, so even that is asymptotically linear, but the source uses the smallest and second-smallest three-character switch costs.

For each $i$ with at least three positions remaining, it computes the switch value for every `char` and remembers:

- `best_value` and its `best_char`;
- `second_value`, the next smallest value.

Then the cheapest switch excluding `last` is `second_value` when `best_char == last`, otherwise `best_value`. Equal costs are handled correctly: the `elif value < second_value` branch may store another value equal to the best, so excluding one best character can still use a tied alternative.

For every `last`, the DP stores the smaller of extension and this allowed switch.

**Choose the first run separately.** Before position zero, no valid previous run exists. The caption must begin with at least three equal characters. The source tries every first character:

`abs(values[0] - char) + abs(values[1] - char) + abs(values[2] - char) + dp[char][3]`.

The loop visits letters from `a` to `z` and replaces `first_char` only on a strictly smaller cost. Therefore, cost ties keep the lexicographically smallest first output character.

**Reconstruct the lexicographically smallest minimum-cost caption.** The answer begins with three copies of `first_char`. At a later state $(last,i)$, `target = dp[last][i]` is the optimal remaining cost.

The source first checks whether extending `last` attains `target`. It then checks every different three-character switch that also attains `target`. Among all optimal actions, `chosen` becomes the smallest next character.

This greedy tie-breaking is correct because lexicographic order is decided at the first position where two outputs differ. Every considered action is already guaranteed by the DP to achieve the same minimum total cost. Choosing the smallest immediate output character therefore yields the smallest entire optimal suffix; future ties are resolved in the same way at later states.

If `chosen == last`, reconstruction appends one character and advances by one. Otherwise, it appends three copies of the new character and advances by three. Every created run consequently begins with three letters and can only grow through extensions.

**Why the DP describes all good captions.** Any good suffix following an established run either continues that run at its next position or begins a different run. A different run must contain at least three positions, so its first three letters can be taken together exactly as the switch transition does. These cases are exhaustive and disjoint. Backward induction proves every DP cost is minimal, and the reconstruction follows only equal-cost transitions.

The sentinel `inf = 2_000_000` safely exceeds the largest possible real cost: at most $25$ changes per character across at most $50{,}000$ positions, or $1{,}250{,}000$.

The table uses unsigned integer arrays. All stored real costs and the sentinel are nonnegative and fit the chosen representation.

## Complexity detail

Let $n=\lvert\texttt{caption}\rvert$ and let the alphabet size be $A=26$. For every position, the source scans $A$ characters to obtain switch minima and scans $A$ last-character states. Reconstruction may scan $A$ switch characters per output decision. Total time is $O(An)$, which is $O(n)$ because $A$ is fixed.

The DP stores $A(n+1)$ integers, using $O(An)=O(n)$ space. The numeric input values and reconstructed output also use $O(n)$ space. These bounds match the manifest.

## Alternatives and edge cases

- **Backtrack over all run partitions and letters:** The number of captions is exponential. The suffix state merges all histories that share the current run letter.
- **Store whole best strings in DP:** It simplifies tie-breaking conceptually but can require quadratic copying and enormous memory. Numeric costs plus greedy reconstruction avoid that.
- **Start a run with one character:** That could leave an invalid short run if a later switch occurs. Every new run must commit three characters immediately.
- **Final one or two positions:** They cannot start a new run, but they can extend the already valid current run.
- **Caption shorter than three:** No good caption of the same length exists, so the empty result is required.
- **Caption length exactly three:** The first-run enumeration chooses the cheapest common character, breaking ties alphabetically.
- **Adjacent runs with the same letter:** They are really one run. The DP represents them through extension and forbids a redundant same-letter switch.
- **Cost ties:** Strict comparison selects the smallest first character, and reconstruction selects the smallest next character among all optimal transitions.
- **Large sentinel:** It must exceed every achievable cost so an impossible switch never wins; the stated bound proves this sentinel is safe.
- **Run length greater than three:** Repeated extension naturally creates runs of any larger length.
