## General

Future joins can inspect only the current string's first and last characters. Its interior content no longer affects whether a new word saves one character. This permits a dynamic-programming state keyed by an endpoint pair: after processing a prefix of `words`, store the smallest attainable length among strings beginning with character $a$ and ending with character $b$.

Initialize the single state formed by `words[0]`. For a later word with first character $f$, last character $l$, and length $m$, extend every current state in both permitted ways. Appending the word changes the right endpoint to $l$ and adds $m-1$ characters exactly when $b=f$; otherwise it adds $m$. Prepending changes the left endpoint to $f$ and saves one character exactly when $l=a$. If several histories reach the same new endpoint pair, retain only the shortest because all of them have identical behavior in every future join.

Each transition represents one legal choice, so every stored value is attainable. Conversely, any legal sequence has some endpoint pair after each prefix, and applying its next left-or-right choice is exactly one of the two transitions. Inductively, the table retains a value no larger than every possible history for each pair. Taking the minimum final state therefore gives the global optimum.

## Complexity detail

Let $n$ be the number of words. There are at most $26^2$ endpoint pairs, and each word performs constant work for every pair. Because the lowercase alphabet is fixed, the total time is $O(n)$ and the two rolling state maps use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Top-down memoization:** Memoizing `(index, first, last)` states has the same asymptotic bounds, but iterative rolling states avoid recursion depth concerns for $n=1000$.
- **Store complete constructed strings:** Keeping a representative string for each state copies growing interiors that future transitions never inspect, producing avoidable superlinear work and memory use.
- **Greedily take an immediate merge:** Saving a character now may choose endpoints that prevent more later merges, so local savings alone do not determine the optimum.
- With one word, no join occurs and its original length is returned.
- A one-character word has the same first and last endpoint; both transition directions must still be considered.
- If both directions reach the same endpoint pair, only their smaller length should survive.
- The processing order of `words` is fixed even though each new word may be placed on either side.
