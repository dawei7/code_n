## General

**Parse the original input from left to right**

The parser recognizes exactly six encoded strings and replaces each recognized source token with one character. The dictionary `d` is the complete translation table used by the implementation:

| Source token | Appended character |
|---|---|
| `&quot;` | `"` |
| `&apos;` | `'` |
| `&amp;` | `&` |
| `&gt;` | `>` |
| `&lt;` | `<` |
| `&frasl;` | `/` |

The algorithm maintains index `i` as the first unconsumed position in the original `text`. Everything before `i` has already been translated exactly once and represented in `ans`. Everything from `i` onward is still untouched source input.

This one-pass viewpoint is important for nested-looking text. If the source contains `&amp;gt;`, the parser recognizes `&amp;`, appends a literal ampersand, and later copies the remaining characters `gt;`. It returns `&gt;`; it does not recursively parse the ampersand it just produced. Appended output is never fed back into the input scan.

**Why only lengths one through seven are tested**

At each position, the inner loop tries:

```python
for l in range(1, 8):
    j = i + l
```

Python's upper range boundary is excluded, so `l` takes values from 1 through 7. Seven is the length of the longest supported token, `&frasl;`. No valid entity can require a longer slice.

The shorter tokens also fall within that range: `&gt;` and `&lt;` have length four, `&amp;` has length five, `&quot;` and `&apos;` have length six, and `&frasl;` has length seven.

Trying slices that extend beyond the end is safe in Python. `text[i:j]` simply stops at the string boundary rather than raising an error. Those shorter suffixes will not equal a complete dictionary key unless a complete token is actually present.

**Recognizing and consuming an entity**

For every candidate ending position `j`, the code asks whether `text[i:j]` is a key in `d`. If it is, the same slice retrieves the replacement:

```python
ans.append(d[text[i:j]])
i = j
break
```

Appending the dictionary value emits exactly one decoded character. Setting `i = j` consumes the entire source entity, including its leading ampersand and trailing semicolon. The `break` exits the length loop so the entity cannot also be copied character by character.

The code checks lengths from shortest to longest. This is safe for this fixed dictionary because no supported entity token is a complete prefix of another supported token. There is therefore no situation where an early shorter match steals the beginning of a different valid longer match.

**The `for`-`else` is the non-entity path**

Python attaches the `else` to the `for` loop, not to the inner `if`. That `else` runs only if all seven candidate lengths finish without executing `break`:

```python
else:
    ans.append(text[i])
    i += 1
```

When no supported token starts at `i`, the current character must remain unchanged. The code appends that one character and advances by one position. This behavior preserves ordinary letters, spaces, punctuation, lone ampersands, incomplete entities, and unknown strings such as `&ambassador;`.

Every iteration advances `i` by at least one. A match advances it by the token length, while a non-match advances it by one. Thus the outer `while i < n` loop cannot become stuck.

**Why scanning every position works**

The code does not first test `text[i] == '&'`. At an ordinary position it still tries up to seven short slices, none of which can be dictionary keys because every key starts with an ampersand. This adds a small constant amount of work but keeps the control flow uniform.

The result is accumulated as a list rather than with repeated string concatenation. Python strings are immutable, so repeatedly extending one can copy the growing prefix. `ans.append` records pieces efficiently, and `''.join(ans)` performs one final construction.

**A representative trace**

Consider the source fragment `x&amp;y&bad;z`.

1. At `x`, no key matches, so `x` is copied.
2. At the first ampersand, lengths one through four do not form a key. Length five produces `&amp;`, so `&` is appended and all five source characters are consumed.
3. `y` is copied.
4. At `&bad;`, no supported key matches. The ampersand is copied, then later iterations copy `b`, `a`, `d`, and the semicolon.
5. `z` is copied.

The output is `x&y&bad;z`. Known entities change, while unknown entity-like text is preserved exactly.

**Why the parser is correct**

Maintain the invariant that `ans` is the correct parsing of `text[:i]`. Initially, both are empty. If a supported entity begins at `i`, the dictionary maps that complete source token to its required character, and advancing to `j` extends the invariant over the entire token. If none begins there, the rules require `text[i]` to remain literal, so copying it extends the invariant by one character. These are the only two possibilities.

When `i == n`, the invariant covers the entire input. Joining the accumulated characters therefore returns exactly one nonrecursive replacement of every supported entity and preserves every other character.

## Complexity detail

Let $n$ be the number of characters in `text`. The outer loop consumes at least one source character per iteration, so it runs at most $n$ times. Each iteration checks at most seven candidate lengths. Every tested slice has length at most seven, and dictionary lookup involves one of these constant-size strings. The work per outer iteration is therefore bounded by a constant, giving $O(n)$ time.

The answer list contains at most $n$ appended characters because an entity shortens several source characters to one and a non-match contributes exactly one. The final output also has length at most $n$. Hence output construction uses $O(n)$ space. The dictionary has exactly six fixed entries and all counters are constant-size, so auxiliary state excluding output is $O(1)$.

Although the same slice may be formed once for membership and again for dictionary access on a successful length, each slice is at most seven characters. That duplication changes only a constant factor, not the linear bound.

## Alternatives and edge cases

- **Check for ampersand first:** Copy ordinary characters immediately and test entities only when `text[i] == '&'`. This reduces constant work while keeping the same $O(n)$ complexity and semantics.
- **Trie of entity tokens:** A trie can consume characters until a token matches or fails. It becomes attractive with a large or extensible entity vocabulary, but six tokens of maximum length seven do not require that machinery.
- **Repeated global replacement:** Calling `replace` once per entity is concise but scans the full string several times and can accidentally introduce ordering questions when one replacement produces text resembling another entity.
- **Regular expression:** A pattern can find supported tokens and use a callback dictionary. It is valid but hides the straightforward consumption invariant behind regex behavior.
- **Recursive decoding:** Parsing newly produced output again is incorrect for this task. `&amp;gt;` should undergo the source scan once rather than automatically becoming `>` through two rounds.
- **Unknown entity-like text:** A string such as `&ambassador;` is not a dictionary key, so every character is preserved.
- **Incomplete entity:** A trailing fragment such as `&quo` never matches a complete key and remains unchanged.
- **Adjacent entities:** After one match sets `i` to its end, the next outer iteration begins exactly at the following entity and decodes it independently.
- **Ordinary ampersand:** A lone `&` fails all token tests and is copied literally.
- **Longest entity:** `&frasl;` is found when `l == 7`; using `range(1, 7)` would miss it because the upper bound is exclusive.
- **Quotes and apostrophes:** The dictionary values use appropriate Python quoting but each represents a single literal output character.
- **All ASCII input:** Characters outside the six supported source sequences pass through unchanged, regardless of whether they have special meaning in broader HTML standards.
