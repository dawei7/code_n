# Guided Example: Find the String with LCP

## 1. What the matrix actually asserts about the hidden string

For a string `word` of length $n$, the entry $\text{lcp}[i][j]$ is the length of the longest common prefix of the two suffixes `word[i..n-1]` and `word[j..n-1]`. Two elementary consequences of that definition drive everything in this problem.

1. **The first-character test.** $\text{lcp}[i][j] > 0$ holds exactly when `word[i] = word[j]`, and $\text{lcp}[i][j] = 0$ holds exactly when `word[i] \ne word[j]`. A positive entry is therefore not a length claim about one character; it is an equality claim about one character.
2. **The suffix recurrence.** If `word[i] = word[j]` and both suffixes continue past their first character, then removing that shared character leaves two suffixes whose longest common prefix is one shorter: $\text{lcp}[i][j] = 1 + \text{lcp}[i+1][j+1]$. If either index equals $n-1$, one suffix has no character left to match, so $\text{lcp}[i][j] = 1$. If `word[i] \ne word[j]`, the value is $0$.

Read together, the positive entries are equality constraints on individual characters, so they partition the positions into classes that must carry one common letter, while the zero entries are inequality constraints that force different classes to receive different letters. The recurrence is what makes the matrix far more demanding than a partition: it also fixes how the whole suffix structure must extend, and a matrix can satisfy every character-level constraint while still being impossible.

## 2. The representative instance

- Input: $\text{lcp} = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]$
- Required output: `"abab"`

| $i$ | $\text{lcp}[i][0]$ | $\text{lcp}[i][1]$ | $\text{lcp}[i][2]$ | $\text{lcp}[i][3]$ | Columns $j$ with $\text{lcp}[i][j] > 0$ |
|---|---|---|---|---|---|
| 0 | 4 | 0 | 2 | 0 | `0`, `2` |
| 1 | 0 | 3 | 0 | 1 | `1`, `3` |
| 2 | 2 | 0 | 2 | 0 | `0`, `2` |
| 3 | 0 | 1 | 0 | 1 | `1`, `3` |

The diagonal already reveals the required suffix lengths: $\text{lcp}[i][i]$ must equal $n - i$, that is $4, 3, 2, 1$, because a suffix is its own longest common prefix. The off-diagonal positive entries come in two separate blocks, which immediately suggests two groups of positions that share a letter — and two groups is exactly what the answer `"abab"` shows.

## 3. Step one: build the equality classes

Scan positions from left to right. Take the first position that has no letter yet, give it the smallest letter not yet used, and force that same letter onto every position $j$ with $\text{lcp}[\text{anchor}][j] > 0$. The anchor's row is the complete list of positions that must share its letter, so one row decides a whole class.

| Round | Letter | Anchor (first unfilled position) | Positive entries in the anchor's row | Positions labelled |
|---|---|---|---|---|
| 1 | `a` | `0` | $\text{lcp}[0][0] = 4$, $\text{lcp}[0][2] = 2$ | `0`, `2` |
| 2 | `b` | `1` | $\text{lcp}[1][1] = 3$, $\text{lcp}[1][3] = 1$ | `1`, `3` |
| 3 | — | none, every position already carries a letter | — | — |

After round 1 the candidate is `a ? a ?`, after round 2 it is `a b a b`, and the scan stops because no unfilled position remains. Two facts make this merge legitimate rather than a guess.

**Positive entries are transitive.** Suppose $\text{lcp}[p][j] > 0$ and $\text{lcp}[i][j] > 0$. Both say the first characters coincide, so `word[p] = word[j] = word[i]`, hence `word[p] = word[i]` and therefore $\text{lcp}[p][i] > 0$. Equality of first characters is an equivalence relation, so the classes it induces are well defined and a single anchor row lists a complete class.

**The merge never has to undo itself on a consistent matrix.** When the anchor $i$ is chosen, every $j$ with $\text{lcp}[i][j] > 0$ is still unlabelled. If some such $j$ had already been labelled in the round anchored at $p < i$, then $\text{lcp}[p][j] > 0$ together with $\text{lcp}[i][j] > 0$ would give $\text{lcp}[p][i] > 0$, which would have labelled $i$ in that same round and made $i$ ineligible as an anchor. Consistency is precisely what the verification of section 5 tests; an inconsistent matrix may indeed force an overwrite, and it is always rejected there.

## 4. Step two: the letters are forced, in order of first appearance

Distinct classes must receive distinct letters, because two positions in different classes have $\text{lcp}[i][j] = 0$, which says their characters differ. Once the classes are known, the only freedom left is which letter names each class, and the lexicographic requirement removes that freedom completely.

| Class | Positions | Smallest position in the class | Letter | Why that letter is forced |
|---|---|---|---|---|
| $C_1$ | `0`, `2` | 0 | `a` | it owns the very first character of the answer, so the smallest possible letter wins immediately |
| $C_2$ | `1`, `3` | 1 | `b` | $\text{lcp}[0][1] = 0$ forbids `a`, so `b` is the smallest letter still available |

Formally, let the classes be ordered by their smallest position. Any valid string uses a distinct letter per class, so at position 0 it uses some letter $\ell_1 \ge$ `a`, and the smallest choice is `a`. If the first $k-1$ classes already match the greedy labels, then position $\min(C_k)$ is the earliest position where the next free choice appears; the greedy puts there the smallest letter not used by the earlier classes, while any other valid string must put a strictly larger letter there. The greedy string is therefore strictly smaller than every other valid string, so it is the unique lexicographically smallest answer — provided the number of classes does not exceed the 26 letters of the alphabet, since a class with no letter left means no valid string exists at all.

## 5. Step three: verify the suffix recurrence

A partition can be consistent while the lengths are not, so the candidate `a b a b` must be checked against every entry. The rule is applied by whether the two positions share a letter and by whether either suffix ends.

| Pair $(i,j)$ | Letters | $\text{lcp}[i][j]$ given | Rule that applies | Required value | Verdict |
|---|---|---|---|---|---|
| `(0,0)` | `a`, `a` | 4 | both indices below $n-1$ | $\text{lcp}[1][1] + 1 = 3 + 1 = 4$ | holds |
| `(0,2)` | `a`, `a` | 2 | both indices below $n-1$ | $\text{lcp}[1][3] + 1 = 1 + 1 = 2$ | holds |
| `(1,1)` | `b`, `b` | 3 | both indices below $n-1$ | $\text{lcp}[2][2] + 1 = 2 + 1 = 3$ | holds |
| `(2,0)` | `a`, `a` | 2 | both indices below $n-1$ | $\text{lcp}[3][1] + 1 = 1 + 1 = 2$ | holds |
| `(2,2)` | `a`, `a` | 2 | both indices below $n-1$ | $\text{lcp}[3][3] + 1 = 1 + 1 = 2$ | holds |
| `(3,3)` | `b`, `b` | 1 | $i = n-1$ | 1, the suffix has length one | holds |
| `(1,3)` | `b`, `b` | 1 | $j = n-1$ | 1, the suffix has length one | holds |
| `(3,1)` | `b`, `b` | 1 | $i = n-1$ | 1, the suffix has length one | holds |

Every one of the eight equal-letter pairs satisfies its rule, including the two that share the class across the symmetry of the matrix. The eight ordered pairs whose letters differ must all carry $0$:

| Pair $(i,j)$ | Letters | $\text{lcp}[i][j]$ given | Required value | Verdict |
|---|---|---|---|---|
| `(0,1)` | `a`, `b` | 0 | 0 | holds |
| `(0,3)` | `a`, `b` | 0 | 0 | holds |
| `(1,0)` | `b`, `a` | 0 | 0 | holds |
| `(1,2)` | `b`, `a` | 0 | 0 | holds |
| `(2,1)` | `a`, `b` | 0 | 0 | holds |
| `(2,3)` | `a`, `b` | 0 | 0 | holds |
| `(3,0)` | `b`, `a` | 0 | 0 | holds |
| `(3,2)` | `b`, `a` | 0 | 0 | holds |

All sixteen ordered pairs agree, and no position was left without a letter, so the answer is `"abab"`. Notice that the candidate already passed the character-level class test after section 3; only this second test decides that the lengths are realizable.

## 6. Why the reasoning is correct: soundness, necessity, and minimality

**If the checks pass, the candidate really has this matrix.** The invariant being established is that the candidate reproduces the given matrix on the diagonal band just processed, and it is proved by induction on $m = \max(i,j)$ downwards from $n-1$. For $m = n-1$, one suffix has length one: if the letters are equal the true longest common prefix is $1$, which the terminal rule demands and confirms, and if the letters differ it is $0$, which the inequality rule demands. For $m < n-1$: differing letters give a true value of $0$, again confirmed; equal letters give $1 + (\text{true value at } (i+1,j+1))$, and by the induction hypothesis applied to the larger index pair $\max(i+1,j+1) = m+1$ the second term equals the given $\text{lcp}[i+1][j+1]$, which is exactly the recurrence the check enforces. Every entry is therefore the genuine longest common prefix length, so the candidate string is a valid answer.

**If a check fails, no string can exist.** Any string whose matrix is the input satisfies all three rules at every pair, because they are consequences of the definition of longest common prefix. A violation of any rule is thus an impossibility proof, not a defect of the candidate, and returning the empty string is the only correct response. The same holds when a position is still unlabelled after the alphabet is exhausted: more than 26 classes would be needed, and a string over 26 letters cannot supply them.

**If the checks pass, no smaller string works.** Section 4 shows that the class partition and the order of first appearance are determined by the matrix alone, and that the greedy labels are pointwise minimal among all valid labellings. Two different valid strings would have to name the same classes, and the first class whose name is larger produces a lexicographically larger string at that class's smallest position. So the verified candidate is the lexicographically smallest answer, and it is returned immediately; there is no second candidate to test.

The two failures the instance class exposes as real are the terminal rule and the recurrence: a diagonal entry $\text{lcp}[i][i]$ above $n - i$ contradicts the terminal rule for the last row, and a positive entry whose successor entry is not exactly one smaller breaks the recurrence. Both are unrecoverable, because they contradict the definition rather than the particular candidate.

## 7. Traps this problem sets

| Trap | Concrete instance | What goes wrong |
|---|---|---|
| Trusting the class partition as the whole answer | $[[3,0,1],[0,2,1],[1,1,1]]$ has positive entries that suggest classes `{0,2}` and `{1,2}` | the recurrence chain is broken, so no string exists and the empty string is required |
| Assuming the diagonal is arbitrary | $[[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]$ | the terminal rule forces $\text{lcp}[3][3] = 1$, and the given $3$ refutes the matrix |
| Assuming symmetry is guaranteed | $[[3,0,0],[1,2,0],[0,0,1]]$ with $\text{lcp}[1][0] = 1$ and $\text{lcp}[0][1] = 0$ | ordered pairs are checked both ways, so an asymmetric pair always fails one direction |
| Reading a zero entry as "no constraint" | $\text{lcp}[0][1] = 0$ in the representative instance | zero says `word[0] \ne word[1]`, which is what forces the second class to use `b` rather than `a` |
| Renaming classes by diagonal order instead of first appearance | the matrix with classes `{0,3}`, `{1,4}`, `{2}` | the answer is `"abcab"`, not `"ababc"`; the earliest occurrence of each class fixes its letter |
| Forgetting the alphabet limit | a $27 \times 27$ matrix with only the diagonal positive | 27 classes need 27 letters, so the empty string is returned even though the lengths are consistent |
| Treating equal letters as always extending | pair `(1,3)` in the representative instance | when either suffix ends, the value must be exactly $1$, never the successor entry plus one |

The same reasoning verified against inputs whose outcomes isolate one idea each:

| Input | Output | Reading |
|---|---|---|
| $[[1]]$ | `a` | one position and one class; the terminal rule demands $\text{lcp}[0][0] = 1$ |
| $[[3,0,0],[0,2,0],[0,0,1]]$ | `abc` | three independent classes, only the diagonal positive, so the letters are `a`, `b`, `c` in order |
| $[[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]$ | `aaaa` | a single class, so one letter repeats and the triangular recurrence chain reproduces every entry |
| $[[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]$ | empty | $\text{lcp}[3][3] = 3$ contradicts the terminal rule |
| $[[3,0,0],[1,2,0],[0,0,1]]$ | empty | asymmetry between two ordered pairs |
| $[[3,0,1],[0,2,1],[1,1,1]]$ | empty | a broken recurrence chain on the last diagonal |
| $[[5,0,0,2,0],[0,4,0,0,1],[0,0,3,0,0],[2,0,0,2,0],[0,1,0,0,1]]$ | `abcab` | classes `{0,3}`, `{1,4}`, `{2}` are labelled in order of first appearance |
| $[[6,0,0,3,0,0],[0,5,0,0,2,0],[0,0,4,0,0,1],[3,0,0,3,0,0],[0,2,0,0,2,0],[0,0,1,0,0,1]]$ | `abcabc` | a periodic structure where the classes repeat with period three |

## 8. Time and auxiliary space

Let $n$ be the length of the unknown string, so the matrix has $n^2$ entries.

- **Class construction.** At most 26 rounds run, one per letter, and each round scans the anchor's row of at most $n$ entries while the shared cursor advances monotonically across positions. The work is $O(26n)$, which is linear in $n$ for a fixed alphabet.
- **Verification.** Every ordered pair $(i,j)$ is examined once and answered by a constant-time comparison against one neighbour entry, so this phase is $\Theta(n^2)$. It dominates: the total running time is $O(n^2)$, which matches the size of the input and is optimal since every entry must be read at least once.
- **Auxiliary space.** The candidate string and the class bookkeeping need $O(n)$ storage, plus $O(1)$ counters for the anchor cursor and the current letter. No second $n \times n$ table is ever built, because every check reads entries of the given matrix instead of recomputing prefix lengths; that is what keeps the extra space linear while the input itself already occupies $\Theta(n^2)$.
- The constraint $n \le 1000$ makes the quadratic verification about a million pair tests, and the alphabet boundary at 26 classes is a separate limit that no value of $n$ can work around.
