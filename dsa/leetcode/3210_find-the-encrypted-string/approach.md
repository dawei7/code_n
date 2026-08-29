## General

**Translate “$k$th character after” into an index.** Let the string length be $n$. The character originally at index `i` is replaced by the character reached after moving $k$ positions forward around the circle. Before wrapping, that position is $i+k$. Modulo $n$ maps it back into the valid index range:

$$
\textit{source}(i)=(i+k)\bmod n.
$$

Therefore the encrypted output must satisfy

`result[i] = s[(i + k) % n]`

for every index from zero through $n-1$.

The direction is important. Reading from `i+k` into output position `i` is a left rotation of the source by $k$ positions. It is not a right rotation, which would use `i-k`.

**Build a mutable output container.** Python strings are immutable, so individual character positions cannot be assigned. The source starts with `cs = list(s)`, producing a list of $n$ characters. It then overwrites every list entry with its encrypted source character.

The initial characters copied into `cs` are not logically needed because every position is replaced. The list is simply a convenient correctly sized mutable buffer. Crucially, each assignment reads from the original immutable string `s`, not from already modified `cs`. This prevents earlier writes from influencing later source lookups.

After the loop, `"".join(cs)` combines the characters into the required new string.

**Why modulo implements repeated cycling.** Moving forward by $n$ positions returns to the same character. Write

$$
k=qn+r,\qquad 0\le r<n.
$$

Then

$$
(i+k)\bmod n=(i+r)\bmod n.
$$

All $q$ complete laps disappear. The source does not explicitly assign `k %= n` once; it performs the equivalent reduction inside each index expression. This remains correct even when $k$ is much larger than the string.

**Why every output position is correct and unique.** The loop visits each output index exactly once. For index `i`, the formula is exactly the encryption rule, so the written character is correct. Modulo translation by a fixed $k$ is a permutation of indices: if two outputs read the same source index, then their index difference is divisible by $n$, which within $0$ through $n-1$ means the indices are equal. Thus every original character is used exactly once, consistent with a rotation rather than duplication or loss.

**Trace `s = "dart", k = 3`.** Here $n=4$:

- output $0$ reads source $(0+3)\bmod4=3$, which is `t`;
- output $1$ reads source $0$, which is `d`;
- output $2$ reads source $1$, which is `a`;
- output $3$ reads source $2$, which is `r`.

The resulting string is `"tdar"`.

For `"aaa"` and any offset, all looked-up characters are `a`. The positional rotation still occurs, but equal characters make it visually unchanged.

**Why the original string must remain the read source.** If one tried to update a mutable character array in place while also reading future characters from it, cycles could overwrite data before it was used. A true in-place rotation needs reversal or cycle-decomposition logic. The exact source avoids this hazard by maintaining separate immutable input and mutable output views.

## Complexity detail

Let $n$ be the length of `s`. Converting the string to a list takes $O(n)$ time. The loop performs $n$ constant-time index calculations and assignments. Joining the $n$ characters takes another $O(n)$ time. Total time is $O(n)$.

The character list uses $O(n)$ auxiliary space, and the returned string itself contains $n$ characters. Depending on whether required output storage is excluded, the working buffer alone already establishes $O(n)$ auxiliary space, matching the manifest.

The source performs a modulo operation for every character. Explicitly reducing `k` once would slightly reduce constant work but not change the asymptotic bound. The nonempty-string guarantee prevents division by zero in `% n`.

## Alternatives and edge cases

- **Slice rotation:** After `r = k % n`, return `s[r:] + s[:r]`. This is concise and $O(n)$ but still allocates the result and relies on recognizing the operation as a left rotation.
- **List comprehension:** `"".join(s[(i+k)%n] for i in range(n))` expresses the same mapping without first copying `s` into a list.
- **Repeated one-step rotation:** Applying the transformation $k$ times can cost $O(nk)$ and is unnecessary because modulo combines all steps.
- **In-place cycle replacement:** On a mutable array, permutation cycles can rotate with $O(1)$ auxiliary storage, but strings are immutable and the returned string still requires allocation.
- **$k$ smaller than $n$:** The formula moves directly to the desired later position.
- **$k$ equal to $n$:** Every index maps to itself, so the encrypted string equals `s`.
- **$k$ larger than $n$:** Complete laps vanish through modulo.
- **Length one:** Every offset maps index zero back to zero.
- **Repeated characters:** Rotation may look unchanged, but the index mapping remains correct.
- **All distinct characters:** Direction errors are easy to detect; the exact formula produces a left rotation.
- **Nonempty guarantee:** Without it, modulo by zero would fail. The contract provides at least one character.
- **Lowercase-only constraint:** Character content does not affect the algorithm; the guarantee merely bounds the alphabet.
- **Read from `s`, write to `cs`:** Keeping source and destination separate prevents overwrite corruption.
- **Input preservation:** Python strings are immutable, and the method returns a new string without changing `s`.
