# Guided Example: Guess the Word

We trace the step-by-step interactive Master API protocol, Hamming coordinate match count calculation ($matches(u, v) = \sum \mathbb{I}[u_k == v_k]$), Minimax candidate selection across partition buckets, worst-case remaining pool minimization ($\arg\min \max |bucket_s|$), feedback consistency filtering ($matches(guess, c) == score$), and guaranteed termination within the allowed guess quota on representative word vocabularies:

- **Input:**
  $$
  words = [\text{"acckzz"}, \; \text{"ccbazz"}, \; \text{"eiowzz"}, \; \text{"abcczz"}], \quad secret = \text{"acckzz"}
  $$
- **Required outcome:**
  Find the secret word within the allowed guess quota (calling `master.guess(secret)` returning 6).
  - Interactive guessing specifications:
    - All words consist of 6 lowercase letters.
    - One unknown word in $words$ is designated as the $secret$.
    - The API `master.guess(word)` takes a 6-letter word from the list and returns an integer $score \in [0, 6]$, indicating how many positions have the exact same character:
      $$
      score = \sum_{k=0}^5 \mathbb{I}[word[k] == secret[k]]
      $$
    - If $score == 6$, the secret word has been identified and the game is won.
    - We are allowed at most 10 guesses (or 30 in harder variants).
    - For $words = [\text{"acckzz"}, \text{"ccbazz"}, \text{"eiowzz"}, \text{"abcczz"}]$ with $secret = \text{"acckzz"}$:
      - Inspect pairwise coordinate matches:
        - `"acckzz"` vs `"ccbazz"`: indices 4, 5 both have `'z'` $\implies \mathbf{2\ matches}$.
        - `"acckzz"` vs `"eiowzz"`: indices 4, 5 both have `'z'` $\implies \mathbf{2\ matches}$.
        - `"acckzz"` vs `"abcczz"`: indices 0 ('a'), 2 ('c'), 4 ('z'), 5 ('z') $\implies \mathbf{4\ matches}$.
      - If our strategy picks `"acckzz"`, `master.guess("acckzz")` returns 6 immediately.
      - If our strategy picks `"eiowzz"`, `master.guess("eiowzz")` returns 2:
        - We filter the remaining pool to only words that have exactly 2 matches with `"eiowzz"`.
        - `"abcczz"` matches `"eiowzz"` at 2 positions (`"zz"`), `"acckzz"` matches at 2 positions (`"zz"`), `"ccbazz"` matches at 2 positions (`"zz"`).
        - Next guess finds the secret.
- **Minimax Information Partition Invariant:**
  - **The Coordinate Match Function:**
    - For any two words $u$ and $v$:
      $$
      matches(u, v) = \sum_{k=0}^5 \mathbb{I}[u[k] == v[k]] \in \{0, 1, 2, 3, 4, 5, 6\}
      $$
  - **The Partitioning Effect of a Guess:**
    - When we guess word $w$, the Master reveals $score = matches(w, secret)$.
    - The secret word **must** have exactly $score$ matches with $w$.
    - Therefore, all candidates $c$ where $matches(w, c) \ne score$ are **permanently eliminated**!
    - The remaining candidate set after guessing $w$ is:
      $$
      candidates_{next} = \{ c \in candidates \mid matches(w, c) == score \}
      $$
  - **The Minimax Decision Rule:**
    - Since we do not know which score the Master will return, we evaluate the **worst-case outcome**:
      - For a chosen word $w$, group all candidates by their match score with $w$ into 7 buckets (scores $0 \dots 6$).
      - The worst-case remaining candidate pool size is the size of the largest bucket:
        $$
        \text{worst}(w) = \max_{s \in \{0 \dots 6\}} \big| \{ c \in candidates \mid matches(w, c) == s \} \big|
        $$
      - To minimize the worst-case size of the next candidate pool, choose the word with the smallest worst-case bucket:
        $$
        guess = \arg\min_{w \in candidates} \text{worst}(w)
        $$
    - This ensures maximum entropy reduction and the fastest possible contraction of the candidate pool.
- **Step-by-Step Worked Execution Trace on the 4-Word Vocabulary:**
  - Initial candidate pool:
    $$
    candidates = [\text{"acckzz"}, \; \text{"ccbazz"}, \; \text{"eiowzz"}, \; \text{"abcczz"}] \quad (|candidates| = 4)
    $$
  - **Iteration 1: Compute Minimax Scores for Each Candidate:**
    - **Evaluating $w = \text{"acckzz"}$:**
      - vs `"acckzz"`: 6 matches (Bucket 6 has 1 word).
      - vs `"ccbazz"`: 2 matches (Bucket 2).
      - vs `"eiowzz"`: 2 matches (Bucket 2).
      - vs `"abcczz"`: 4 matches (Bucket 4).
      - Bucket distribution: Bucket 2 has 2 words, Bucket 4 has 1 word, Bucket 6 has 1 word.
      - Maximum bucket size: $\text{worst}(\text{"acckzz"}) = \mathbf{2}$.
    - **Evaluating $w = \text{"eiowzz"}$:**
      - vs `"eiowzz"`: 6 matches (Bucket 6 has 1 word).
      - vs `"acckzz"`: 2 matches.
      - vs `"ccbazz"`: 2 matches.
      - vs `"abcczz"`: 2 matches.
      - Bucket distribution: Bucket 2 has 3 words, Bucket 6 has 1 word.
      - Maximum bucket size: $\text{worst}(\text{"eiowzz"}) = \mathbf{3}$.
    - **Evaluating $w = \text{"abcczz"}$:**
      - vs `"abcczz"`: 6 matches.
      - vs `"acckzz"`: 4 matches.
      - vs `"ccbazz"`: 3 matches.
      - vs `"eiowzz"`: 2 matches.
      - Bucket distribution: all buckets have size 1.
      - Maximum bucket size: $\text{worst}(\text{"abcczz"}) = \mathbf{1}$.
  - **Choose Minimax Guess:**
    - The minimum worst-case bucket size is $\mathbf{1}$, achieved by $w = \mathbf{\text{"abcczz"}}.$
    - Submit guess:
      $$
      guess = \text{"abcczz"}
      $$
  - **Master API Response:**
    - Secret is `"acckzz"`.
    - Coordinates matching:
      - Index 0: `'a' == 'a'` (match)
      - Index 1: `'b' \ne 'c'`
      - Index 2: `'c' == 'c'` (match)
      - Index 3: `'c' \ne 'k'`
      - Index 4: `'z' == 'z'` (match)
      - Index 5: `'z' == 'z'` (match)
    - Total matching coordinates: $score = \mathbf{4}$.
  - **Candidate Pool Filtering ($score = 4$):**
    - Retain candidates $c$ satisfying $matches(\text{"abcczz"}, c) == 4$:
      - `"acckzz"`: matches at 4 positions $\implies \mathbf{Retained!}$
      - `"ccbazz"`: matches at 3 positions $\implies \mathbf{Eliminated.}$
      - `"eiowzz"`: matches at 2 positions $\implies \mathbf{Eliminated.}$
      - `"abcczz"`: matches at 6 positions $\implies \mathbf{Eliminated.}$
    - Updated candidate pool:
      $$
      candidates_{next} = [\text{"acckzz"}] \quad (|candidates| = 1)
      $$
  - **Iteration 2:**
    - Only 1 candidate remains: $guess = \mathbf{\text{"acckzz"}}.$
    - Call `master.guess("acckzz")` $\implies score = \mathbf{6}.$
    - Secret word found in only **2 guesses**!
- **Zero-Match Elimination Power ($score = 0$):**
  - If a guess returns $score = 0$, that guess shares **zero letters** with the secret.
  - Every word sharing even one letter with that guess is eliminated, often slashing $80\%$ of the remaining vocabulary in a single round.

This instance demonstrates active hypothesis testing in discrete metric spaces and game-theoretic Minimax tree search, mathematically proves why minimizing maximal partition fiber cardinalities minimizes worst-case query depth, and derives $O(G \cdot N^2 \cdot L)$ runtime where $G \le 10$ and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a list of 6-letter words:
An interactive Master returns $score = \text{number of matching letters at same positions}$.
Find the secret word within at most 10 guesses.

```text
Words: [ "acckzz", "ccbazz", "eiowzz", "abcczz" ]
Secret: "acckzz"

Round 1:
  Minimax picks "abcczz" (minimizes largest bucket).
  master.guess("abcczz") returns 4.
  Filter: keep only words with 4 matches to "abcczz".
  Only "acckzz" has 4 matches!

Round 2:
  Guess "acckzz" -> master.guess("acckzz") returns 6!
  Success in 2 guesses!
```

### The Invariant of Minimax Information Gain
- For each candidate $w$, count how words distribute across score buckets $0 \dots 6$.
- Pick $w$ that minimizes the size of its largest bucket:
  $$
  guess = \arg\min_{w} \max_{s} |\{ c \mid matches(w, c) == s \}|
  $$
- Keep only candidates with $matches(guess, c) == score$.

---

## 2. Conceptual Foundation & Invariants

### 1. Fiber Partition:
$$
\mathcal{B}(w, s) = \{ c \in \mathcal{C} \mid d(w, c) = s \}
$$
$$
\mathcal{C} = \bigsqcup_{s = 0}^6 \mathcal{B}(w, s)
$$

### 2. Minimax Criterion:
$$
w^* = \arg\min_{w \in \mathcal{C}} \max_{0 \le s \le 6} |\mathcal{B}(w, s)|
$$
$$
\mathcal{C}_{t+1} = \mathcal{B}(w^*, \text{score})
$$

> **Entropy Reduction Invariant.** Let $H(\mathcal{C})$ be the entropy of the uniform prior over remaining candidates. The expected entropy reduction $\Delta H = H(\mathcal{C}) - \sum_s p(s) H(\mathcal{B}(w, s))$ is maximized when the fibers $\mathcal{B}(w, s)$ are as balanced as possible, ensuring exponential candidate decay.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Evaluate Minimax
- Candidate `"abcczz"` yields bucket sizes $\le 1$.
- Pick `"abcczz"`.

---

### Step 2: Guess `"abcczz"`
- $score = 4$.
- Filter candidates with 4 matches to `"abcczz"`.

---

### Step 3: Filtered Pool
- `"acckzz"`: 4 matches $\implies$ kept.
- All other candidates eliminated.
- Pool: `["acckzz"]`.

---

### Step 4: Final Guess
- Guess `"acckzz"` $\implies score = 6$. Found!

---

## 4. Complete Execution Trace

| Round | Guess Submitted | Master Score | Filtering Condition | Candidates Remaining | Size $\lvert \mathcal{C} \rvert$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Round $1$ | `"abcczz"` | $4$ | $matches(\text{"abcczz"}, c) == 4$ | `["acckzz"]` | $1$ |
| **Round $2$** | **`"acckzz"`** | **`6`** | **Found!** | **`["acckzz"]`** | **`1`** |

---

## 5. Boundary Cases & Failure Modes

- **$score = 0$ Response:** Powerful filter; eliminates all words sharing any common character at any position with the guess.
- **Small Candidate Pool ($N \le 10$):** Resolves in 1 to 3 guesses.
- **Identical Match Distributions:** Ties broken arbitrarily by `min()`.
- **Large Vocabulary ($N = 100$):** Minimax guarantees finding the secret within 10 guesses with high probability.

---

## 6. Traps & Common Anti-Patterns

- **Guessing Random Words Without Minimax:** Picking candidates at random can leave 80 words in the largest bucket, causing the 10-guess limit to be exceeded.
- **Retaining Words with Different Scores:** If Master returns 2, candidates with 0, 1, 3, 4, 5, or 6 matches must be removed immediately.
- **Re-Guessing Eliminated Words:** Only candidates from the active filtered pool should be considered for subsequent guesses.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of candidates ($N \le 100$) and word length $L = 6$.
  - In each round, pairwise match matrix calculation takes $\mathcal{O}(N^2 \cdot L)$ operations.
  - At most 10 rounds are executed ($G \le 10$).
  - Total Time: strictly bounded $\mathcal{O}(G \cdot N^2 \cdot L) \approx 10 \times 10^4 \times 6 = 6 \times 10^5$ operations. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to maintain the candidate list.
