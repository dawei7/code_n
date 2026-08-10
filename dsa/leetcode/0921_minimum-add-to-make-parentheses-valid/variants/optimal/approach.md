## General

The exact solution uses a stack-like list to cancel matching pairs. After processing any prefix, `stk` contains the parentheses that cannot yet be matched within that prefix.

For each character `c`:

- If `c` is a closing parenthesis and the stack top is an opening parenthesis, they form a valid pair. Pop the opening parenthesis.
- Otherwise, append `c` as unmatched.

An opening parenthesis is always appended because it may be matched by a future closing parenthesis. A closing parenthesis is appended when no unmatched opening parenthesis is available immediately before it in the reduced sequence.

**Why only the stack top matters.** Parentheses matching is nested. A closing parenthesis must match the most recent unmatched opening parenthesis. If the reduced stack top is `(`, pairing and popping preserves possible nesting. If the top is `)` or the stack is empty, there is no opening parenthesis available before this closing symbol; a later opening parenthesis cannot match backward in the string.

**Cancellation exposes new pairs.** For a string such as `(())`, the first two openings are pushed. The first closing pops the inner opening; the second closing then sees and pops the outer opening. The stack process models nested validity without storing explicit pair indices.

At completion, unmatched stack characters have a simple form: zero or more unmatched closing parentheses followed by zero or more unmatched opening parentheses. A pattern `(` before `)` would have been canceled when the closing symbol was processed, so it cannot remain as an adjacent reducible pair.

Every unmatched closing parenthesis needs one inserted opening parenthesis somewhere before it. Every unmatched opening parenthesis needs one inserted closing parenthesis somewhere after it. One insertion cannot fix two unmatched symbols of the same kind or simultaneously supply two missing partners, so at least `len(stk)` insertions are necessary.

Exactly `len(stk)` insertions are sufficient: add one opening parenthesis before each unmatched closing and one closing parenthesis after each unmatched opening. Thus the stack length is the minimum.

For `s = "())"`, the first opening and first closing cancel, leaving one unmatched `)`. Inserting one `(` before it fixes the string, so the result is one.

For `s = "((("`, all three openings remain. Each needs its own closing parenthesis, so the result is three.

For a mixed trace such as `"))(("`, the first two closings are pushed because no earlier opening exists. The following openings are also pushed; they cannot match closings that appeared before them. The reduced stack remains `"))(("` with length four. Two openings must be inserted before the unmatched closings and two closings after the unmatched openings, so four moves are both necessary and sufficient.

**Why greedy cancellation cannot hurt.** Whenever the current `)` can match the most recent unmatched `(`, leaving them unmatched could never help another symbol. That closing cannot match any future opening, and the chosen opening is the best available partner because using an earlier opening would strand the more recent one inside the pair. Canceling immediately therefore preserves every possible valid completion while minimizing remaining work.
After each processed character, removing the stack's unmatched symbols from the prefix leaves characters that can be fully paired, and the stack is the reduced unmatched sequence after all possible valid cancellations. The transition performs the only new possible cancellation involving the current character. By induction the invariant holds through the full string.

The number of unmatched parentheses is also equivalent to a constant-space balance calculation, but the exact file materializes them in `stk`.

The final stack order is relevant during processing but not for the numeric answer. Once no cancellable `()` pattern remains, each stored character independently lacks one partner, and inserting that partner does not interfere with the repairs for other stored characters.

## Complexity detail

Let $n$ be the string length. Each character is appended at most once and popped at most once.

- **Time complexity:** $O(n)$.
- **Space complexity of the exact solution:** $O(n)$ in the worst case for an all-opening or all-closing string.

The manifest's $O(1)$ space corresponds to tracking unmatched openings and required inserted openings with two counters. It does not match this list-based implementation.

## Alternatives and edge cases

- **Two counters:** Maintain open balance; when a closing arrives at balance zero, count a needed opening, otherwise decrement balance. Return needed openings plus remaining balance. This achieves $O(1)$ space and matches the manifest.
- **Repeatedly replace `()` in the string:** It can require many scans and $O(n^2)$ time.
- **Full parser:** A grammar parser is unnecessary for a single parenthesis type.
- **Already valid string:** Every symbol cancels and stack length is zero.
- **All openings:** Every opening needs a closing insertion.
- **All closings:** Every closing needs an earlier opening insertion.
- **Starts with closing:** It cannot be matched by any later opening, so it remains unmatched.
- **Nested pairs:** LIFO popping handles them naturally.
- **Concatenated valid parts:** Each part cancels without interfering with the next.
- **One symbol:** Exactly one complementary parenthesis is needed.
- **Insertions anywhere:** The sufficiency construction can place missing openings before unmatched closings and closings after unmatched openings.
- **Only two character types:** The exact branch's `else` means every nonmatched character is one of the valid parentheses by contract.
- **Manifest mismatch:** The stored list grows with unmatched input; it is not constant-space even though a counter alternative is.
- **Minimum proof:** Stack length supplies a lower bound of one missing partner per symbol and a construction using exactly that many insertions.
