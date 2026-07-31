## General

Begin with one possibility for the case in which Alice made no mistake: the intended string is exactly `word`.

Now consider one maximal run of the same character with displayed length $L$. If this run came from the one long key press, its intended length can be any of $1,2,\ldots,L-1$. These are $L-1$ additional strings. Shortening different runs changes different positions around the run boundaries, so possibilities contributed by distinct runs cannot coincide.

There is no need to identify run boundaries explicitly. A run of length $L$ contains exactly $L-1$ adjacent equal pairs. Therefore, scanning the string from the second character onward and adding one whenever `word[index] == word[index - 1]` accumulates

$$
1+\sum_{\text{runs}}(L-1),
$$

which is precisely the unchanged word plus every valid one-run shortening.

The “at most once” condition is crucial. Contributions from separate runs are added rather than multiplied because a valid history may shorten no run or exactly one run, never several runs simultaneously.

## Complexity detail

Let $n=\lvert\texttt{word}\rvert$. The algorithm compares each adjacent pair once, so it takes $O(n)$ time. It stores only the running count and loop index, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Build every candidate string:** Shortening each run to every possible length and inserting the results into a set is direct, but materializing $O(n)$ strings of length $O(n)$ can take $O(n^2)$ time and space.
- **Run-length array:** Explicitly collecting every run length and summing `length - 1` is correct but uses unnecessary $O(n)$ storage.
- **All characters distinct:** There are no equal adjacent pairs, so only the unchanged word is possible.
- **One repeated run:** A displayed run of length $L$ yields exactly $L$ possibilities including the unchanged word.
- **Several repeated runs:** Add their shortening counts; multiplying them would incorrectly allow more than one long key press.
- **Single character:** It cannot be shortened to an empty string, so the answer is one.
