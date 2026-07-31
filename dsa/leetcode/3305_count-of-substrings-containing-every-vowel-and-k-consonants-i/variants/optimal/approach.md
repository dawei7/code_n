## General

Fix each possible left endpoint and extend the right endpoint one character at a time. Maintain frequencies only for the five vowels and a separate consonant count. The current range qualifies exactly when all five vowel keys are present and the consonant count equals `k`.

Extending a range never decreases its consonant count. Once that count exceeds `k`, no later endpoint for the same left boundary can qualify, so the inner scan may stop immediately. Before that point, every endpoint is examined once and every qualifying positional range is counted at its unique pair of boundaries.

## Complexity detail

Let $n=\lvert word\rvert$. There are $n$ left endpoints and at most $n$ extensions for each, giving $O(n^2)$ time. The vowel set and frequency map contain at most five keys, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Linear sliding windows:** Counting ranges with exactly `k` consonants requires subtracting two at-least counts; that optimization is useful for the larger companion problem but is unnecessary at $n\le250$.
- **Missing vowel:** No range can qualify when the complete word lacks any one vowel.
- **Zero consonants:** Vowel-only ranges are counted as soon as all five vowel types appear.
- **Repeated vowels:** Extra copies preserve validity and can create several qualifying endpoints for one start.
- **Too many consonants:** The inner scan stops immediately after the count becomes `k + 1`.
