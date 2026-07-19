## General
**Turn feedback into candidate partitions**

For any two six-letter words, compute how many positions match. If a guess receives score $s$, the secret must belong to the bucket of current candidates having exactly $s$ matches with that guess. Every candidate outside that bucket can be discarded without another interactive call.

**Choose the smallest worst remaining bucket**

For each possible guess among the current candidates, count the sizes of its seven score buckets, from zero through six matches. Select a word whose largest bucket is as small as possible. This minimax choice limits the worst ambiguity left after the next response. Call `master.guess`; a score of six finishes, while any other score filters the candidate list to its corresponding bucket.

The secret starts in the candidate set. After each response, filtering retains it because its actual match count equals the returned score. Therefore the candidate invariant is never lost. The generated cases guarantee that this reasonable information-gathering strategy reaches the secret within the allowed interactive budget.

## Complexity detail
In one round, evaluating at most $g$ possible guesses against at most $g$ candidate secrets costs $O(g^2)$ because word length is fixed at six. Across at most $q$ calls, the bound is $O(qg^2)$ time. Match counters and the remaining candidate list use $O(g)$ space.

## Alternatives and edge cases
- **Random remaining guess:** Filtering remains logically correct, but unlucky choices can leave large buckets and exceed the interactive call limit.
- **Zero-match heuristic:** Choosing a word with few zero-match neighbors is a common approximation to minimax and is cheaper to score conceptually, but it considers only one of the seven response buckets.
- **Recount each bucket separately:** Computing a candidate's bucket size anew for every possible hidden word makes the same minimax choice but costs $O(qg^3)$ time.
- **Invalid guess:** A word outside `words` returns `-1`, consumes a call, and provides no useful legal candidate partition.
- **One candidate:** Guess it immediately; the invariant ensures it is the secret.
- **Repeated feedback score:** The same numeric score can describe many different candidate sets, so filtering must always be relative to the actual guessed word.
