## General

**What a valid abbreviation really chooses.**

At every position of `word`, the character is either kept literally or belongs to an abbreviated substring. If several consecutive characters are abbreviated, they must be represented by one number equal to the length of that whole run. Writing two numbers next to each other would represent two adjacent abbreviated substrings, which the definition forbids; those substrings should have been merged into one longer substring instead.

For example, a choice pattern for `abcde` might be:

- keep `a`;
- abbreviate `bc`, producing `2`;
- keep `d`;
- abbreviate `e`, producing `1`.

The result is `a2d1`. The literal `d` separates the two abbreviated runs, so they are non-adjacent. By contrast, abbreviating `ab` and then immediately abbreviating `cde` should not produce `23`; with no kept character between the runs, they form one run of length five and must be written as `5`.

The exact optimal source generates valid results by building this separation rule directly into its recursion. It never creates adjacent number tokens and never needs a later cleanup pass.

**Meaning of `dfs(i)`.**

Let $n$ be `len(word)`. The helper `dfs(i)` returns every valid abbreviation of the suffix beginning at index `i`, under the condition that index `i` is the next undecided position. Nothing before `i` needs to be reconsidered.

When `i >= n`, the suffix is empty. There is exactly one abbreviation of an empty suffix: the empty string. Returning `['']` is important. It gives callers one neutral suffix to append, allowing a completed prefix to become one full result. Returning an empty list would incorrectly erase every branch that reaches the end because a loop or list comprehension over that list would produce nothing.

For an ordinary index `i`, the helper divides all possibilities into two disjoint groups according to what happens to `word[i]`.

**Group one: keep the current character.**

The expression based on `word[i] + s for s in dfs(i + 1)` places `word[i]` literally into every abbreviation of the remaining suffix. Once the current character is kept, index `i + 1` is free to begin either another literal portion or an abbreviated run. This produces every result whose first suffix character remains visible.

For instance, if the current suffix is `cd` and the recursive results for `d` are `d` and `1`, prefixing `c` produces `cd` and `c1`.

**Group two: abbreviate a run beginning at `i`.**

The loop chooses an endpoint `j` from `i + 1` through `n`. The half-open substring `word[i:j]` contains exactly `j - i` characters, so the source replaces it with `str(j - i)`. Trying every such `j` tries every possible nonempty abbreviated run beginning at `i`.

Two cases then matter:

- If `j < n`, the run stops just before index `j`. The source immediately appends `word[j]` as a literal separator and asks `dfs(j + 1)` for all abbreviations after that separator.
- If `j == n`, the abbreviated run consumes the entire remaining suffix. There is no separator character to append, so the conditional expression contributes an empty string. The recursive call is `dfs(n + 1)`, which safely reaches the same empty-suffix base case.

Forcing `word[j]` to remain literal is the key design choice. Once `word[i:j]` has been selected as an abbreviated substring, another abbreviated substring may not start at `j`, because that would make the two substrings adjacent. Keeping `word[j]` provides the required gap. The next undecided position is consequently `j + 1`.

Consider `word = "abc"` at `dfs(0)`. The keep branch begins with `a` and generates `abc`, `ab1`, `a1c`, and `a2`. The run choices generate the other four results:

- `j = 1` abbreviates `a`, keeps `b` as the separator, and lets `dfs(2)` decide `c`, producing `1bc` and `1b1`;
- `j = 2` abbreviates `ab`, keeps `c`, and produces `2c`;
- `j = 3` abbreviates the whole word and produces `3`.

Together these are the eight possible abbreviations. Notice that results such as `12` never appear. Abbreviating `a` and then abbreviating `bc` without a literal between them is instead represented by the single result `3`.

**Why every generated result is valid.**

The keep branch adds a literal lowercase character and then uses a recursively valid suffix. It cannot introduce an overlap. A run branch replaces one precisely defined substring `word[i:j]` by its positive length. If characters remain, it consumes `word[j]` literally before recursion continues at `j + 1`. Thus any later abbreviated run is separated from the current one by at least that literal character. The recursive calls only work on positions after everything already consumed, so runs can never overlap. These facts establish that every string placed into `ans` satisfies the rules.

**Why no valid result is missing.**

Take any valid abbreviation of the suffix at `i`. If it keeps `word[i]`, it belongs to group one, and the rest of that abbreviation must be returned by `dfs(i + 1)`. Otherwise, its first token abbreviates a unique nonempty run `word[i:j]`. If the run reaches the end, the `j = n` iteration produces it. If it does not reach the end, validity requires the next position `j` to be literal; the loop appends exactly that character, and `dfs(j + 1)` supplies every valid choice for the rest. Therefore the two groups cover every valid abbreviation.

**Why results are not duplicated.**

The keep and abbreviate groups cannot overlap because one begins with the lowercase character `word[i]` while the other begins with a numeric length. Within the run group, different endpoints produce different first run lengths. Once the endpoint is fixed, recursive uniqueness applies to the remaining suffix. Since the input contains only lowercase letters, literal characters cannot be mistaken for numeric length tokens. Inductively, every valid abbreviation has one and only one construction path.

There are $2^n$ results because each original character has a conceptual binary choice: keep it or abbreviate it. Consecutive abbreviated choices are coalesced into one length token, but that does not merge different choice patterns. A result uniquely reveals which positions are represented by each number and which positions are literal. The contract limits $n$ to `15`, making exhaustive output practical; moreover, no algorithm can return all results without doing work proportional to this exponential output.

## Complexity detail

Let $n$ be the length of `word`. There are exactly $2^n$ abbreviations. Each returned string represents all $n$ source positions and can have $O(n)$ textual length: it may contain many literal characters and number tokens, and constructing it involves string concatenation. The total time complexity is therefore $O(n2^n)$. This bound includes producing the required output, not merely visiting abstract choices.

The repeated calls to `dfs` are not memoized. The same suffix index can be evaluated through different earlier choices. Even so, the overall exponential generation remains within the $O(n2^n)$ output-sensitive bound: the algorithm has to materialize $2^n$ strings, and the string-copying work contributes the factor of $n$. Memoizing suffix lists could reduce repeated structural computation, but it would retain large collections and would not reduce the required output size.

Including the returned strings, the space complexity is $O(n2^n)$ because $2^n$ strings of up to $O(n)$ characters are stored. The recursion itself reaches at most $O(n)$ active calls: every recursive step advances by at least one position. Excluding output, the call stack is $O(n)$, although temporary lists and strings are also created while assembling the final output. The manifest reports $O(n2^n)$ space because it counts the result that the function is required to return.

## Alternatives and edge cases

- **Character-by-character backtracking with a pending count:** At each index, either keep the character or increase a counter for the current abbreviated run. When a character is kept, flush any positive counter before that character. This is a common $O(n2^n)$ method and usually uses only $O(n)$ auxiliary stack space beyond the output. The exact source instead chooses an entire run endpoint at once and forces its separator explicitly.

- **Bitmask enumeration:** Use each integer from `0` through $2^n - 1$ as a keep-or-abbreviate pattern. Scan its bits, count consecutive abbreviated positions, and flush the count before each kept character and at the end. This has the same $O(n2^n)$ time and output space, but constructs each answer independently rather than sharing recursive suffix logic.

- **Memoizing `dfs(i)`:** Caching all suffix result lists avoids recomputing the same index, but the cache itself contains exponentially many strings across suffixes. It can improve constants for this particular recursive structure, yet it cannot improve the asymptotic output bound and may keep more intermediate data alive.

- **Single-character word:** For `word = "a"`, the keep branch returns `a`, while the run ending at `n` returns `1`. These are exactly the two required results.

- **Abbreviating the entire word:** The `j = n` loop choice produces `str(n)` and appends no literal character. The permissive `i >= n` base case handles the subsequent `dfs(n + 1)` call correctly.

- **Multi-digit lengths:** Since $n$ may be `15`, a run length can be `10` through `15`. `str(j - i)` emits the whole decimal number as one token. It must not be treated as separate adjacent abbreviations such as `1` and `0`.

- **Repeated letters:** Equal characters at different positions do not create duplicate construction paths. Numeric tokens determine how many source positions were skipped, so the left-to-right parsing still identifies positions. The recursion's endpoint and suffix choices remain unique.

- **Output order:** The method lists all keep-first results before its run-first results at each recursion level. The problem accepts any order, so no sorting is necessary; sorting would add work without changing correctness.

- **Empty input:** The stated contract guarantees at least one character. The helper would still return `['']` for an empty word, but that behavior is outside the required input domain and does not need a separate public-case branch.
