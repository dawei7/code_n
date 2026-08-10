## General

**Nested encodings require remembering unfinished outer work**

While decoding `3[a2[c]]`, the parser begins the outer repeated section, then encounters another repeated section before the outer one is complete. It must remember both the outer repeat count `3` and the already-decoded text that appeared before that section. A stack is appropriate because the innermost bracket closes first: the most recently opened context is the first one completed.

The exact solution uses two parallel stacks:

- `s1` stores repeat counts for open brackets;
- `s2` stores decoded prefixes that appeared before those brackets.

It also keeps two current values:

- `num` is the repeat count currently being read from consecutive digits;
- `res` is the decoded text at the current nesting level.

Entries at the same index in `s1` and `s2` belong to the same open bracket. Their sizes always match.

**Reading a multi-digit repeat count**

When `c.isdigit()` is true, the update is

```text
num = num * 10 + int(c)
```

Multiplying by ten shifts the previously read decimal digits left by one place, and adding the new digit appends it. For example, reading `1`, then `2`, then `3` changes `num` through `1`, `12`, and `123`.

The code must accumulate digits this way because repeat counts can be larger than nine. Treating each digit as a separate count would decode `12[a]` incorrectly.

The input guarantee says digits occur only as positive repeat counts immediately before `[`. Therefore, `num` never needs to represent a literal digit in the decoded output.

**Opening a bracket creates a new frame**

On `[`, the number just read applies to the enclosed section. The algorithm pushes `num` onto `s1` and the current `res` onto `s2`.

The saved `res` is the decoded prefix that must appear before the repeated bracket result. For `ab3[c]`, it saves `"ab"`; after decoding `c`, the bracket result will become `"ab" + "c" * 3`.

After pushing, it resets `num, res = 0, ''`. The parser is now inside the new brackets:

- a future number should start fresh, not continue the outer count;
- text inside the brackets should be accumulated independently of the outer prefix.

This is analogous to making a recursive call and storing the caller’s local state, but the stacks make that call state explicit.

**Letters extend the current decoded segment**

Any character that is not a digit or bracket is a lowercase letter under the valid-input grammar. The code performs `res += c`.

Letters outside encoded groups and letters inside groups are handled identically. Their meaning depends only on the current frame. For `2[abc]ef`, `abc` is collected while the bracket frame is active; after the bracket closes, `ef` is appended to the resulting outer-level `res`.

**Closing a bracket completes the innermost frame**

On `]`, the current `res` is the fully decoded contents of the innermost still-open bracket. Nested groups inside it have already closed and been expanded, because the scan proceeds left to right.

The solution executes

```text
res = s2.pop() + res * s1.pop()
```

Read the expression from its components:

- `s1.pop()` retrieves the repeat count associated with this bracket;
- `res * count` repeats the decoded inner text;
- `s2.pop()` retrieves the decoded outer prefix saved at the matching `[`;
- concatenation rejoins that prefix with the expanded bracket result.

After assignment, `res` again represents decoded text in the enclosing frame. The completed frame has been removed from both stacks.

Because the input brackets are well formed, every closing bracket has one count and one prefix to pop, and both stacks are empty after the complete top-level string is processed.

**Tracing a nested example**

For `s = "3[a2[c]]"`, the important states are:

| Input event | `s1` | `s2` | `num` | `res` |
|---|---|---|---:|---|
| read `3` | `[]` | `[]` | `3` | `""` |
| read first `[` | `[3]` | `[""]` | `0` | `""` |
| read `a` | `[3]` | `[""]` | `0` | `"a"` |
| read `2` | `[3]` | `[""]` | `2` | `"a"` |
| read second `[` | `[3,2]` | `["","a"]` | `0` | `""` |
| read `c` | `[3,2]` | `["","a"]` | `0` | `"c"` |
| close inner `]` | `[3]` | `[""]` | `0` | `"acc"` |
| close outer `]` | `[]` | `[]` | `0` | `"accaccacc"` |

The inner bracket is decoded first because its saved state is on top. Its result becomes part of the outer frame before the outer repetition is applied.

**Literal text before and after groups**

Consider `2[abc]3[cd]ef`.

The first group produces `"abcabc"`. Since the parser is back at top level, that remains in `res`. Reading the next count and `[` pushes this existing text into `s2`. Closing the second group reconstructs `"abcabc" + "cd" * 3`, and the final letters append `"ef"`. The answer becomes `"abcabccdcdcdef"`.

This illustrates why the prefix stack is necessary even without nesting: several adjacent encoded and literal segments must be joined in their original order.

**The frame invariant**

After processing any prefix of the encoded input:

- `res` is the complete decoded text seen so far at the current nesting level after its most recent opening bracket;
- `num` is either zero or the decimal repeat count whose digits have just been read and whose `[` has not yet appeared;
- each pair in `s2` and `s1` stores an enclosing level’s decoded prefix and the repeat count for the open bracket that followed it;
- stack order follows bracket nesting from outermost at the bottom to innermost at the top.

Digit and letter updates plainly preserve their parts of the invariant. Opening a bracket saves the complete caller state and starts an empty child frame. Closing a bracket uses the most recent pair to apply exactly the rule $k[\text{encoded string}]$ and restores the enclosing decoded state.

At the end of a valid input, no bracket is open and `res` is therefore the decoded top-level text. Returning it is correct.

## Complexity detail

Let $n$ be the encoded input length, $m$ be the fully decoded output length, and $d$ be maximum bracket nesting depth.

The control-flow scan examines each of the $n$ input characters once. Any implementation must also produce all $m$ output characters, so an ideal builder- or rope-based realization of this stack algorithm can be described as $O(n+m)$ time. That is the bound recorded in the variant manifest.

The exact Python source uses immutable strings, however. Operations such as `res += c`, `res * count`, and `prefix + repeated` may copy their operands. Nested expressions can cause already-decoded text to be copied again at several closing levels. A family with long prefixes wrapped in repeat-one groups can make the sum of copied lengths $O(md)$, which is $O(nm)$ in a coarse worst-case bound. CPython may optimize some uniquely referenced `+=` operations and multiplication by one, but those interpreter details do not justify a language-level worst-case $O(n+m)$ guarantee for the exact source.

The two stacks hold at most $d$ frames. Saved prefix strings across active frames originate from different portions of the encoded path, while current and expanded strings can reach output size $m$. Peak working storage, including constructed decoded text and temporary concatenation results, is $O(n+m)$ under the normal accounting; the final returned string alone requires $O(m)$. The stack metadata itself is $O(d)$.

The problem caps output length at $10^5$, which keeps actual expansion finite and bounds the otherwise potentially enormous effect of nested repeat counts.

## Alternatives and edge cases

- **Recursive descent:** Parse until `]`, recursively decode nested contents, and return them to the caller. This mirrors the grammar naturally but uses the language call stack and may face recursion-depth limits. Its string-building costs require the same care as the iterative version.

- **Single character stack:** Push raw input characters; on `]`, pop the inner text and preceding number, expand it, and push the result characters back. This is correct but repeatedly moving individual decoded characters can be less efficient and harder to follow than storing whole prefixes and counts separately.

- **Builder or chunk-list frames:** Store lists of string chunks per frame and join strategically. This reduces repeated immutable-string concatenation and better realizes output-sensitive $O(n+m)$ behavior.

- **Multi-digit count:** Decimal accumulation ensures `12[a]` repeats `a` twelve times, not once and then twice.

- **Nested count:** The innermost `]` always pops the most recently opened frame, so nested repetitions apply from inside outward.

- **Adjacent encoded groups:** After one group closes, its result stays in `res`; opening the next saves that entire prefix, preserving adjacency.

- **Letters outside brackets:** They append directly to top-level `res` and are returned in place.

- **Repeat count one:** `1[text]` yields `text`. The frame still opens and closes normally.

- **Large repeat count with short text:** String multiplication creates exactly the required number of copies; output-size work is unavoidable.

- **Empty bracket contents:** The stated grammar describes encoded strings of lowercase letters and valid inputs; if `k[]` were allowed, the mechanics would repeat the empty string and still behave consistently.

- **Well-formed-input guarantee:** The code does not check stack underflow, missing counts, extra brackets, or literal digits. Those malformed cases are excluded by the contract.

- **No encoded group:** A plain lowercase string never touches the stacks and is returned unchanged.

- **Output bound:** Even though each individual count is at most 300, nesting multiplies lengths. The separate guarantee that decoded output stays within $10^5$ is what keeps expansion practical.
