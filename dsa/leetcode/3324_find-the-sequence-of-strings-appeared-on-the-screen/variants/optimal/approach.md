## General

When constructing the character at target position $i$, key 1 is mandatory: it is the only operation that increases screen length, and it creates that position as `a`. Record the resulting screen immediately because every post-press state belongs in the answer.

Key 2 affects only the last character. Starting from `a`, advance that new character one step at a time until it equals `target[i]`, recording the complete screen after every advance. Advancing past the desired character and wrapping around would add 26 unnecessary presses, so the direct alphabetical path is uniquely minimal. Earlier positions already match the corresponding target prefix and remain untouched.

After finishing position $i$, the screen equals `target[:i + 1]`. This establishes the condition needed for the next iteration and, at the final position, proves that the simulation ends at `target`. Every mandatory append and every necessary increment is recorded exactly once and in execution order.

## Complexity detail

Let $n=\lvert\texttt{target}\rvert$, and let $R$ be the total number of characters across all returned screen states. At position $i$, at most 26 states of length $i+1$ are emitted, so $R=O(n^2)$ because the alphabet size is constant. Joining the current character list once per state takes $O(R)=O(n^2)$ total time. The returned strings occupy $O(R)=O(n^2)$ space, while the mutable screen itself uses only $O(n)$ auxiliary space. The output size supplies a matching $\Omega(R)$ lower bound.

## Alternatives and edge cases

- **Recompute every earlier prefix:** Replaying the simulation from the empty screen for each target prefix duplicates already produced work and can take $O(n^3)$ character processing.
- **Use alphabet wraparound:** Beginning at `a`, wrapping past `z` can never shorten the route to a lowercase target character.
- **Append the desired character directly:** Key 1 always appends `a`; skipping that visible state violates both the keyboard rules and the required output.
- **Target character a:** Record only the append state for that position because no increment is necessary.
- **Target character z:** Record all 26 states for that new position, from `a` through `z`.
- **Repeated characters:** Each position is independent; even when it matches the previous character, the new position still starts at `a`.
- **Output cost:** Complexity must include copying every returned screen string, not merely counting key presses.
