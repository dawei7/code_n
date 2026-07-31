## General

The transformation can be emitted from left to right without first splitting or rebuilding the caption. Start the output with `#`. Two Boolean states are sufficient: `seen_word` records whether the first real word has begun, and `inside_word` records whether the previous processed character belongs to the current word.

A space ends the current word by clearing `inside_word`; leading and repeated spaces therefore have no output. For a letter that begins a word, lowercase it when no earlier word exists and uppercase it otherwise. Every letter encountered while already inside a word is lowercased. This exactly implements the first-word and later-word camelCase rules while discarding every space.

The output is a prefix-preserving transformation, and truncation keeps only its first 100 characters. Once the output list reaches length 100, no unread caption character can affect the returned prefix, so processing may stop immediately. Joining the retained characters produces the required tag.

## Complexity detail

Let $n$ be the caption length. Each inspected character receives constant work, so time is $O(n)$; early truncation can stop sooner but does not change the upper bound. The retained output contains at most 100 characters and the algorithm stores only two flags beyond it, so auxiliary space is $O(1)$ under the fixed output cap.

The benchmark defines $S=n$ and interleaves one-letter words with spaces so the output remains below 100 characters and the accepted scan must inspect the full caption. The calibrated slower implementation repeatedly rescans each processed prefix to rediscover word boundaries, taking $O(S^2)$ time while generating the same tag.

## Alternatives and edge cases

- **Split and join:** Building a word list and a second combined string is concise and still linear, but uses $O(n)$ temporary storage instead of streaming into the capped result.
- **Repeated prefix rescanning:** Recomputing whether each letter begins the first or a later word from the entire preceding prefix is correct but quadratic.
- **Repeated spaces:** They do not create words and must not trigger capitalization by themselves.
- **First word:** Its first letter is lowercase even when the original caption begins with uppercase letters or spaces.
- **Later word:** Only its first letter is uppercase; every following letter is forced to lowercase.
- **Spaces-only caption:** No word is emitted, so the result is just `#`.
- **Length cap:** The leading `#` counts toward 100, leaving room for at most 99 letters.
