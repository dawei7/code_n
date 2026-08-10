## General

The output must contain exactly the same character occurrences as the input, but characters with larger frequencies must form groups before characters with smaller frequencies. The exact solution follows that description directly:

1. Count how often every distinct character occurs.
2. Sort the distinct `(character, frequency)` pairs by decreasing frequency.
3. Recreate each character the counted number of times and join the groups.

The solution never sorts all `n` character occurrences. It sorts only the distinct characters, which is especially useful here because the source alphabet is restricted to uppercase English letters, lowercase English letters, and digits.

**Count frequencies with `Counter`**

`Counter(s)` scans the string and builds a mapping from each character to its number of occurrences. For `s = "tree"`, the mapping contains `t: 1`, `r: 1`, and `e: 2`. Uppercase and lowercase characters are different keys, so `A` and `a` are counted independently without any special logic.

A frequency map is the right summary because the desired order depends only on counts. Once it has been built, the original positions of equal characters no longer matter. The final construction will deliberately gather all copies of a character into one contiguous group.

**Why a negative sort key produces decreasing order**

`cnt.items()` supplies `(character, frequency)` pairs. Python's `sorted` orders keys in increasing order by default. The key function `lambda x: -x[1]` negates each frequency, so a larger original frequency becomes a smaller key:

$$
5 > 2 \quad\Longrightarrow\quad -5 < -2.
$$

Ascending order of the negative values is therefore descending order of the actual frequencies. The code does not need a secondary key. When two characters have equal frequency, either relative order is accepted by the contract.

Python's sort is stable, and `Counter` preserves the first-insertion order of keys in current Python versions, so tied groups commonly follow the order in which their characters first appeared. That behavior is not part of the algorithm's correctness and should not be relied upon by tests: the problem explicitly allows any tie order.

**Build one contiguous block per character**

For every sorted pair `(c, v)`, the expression `c * v` creates a string containing `v` copies of `c`. If the pair is `('e', 2)`, the group is `"ee"`. The generator supplies those groups to `''.join(...)`, which combines them into one output string.

Using `join` is important. Python strings are immutable, so repeatedly doing `answer += group` can repeatedly copy the growing prefix and lead to unnecessary quadratic work. `join` knows all pieces and constructs the final string efficiently.

For `s = "tree"`, the `e` group has frequency two and must come before the one-character `t` and `r` groups. Depending on tie order, the result may be `"eetr"` or `"eert"`; both are valid.

For `s = "cccaaa"`, the two groups both have frequency three. Either `"cccaaa"` or `"aaaccc"` is correct. An interleaving such as `"cacaca"` is not produced, because the reconstruction creates exactly one complete block for each distinct character.

For `s = "Aabb"`, `b` has frequency two, while `A` and `a` each have frequency one. The `bb` group comes first, and the case-distinct singletons may follow in either order.

**Why the result is a permutation of the input**

For each distinct character `c`, the counter stores exactly the number of occurrences of `c` in `s`. The construction emits exactly `cnt[c]` copies of that character. No other expression creates or removes characters. Summing the emitted group lengths gives

$$
\sum_c \texttt{cnt}[c] = n,
$$

so the output has the same length and the same frequency for every character as the input. It is therefore a permutation of `s`.

**Why the frequency order is valid**

The sorted pair sequence has nonincreasing frequencies because of the negative key. Each pair becomes exactly one contiguous group, and `join` preserves the pair order. Therefore every group before another has frequency greater than or equal to the later group's frequency. That is precisely the required ordering. Equal-frequency groups can appear in either order and remain valid.

## Complexity detail

Let $n$ be the length of `s`, and let $k$ be the number of distinct characters.

Building the counter takes expected $O(n)$ time and $O(k)$ mapping space. Sorting its $k$ entries takes $O(k\log k)$ time and $O(k)$ space for the sorted list, subject to the sorting implementation. Constructing all repeated groups and joining them processes exactly $n$ output characters, so it takes $O(n)$ time and $O(n)$ space for the required result and temporary pieces.

The most general bound is therefore

$$
O(n+k\log k) \text{ time and } O(n+k) \text{ space}.
$$

Under this problem's actual alphabet, $k\le 26+26+10=62$. Since `62` is a fixed constant independent of $n$, sorting the distinct entries is bounded by a constant amount of work asymptotically. The source-specific bounds simplify to $O(n)$ time and $O(n)$ space, matching the manifest. If the same code were used for an unrestricted alphabet where $k$ could grow to $n$, its worst-case time would instead be $O(n\log n)$.

The final output string necessarily occupies $O(n)$ space. Even if required output storage is excluded from auxiliary-space accounting, the generated group strings together contain $n$ characters before joining, so this exact Python expression still has linear peak storage.

## Alternatives and edge cases

- **Bucket sort by frequency:** Place each distinct character in a bucket indexed by its count, then scan frequencies from `n` down to `1`. This gives $O(n)$ time even for a growing alphabet, at the cost of an $O(n)$ bucket structure.
- **Heap of distinct characters:** A max-heap can repeatedly extract the largest frequency in $O(k\log k)$ time. It is useful for streaming variants but adds complexity here.
- **Sort all input characters:** A comparator based on frequency can sort all `n` occurrences, but that costs $O(n\log n)$ and must still ensure identical characters remain grouped.
- **Repeated string concatenation:** Logically correct, but immutable-string copying can make construction quadratic. Building pieces and calling `join` avoids that trap.
- **Single character:** The counter has one entry, sorting changes nothing, and the original one-character string is returned.
- **All characters identical:** One group of length `n` is emitted, so the answer equals the input.
- **All frequencies equal:** Any ordering of the character groups is valid; the algorithm's stable tie order is merely one allowed choice.
- **Uppercase versus lowercase:** `A` and `a` are separate counter keys and may have different frequencies.
- **Digits:** Digits are ordinary one-character keys; numeric value plays no role.
- **Empty string outside this contract:** The exact code would return an empty string naturally, although the stated input is nonempty.
