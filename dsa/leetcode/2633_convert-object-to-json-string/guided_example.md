# Guided Example: Convert Object to JSON String

## 1. The instance we will serialize

Serialization asks a single question for every part of a value: *what characters does this part contribute, and in which position?* The instance below is chosen so that one pass through it exercises every answer that question can have — a nested container, an empty container, each of the four primitive kinds, and a set of keys whose insertion order is deliberately **not** the order in which the keys must be emitted.

$$
V = \{\, \texttt{"y"}: 1,\ \texttt{"10"}: \text{false},\ \texttt{"2"}: [\,\{\},\ \text{null},\ \texttt{"Hi"}\,],\ \texttt{"x"}: 2 \,\}
$$

The required outcome is the compact string

`{"2":[{},null,"Hi"],"10":false,"y":1,"x":2}`

Three facts about that target are worth noticing before any machinery is introduced. It contains no spaces or line breaks anywhere, because compact output forbids decorative whitespace. The key `"2"` opens the object even though `"y"` was inserted first. And the empty object inside the array survives as the two characters `{}` rather than disappearing or gaining a separator.

The statement forbids the built-in `JSON.stringify` routine, so the emitted text has to be produced by an explicit traversal of the value's own structure. The remainder of this lesson derives that traversal and shows that it can only produce the string above.

## 2. The output grammar: six kinds of value, six emissions

Every JSON value falls into one of six kinds, and each kind has exactly one legal rendering. Recognition is by the *kind* of the value, never by what its text looks like, which is why the string `"Hi"` and the key text `Hi` are treated differently.

| Kind of value | How it is recognised | Characters it contributes | Members of $V$ that use it |
|---|---|---|---|
| null | the distinguished empty value | `null` | the second array member |
| string | a sequence of characters | those characters wrapped in double quotes | `"Hi"`, and every key |
| number | a numeric value, possibly negative or fractional | its decimal text, unquoted | `1` under `"y"`, `2` under `"x"` |
| boolean | one of the two truth values | `true` or `false` | `false` under `"10"` |
| array | an ordered, index-addressed container | `[` members separated by `,` then `]` | the value under `"2"` |
| object | a key-addressed container | `{` entries separated by `,` then `}` | the root $V$, and the empty object inside the array |

The fourth column matters pedagogically: the same six rules are applied identically at the root, three levels down, and inside an empty container. There is no special case for "top level" and no special case for "inside an array".

## 3. Key order: why `"2"` is emitted before `"10"`, and both before `"y"`

An object is a mapping, so its keys have no intrinsic sequence; the statement fixes one by requiring the order that `Object.keys()` returns. That order has two tiers, and this instance separates them.

| Insertion position | Key | Integer-index key? | Emitted position |
|---|---|---|---|
| 1 | `"y"` | no | 3 |
| 2 | `"10"` | yes, index 10 | 2 |
| 3 | `"2"` | yes, index 2 | 1 |
| 4 | `"x"` | no | 4 |

Keys whose names are canonical array indices are enumerated first, in **ascending numeric** order, and only then are the remaining keys enumerated in insertion order. So the two tiers give `"2"`, `"10"`, then `"y"`, `"x"`.

This is precisely where a plausible implementation goes wrong. Sorting *all* keys as text would place `"10"` first, because the character `1` precedes the character `2`; that yields a document that opens with `"10"` and is wrong. Preserving pure insertion order would place `"y"` first; that is also wrong. Only the two-tier rule reproduces the target. The same rule explains the authored check whose input is `{"2":"b","1":"a","z":0}` and whose expected output is `{"1":"a","2":"b","z":0}`: the numeric names are reordered by value while `"z"` stays last.

## 4. Depth-first emission of the whole instance

The traversal visits the root, then each member in the order just established, descending immediately into any container it meets and finishing that container before moving to the next sibling. The figure shows the shape it walks.

```mermaid
accTitle: Container hierarchy of the traced instance
accDescr: The root object has four entries; the entry under key 2 holds an array whose three members are an empty object, null, and the string Hi, while the other three entries hold the primitives false, 1, and 2.
graph TD
    R["V, root object, 4 entries"] -->|"key 2"| A["array, 3 members"]
    R -->|"key 10"| B["false"]
    R -->|"key y"| C["1"]
    R -->|"key x"| D["2"]
    A -->|"member 0"| E["empty object"]
    A -->|"member 1"| F["null"]
    A -->|"member 2"| G["string Hi"]
```

The trace below shows the accumulated output buffer after each event. A separator is written *before* a member, and only when that member is not the first, so no container can ever begin or end with a stray comma.

| Step | Container in focus | Event | Appended | Buffer after the step |
|---|---|---|---|---|
| 1 | root object | open the object | `{` | `{` |
| 2 | root object | emit first key | `"2":` | `{"2":` |
| 3 | array | open the array | `[` | `{"2":[` |
| 4 | array | first member is an empty object | `{}` | `{"2":[{}` |
| 5 | array | separator, then the second member | `,null` | `{"2":[{},null` |
| 6 | array | separator, then the third member | `,"Hi"` | `{"2":[{},null,"Hi"` |
| 7 | array | close the array | `]` | `{"2":[{},null,"Hi"]` |
| 8 | root object | separator and second key | `,"10":` | `{"2":[{},null,"Hi"],"10":` |
| 9 | root object | value is a boolean | `false` | `{"2":[{},null,"Hi"],"10":false` |
| 10 | root object | separator and third key | `,"y":` | `{"2":[{},null,"Hi"],"10":false,"y":` |
| 11 | root object | value is a number | `1` | `{"2":[{},null,"Hi"],"10":false,"y":1` |
| 12 | root object | separator and fourth key | `,"x":` | `{"2":[{},null,"Hi"],"10":false,"y":1,"x":` |
| 13 | root object | value is a number | `2` | `{"2":[{},null,"Hi"],"10":false,"y":1,"x":2` |
| 14 | root object | close the object | `}` | `{"2":[{},null,"Hi"],"10":false,"y":1,"x":2` |

Step 4 is the one that separates a careful traversal from a careless one: the empty object has no entries, so its opening character is immediately followed by its closing character, with no separator and no whitespace between them. Step 7 completes the array before step 8 touches the next root key — that is what makes the emission depth-first rather than breadth-first.

## 5. Invariant and correctness of the depth-first emission

Let $\hat{E}(v)$ denote the canonical encoding of a value $v$ under the six grammar rules and the two-tier key order, and let $B$ be the character buffer the traversal fills.

**Invariant.** At every moment the buffer equals a prefix of the final string, and whenever a call entered on a value $v$ returns, the buffer has grown by exactly $\hat{E}(v)$ appended to whatever it held on entry.

*Proof by structural induction on nesting depth.* A value of depth $0$ is primitive: null contributes `null`, a string contributes its own characters between double quotes, a number contributes its decimal text, and a boolean contributes its truth word. Each case appends exactly the encoding the grammar prescribes, and each is one uninterrupted append, so the invariant holds. For a container of depth $d > 0$, the traversal appends the opening character, then for each member in order writes a separator if and only if the member is not the first, then descends into a member of strictly smaller depth. By the induction hypothesis each descent appends exactly that member's encoding, and the separators sit exactly at the boundaries between adjacent members. Hence the container as a whole appends its opening character, the member encodings separated by single commas in the required order, and its closing character — which is $\hat{E}$ of that container. Depth strictly decreases at each descent, so the induction is well founded.

**Consequences.** Because $B$ starts empty, the outermost call returns having appended $\hat{E}(V)$ and nothing else, so the delivered string is exactly $\hat{E}(V)$: the traversal is *sound*, never emitting an illegal character, and *complete*, emitting every required character exactly once. The output is also uniquely determined, because the two tiers of the key order fix one sequence of keys per object and array indices are fixed by position.

## 6. Traps this instance exposes

| Trap | The tempting but wrong move | What this instance reveals |
|---|---|---|
| Key order, tier one | sort every key as text | `"10"` would precede `"2"`; ascending numeric order inside tier one is required |
| Key order, tier two | emit keys in insertion order throughout | `"y"` would precede the numeric names; non-index keys wait until tier one is finished |
| Value identity | decide by the printed form of a value | the string `"Hi"` and the bare key text `Hi` look alike, and only the string form is quoted |
| Numbers and booleans | quote every scalar | `1`, `2` and `false` must appear unquoted, or they become strings rather than numbers and booleans |
| Empty containers | assume every container has members | the empty object emits `{}` with no separator, and an empty array would emit `[]` |
| The empty value | test for a container before testing for the empty value | a language that reports the type of its empty value as object-like misroutes it into the object branch and emits `{}` instead of `null` |
| Separator placement | append a comma after each member | the last member would be followed by a comma, closing the array as `,"Hi",]`, which is not a legal document |
| Scalar roots | assume the outer value is a container | a bare string input must still be quoted, and a bare boolean or number must not be |

The sixth row is the classic boundary between a working serializer and a broken one. The statement admits the empty value, booleans, numbers, strings and both container kinds as the *whole* input, so no branch may assume a wrapper.

## 7. Complexity: one emission per output character

Let $S$ denote the serialized length of the input, with $1 \le S \le 10^{5}$ as the statement guarantees, and let $D$ denote the nesting depth, with $D \le 1000$ as the statement guarantees.

**Time.** Every value contributes its own characters to the buffer exactly once: a primitive contributes its literal text, a container contributes one opening and one closing character, and each object contributes one quoted key and one colon per entry. Separators number exactly one fewer than the members of each container that has a separator at all. Each of these quantities is bounded by the number of characters the corresponding value contributes to the output, so the total number of appends is $O(S)$, and appending to one shared buffer costs $O(1)$ amortised per append. The running time is therefore

$$
O(S).
$$

**Auxiliary space.** The buffer itself holds $S$ characters and *is* the output; the traversal's own auxiliary state is the stack of containers it is still inside, whose size is the current depth, at most $D$. So the extra working space beyond the returned string is $O(D)$, and the total space including the result is $O(S)$.

**Why one shared buffer matters.** An alternative design lets every call build and return the text of its own subtree and then concatenates those pieces in the parent, which re-copies each subtree once per enclosing level. On a chain of nested single-member containers that costs $O(S \cdot D)$ character copies, far worse than the single-buffer traversal at the allowed depth of 1000. Appending into one buffer keeps the copy count proportional to the output length. If the depth allowance were ever raised far beyond 1000, the same traversal could instead be driven by an explicit stack of open containers, trading call-stack depth for heap-allocated frames while keeping the same $O(S)$ character work.
