## General

**See the result as a sequence of independent choices**

Every digit has exactly one allowed form: it must remain unchanged. Every letter has exactly two allowed forms: lowercase and uppercase.

If the string contains $\ell$ letters, choosing one of two cases independently for each letter creates $2^\ell$ distinct output strings. The algorithm must produce all of them, so exponential output size is unavoidable. The goal is to generate that complete set systematically without doing unrelated work.

**Use depth-first search over string positions**

The mutable list `t = list(s)` holds the characters of the current candidate. Function `dfs(i)` is responsible for generating every valid completion of positions `i` through the end, while positions before `i` already represent choices made on the current recursion path.

At every position, the function first calls `dfs(i + 1)` without changing `t[i]`. This branch keeps the character in its current case.

If `t[i].isalpha()` is true, there is a second valid choice. The algorithm toggles the character's case and calls `dfs(i + 1)` again. For a digit, there is no second call because changing a digit is not permitted.

Thus a letter creates two branches and a digit creates one.

**Understand the base case**

When `i >= len(t)`, every input position has been assigned a valid character. The method joins the list into a string and appends that completed candidate to `ans`.

Joining is important. If the algorithm appended the mutable list `t` itself, later toggles would change the already stored results because every entry would refer to the same list object. `"".join(t)` creates an independent immutable string snapshot.

The index advances by one in every recursive call, so every path eventually reaches this base case.

**Why XOR with 32 changes English-letter case**

Under the character encoding used for English ASCII letters, an uppercase letter and its lowercase version differ in bit value 32. For example, the character codes for `A` and `a` are 65 and 97, and $65 \mathbin{\text{XOR}} 32 = 97$.

The expression:

`chr(ord(t[i]) ^ 32)`

therefore maps lowercase to uppercase and uppercase back to lowercase. XOR is its own inverse, so applying the same operation twice restores the original case.

This technique is safe here because the contract restricts letters to lowercase and uppercase English letters. It should not be generalized to arbitrary Unicode alphabetic characters merely because `isalpha()` recognizes them.

**Why the first branch means “keep the current case,” not always lowercase**

The input may contain either uppercase or lowercase letters. The task asks for both case choices, so it does not matter which one is emitted first.

At a letter, the first branch preserves whatever case is currently stored in `t[i]`, and the second branch emits its opposite. Together they cover exactly the two allowed choices. No normalization step is required.

**Why the implementation can omit a conventional restore step**

Many backtracking algorithms toggle a value, recurse, and then immediately toggle it back. This implementation does not restore `t[i]` after its second branch.

That is still correct because a completed call to `dfs(i)` guarantees only that it has generated both cases for every suffix position, not that the suffix list is restored to a particular spelling. When an earlier parent later calls `dfs(i)` again, the current character at position `i` may be in either case. The first branch generates completions using that current case, and the XOR branch generates completions using the other case. The pair of choices is complete regardless of which case happens to come first.

No later operation changes positions smaller than its current index. Therefore the prefix choices belonging to the parent path remain intact. Persistent changes occur only within the suffix that the next call will enumerate in both possible ways anyway.

**Trace `s = "a1b"`**

Start with `t = ['a','1','b']`.

At index zero, the first branch keeps `a`. Index one is a digit, so it has only the unchanged branch. At index two, the first branch produces `"a1b"` and the toggled branch produces `"a1B"`.

After that suffix call, `t[2]` may remain `B`. The algorithm toggles index zero to `A` and explores the suffix again. At index two, keeping its current `B` produces `"A1B"`, and toggling it produces `"A1b"`.

The order differs from some sample listings, but the problem permits any order. All four valid strings appear exactly once.

**Why every valid permutation is generated**

Consider any desired output. At each letter position, its character is either the case currently offered by the first branch or the opposite case offered by the second branch. Choose the corresponding branch. At every digit there is one forced branch.

Following these choices reaches the base case with exactly that desired string, so no valid permutation is missing.

**Why no duplicate is generated**

Two different root-to-leaf paths must first differ at some letter position. One path uses one case there and the other uses the opposite case. Their final strings therefore differ at that position.

Digits do not branch, and English lowercase and uppercase versions of a letter are distinct. Hence distinct recursion paths yield distinct strings.

**Output order and input preservation**

Depth-first traversal determines the output order, but the contract explicitly accepts any order. The original string `s` is immutable and never changed. All mutations apply to the separate list `t`.

## Complexity detail

Let $n$ be the string length and $\ell$ the number of letters. There are exactly $2^\ell$ leaves. Creating each result with `"".join(t)` writes $n$ characters, so output construction takes $\Theta(n \cdot 2^\ell)$ time. This is also an unavoidable lower bound because the returned data itself contains that many characters.

The answer list stores $2^\ell$ strings of length $n$, requiring $\Theta(n \cdot 2^\ell)$ output space. The mutable list uses $O(n)$ space and recursion reaches depth $n$, adding $O(n)$ call-stack space. Including the required output, total space is $O(n \cdot 2^\ell)$.

## Alternatives and edge cases

- **Iterative answer doubling:** Start with one prefix and duplicate all existing prefixes for every letter. It has the same output-sensitive complexity but may allocate more intermediate strings.

- **Bit-mask enumeration:** Number the $\ell$ letters and let each mask choose their cases. It is direct but scans or maps positions for every one of the $2^\ell$ masks.

- **Cartesian product:** Build a one-choice collection for each digit and a two-choice collection for each letter, then join every product tuple. This is concise when a suitable library is available.

- **All digits:** No position branches, so the single result is the original string.

- **All letters:** The result contains exactly $2^n$ strings, which is the maximum under the constraints.

- **Originally uppercase letters:** The first branch may emit uppercase first and the XOR branch lowercase; both are correct.

- **No restore after recursion:** It changes generation order but not the set, because every revisited letter always explores its current form and its opposite.

- **Non-English alphabetic input:** XOR 32 would not be a general case-conversion rule, but such input is excluded by the contract.

- **Maximum length:** At $n = 12$, at most 4,096 strings are generated, consistent with the intended exhaustive output.
