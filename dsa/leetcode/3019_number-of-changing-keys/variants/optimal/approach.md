## General

**Separate a physical key from the case of the character.** The string records typed letters, but uppercase and lowercase versions of the same English letter represent the same keyboard key. A “change” happens only when two consecutive characters, after ignoring case, name different letters. For example, moving from `'a'` to `'A'` is not a key change, while moving from `'A'` to `'b'` is.

The exact solution expresses that definition in one line:

`return sum(a != b for a, b in pairwise(s.lower()))`

Each part has a specific job. First, `s.lower()` creates a normalized string in which case can no longer affect equality. Next, `pairwise(...)` produces consecutive overlapping pairs:

$$
(s_0,s_1), (s_1,s_2), \ldots, (s_{N-2},s_{N-1}).
$$

Finally, `a != b` is `True` exactly when that adjacent boundary changes keys. Python treats `True` as 1 and `False` as 0, so summing these comparisons counts the changes.

**Why adjacent comparisons are enough.** Typing begins on the first character's key. That initial placement is not described as a change, so there is nothing to count before index 0. For every later position $i$, precisely one question matters: is the normalized character at $i$ different from the normalized character at $i-1$? If yes, the user changed keys once at that boundary. If no, the same key continued. There are exactly $N-1$ such boundaries, and every possible key change occurs at one of them.

This also explains why the method must not count distinct letters globally. The string `"ababa"` contains only two different keys but changes keys four times. Conversely, `"aaaa"` has one distinct key and zero changes. The answer describes transitions in sequence order, not the size of a set.

**Normalization before pairing avoids subtle case errors.** One could compare `a.lower()` and `b.lower()` for every pair, but normalizing the entire string once makes the logic easier to read. Suppose the input is `"aAaBb"`. Lowercasing produces `"aaabb"`. Its adjacent comparisons are equal, equal, different, equal, so the answer is one. That agrees with the physical sequence: the first three characters use the A key, then typing moves once to the B key and stays there.

**Why summing Booleans is correct.** In Python, `bool` is an integer-like type: `False` contributes zero and `True` contributes one to `sum`. The generator does not build a separate list of comparison results. It requests one adjacent pair at a time, evaluates inequality, and passes that Boolean to `sum`. The accumulator after processing the first $t$ boundaries is therefore exactly the number of changes among those $t$ boundaries.

This provides a simple loop invariant. Before the generator examines the pair ending at normalized index $i$, the running sum equals the number of key changes through index $i-1$. The new comparison adds one exactly if the boundary from $i-1$ to $i$ changes the normalized letter. Hence afterward the sum is correct through index $i$. Induction over all boundaries proves the returned result.

**The input constraint makes lowercase normalization semantically safe.** The problem uses English letters. For these characters, lowercasing maps an uppercase letter to its matching lowercase letter and leaves an already lowercase letter unchanged. There are no locale-dependent multi-character case conversions to consider under this contract. The normalized string therefore has the same length and positions as the input.

**A step-by-step trace.** For `s = "aAbBcCaa"`, normalization gives `"aabbccaa"`. The pairs are `("a","a")`, `("a","b")`, `("b","b")`, `("b","c")`, `("c","c")`, `("c","a")`, and `("a","a")`. Their inequality values are 0, 1, 0, 1, 0, 1, 0. The sum is 3. Notice that repeated runs contribute nothing internally; only the boundary between runs contributes.

## Complexity detail

Let $N$ be the length of `s`. Python's `s.lower()` visits all $N$ characters and constructs a new normalized string, taking $O(N)$ time and $O(N)$ space. `pairwise` then traverses the normalized string once and `sum` performs one comparison for each of the $N-1$ adjacent pairs, taking another $O(N)$ time.

The total time is $O(N)$. For this exact Python source, the auxiliary space is $O(N)$ because the lowercased string is a distinct string object. The generator returned by `pairwise` and the generator expression themselves keep only a constant number of references at a time.

The local manifest labels the space bound $O(1)$, which would fit a manual scan that lowercases one character at a time. It does not accurately describe `s.lower()` in the protected implementation. The input is not mutated—Python strings are immutable—and the returned integer takes $O(1)$ result space.

## Alternatives and edge cases

- **Manual one-pass normalization:** Keep the lowercase form of only the previous character, lowercase each new character, compare, and update the previous value. That preserves $O(N)$ time while reducing auxiliary space to $O(1)$, but it is not the exact implementation shown here.
- **Compare character codes with a fixed offset:** ASCII arithmetic can ignore case, but it is less clear and easier to get wrong. The language's lowercase operation directly communicates the intended equivalence.
- **Count runs after normalization:** The answer equals the number of normalized runs minus one. Building or grouping all runs works, but directly counting unequal adjacent pairs obtains the same value with less machinery.
- **Count distinct normalized letters:** This is incorrect because a key may be revisited many times. `"ababa"` has two distinct keys but four changes.
- **Length-one string:** `pairwise` yields no pairs, and `sum` of an empty generator is zero. This correctly represents typing one key without changing from a previous key.
- **Every character has the same letter in mixed case:** Lowercasing makes all adjacent pairs equal, so the answer is zero.
- **Every adjacent character differs:** Every one of the $N-1$ comparisons is true, producing the maximum possible answer $N-1$.
- **A key is revisited:** A sequence such as `"aba"` changes at both boundaries. The fact that A appeared before does not cancel the later transition back to it.
- **Input preservation:** `lower()` returns a new string rather than editing `s`, so the caller's original casing remains intact.
- **Space accounting:** Calling the generator lazy does not make the whole expression constant-space, because the complete lowercase string already exists before `pairwise` begins.
