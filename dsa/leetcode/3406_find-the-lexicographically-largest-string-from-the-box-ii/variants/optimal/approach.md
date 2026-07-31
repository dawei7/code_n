## General

Let $n=\lvert\texttt{word}\rvert$ and suppose `numFriends > 1`. Any one piece can use at most

$$
L=n-\texttt{numFriends}+1
$$

characters, because the other friends must each receive at least one character. Conversely, a substring of length at most $L$ can be included in some valid split whenever it is placed at its chosen position: the characters outside it provide enough room for the remaining cuts. For a fixed starting index, the longest legal piece is lexicographically at least as large as each of its proper prefixes. It is therefore enough to compare `word[i : i + L]` over all starts $i$.

These candidates are capped prefixes of suffixes. If one complete suffix is lexicographically larger than another, truncating both at $L$ characters can make them tie but cannot reverse their order. Thus a starting position of the lexicographically largest suffix also yields a largest legal piece.

Find that suffix without constructing or sorting all suffixes. Keep `best` and `candidate` as two competing starts and let `offset` be the length of their known common prefix. If the characters at that offset are equal, extend the comparison. If the candidate character is larger, the current best and every start through the mismatching position can be discarded, so advance `best` beyond that range and restart with the next candidate. If the best character is larger, discard the candidate and all starts through its mismatching position instead. Every discarded index is passed only a constant number of times, so the scan is linear.

When only one friend participates, no cut is made and the sole possible piece is the entire `word`; handle that case directly. Otherwise, return at most $L$ characters from the winning suffix start.

## Complexity detail

Each start is eliminated once, and the equal-character offset advances only across ranges that are subsequently discarded. The suffix selection therefore takes $O(n)$ time. The algorithm stores only three indices, so its auxiliary space is $O(1)$; the returned string itself can contain $O(n)$ characters.

The benchmark defines `size` as $n$ and uses legal 40-, 80-, and 160-character all-equal strings, spanning 4x. Equal prefixes force a direct pairwise suffix comparator to revisit quadratically many characters. The accepted two-pointer scan remains linear, while that correct $O(n^2)$ alternative fails only the scaling verdict.

## Alternatives and edge cases

- **Sort every suffix:** Materializing and sorting suffixes can require $O(n^2)$ stored characters and at least quadratic total copying or comparison work.
- **Compare every capped candidate directly:** This is simple and correct, but repeated long common prefixes make it take $O(n^2)$ time.
- **Suffix array:** A suffix array also identifies the largest suffix, but it uses substantially more machinery and at least $O(n)$ auxiliary storage.
- **One friend:** The entire input is the only piece; selecting a proper suffix would be illegal.
- **One character per friend:** When `numFriends == n`, every piece has length one, so the answer is the largest character.
- **Repeated prefixes:** The offset must reset after either competitor is discarded; otherwise comparisons can skip the first distinguishing character.
- **Winning suffix shorter than the cap:** Slicing naturally returns the complete suffix, which is a legal piece because the remaining prefix can supply the other friends.
