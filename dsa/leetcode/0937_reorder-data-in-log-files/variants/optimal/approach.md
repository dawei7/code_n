## General

**Translate the rules into one sortable key**

Every log has an identifier followed by content. The content determines whether it is a letter-log or digit-log. The required order has three layers:

1. every letter-log precedes every digit-log;
2. letter-logs are ordered by content, with identifier as the tie-breaker;
3. digit-logs keep their input order.

Python's `sorted` can enforce all three rules when the key function expresses them carefully.

**Split once, not on every space**

The key function executes `id_, rest = log.split(" ", 1)`. The second argument limits splitting to the first space.

This matters because `rest` must remain the complete content, including the spaces between all later words. If `"let1 art can"` were split into every token, the implementation would need to join or separately compare the content tokens again. With one split, `id_` is `"let1"` and `rest` is `"art can"`.

The contract guarantees one identifier and at least one following word, so both components exist. It also guarantees single spaces between tokens, so `rest[0]` is the first character of the first content word, not whitespace.

**Classifying the log**

Letter-log content consists of lowercase English letters and spaces, while digit-log content consists of digits and spaces. Looking at `rest[0]` is sufficient because every content word in a log has the same required type.

The expression `rest[0].isalpha()` is true for a letter-log and false for a digit-log under the stated input contract.

The function returns different tuple keys:

- a letter-log receives `(0, rest, id_)`;
- a digit-log receives `(1,)`.

Python compares tuples lexicographically. It compares the first elements first and consults later elements only when all earlier compared elements are equal.

**Why letter-logs come first**

The first key component is zero for every letter-log and one for every digit-log. Since zero is less than one, every letter-log sorts before every digit-log, regardless of its content or original position.

The tuples have different lengths, but Python never needs to compare a letter content string with a missing digit component. For a letter-log and digit-log, their first integers already differ and decide the order.

**Why letter-logs receive exactly the specified ordering**

When two letter-logs are compared, both first components are zero, so tuple comparison proceeds to `rest`. Their complete contents are compared lexicographically.

If the contents differ, that comparison determines the result. If the contents are identical, tuple comparison reaches `id_` and orders the identifiers lexicographically. This precisely matches the two letter-log rules.

For example, `"let1 art can"` has key `(0, "art can", "let1")` and `"let3 art zero"` has key `(0, "art zero", "let3")`. The common prefix `"art "` is followed by `c` in one content and `z` in the other, so `"art can"` comes first. If two contents were both `"art can"`, their identifiers would break the tie.

**Why digit-log order is preserved**

Every digit-log receives the identical key `(1,)`. Python's sort is stable: elements whose keys compare equal remain in the same relative order they had in the input.

The solution is not numerically sorting the digit contents, and it is not sorting digit identifiers. Stability is the mechanism that implements the rule. Returning different keys for digit-logs, even keys based on their original strings, would destroy the required relative ordering.

**The decorate-sort-undecorate behavior**

Python computes the key once per element, associates it with the original log, sorts by those keys, and returns the original log strings in the resulting order. The function does not need to manually divide logs into two arrays.

Conceptually, the sort first partitions by the type flag. Within the zero partition, it sorts by content and identifier. Within the one partition, all keys tie and stability retains the input order.

**Why the returned list is correct**

Consider any two output logs.

If one is a letter-log and the other a digit-log, their first key components force the letter-log first. If both are letter-logs, tuple ordering uses content and then identifier, exactly matching the required lexicographic rule. If both are digit-logs, their keys are equal, so stable sorting preserves their input relationship.

These pairwise rules define the full required ordering. Since `sorted` returns every original element exactly once, its result contains the same logs in the correct order.

## Complexity detail

Let `S` be the total number of characters across all logs, `L` the number of letter-logs, and `C` the maximum number of characters that may need to be examined while comparing two letter-log keys.

Computing all keys and splitting every log once costs `O(S)` time. Sorting the letter-log keys requires `O(L log L)` comparisons in the worst case, and a lexicographic comparison can inspect up to `O(C)` characters. Digit-log keys all compare equal, while type comparisons are constant after the keys exist. The stated bound is therefore `O(S + L C log L)`.

If `N` is the total number of logs and every log has length at most `C`, the familiar coarser bound is `O(N C log N)`.

The split components and cached key tuples collectively refer to or store content proportional to the input text, and `sorted` creates a result list plus sorting workspace. The auxiliary space bound is `O(S)` under the manifest's character-based measure. The returned list itself contains references to the original strings; the strings are not rewritten.

## Alternatives and edge cases

- **Separate, sort, and concatenate:** Scan into letter and digit lists, sort only letter-logs by `(content, identifier)`, and append digit-logs unchanged. This is equally sound and makes stability for digits explicit, but the single-key solution is more compact.
- **Custom comparator:** Directly encode all pairwise cases. It can work, but repeatedly splitting strings inside comparisons performs redundant parsing and makes transitivity mistakes easier than a tuple key.
- **Sort the full original strings:** This incorrectly lets identifiers dominate because the identifier appears first even though letter content must be the primary key.
- **Give digit-logs their content as a key:** That would reorder them numerically or lexicographically, violating their stable input-order requirement.
- **Identical letter content:** The identifier is the required tie-breaker. Omitting the third tuple component would leave these logs in input order instead.
- **Several digit-logs with identical or different content:** All receive `(1,)`. Their content is deliberately ignored, and stable sort retains their exact relative sequence.
- **One log:** The key is computed and sorting returns the same single element, whether it is a letter-log or digit-log.
- **Content with several words:** `split(" ", 1)` preserves the rest verbatim, so lexicographic comparison includes every word and intervening space.
- **Classification contract:** Checking only `rest[0]` is safe because a log is guaranteed to contain either letter words or digit words. With mixed or malformed content, this shortcut would need reconsideration.
- **Tuple-length safety:** Letter and digit tuples differ in length, but their integer type flag always decides cross-type comparisons before tuple length or string components matter.
- **Stable-sort dependency:** The digit rule relies on Python's documented stable sorting. Porting this key idea to a language with an unstable sorting routine would require attaching original indices or separating digit-logs first.
