## General

**Model the grammar as a deterministic finite automaton**

A deterministic finite automaton, or DFA, remembers only which structural prefix has been read. For each new character category, a table identifies the only possible next state. A transition of `-1` means no valid number can have that prefix, so the method returns false immediately.

The source classifies characters into six input types: invalid, whitespace, sign, digit, dot, and exponent marker. Rows in `transition_table` are states; columns are input types. `state = transition_table[state][inputType]` applies one grammar step.

**Character classification order**

Whitespace is detected with `isspace()`, signs by explicit comparison, digits with `isdigit()`, dot explicitly, and exponent markers as `e` or `E`. Anything else remains `INVALID` and maps to `-1` from every state.

The package's formal input alphabet excludes spaces, but this older automaton intentionally supports leading and trailing whitespace. It therefore accepts some out-of-contract strings such as `" 2 "`. On all stated inputs, the space transitions are simply unused.

Like `isnumeric`, `isdigit()` can recognize some Unicode digits beyond `0-9`. Official constraints restrict input to the declared ASCII characters, so this broader library predicate does not alter in-domain correctness.

**State 0: before the number**

State 0 is the start and leading-space state. Another space stays in 0. A sign moves to state 3, a digit to state 1, and a dot to state 2. An exponent or invalid character fails.

State 0 is not accepting: an empty string or only spaces does not contain a number.

**State 3: sign before the mantissa**

After a leading sign, a digit moves to integer state 1 and a dot moves to state 2. Another sign, exponent, whitespace, or invalid character fails. This forces the sign to be immediately followed by numeric mantissa content.

**State 1: one or more integer digits**

State 1 loops on digits. A dot moves to decimal state 4, and an exponent marker moves to exponent-start state 5. Whitespace moves to trailing-space state 8. A sign or invalid character fails.

State 1 is accepting because an integer with at least one digit is complete.

**State 2: dot seen before any digit**

This represents forms beginning with a dot, optionally after a sign. Only a digit is allowed next, moving to state 4. The state is not accepting, so `"."` and `"+."` fail. Requiring a digit creates valid forms such as `".9"`.

**State 4: a valid decimal mantissa**

State 4 represents either digits followed by a dot or a leading dot followed by digits. It loops on digits, may move to exponent-start state 5, and may move to trailing spaces in state 8. A second dot and a sign fail.

State 4 is accepting. This is why both `"4."` and `"4.2"` are valid.

**States 5, 6, and 7: exponent grammar**

State 5 means an exponent marker has just been read. A sign moves to state 6, and a digit moves to state 7. Nothing else is legal. Neither state 5 nor 6 is accepting because the exponent needs at least one digit.

State 6 means the optional exponent sign was read; only a digit can move to state 7. State 7 loops on exponent digits and can transition to trailing spaces. State 7 is accepting because the mantissa and integer exponent are complete.

Dots and further exponent markers have `-1` transitions from these states, rejecting `"1e2.3"` and `"1e2e3"`.

**State 8: trailing whitespace only**

State 8 loops only on whitespace. Any later digit, sign, dot, or exponent fails, so internal or post-number non-space content cannot be ignored. It is accepting because it can be reached only from accepting numeric states 1, 4, or 7.

Within this package's space-free input constraints, state 8 is never entered, but it explains the automaton's broader source behavior.

**Why only four final states are accepted**

The return condition accepts states 1, 4, 7, and 8. They correspond respectively to a complete integer, complete decimal, complete exponent form, or one of those forms followed by spaces.

States 0, 2, 3, 5, and 6 represent incomplete prefixes: no number yet, dot without digit, leading sign without mantissa, exponent marker without digits, or exponent sign without digits. Rejecting them enforces all mandatory components at end of input.

**Correctness of table-driven parsing**

Each state summarizes exactly the grammatical facts needed for future characters: whether mantissa digits exist, whether a dot was used, whether exponent parsing began, and whether parsing has ended in trailing spaces. The transition row admits precisely the characters that can extend that prefix. Induction over the string shows the state always represents the full consumed prefix. Final-state membership then equals acceptance by the grammar.

The fixed table is created inside each call, but its dimensions are always 9 by 6 and do not grow with input length.

## Complexity detail

The loop classifies and transitions once per character, performing constant work. Time is $O(n)$.

The transition table has a fixed 54 entries, and parser state uses a few scalars. Its size is independent of the string length, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Flag-based direct scan:** Track whether a dot or exponent has occurred and validate signs by position. It uses less table data but can become a collection of subtle conditionals.
- **Regular expression:** `Solution2` provides an anchored pattern for the same older whitespace-tolerant grammar. It is concise but delegates state behavior to the regex engine.
- **Split mantissa and exponent:** Validate each component with smaller helpers, carefully rejecting more than one exponent marker.
- **Empty or only spaces:** The automaton ends in non-accepting state 0.
- **Leading dot:** State 2 requires a following digit.
- **Trailing dot after digits:** State 4 is accepting, so it is valid.
- **Exponent without digits:** States 5 and 6 are non-accepting.
- **Repeated exponent or dot:** Their transitions are invalid once the corresponding grammar phase has passed.
- **Leading/trailing whitespace outside this package's alphabet:** The automaton accepts it intentionally, which is broader than the local formal contract.
- **Whitespace inside a number:** Once state 8 is entered, any non-space fails, so internal separation is rejected.
- **Unicode digit predicates outside the contract:** `isdigit()` can accept more than ASCII `0-9`; an explicit range check would enforce the formal grammar exactly.
