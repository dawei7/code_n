## General

Scan `s` from left to right while tracking the length of the current maximal equal-character block. Matching adjacent characters extend that run. A changed character—or the position just past the end of the string—closes it, at which point increment the frequency associated with its length and begin the next run.

Maintain the greatest frequency seen after every completed run. Each maximal run is closed exactly once: a boundary occurs precisely where the next character differs or the string ends. Therefore the frequency table contains the exact number of runs of every length. Selecting all runs in its most frequent length class is legal, while no selection can contain more runs because all selected runs must come from one such class. The recorded maximum is consequently the answer.

## Complexity detail

Let $N=\lvert s\rvert$. The scan visits each character once, so it takes $O(N)$ time. The length-frequency structure has at most $N$ entries and uses $O(N)$ auxiliary space in the worst-case bound.

## Alternatives and edge cases

- **Store every run length first:** Building a list and counting it afterward is also linear with a hash map, but the streaming version avoids retaining one entry per run.
- **Recount each run length:** Calling a linear count for every stored run is correct but can require $O(N^2)$ work when the string has many runs.
- **Maximality:** A block such as `"aaaa"` is one run of length four, not four runs of length one or two shorter runs.
- **Different letters:** Runs `"a"`, `"b"`, and `"c"` can be selected together because length, not character, defines compatibility.
- **Single run:** A one-character string or a string of one repeated letter has answer `1`.
- **Alternating characters:** Every character is a length-one run, so the answer equals the string length.
- **Separated equal letters:** Runs with the same letter remain distinct when another character lies between them, as in the two `"aaa"` runs of Example 2.
