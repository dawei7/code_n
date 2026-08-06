## Description

Design an autocomplete system for a search engine. A user enters a sentence containing at least one word and finishes it with the special character `#`.

The system begins with two parallel arrays: `sentences` contains previously typed sentences, and `times[i]` records how many times `sentences[i]` has been entered. After each typed character other than `#`, return up to three historical sentences whose prefix matches everything typed in the current search.

Apply these ranking and stream rules:

- A sentence's **hot degree** is the number of times that exact sentence was previously entered.
- Rank matches by decreasing hot degree. Break equal-frequency ties by ASCII-code order, placing the smaller sentence first.
- If fewer than three historical sentences match, return every match.
- The character `#` ends the current sentence, stores that completed input in the history, and produces an empty result.
