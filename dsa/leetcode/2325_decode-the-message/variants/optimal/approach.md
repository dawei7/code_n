## General

Scan `key` from left to right while maintaining a substitution table. Seed the
table with a space-to-space entry. Whenever a lowercase letter is absent from
the table, assign it the next unused plaintext letter: the first distinct key
letter receives `a`, the second receives `b`, and so forth. Repeated key
letters and spaces therefore have no effect on the established order.

**Why first occurrences are sufficient**

The cipher definition depends only on the order in which distinct letters
first appear. Once a letter has been assigned, every later occurrence must use
the same substitution, so revisiting it cannot add information. The guarantee
that all 26 letters occur ensures the completed table can decode every
lowercase letter in `message`.

After the key scan, translate the message from left to right with direct table
lookups and join the translated characters. The explicit space entry preserves
both isolated and consecutive spaces without separate output logic.

## Complexity detail

Let $k=\lvert\texttt{key}\rvert$ and
$m=\lvert\texttt{message}\rvert$. The two scans take $O(k+m)$ time. The
substitution table contains at most 27 entries, a constant independent of the
input lengths, so auxiliary space is $O(1)$. The returned string requires
$O(m)$ output space.

## Alternatives and edge cases

- **Repeatedly search the key:** Reconstructing a letter's first-occurrence
  rank for every message character is correct but can take $O(km)$ time.
- **Remove duplicates first:** Building a distinct-letter string and then a
  table also works, but the direct scan avoids an unnecessary intermediate
  representation.
- **Repeated key letters:** Only the first occurrence advances the plaintext
  alphabet; later copies must retain the original mapping.
- **Spaces:** Spaces in the key do not consume a substitution position, while
  every space in the message must remain in its exact position.
- **Alphabetical key:** This produces the identity mapping and must return the
  message unchanged.
