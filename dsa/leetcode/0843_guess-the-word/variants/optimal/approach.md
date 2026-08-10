## General

**Each guess partitions the remaining candidates**

Every word has six positions. When `master.guess(guess)` returns a score from 0 through 6, it tells us how many positions the guess shares with the secret.

For any remaining candidate, we can compute the score it would produce against the guess. Only candidates producing the returned score can still be the secret. Thus, a guess partitions the candidate set into at most seven buckets, one for each possible match count.

After observing the actual score, we retain exactly one bucket.

**Count matching positions**

Helper `matches(first, second)` zips the two six-letter strings and sums `left == right`.

Each equality is a Boolean, which contributes one for a positional match and zero otherwise. This is exactly the feedback definition; characters appearing at different positions do not count.

All words have length six, so `zip` compares every position.

**Maintain the candidate invariant**

`candidates` begins as a copy of `words`. Its invariant is:

> Every word in `candidates` is consistent with all feedback received so far, and the secret is among them.

The secret belongs initially because the contract says it appears in `words`.

After guessing `guess` and receiving `score`, the filtering expression keeps candidate `candidate` only when:

`matches(guess, candidate) == score`.

The actual secret necessarily satisfies this equality because `score` came from comparing the guess with that secret. Every candidate with a different hypothetical score contradicts the observed feedback and is safely discarded. The invariant is preserved.

**Choose a guess that controls the worst remaining bucket**

For one possible `word`, the expression:

`Counter(matches(word, candidate) for candidate in candidates)`

counts how many current candidates would produce each score if `word` were guessed.

Whatever feedback arrives, the next candidate set can contain no more than the largest of those bucket counts. The key function returns that maximum.

`min(candidates, key=...)` chooses the guess whose largest bucket is as small as possible among candidate guesses. This is a minimax decision:

- assume the least informative feedback bucket occurs;
- choose the guess that makes that worst bucket as small as possible.

It aims to guarantee the strongest candidate reduction available under this particular guess set, rather than choosing an arbitrary or random word.

**Why the guessed word is valid**

The guess is chosen from `candidates`, which is a subset of the original `words`. Therefore, it always satisfies the API requirement that guessed strings belong to the supplied list. `master.guess` cannot return `-1` for these guesses.

**Stop on score six**

All words have length six. A score of six means every character matches at every position, so the guessed word equals the secret. The function returns immediately.

If the score is smaller, filtering removes the guess itself because a word matches itself in six positions, not in `score` positions. Thus, an unsuccessful guess cannot be repeated.

**Why minimax is more useful than brute-force order**

Guessing candidates in input order guarantees eventual success only if enough guesses are allowed; it may eliminate just one word at a time. The minimax selection examines the possible information outcome before committing.

For each proposed guess, it asks how badly the candidate set might shrink. Selecting the smallest worst bucket usually reduces uncertainty quickly enough for the test cases' allowed-guess budget, which the Reference says is generated for a reasonable strategy.

This is an interactive problem: the function does not return the secret. Success means it calls `master.guess` with the secret within the allowed number of calls.

**A conceptual round**

Suppose ten candidates remain. Candidate guess A divides them into feedback buckets of sizes 1, 1, and 8. Its worst result leaves eight possibilities.

Candidate guess B divides them into buckets of sizes 2, 3, and 5. Its worst result leaves five. The key for B is smaller, so minimax prefers B even if neither is known to be especially likely as the secret.

After real feedback selects one bucket, the process repeats on only those consistent words.

**Why filtering is logically correct**

Assume before a round that the secret belongs to `candidates`. Feedback `score` equals `matches(guess, secret)`, so the secret passes the filter. Every removed word would have caused different feedback and therefore cannot be secret.

By induction, the secret remains until guessed. Each failed candidate guess is removed, so the candidate set makes strict progress. With no external guess limit, termination is guaranteed. The minimax heuristic is what targets termination within the test's limited calls.

## Complexity detail

Let `g` be the initial number of candidates, let the fixed word length be six, and let `q` be the number of guess rounds.

In a round with `c` candidates, evaluating one proposed guess compares it with all `c` candidates. Doing this for all `c` proposals takes `O(c^2)` fixed-length comparisons. Filtering adds `O(c)` comparisons. Bounding `c` by `g` gives `O(qg^2)` time.

The candidate list stores `O(g)` word references. While evaluating one key, the Counter stores at most seven score buckets, though the generator and selection machinery operate over the candidates. The replacement candidate list also uses `O(g)` space. Total auxiliary space is `O(g)`.

If word length were a variable `\ell` rather than fixed at six, time would be `O(qg^2\ell)`.

## Alternatives and edge cases

- **Guess candidates in arbitrary order:** It eventually finds the secret but may exceed the limited call budget.

- **Random guessing:** Often works on generated cases but provides no deliberate worst-bucket control and makes behavior nondeterministic.

- **Choose from all original words, not only candidates:** A noncandidate probe can sometimes partition better, but the exact source restricts guesses to current candidates and guarantees every guess remains valid.

- **Score six:** The secret has been found and no filtering is needed.

- **Score zero:** Retain only words sharing no positions with the guess.

- **One candidate remains:** Minimax chooses it, and it must be the secret by the invariant.

- **Tied minimax keys:** Python `min` chooses the first candidate with the smallest key; any tied choice has the same worst bucket size.

- **Unique input words:** A failed guess disappears from the next set and cannot recur.

- **Secret preservation:** The real score always makes the secret pass filtering.

- **Allowed-guess budget:** The strategy is a heuristic chosen for the generated reasonable cases; the source does not explicitly count or enforce the budget.

- **No return value:** The required interaction is performed through `Master`, so successful completion returns `None`.

- **No input mutation:** `candidates` is a new list and later rebindings do not change `words`.
