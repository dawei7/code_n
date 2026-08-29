## General

**Locate the exact reversal endpoint**

`word.find(ch)` returns the index of the first occurrence of `ch`. That is exactly the endpoint specified by the problem. If the character is absent, Python returns -1.

The source stores this result in `i` and uses a conditional expression. When `i == -1`, it returns the original `word` unchanged. This explicit check is important because using -1 directly in slicing would refer to the last character rather than mean "not found."

**Reverse the inclusive prefix with a negative step**

When `ch` is present, the prefix includes indices zero through `i`. Python slice

`word[i::-1]`

starts at index `i`, moves backward by one, and continues to the beginning because the stop is omitted. It therefore yields characters

`word[i], word[i - 1], ..., word[0]`.

The character `ch` itself appears first in this reversed prefix because the endpoint is inclusive.

**Append the untouched suffix**

`word[i + 1 :]` contains every character strictly after the first `ch` in its original order. Concatenating the reversed prefix and this suffix produces a string of the same length with exactly the requested segment changed.

For `word="abcdefd"` and `ch="d"`, `find` returns three. The first slice is `"dcba"` and the second is `"efd"`, producing `"dcbaefd"`. The later d does not affect the result because `find` chose the first occurrence.

**Why no character is lost or duplicated**

The prefix slice covers original indices from `i` down to zero exactly once. The suffix slice covers indices `i+1` through the last index exactly once. These two index sets are disjoint and together cover the entire string.

Reversal changes only order, not membership. Concatenation therefore preserves all characters and the original length.

**Boundary behavior**

If `ch` is the first character, `i=0`. The reverse slice has one character, so the result equals the original word. A one-character reversal is still the correct operation.

If `ch` is last, the suffix is empty and the whole word is reversed.

If `word` itself has length one, the same cases apply safely: present returns that one character through slicing, absent returns the original.

**Why the method is correct**

When `ch` is absent, the contract requires no operation and the first branch returns precisely the input.

When present, `find` supplies the unique required endpoint: the smallest index containing `ch`. The backward slice returns exactly the inclusive prefix in reverse order, and the forward slice returns exactly the remaining suffix unchanged. Their concatenation is therefore the specified result.

**Python strings and allocation**

Python strings are immutable. Neither slicing nor concatenation changes `word` in place. Each slice creates a new string, and concatenation creates the returned string.

This is why the space bound is linear even though the expression looks constant-sized. A language with mutable character storage could reverse the prefix in place, but that is not what this exact Python source does.

**Why built-ins still express the algorithm clearly**

`find` is a linear search for the first matching character. The two slices are a compact expression of index traversal in reverse and forward directions. Their use does not change the underlying work: locate the boundary, emit the prefix backward, and emit the suffix forward.

The method avoids a manual stack or character list because Python's slicing already performs the necessary string construction safely.

**Evaluation of the conditional expression**

Python evaluates only the selected branch of `word if i == -1 else ...`. When `ch` is absent, neither slice nor concatenation is performed, and the exact original string object can be returned. When it is present, both slices use the already computed index; the search is not repeated. This keeps the control flow compact while preserving the important absent-character guard.

## Complexity detail

Let $N$ be the word length. `find` scans up to $N$ characters. When the character is present, the two slices collectively copy $N$ characters and concatenation builds an $N$-character result. Total time is $O(N)$.

The prefix, suffix, and returned concatenation require $O(N)$ temporary/returned string space. Even if output space is excluded, slicing can hold linear temporary data. The original string is unchanged.

## Alternatives and edge cases

- **Two-pointer character list:** Convert to a list, swap prefix endpoints inward, and join. It is explicit and linear but also uses $O(N)$ Python space.
- **Stack:** Push through the first target and pop to reverse, then append the suffix; more machinery for the same bounds.
- **Manual concatenation in a loop:** Repeated immutable-string addition can become $O(N^2)$ in Python.
- **Character absent:** Return `word`; do not use the -1 index as a real endpoint.
- **Character at index zero:** Reversing one character leaves the word unchanged.
- **Character at final index:** The entire word is reversed.
- **Repeated target character:** Only the first occurrence determines the prefix.
- **One-character word:** Both present and absent cases are handled.
- **Inclusive endpoint:** `word[i::-1]` includes `word[i]`.
- **Suffix preservation:** `word[i + 1 :]` keeps its original order.
- **Lowercase guarantee:** No case normalization or Unicode matching policy is needed.
- **Input preservation:** Strings are immutable and the method returns a newly constructed value when reversal occurs.
