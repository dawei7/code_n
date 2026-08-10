## General

**What must be changed**

The string contains lowercase English letters and question marks. Every question mark must be replaced by a lowercase letter so that no two adjacent characters are equal. Characters that are already letters must remain unchanged. The implementation constructs one valid result; it does not need to find a lexicographically smallest result or minimize how many distinct letters are used.

Python strings are immutable, so the solution first converts `s` into a list of individual characters. That list allows an assignment such as `s[i] = c` when a replacement is chosen. After all positions have been processed, `"".join(s)` turns the list back into the required string.

**Why the decision is local**

Whether the character at index `i` is valid depends only on its immediate neighbors:

- if `i > 0`, it must differ from `s[i - 1]`;
- if `i + 1 < n`, it must differ from `s[i + 1]`.

No character farther away can become adjacent to position `i`, because this problem replaces characters without deleting or moving them. Therefore, choosing a replacement does not require dynamic programming, backtracking, or knowledge of the whole prefix beyond its final adjacent character.

The scan moves from left to right. When it reaches a question mark, the position on the left has already been finalized. It is either an original letter or a question mark that an earlier iteration replaced. The position on the right has not necessarily been processed, but its current value still gives all the information needed:

- if the right character is a fixed letter, the current replacement must avoid it;
- if the right character is `?`, it imposes no restriction yet, because that question mark will make its own safe choice when the scan reaches it.

This asymmetry is important. The algorithm never needs to predict what a future question mark will become. The future position will see the current chosen letter as its finalized left neighbor and will avoid it then.

**Why only `a`, `b`, and `c` are tried**

For each question mark, the inner loop tries the three candidates in `"abc"`. At most two letters can be forbidden: one by the left neighbor and one by the right neighbor. Even when those neighbors contain two different letters, three candidates guarantee that at least one candidate remains. If both neighbors contain the same letter, only one candidate is forbidden. At an endpoint, there is at most one neighbor, and a one-character string has none.

The source checks a candidate with two short-circuit conditions. The expression `i and s[i - 1] == c` is false at index zero, so it does not access a nonexistent left neighbor. The second condition, `i + 1 < n and s[i + 1] == c`, first verifies that a right neighbor exists. If either existing neighbor equals `c`, `continue` rejects that candidate. Otherwise, the candidate is assigned and `break` stops the three-letter search.

There is no fallback after that loop because the three-candidate argument proves that one candidate must be available. The loop may try one, two, or three letters, but it always assigns the question mark.

**A left-to-right example**

Consider `s = "?zs"`. At index zero, `a` differs from the fixed right neighbor `z`, so the algorithm writes `a`. The other positions are fixed and remain untouched, producing `"azs"`.

Now consider `s = "ubv?w"`. When the scan reaches the question mark, its left neighbor is `v` and its right neighbor is `w`. The first candidate, `a`, differs from both, so it is chosen immediately.

A run of question marks shows why no lookahead search is needed. For `"??"`, the first position can become `a` because its right neighbor is still `?`. At the second position, `a` is rejected because the newly finalized left neighbor is `a`, so `b` is chosen. The result `"ab"` is valid. A longer run alternates or varies among the available candidates through the same local rule.

**Why the finished string is valid**

The problem guarantees that the original string has no adjacent equal letters at positions that are both already fixed. Consequently, the only adjacency pairs that could require repair are pairs containing at least one question mark.

Whenever the algorithm replaces a question mark at position `i`, it explicitly chooses a character different from every fixed adjacent letter visible at that moment. Its left neighbor is final, so the pair `(i - 1, i)` becomes valid permanently. If the right neighbor is already a letter, the pair `(i, i + 1)` also becomes valid immediately. If the right neighbor is a question mark, that pair becomes valid later: when index `i + 1` is processed, it rejects the letter now stored at index `i`.

Thus every adjacent pair falls into one of three cases. Two original letters were already valid by the input guarantee; an original letter and a replacement are checked when the replacement is made; or two replacements are checked when the later one is made. Every question mark is replaced because three letters are enough, and no original letter is modified. These facts establish both required properties of the returned string.

## Complexity detail

Let $N$ be the length of `s`.

Converting the immutable string to a list takes $O(N)$ time and stores $N$ characters. The outer loop visits each position exactly once. At a question mark, the inner loop examines at most three candidates, and each candidate performs only constant-time boundary and character comparisons. Three is a fixed constant independent of $N$, so all replacement work is $O(N)$ rather than $O(3N)$ as a distinct asymptotic class.

Joining the final list also takes $O(N)$ time because Python must create the returned string and copy its characters. The total time complexity is therefore $O(N)$.

The mutable character list occupies $O(N)$ auxiliary space, and the returned string also occupies $O(N)$ output space. Apart from those character containers, the loop uses only the index, the length, and one candidate character, which is $O(1)$ extra state. Under the checked-in Python implementation’s accounting, the overall space complexity is $O(N)$. An environment with a mutable string buffer could update that buffer directly, but producing an $N$-character result still requires the output storage.

## Alternatives and edge cases

- **Backtracking over all lowercase letters:** Trying a letter, recursing, and undoing choices can eventually find a valid string, but it solves a much larger search problem than necessary. Adjacency is local, and three candidates always leave a valid choice, so the greedy decision never needs to be reconsidered.
- **Trying all 26 lowercase letters:** This is correct but unnecessary. At most two neighboring letters are forbidden, so `a`, `b`, and `c` already provide the mathematical guarantee the algorithm needs.
- **Copying only the previous character:** A method that avoids the left neighbor but ignores a fixed right neighbor can create an invalid pair. For example, choosing `a` for the middle of `"b?a"` would conflict with the right side. The checked-in implementation tests both existing neighbors.
- **Treating a right-side question mark as a fixed restriction:** A question mark has no chosen letter yet and should not forbid a candidate. It will avoid the current letter when its own turn arrives.
- **Single-character input:** A lone question mark becomes `a`, while a lone fixed letter is returned unchanged. With no adjacent pair, either result automatically satisfies the condition.
- **Question mark at the first or last position:** The short-circuit boundary tests safely consider only the neighbor that exists. There is no negative-index lookup at the first position and no out-of-range lookup at the last.
- **Several consecutive question marks:** Each later replacement sees the finalized replacement immediately to its left. This prevents equal adjacent choices without needing to plan the whole run in advance.
- **Fixed letters outside `a`, `b`, and `c`:** They do not cause difficulty. A fixed `z`, for example, forbids none of the three candidates unless a candidate actually equals it, so `a` is immediately usable.
- **Two different fixed neighbors:** Even if the neighbors forbid two of the three candidates, the third remains. This is the tight reason that a three-letter candidate set is sufficient.
- **Input guarantee about original letters:** The algorithm cannot repair an equal adjacent pair made of two non-question-mark characters because it intentionally never changes fixed letters. Correctness therefore relies on the stated guarantee that such a conflict is absent from the input.
