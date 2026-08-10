## General

**Prepare constant-time key lookup**

The knowledge list contains unique keys. The solution first builds dictionary `d` mapping every key to its value. A bracket pair can then be evaluated with expected constant-time lookup rather than scanning the knowledge list repeatedly.

If a key is missing, `d.get(key, '?')` returns the required question mark.

**Scan ordinary text and bracket pairs differently**

Index `i` moves from left to right through `s`. List `ans` collects output pieces.

When `s[i]` is an ordinary lowercase letter, the solution appends that one character unchanged and increments `i`.

When `s[i] == '('`, the solution uses `s.find(')', i + 1)` to locate the matching close bracket at index `j`. The constraints guarantee that it exists and that brackets are not nested, so the next close bracket is the correct partner.

Slice `s[i + 1:j]` is the nonempty key. The dictionary value or `"?"` is appended as one output piece. The solution assigns `i = j`, and the common increment at the loop bottom moves past the close bracket. Neither parenthesis nor the key text itself is copied into the output.

**Why `find` does not make the total scan quadratic here**

Each call to `find` scans only from an opening bracket to its corresponding closing bracket. After replacement, `i` jumps beyond that entire bracket region. Because bracket pairs are non-nested and disjoint, these searched regions do not overlap.

Consequently, the total number of characters examined across all `find` calls is linear in the input length. Ordinary text outside brackets is also visited once by the outer scan.

This argument depends on the source guarantees. Arbitrary nested or malformed parentheses would need a different parser.

**Build output pieces instead of repeated string concatenation**

Appending characters and replacement strings to a list is efficient. At the end, `''.join(ans)` allocates the resulting string once.

Repeatedly adding to an immutable string could copy the growing prefix many times and become quadratic. The piece-list strategy keeps construction proportional to the amount of output.

**Following the first example**

For `"(name)is(age)yearsold"`, the initial open bracket leads `find` to the close after `"name"`. Dictionary lookup returns `"bob"`, which is appended. The scan resumes at `"i"` and copies `"is"` character by character.

The next bracket key `"age"` maps to `"two"`. Remaining letters are copied. Joining the pieces produces `"bobistwoyearsold"`.

For `"hi(name)"` with no `"name"` entry, ordinary `"hi"` remains and the bracket pair contributes `"?"`.

For repeated `"(a)"` pairs, every occurrence independently performs the same dictionary lookup. Knowledge keys are unique, but a key may appear many times in `s`.

**Why letters outside brackets are not evaluated**

Dictionary replacement happens only in the branch entered by `'('`. A plain sequence such as `"aaa"` is appended literally even if `"a"` is a known key. This matches the rule that only bracket pairs are evaluated.

**Why the result is correct**

Partition `s` into ordinary-character positions and complete bracket-pair regions. The loop processes these pieces in their original order.

For an ordinary character, it appends exactly that character. For a bracket region, it extracts exactly the enclosed key and appends its known value or the mandated question mark. It then skips the entire consumed region.

Every input piece is processed once, no bracket syntax leaks into the output, and the ordering of replacements and literal text is preserved. Joining `ans` therefore yields exactly the fully evaluated string.

## Complexity detail

Let $N$ be the length of `s`, let $K$ be the total number of characters stored across the knowledge keys and values, and let $R$ be the output length.

Building the dictionary takes expected $O(K)$ time. Disjoint scanning, key slicing, and hashing account for expected $O(N)$ total work, and joining costs $O(R)$. Exact total time is $O(N+K+R)$.

Under the given bound that every knowledge value has length at most 10, output length is $O(N)$, so this simplifies to the manifest's $O(n+k)$ style bound.

The dictionary stores $O(K)$ characters and the output pieces plus final result require $O(R)$ space. Thus exact auxiliary/output construction space is $O(K+R)$, or $O(n+k)$ under the stated bounds.

## Alternatives and edge cases

- **Repeatedly concatenate strings:** It is easy to write but can copy an ever-growing result and become quadratic.
- **Scan knowledge per bracket:** It costs up to $O(N\cdot|\texttt{knowledge}|)$; a dictionary makes lookup expected $O(1)$.
- **Regular-expression replacement:** It can work but still needs a callback and dictionary, while the direct parser follows the simple grammar clearly.
- **Stack parser:** Useful for nested brackets, but nesting is explicitly absent here.
- **Unknown key:** Append exactly one question mark and omit the bracket syntax.
- **Known key:** Append its entire mapped value as one piece.
- **Repeated bracket key:** Each occurrence is replaced; dictionary construction happens only once.
- **Known letters outside brackets:** They remain literal and are never treated as keys.
- **Empty knowledge:** Every bracket pair becomes `"?"`.
- **No bracket pairs:** Every character is copied and the result equals `s`.
- **Bracket at the beginning or end:** Index jumps and the common increment handle both boundaries.
- **Nonempty-key guarantee:** The slice never represents an intentionally empty key.
- **Matched-bracket guarantee:** `find` never returns -1 on valid input.
- **No nesting:** The first following close bracket always matches the current open bracket.
- **Unique knowledge keys:** Dictionary construction never faces conflicting values.
- **Output length:** Replacements may change length, so complexity should include produced characters.
- **Input preservation:** The method creates a dictionary and result string without modifying `s` or `knowledge`.
