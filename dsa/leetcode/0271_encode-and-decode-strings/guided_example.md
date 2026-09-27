# Guided Example: Encode and Decode Strings

We trace the step-by-step length-prefixed chunk framing, 4-character fixed-width header generation, pointer slicing, and reversible round-trip deserialization on representative string list instances:

- **Input:** `strs = ["Hello", "World"]`
- **Encoded Payload:** `"   5Hello   5World"` (Each string is preceded by a 4-character right-aligned length header)
- **Decoded Output:** `["Hello", "World"]` (Exact original list restored)
- **Empty String Instance:** `strs = [""] \implies \text{Encoded: } \mathbf{\text{"   0"}} \implies \text{Decoded: } [""]`
- **Multiple Adjacent Empty Strings:** `strs = ["", ""] \implies \text{Encoded: } \mathbf{\text{"   0   0"}} \implies \text{Decoded: } ["", ""]`
- **Payload Mimicking Header:** `strs = ["   5", "#12"] \implies \text{Encoded: } \mathbf{\text{"   4   5   3#12"}} \implies \text{Decoded: } ["   5", "#12"]`

This instance demonstrates serialization protocol design, explains why delimiter-based splitting fails on arbitrary 256-ASCII character inputs, formalizes fixed-width length-prefixed framing, proves bijective round-trip invertibility ($\text{decode}(\text{encode}(S)) = S$), and runs in strictly $O(N)$ linear time and space.

---

## 1. Instance & Teaching Goal

Design an encoding scheme to serialize a list of strings `strs` into a single string, and a decoding scheme to recover the original list.
Given:
$$
\text{strs} = [\text{"Hello"}, \text{"World"}]
$$
Encoded representation:
$$
\mathbf{\text{"   5Hello   5World"}}
$$
Decoded output:
$$
[\text{"Hello"}, \text{"World"}]
$$

### Why Simple Delimiters Fail
If we join strings with a separator character such as `,` or `#` (e.g. `"Hello#World"`):
- What if an input string already contains `#`?
  For example, `strs = ["Hel#lo", "World"]` joined with `#` becomes `"Hel#lo#World"`.
  The decoder splits on `#` and produces `["Hel", "lo", "World"]`—corrupting the data!
- Because input strings may contain **any of the 256 ASCII characters** (including commas, hashes, colons, null bytes, and newlines), no single character can be assumed to be a safe delimiter without escaping.

### The Length-Prefixed Framing Solution
Instead of searching for a delimiter inside the text, we prepend the **exact length of the string** as a header:
$$
\text{Chunk} = \text{Fixed-Width Length Header} + \text{Raw Payload}
$$
Because the header tells the decoder exactly how many characters to read, the payload can contain any character—including numbers, spaces, and symbols—without ambiguity.

---

## 2. Conceptual Foundation & Invariants

### Fixed-Width Length Header Protocol
Under the problem constraint that each string has length $\le 200$, a fixed width of **4 characters** suffices to represent any length in $[0, 200]$:
$$
\text{header} = \text{"{:4}"}.\text{format}(\text{len}(s))
$$
- If $\text{len}(s) = 5$: Header is `"   5"` (three spaces followed by `'5'`).
- If $\text{len}(s) = 0$: Header is `"   0"` (three spaces followed by `'0'`).
- If $\text{len}(s) = 200$: Header is `" 200"` (one space followed by `"200"`).

### Encoding Algorithm
Initialize `ans = []`:
For each string $s \in \text{strs}$:
$$
\text{chunk} = \text{"{:4}"}.\text{format}(\text{len}(s)) + s
$$
$$
\text{ans}.\text{append}(\text{chunk})
$$
Return `"".join(ans)`.

### Decoding Algorithm
Initialize `result = []`, index cursor $i = 0$, and length $N = \text{len}(\text{encoded})$:
While $i < N$:
1. Read the 4-character length header:
   $$
   \text{size} = \text{int}(\text{encoded}[i : i + 4])
   $$
2. Advance cursor past header: $i \leftarrow i + 4$.
3. Slice the payload of length $\text{size}$:
   $$
   \text{payload} = \text{encoded}[i : i + \text{size}]
   $$
   $$
   \text{result}.\text{append}(\text{payload})
   $$
4. Advance cursor past payload: $i \leftarrow i + \text{size}$.

> **Invariant.** At the start of each iteration in the decoding loop, cursor $i$ points to the first character of a valid 4-character length header. Slicing $i : i + 4$ yields the exact integer size of the immediately following payload.

---

## 3. Step-by-Step Worked Execution

We trace the full encode and decode cycle for $\text{strs} = [\text{"Hello"}, \text{"World"}]$:

### Phase 1: Encoding

#### Chunk 1: `"Hello"`
- Length: $\text{len}(\text{"Hello"}) = 5$.
- Format 4-width header: `"   5"`.
- Chunk: `"   5" + "Hello" = \mathbf{\text{"   5Hello"}}`.

#### Chunk 2: `"World"`
- Length: $\text{len}(\text{"World"}) = 5$.
- Format 4-width header: `"   5"`.
- Chunk: `"   5" + "World" = \mathbf{\text{"   5World"}}`.

#### Complete Encoded String:
$$
\text{encoded} = \text{"   5Hello   5World"} \quad (\text{Total Length} = 18)
$$

---

### Phase 2: Decoding

Initialize cursor $i = 0, \quad N = 18, \quad \text{result} = []$.

#### Step 1: Decode First Chunk
- Read header slice $[0 : 4]$:
  $$
  \text{encoded}[0:4] = \text{"   5"} \implies \text{size} = \text{int}(\text{"   5"}) = \mathbf{5}
  $$
- Advance cursor past header: $i \leftarrow 0 + 4 = 4$.
- Read payload slice $[4 : 4 + 5] = [4 : 9]$:
  $$
  \text{payload} = \text{encoded}[4 : 9] = \mathbf{\text{"Hello"}}
  $$
  $\text{result}.\text{append}(\text{"Hello"})$.
- Advance cursor past payload: $i \leftarrow 4 + 5 = \mathbf{9}$.

#### Step 2: Decode Second Chunk
- Read header slice $[9 : 13]$:
  $$
  \text{encoded}[9:13] = \text{"   5"} \implies \text{size} = \text{int}(\text{"   5"}) = \mathbf{5}
  $$
- Advance cursor past header: $i \leftarrow 9 + 4 = 13$.
- Read payload slice $[13 : 13 + 5] = [13 : 18]$:
  $$
  \text{payload} = \text{encoded}[13 : 18] = \mathbf{\text{"World"}}
  $$
  $\text{result}.\text{append}(\text{"World"})$.
- Advance cursor past payload: $i \leftarrow 13 + 5 = \mathbf{18}$.

#### Step 3: Termination
- Cursor $i = 18 == N$. Loop terminates.
- Final output:
  $$
  \mathbf{[\text{"Hello"}, \text{"World"}]}
  $$

---

## 4. Complete Execution Trace

```text
Encode:
  strs = ["Hello", "World"]
  "Hello" -> len 5 -> "   5Hello"
  "World" -> len 5 -> "   5World"
  Encoded: "   5Hello   5World"

Decode:
  i = 0:  header = s[0:4]   = "   5" -> size = 5
          payload = s[4:9]  = "Hello" -> append -> i = 9
  i = 9:  header = s[9:13]  = "   5" -> size = 5
          payload = s[13:18]= "World" -> append -> i = 18
  i == 18 -> End

Result: ["Hello", "World"]
```

| Cursor $i$ | Header Slice $[i : i+4]$ | Parsed Size | Payload Slice $[i+4 : i+4+\text{size}]$ | Extracted String | New Cursor $i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `"   5"` | 5 | $\text{encoded}[4 : 9]$ | `"Hello"` | 9 |
| 9 | `"   5"` | 5 | $\text{encoded}[13 : 18]$ | `"World"` | 18 |
| **18** | Reached End ($i == N$) | - | - | - | **Terminates** |

### Contrast: Handling Empty Strings (`strs = ["", "a"]`)
1. First chunk: length 0 $\implies$ header `"   0"`, payload `""`.
   - Cursor reads $[0:4] = \text{"   0"}$, size $= 0$.
   - Payload $[4:4] = \text{""}$.
   - Cursor advances to $4 + 0 = 4$.
2. Second chunk: length 1 $\implies$ header `"   1"`, payload `"a"`.
   - Cursor reads $[4:8] = \text{"   1"}$, size $= 1$.
   - Payload $[8:9] = \text{"a"}$.
   - Cursor advances to $8 + 1 = 9$.
- Perfectly distinguishes between empty strings and missing entries!

---

## 5. Algorithmic Correctness

**Soundness.** Python's `int("   5")` ignores leading whitespace and correctly parses the integer value $5$. Because the payload length is bounded by 200, its decimal representation never exceeds 4 digits, ensuring that the header slice `s[i : i + 4]` always captures the full length and never spills into the payload.

**Completeness.** Since the decoder directly jumps over the payload using slice indices (`i : i + size`), characters inside the payload are never evaluated as headers or delimiters. Thus, any ASCII character—including spaces, digits, and control characters—can safely appear inside the strings without causing ambiguity.

---

## 6. Traps This Instance Exposes

- **Delimiter Collision Trap:** Using a delimiter like `#` fails whenever `#` appears in the payload text. Length-prefixed framing completely bypasses delimiter collisions.
- **Variable-Length Length Prepending ($L\#\text{payload}$):** An alternative encoding writes `len(s) + "#" + s`. This is also valid, but requires scanning for the delimiter `#` to find where the length ends. The fixed 4-character header reads the exact slice $[i : i + 4]$ without any linear scanning.
- **Repeated String Concatenation ($s = s + \text{chunk}$):** In Python, strings are immutable. Repeatedly concatenating to a single string causes $O(C^2)$ quadratic copying. Appending chunks to a list and calling `"".join(ans)` guarantees strictly $O(C)$ linear performance.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$ where $C = \sum \text{len}(s_i)$ is the total character count across all strings. Encoding creates 4 characters of header per string and copies each character once ($O(C)$). Decoding performs one slice for the header and one slice for the payload per string, copying all characters once ($O(C)$).
- **Auxiliary Space Complexity:** $O(C)$ auxiliary space to construct the encoded transport string and the decoded output list.
