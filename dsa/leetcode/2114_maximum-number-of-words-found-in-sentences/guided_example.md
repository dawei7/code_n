# Guided Example: Maximum Number of Words Found in Sentences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input Sentences:** `["alice and bob love leetcode", "i think so too", "this is great thanks very much"]`
- **Expected Output:** `6`

This instance illustrates how word counting simplifies to space counting under standard sentence formatting guarantees, showing how the maximum word count is evaluated across multiple candidate sentences without string allocations.

---

## 1. Problem Overview & Representative Instance

A sentence is defined as a list of words separated by a single space character with no leading or trailing spaces. Given an array of sentences, we need to determine the maximum number of words contained within any single sentence.

Consider the representative input array consisting of three sentences:
1. Sentence $0$: `"alice and bob love leetcode"`
2. Sentence $1$: `"i think so too"`
3. Sentence $2$: `"this is great thanks very much"`

Our objective is to compute the word count for each sentence, identify the maximum across the collection, and return this value without incurring memory overhead from string splitting.

---

## 2. Mathematical & Algorithmic Principles

### Bijective Separator Invariant
Let a sentence $T$ consist of $k$ non-empty words $w_1, w_2, \dots, w_k$ concatenated with single delimiters. The structural form is:

$$T = w_1 \cdot \text{' '} \cdot w_2 \cdot \text{' '} \cdots \text{' '} \cdot w_k$$

Because there are strictly zero leading spaces, zero trailing spaces, and no consecutive spaces, each space character acts as a separator between two adjacent words. By elementary induction on the number of separators:
- If a sentence contains $k$ words, there are exactly $k - 1$ boundary positions between them.
- Each boundary position contains exactly one space character.
- Therefore, the number of spaces $S$ in sentence $T$ satisfies:

$$S = k - 1 \implies k = S + 1$$

### Commutativity of Monotonic Shifts
To find the maximum word count across a set of sentences $\{T_1, T_2, \dots, T_m\}$, we observe:

$$\max_{1 \le i \le m} (\text{words}(T_i)) = \max_{1 \le i \le m} (S_i + 1) = 1 + \max_{1 \le i \le m} S_i$$

where $S_i$ denotes the count of space characters in sentence $T_i$. This equivalence demonstrates that adding $1$ to each word count commutes with taking the maximum. Hence, one can stream through characters, count spaces per sentence, maintain a running maximum of spaces, and add $1$ once at the conclusion.

| Component | Role in Evaluation | Mathematical Property |
|---|---|---|
| Delimiter Count $S_i$ | Number of ASCII space characters in sentence $i$ | $S_i \ge 0$ for all valid sentences |
| Word Count $W_i$ | Number of words in sentence $i$ | $W_i = S_i + 1$ |
| Global Maximum $\mu$ | Maximum space count observed across all sentences | $\mu = \max(S_1, S_2, \dots, S_m)$ |
| Final Result | Global maximum word count | $\mu + 1$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We process each sentence sequentially, scanning character by character or counting space characters directly.

### Sentence 0: `"alice and bob love leetcode"`
- Characters: `'a'`, `'l'`, `'i'`, `'c'`, `'e'`, `' '`, `'a'`, `'n'`, `'d'`, `' '`, `'b'`, `'o'`, `'b'`, `' '`, `'l'`, `'o'`, `'v'`, `'e'`, `' '`, `'l'`, `'e'`, `'e'`, `'t'`, `'c'`, `'o'`, `'d'`, `'e'`
- We detect spaces at 4 positions (between "alice" and "and", "and" and "bob", "bob" and "love", "love" and "leetcode").
- Space count $S_0 = 4$.
- Derived word count: $W_0 = 4 + 1 = 5$.
- Running maximum space count: $\max(0, 4) = 4$.

### Sentence 1: `"i think so too"`
- Characters: `'i'`, `' '`, `'t'`, `'h'`, `'i'`, `'n'`, `'k'`, `' '`, `'s'`, `'o'`, `' '`, `'t'`, `'o'`, `'o'`
- We detect spaces at 3 positions (between "i" and "think", "think" and "so", "so" and "too").
- Space count $S_1 = 3$.
- Derived word count: $W_1 = 3 + 1 = 4$.
- Running maximum space count: $\max(4, 3) = 4$.

### Sentence 2: `"this is great thanks very much"`
- Characters: `'t'`, `'h'`, `'i'`, `'s'`, `' '`, `'i'`, `'s'`, `' '`, `'g'`, `'r'`, `'e'`, `'a'`, `'t'`, `' '`, `'t'`, `'h'`, `'a'`, `'n'`, `'k'`, `'s'`, `' '`, `'v'`, `'e'`, `'r'`, `'y'`, `' '`, `'m'`, `'u'`, `'c'`, `'h'`
- We detect spaces at 5 positions.
- Space count $S_2 = 5$.
- Derived word count: $W_2 = 5 + 1 = 6$.
- Running maximum space count: $\max(4, 5) = 5$.

### Termination and Final Computation
All $3$ sentences have been evaluated. The maximum space count across all sentences is $\mu = 5$.
Adding the constant offset gives:

$$\text{Maximum Words} = \mu + 1 = 5 + 1 = 6$$

---

## 4. Comprehensive State Trace

The table below details the evaluation metrics for each sentence in the input collection.

| Sentence Index | Sentence Text | Character Length | Counted Spaces ($S_i$) | Calculated Words ($S_i + 1$) | Running Max Spaces ($\mu$) |
|---|---|---|---|---|---|
| $0$ | `"alice and bob love leetcode"` | $26$ | $4$ | $5$ | $4$ |
| $1$ | `"i think so too"` | $14$ | $3$ | $4$ | $4$ |
| $2$ | `"this is great thanks very much"` | $30$ | $5$ | $6$ | $5$ |

Final result returned: $5 + 1 = 6$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** The correctness relies on the strict formatting guarantee given by the problem:
1. Sentences do not contain leading or trailing whitespace. Thus, neither the first character nor the last character is ever a space.
2. Consecutive words are separated by exactly one space. Thus, no two spaces appear consecutively, preventing spurious empty word tokens.
3. Every word consists of at least one non-space character.
Because every space character corresponds to an adjacent word boundary, the bijective relation between boundaries and words is preserved. No spaces can be misattributed, ensuring that $S_i + 1$ matches the exact number of words for every sentence.

**Completeness.** Every sentence in the input array is inspected. Because the maximum operator is monotonic and associative, considering all sentences guarantees that the global supremum is found.

---

## 6. Edge Cases & Anti-Patterns

- **Single-Word Sentences:** A sentence like `"hello"` contains zero spaces. The formula correctly computes $0 + 1 = 1$ word.
- **Identical Word Counts:** If multiple sentences tie for the maximum word count, the supremum operator naturally captures the tied value without requiring special tie-breaking logic.
- **Array of Length One:** When the input consists of a single sentence, the loop executes once and immediately outputs the word count of that lone sentence.
- **Anti-Pattern — Substring Allocation:** Splitting strings into arrays of substrings (e.g. splitting on whitespace) allocates auxiliary memory for each word in each sentence, creating unnecessary garbage collector churn. Counting delimiters directly in a single pass operates in strictly $O(1)$ auxiliary space.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L)$, where $L$ is the total number of characters across all sentences in the input array. Each character is examined exactly once during the delimiter counting pass.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$, as only a few scalar variables are maintained to track the current sentence's space count and the global maximum space count. No heap-allocated arrays or split word tokens are generated.
