## General

**The unknown word boundaries require backtracking**

Each pattern character must map to a nonempty substring, but the input does not say how long that substring is. For pattern `"abab"` and target `"redblueredblue"`, the successful boundaries are `red | blue | red | blue`, yet the first `a` could initially be tried as `"r"`, `"re"`, `"red"`, or many longer prefixes.

The algorithm must explore possible substring boundaries and abandon a choice when later pattern positions become inconsistent. That is a backtracking search.

The exact helper `dfs(i, j)` means that pattern positions before `i` have already expanded to exactly the target prefix before index `j`. Its task is to decide whether `pattern[i:]` can expand to `s[j:]` under the current mapping.

**Store both sides of the bijection constraint**

Dictionary `d` maps an assigned pattern character to its chosen substring. This enforces the function property: once character `a` maps to `"red"`, every later `a` must use exactly `"red"`.

Set `vis` stores every substring already assigned to some character. A new pattern character may use candidate `t` only when `t not in vis`. This enforces injectivity: two different characters cannot map to the same substring.

Together, the character-to-substring map and used-substring set enforce a bijection between the pattern characters that occur and their assigned target substrings.

**Base cases require both suffixes to finish together**

If `i == m` and `j == n`, both the pattern and target have been consumed exactly, so the current mapping is a complete match and the helper returns true.

If only one index reaches its end, the branch returns false. A finished pattern cannot explain leftover target characters, and a finished target cannot supply the nonempty substring required by remaining pattern positions.

Testing the joint-success case first matters: when both indices reach their ends, it must return true rather than being caught by the one-end failure condition.

**Prune when too few target characters remain**

Every remaining pattern occurrence needs at least one target character because mappings must be nonempty. There are `m - i` pattern positions and `n - j` target characters left. If

$$
n-j<m-i,
$$

even assigning one character to every remaining occurrence is impossible, so the source returns false immediately.

This is a safe necessary-condition prune, although it is not the strongest possible one. A character already mapped to a multi-character substring may require more than one target character. The exact source checks only the universal one-character minimum and lets ordinary matching reject tighter impossibilities later.

**Generate every nonempty substring starting at `j`**

The loop chooses endpoint `k` from `j` through `n - 1` and sets `t = s[j : k + 1]`. The shortest candidate has one character; increasing `k` tries every longer target prefix through the entire remaining suffix.

Because `k + 1 > j`, an empty mapping is never generated. Every recursive call advances target index to `k + 1`, so successful paths consume target characters monotonically and cannot reuse or reorder them.

**When the pattern character is already mapped**

If `pattern[i]` already has mapping `d[pattern[i]]`, the current target prefix must equal that exact string. The source compares the mapping with each grown candidate `t`. When equality occurs, it recursively advances to the next pattern position and the endpoint after `t`.

If that recursive call succeeds, the helper returns true immediately. If it fails, the loop continues, but no other candidate length can equal the one fixed mapping. The exact implementation nevertheless keeps growing substrings through the loop. A more direct implementation could use `s.startswith(mapped, j)` and make at most one recursive call; that would be a performance refinement, not a different search result.

While a character is mapped, the new-assignment branch is disabled by `pattern[i] not in d`, so the existing character can never silently acquire a second substring.

**When the pattern character is new**

For an unseen character, every candidate `t` not already in `vis` is a possible new assignment. The source records it in both structures:

```text
d[pattern[i]] = t
vis.add(t)
```

It then recurses on the next pattern position and the target suffix after `t`.

If that recursive branch succeeds, the mapping completes a valid match and true propagates immediately to the caller. If it fails, the source removes the dictionary entry and set member before trying the next candidate:

```text
d.pop(pattern[i])
vis.remove(t)
```

This restoration is backtracking. Without it, a failed guess would remain visible in sibling branches and incorrectly forbid other assignments. After restoration, the mapping state is exactly what it was before trying `t`.

**Why `vis` is necessary even with consistent character mappings**

Consider pattern `"ab"` and target `"aa"`. Without `vis`, the search could assign both `a -> "a"` and `b -> "a"`, concatenate them to the target, and incorrectly return true. The dictionary alone prevents one character from changing values but does not prevent two characters from sharing a value.

When `a -> "a"` is active, `"a"` is in `vis`, so the new character `b` cannot select it. Other splits fail, and the correct result is false.

**Why the search is complete**

Suppose a valid bijection exists. At state `(i, j)`, the mapping's next expansion is some nonempty substring `s[j : k + 1]`. The endpoint loop tries that exact `k`.

If the character was seen earlier, the valid bijection requires the candidate to equal its stored mapping, so the existing-mapping branch follows it. If the character is new, bijectivity guarantees its substring is not in `vis`, so the new-assignment branch records it. Repeating this argument reaches `(m, n)` and returns true.

Conversely, any branch that reaches `(m, n)` has consumed all of `s` in consecutive nonempty pieces. Repeated characters were allowed to advance only through their one stored string, and new characters were assigned only unused strings. The active mapping is therefore bijective and its expansion is exactly `s`, so every reported success is valid.

**Trace the first example conceptually**

For `pattern = "abab"` and `s = "redblueredblue"`, many short guesses fail. On the successful branch:

1. assign `a -> "red"` and mark `"red"` used;
2. assign `b -> "blue"` and mark `"blue"` used;
3. encounter `a` again and match the next `"red"` exactly;
4. encounter `b` again and match the final `"blue"` exactly;
5. reach the ends of both strings together.

For `pattern = "aaaa"` and `s = "asdasdasdasd"`, assigning `a -> "asd"` lets each later `a` consume the same three-character substring, producing a valid result.

For the third example, every possible set of boundaries or assignments eventually causes a mapped-substring mismatch, a reused-substring conflict, a suffix-length failure, or unequal completion, so the search returns false.

## Complexity detail

Let $n$ be the target length and $p$ the pattern length. A complete expansion partitions `s` at some subset of its $n-1$ internal gaps. There are at most $2^{n-1}$ such boundary patterns. Mapping and bijection constraints prune many of them, but exponential exploration remains possible.

Creating and comparing Python substrings can cost $O(n)$ along a branch. A conventional conservative bound is therefore $O(n\cdot2^n)$ time, matching the manifest. If $p>n$, the minimum-suffix prune rejects immediately; otherwise $p\le n$ on branches that survive the initial feasibility check.

Recursion depth is at most $p$. Along one active branch, the distinct mapped substrings are disjoint contributions to the consumed target structure in a successful-style assignment, and their combined content is bounded by $O(n)$. The dictionary and set hold at most one entry per distinct pattern character, so auxiliary state is $O(n+p)$, including the recursion stack, matching the manifest.

Python substring slices are separate string objects. Temporary candidates and active mapped strings contribute to that same linear-content reasoning for the conventional bound, though failed-loop temporaries are released as later candidates replace them. The method returns one Boolean and stores no list of solutions.

## Alternatives and edge cases

- **Direct jump for mapped characters:** Retrieve the one mapped word, check `s.startswith(word, j)`, and recurse once. This avoids constructing every longer candidate when the character is already assigned and is the main local optimization missing from the exact source.
- **Stronger remaining-length pruning:** Sum the known mapped lengths for remaining pattern occurrences and one for each unknown occurrence. This can cap candidate endpoints much earlier than the source's simple `n - j < m - i` check.
- **Map without a used set:** Incorrect because two pattern characters could receive the same substring, violating bijectivity.
- **Used set without a map:** It cannot force repeated occurrences of one pattern character to reuse the same substring.
- **One-character mappings:** They are valid; the endpoint loop begins at `k = j`.
- **Empty mappings:** They are forbidden and never generated because every slice ends at least one position after `j`.
- **Repeated pattern character:** It must match its stored substring exactly at every occurrence.
- **All pattern characters distinct:** The search partitions `s` into nonempty pairwise-distinct substrings.
- **Pattern longer than target:** The minimum-length prune returns false at the root.
- **Both inputs exhausted:** This is the only successful base case.
- **Target exhausted first:** Remaining pattern positions cannot receive nonempty strings, so the branch fails.
- **Pattern exhausted first:** Unconsumed target characters make the expansion incomplete, so the branch fails.
- **Failed assignment restoration:** Both `d` and `vis` must be restored. Removing only one would leave the two bijection structures inconsistent.
- **Early success:** Because the return value is Boolean rather than all mappings, the source stops at the first valid assignment.
- **Lowercase alphabet:** At most 26 distinct character keys can occur, though repeated positions still determine recursion depth.
