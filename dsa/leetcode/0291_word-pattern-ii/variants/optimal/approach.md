## General
**Why this is not ordinary pattern matching**

The pattern does not say where one replacement ends and the next begins. For `pattern = "ab"`, every split of `s` into two nonempty pieces is initially possible. The algorithm must discover both the boundaries and the character assignments, which naturally leads to backtracking.

**The search state**

Two positions describe how much of each input has been consumed. A character-to-substring map remembers established
meanings, while a set of used substrings enforces the reverse direction of the bijection.

If the next pattern character is already mapped, there is no branching: its known substring must occur at the current
target position. If it is new, each nonempty prefix of the remaining target is a possible assignment, except prefixes
already used by another character. Each tentative pair is removed from both structures when its recursive branch
fails.

**Leave enough text for the suffix**

A candidate cannot consume characters needed by later pattern positions. For each remaining occurrence, an assigned
character needs the full length of its known substring and an unassigned character needs at least one character. This
safe lower bound limits the last candidate endpoint and cuts off impossible branches before recursion.

For `pattern = "abab"` and `s = "redblueredblue"`, a successful branch assigns `a -> "red"` and `b -> "blue"`. The
final two pattern positions then perform direct prefix checks; they do not branch again.

**Why the search is complete**

Any valid substitution determines a sequence of substring endpoints. When the search first encounters a character,
it tries the endpoint used by that substitution; later occurrences follow the stored value. Therefore the valid
sequence is among the explored branches. A branch is accepted only when both inputs end together, so partial or
overlong matches cannot succeed.

## Complexity detail
Let $n = \lvert\texttt{s}\rvert$ and $p = \lvert\texttt{pattern}\rvert$. Choosing nonempty pieces can explore up to
all boundary subsets of the target. Creating and checking substrings adds at most a linear factor, giving
$O(n \cdot 2^n)$ worst-case time. The recursion has depth at most $p$, while the live assigned substrings contain at
most $n$ target characters, so the auxiliary space is $O(n + p)$.

## Alternatives and edge cases
- **Validate only complete partitions:** repeats a combinatorial amount of work that immediate assignment checks can
  reject near the root.
- **Forward map alone:** permits two different pattern characters to receive the same substring and therefore does
  not enforce a bijection.
- **Empty assignments:** must never be tried; every candidate endpoint starts strictly after the current target
  position.
- **Exact exhaustion:** reaching the end of only one input fails; success requires the pattern and target to end
  together.
