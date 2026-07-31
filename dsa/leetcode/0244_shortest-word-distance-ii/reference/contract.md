## Function Contract

The app presents the persistent class operations as one equivalent batch call.

**Inputs**

- `wordsDict`: The fixed string array used to initialize the data structure.
- `queries`: The ordered `[word1, word2]` calls to `shortest`; each pair contains different words present in `wordsDict`.

**Return value**

Return the shortest distance for every query in the same order.
