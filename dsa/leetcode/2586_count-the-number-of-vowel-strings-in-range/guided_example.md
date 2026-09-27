# Guided Example: Count the Number of Vowel Strings in Range

## 1. The instance we will count

The second official instance supplies an array, a window, and two one-sided traps:

- `words = ["hey", "aeo", "mu", "ooo", "artro"]`, of length $5$;
- `left = 1` and `right = 4`, so the window is the inclusive index range $[1, 4]$;
- the required outcome is `3`.

A word is a **vowel string** when its first character is one of `a`, `e`, `i`, `o`, `u` **and** its last character is one of those five letters. The requested value is the number of vowel strings at indices $i$ with `left <= i <= right`. The instance is well chosen because index $2$ holds `"mu"`, whose final letter is the vowel `u` while its first letter is a consonant: reasoning that inspects only the final character will count it and return `4` instead of `3`. The same array also contains `"hey"` at index $0$, one position left of the window, so the range boundary has to be respected independently of the predicate.

## 2. Reducing the definition to two endpoint tests

The definition mentions only the first and the last character of a word, so a word of length $L$ carries exactly two relevant facts, no matter how large $L$ is. Write

$$
A(i) \;=\; \bigl(\, \text{words}[i][0] \in V \,\bigr) \;\wedge\; \bigl(\, \text{words}[i][L_i - 1] \in V \,\bigr),
\qquad V = \{\texttt{a},\texttt{e},\texttt{i},\texttt{o},\texttt{u}\}
$$

where $L_i$ is the length of `words[i]` and $A(i)$ is the indicator of "is a vowel string". Evaluating $A$ for the five words of the instance gives the complete picture before any counting starts.

| Index $i$ | `words[i]` | Length $L_i$ | First character | Last character | Starts with a vowel? | Ends with a vowel? | $A(i)$ |
|---|---|---|---|---|---|---|---|
| 0 | `"hey"` | 3 | `h` | `y` | no | no | `0` |
| 1 | `"aeo"` | 3 | `a` | `o` | yes | yes | `1` |
| 2 | `"mu"` | 2 | `m` | `u` | no | yes | `0` |
| 3 | `"ooo"` | 3 | `o` | `o` | yes | yes | `1` |
| 4 | `"artro"` | 5 | `a` | `o` | yes | yes | `1` |

The conjunction in $A$ is the whole difficulty of the problem. Index $2$ is the decisive row: the last-character test succeeds there, so the word is a *partial* match, and only the first-character test removes it. Because the two tests are independent, the indicator is `1` exactly when both columns read "yes".

## 3. The window restricts which indices are examined

The count ranges over indices, not over array values. The window is inclusive on both ends, so the inspected indices are precisely $left, left + 1, \dots, right$, a set of exactly

$$
r - l + 1 = 4 - 1 + 1 = 4
$$

positions, where $l$ and $r$ abbreviate `left` and `right`. Index $0$ and any index above $4$ are outside the window and cannot contribute, regardless of whether they hold vowel strings.

| Window parameter | Value in this instance | Effect |
|---|---|---|
| Indices examined | `1, 2, 3, 4` | Exactly $r - l + 1 = 4$ candidate positions |
| Indices excluded below | `0` | `"hey"` is never tested, even though it would not qualify anyway |
| Indices excluded above | `5, 6, ...` | None exist, since `words.length - 1 = 4` |
| Endpoints | `left = 1` and `right = 4` | Both are included; dropping either would change the answer |

Note that the guarantees $0 \le left \le right < \text{words.length}$ make the window always non-degenerate and always in bounds, so no clamping, swapping, or empty-window handling is needed. A useful consequence is that the answer is `0` only when every word inside the window fails at least one endpoint test; it can never be `0` merely because the window is empty.

## 4. Accumulating the answer position by position

The answer is the sum of the indicators over the window,

$$
\text{answer} \;=\; \sum_{i=l}^{r} A(i) \;=\; A(1) + A(2) + A(3) + A(4),
$$

and it is computed by one left-to-right sweep that maintains a single counter. The invariant of the sweep is that the counter holds the number of vowel strings among the positions already visited, that is, among indices $l, \dots, i$ after step $i$ has been applied.

| Step | Index $i$ | `words[i]` | $A(i)$ | Counter before | Counter after | Meaning of the counter after the step |
|---|---|---|---|---|---|---|
| 1 | 1 | `"aeo"` | `1` | 0 | 1 | One vowel string among indices $1$ to $1$ |
| 2 | 2 | `"mu"` | `0` | 1 | 1 | One vowel string among indices $1$ to $2$ |
| 3 | 3 | `"ooo"` | `1` | 1 | 2 | Two vowel strings among indices $1$ to $3$ |
| 4 | 4 | `"artro"` | `1` | 2 | 3 | Three vowel strings among indices $1$ to $4$ |

After the final step the counter equals $3$, which matches the required outcome. The two increments come from `"aeo"` and `"ooo"`, the increment at step $4$ comes from `"artro"`, and step $2$ contributes nothing because $A(2) = 0$.

Each position is visited exactly once and contributes either `0` or `1`, so the counter never counts a word twice and never skips one. That is the entire counting argument: a sum of indicators over a contiguous window, evaluated by a single pass.

## 5. Why both endpoint tests are unavoidable

Every wrong answer to this problem comes from dropping one half of the conjunction. The instance contains one word of each failure type, and the authored cases contain the rest.

| Word (or situation) | First character | Last character | Verdict | Which half of the test rejects it |
|---|---|---|---|---|
| `"mu"` | `m`, a consonant | `u`, a vowel | `0` | The first-character test |
| `"hey"` | `h`, a consonant | `y`, a consonant | `0` | Both halves |
| `"ant"` | `a`, a vowel | `t`, a consonant | `0` | The last-character test |
| `"table"` | `t`, a consonant | `e`, a vowel | `0` | The first-character test |
| `"unit"` | `u`, a vowel | `t`, a consonant | `0` | The last-character test |
| `"ooo"` | `o`, a vowel | `o`, a vowel | `1` | Neither half |

A word that begins with a vowel but ends with a consonant, and a word that ends with a vowel but begins with a consonant, are equally disqualified. Checking only the first character, or only the last, is not an approximation of the rule: it is a different rule, and on this instance dropping the first-character test would return `4` rather than `3`.

## 6. Boundaries, degenerate shapes, and traps

| Situation | Instance | Outcome | Why |
|---|---|---|---|
| One-character word that is a vowel | `words = ["a"]`, `left = 0`, `right = 0` | `1` | The first and the last character are the same letter, so both tests read the same character and both succeed |
| One-character word that is a consonant | `words = ["z"]`, `left = 0`, `right = 0` | `0` | Both tests inspect `z` and both fail |
| Window is a single position | `words = ["aa","bc","ee"]`, `left = 1`, `right = 1` | `0` | The qualifying words `"aa"` and `"ee"` lie outside the window; only `"bc"` is tested, and it fails both tests |
| Several qualifying words in range | `words = ["a","e","i","o","u"]`, full window | `5` | Every word is a single vowel, so every indicator is `1` |
| Both endpoints are qualifying | `words = ["aba","bbb","ece"]`, `left = 0`, `right = 2` | `2` | Inclusion of `right` is required: `"ece"` sits exactly on the upper endpoint |
| Duplicate string values | Two identical vowel strings in the window | counted twice | The count is over indices, so equal values occupy two positions and contribute two indicators |
| Longest allowed word | A word of length $10$ with vowel endpoints | `1` | Only the endpoints are inspected; the interior letters are irrelevant and never change the verdict |
| Longest allowed word, bad interior | `"abcdefghia"` | `1` | Interior consonants do not matter, because the definition constrains only the first and last characters |

Two traps deserve explicit statements. First, do not confuse the two index spaces: the window indices describe *positions in the array*, while the first and last characters describe *positions inside a word*, so `left` and `right` must never be compared with a character offset. Second, "starts with a vowel" means exactly membership in the five-letter set $V$; the letter `y` is not in $V$, so `"hey"` ends with a consonant, and uppercase letters cannot occur because the words consist of lowercase English letters only.

## 7. The correctness argument for the sweep

Two properties together establish that the sweep returns the requested number.

**Each counted word satisfies the definition.** The counter is incremented only at positions where both endpoint tests succeed, and those two tests are precisely the definition of a vowel string. A word that fails either test leaves the counter unchanged, so no word is credited without meeting the rule.

**Every qualifying position in the window is counted exactly once.** The sweep visits the indices $l, l+1, \dots, r$ in order, exactly once each, and stops after $r$. The guarantees $0 \le left \le right < \text{words.length}$ ensure this list is non-empty and contains no index outside the array, so no in-window position is skipped and no out-of-window position is visited. Because each visited position changes the counter by the indicator $A(i)$, induction on the number of steps gives the invariant

$$
\text{counter after position } i \;=\; \sum_{j=l}^{i} A(j),
$$

and instantiating it at $i = r$ yields the required sum. The sweep is therefore sound (it never over-counts) and complete (it never under-counts).

**A note on alternatives.** A prefix-sum table would answer many window queries on the same array in $O(1)$ each, at the cost of an $O(n)$ precomputation and $O(n)$ auxiliary storage; that trade is only worthwhile when the number of queries is large, and the interface here provides a single window. A regular-expression match, or a normalisation step such as collecting the endpoints of every word into a boolean array first, would compute exactly the same indicators while adding a second pass over the data; the single sweep already has the optimal shape for one query.

## 8. Complexity: time and auxiliary space

**Time.** Exactly $r - l + 1$ words are inspected, so the work is $\Theta(k)$ where $k = r - l + 1$ is the window width; the worst case over all valid windows is $\Theta(n)$ for $n = \text{words.length}$. Each inspection reads two characters and tests membership in a fixed five-letter set, both of which are $O(1)$ operations that do not depend on the word length $L_i \le 10$. The total cost is therefore independent of the interior of the words, which is why very long words cost the same as very short ones.

**Auxiliary space.** The sweep stores one counter and one loop index, so the extra space is $O(1)$; it never builds a slice of the array, a prefix-sum table, or an endpoint array. The input array and its strings are read-only and are not counted as auxiliary storage, so the reported memory does not grow with $n$.
