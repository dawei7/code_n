## Abbreviation Rules

1. Begin each word's abbreviation with its first character, the number of characters between the first and last
   characters, and its last character.
2. Whenever several words have the same abbreviation, extend the retained prefix of every colliding word by one
   character. Repeat until every abbreviation is unique.

   For example, `"abcdef"` and `"abndef"` progress together as
   `["a4f","a4f"] -> ["ab3f","ab3f"] -> ["abc2f","abn2f"]`.
3. If the resulting abbreviation is not shorter than its original word, keep the original word instead.
