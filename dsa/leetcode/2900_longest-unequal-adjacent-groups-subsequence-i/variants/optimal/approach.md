## General

Partition `groups` into maximal contiguous runs of equal values. A valid alternating subsequence can select at most one word from any one run: if it selected two words from the same run, every index between them also has that same group, so no selected word between the two could provide the opposite group needed to separate them.

Conversely, selecting one word from every run is valid. Consecutive runs have different binary group values by definition, and their representatives preserve their original index order. If there are $r$ runs, this construction has length $r$, while the at-most-one-per-run observation proves that no valid subsequence can be longer.

Choose the first word as the representative of the first run. Scan the remaining paired entries and append a word exactly when its group differs from the group of the last selected word. This happens at each run boundary and nowhere else, so the result contains one representative from every run. The problem accepts any longest answer, making the first representative of each run a deterministic valid choice.

## Complexity detail

Let $n=\lvert\texttt{words}\rvert$. The scan examines each paired entry once, taking $O(n)$ time. The returned subsequence may contain all $n$ words, so the total result storage is $O(n)$; aside from the output, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming by final index:** Tracking the best subsequence ending at every word works, but a direct transition implementation takes $O(n^2)$ time and stores unnecessary state.
- **Choose the last word of each run:** This is just as optimal as choosing the first; the contract permits any longest result.
- **Single group run:** Only one word can be selected, and the first word is a valid answer.
- **Already alternating groups:** Every word is selected because every element begins a new run.
- **Several valid answers:** Case validation must check subsequence order, alternating groups, and maximum length rather than require one unique sequence.
- **Distinct words:** A selected word identifies its original index unambiguously, which keeps the group correspondence well-defined.
