## Description

A word's abbreviation consists of its first letter, the number of letters strictly between its first and last letters, and its last letter. A two-letter word remains unchanged because it has no middle letters. For example:

- `dog` becomes `d1g` because one letter lies between `d` and `g`.
- `internationalization` becomes `i18n` because eighteen letters lie between `i` and `n`.
- `it` remains `it` because its length is two.

Implement the `ValidWordAbbr` class:

- `ValidWordAbbr(String[] dictionary)` initializes the object from `dictionary`.
- `boolean isUnique(string word)` returns true when either no dictionary word has the same abbreviation as `word`, or every dictionary word with that abbreviation is exactly `word` itself.
