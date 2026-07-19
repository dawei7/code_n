## General
**Turn each end position into a counting question.** Process the string from left to right while storing the latest index at which each of `a`, `b`, and `c` appeared. Consider a substring ending at the current index. It contains all three characters exactly when its start is no later than all three stored indices.

**Find the latest valid-start boundary.** Let $m$ be the minimum of the three latest indices. If one character has not appeared, its index remains $-1$, so $m+1=0$ and this end position contributes nothing. Otherwise, every start from index $0$ through index $m$ produces a valid substring ending here, while any later start omits the character whose latest occurrence is at $m$. Therefore this position contributes exactly $m+1$ substrings.

Add that contribution after updating the current character's latest index. Each valid substring has one unique end position and is counted once among that position's valid starts, so the accumulated total is exact.

## Complexity detail
Each of the $n$ characters causes one index update, a minimum over three fixed values, and one addition. The running time is $O(n)$. The three latest indices and the result use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Sliding window with frequencies:** Move a left pointer while a frequency table contains all three characters, adding the number of valid starts for each right endpoint. This is also $O(n)$ but uses more mutable state.
- **Enumerate every substring:** Checking all start and end pairs is correct but costs at least $O(n^2)$ time.
- **Repeated suffix searches:** Finding the next `a`, `b`, and `c` from every start can also degrade to $O(n^2)$ even when the search operations are concise.
- **First complete prefix:** Contributions remain zero until all three latest indices are nonnegative.
- **Repeated characters:** Several copies of one character simply move its latest index; they do not by themselves make a substring valid.
- **Minimum input:** A three-character string contributes one only when it contains all three distinct required characters.
