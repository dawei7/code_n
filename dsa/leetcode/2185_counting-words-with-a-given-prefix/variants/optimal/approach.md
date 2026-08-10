## General

The solution examines each word independently and asks one precise question: does this word begin with every character of `pref` in the same order?

Python's `str.startswith` implements that prefix comparison directly. The generator produces one boolean per word, and `sum` counts the true results.

**What “prefix” requires**

For `pref` of length $p$ to be a prefix of word `w`, two conditions must hold:

- `w` must contain at least $p$ characters;
- for every index $q$ from zero through $p-1$, `w[q] == pref[q]`.

The matching characters must begin at index zero. Finding `pref` later inside the word does not qualify.

For example, `"attention"` starts with `"at"`, while `"practice"` does not. A word such as `"format"` contains `"at"` near its end but still fails the prefix test.

**Delegate the character comparison to `startswith`**

`w.startswith(pref)` returns true exactly when `pref` matches the leading characters of `w`. If `w` is shorter, it safely returns false rather than indexing beyond the word.

The built-in operation compares only as far as necessary. It can stop at the first mismatching character. In the worst case—when the whole prefix matches or the mismatch is at the end—it examines all $p$ prefix characters.

Using the built-in avoids manual boundary checks and makes the code's intent explicit. It does not change the fundamental work: prefix characters still have to be compared.

**Generate one result per input word**

The expression `(w.startswith(pref) for w in words)` is a generator. It obtains words one at a time and yields a boolean for each.

It does not build a list of all booleans. This keeps the extra memory constant while `sum` consumes the results.

Every word occurrence is evaluated separately. If the same matching string appears twice in `words`, both occurrences contribute because the task counts strings in the array, not distinct string values.

**Use boolean arithmetic to count matches**

In Python, true behaves as integer one and false as integer zero when summed. Therefore

`sum(w.startswith(pref) for w in words)`

adds one for each matching word and zero for each nonmatching word.

This is equivalent to initializing a counter, looping over the words, and incrementing inside an `if` statement. The compact form preserves the same logic.

**Why the return value is exact**

Take any word that contributes one. `startswith` returned true, so all characters of `pref` match the word from position zero and the word is long enough. It satisfies the definition.

Conversely, any word containing `pref` as a prefix must make `startswith(pref)` return true, so it contributes one. The generator visits every array element exactly once, and no element contributes more than one.

The sum is therefore exactly the number of words whose leading contiguous substring equals `pref`.

For `["pay", "attention", "practice", "attend"]` and `pref = "at"`, the booleans are false, true, false, true. Their numeric sum is two.

**Why a trie is unnecessary for one query**

A trie is useful when many prefix queries will reuse the same large word collection. Building one for this single query requires reading every character of every word and allocating nodes, while direct checks may stop early and allocate no growing structure.

The exact problem asks for one `pref`, so scanning the leading characters directly is the simplest fit.

**Interpret the manifest's symbol `C`**

Let

$$
C=\sum_{w\in\texttt{words}}\min(\lvert w\rvert,\lvert\texttt{pref}\rvert).
$$

This is an upper bound on the total number of character positions that prefix checks may inspect. The implementation's time is $O(C)$. If there are $n$ words and prefix length $p$, the familiar looser bound is $O(np)$.

Early mismatches can make actual work smaller, but asymptotic worst-case analysis assumes comparisons reach their maximum possible length.

## Complexity detail

With $C$ defined above, total time is $O(C)$. Equivalently, it is $O(np)$ when $n$ is the number of words and $p$ is the prefix length.

The generator, running sum, and loop reference use $O(1)$ auxiliary space. `startswith` does not require slicing a prefix-sized substring in the visible Python code. The input strings and array are not modified.

The integer answer ranges from zero through $n$. Output space is constant.

## Alternatives and edge cases

- **Manual two-pointer comparison:** Check length and compare characters from index zero. It has the same complexity but requires more code and boundary handling.
- **Slice then compare:** `w[:len(pref)] == pref` is concise, but slicing may allocate a temporary substring for every word.
- **Trie:** Build prefix counts when many queries reuse the same words. For one query, its construction and memory are unnecessary.
- **Hash prefixes:** Hashing can help repeated queries but introduces collision considerations and preprocessing.
- **Word shorter than prefix:** `startswith` returns false safely.
- **Word equal to prefix:** The entire word is a valid leading substring, so it counts.
- **Prefix appears only later:** The word does not count because matching must begin at index zero.
- **Duplicate words:** Every array occurrence is counted independently.
- **No matches:** Every boolean is false and `sum` returns zero.
- **All words match:** Each contributes one, so the answer equals `len(words)`.
- **One-character prefix:** Only the first character of each nonempty word needs comparison.
- **Nonempty guarantee:** Both words and `pref` have positive length, so empty-prefix semantics do not arise.
- **Lowercase alphabet:** Comparison is direct and case-sensitive; no normalization is needed.
- **Generator memory:** Results are consumed lazily instead of stored in a boolean list.
- **Input preservation:** Strings are immutable and the word array is read only.
