## General

Each number contributes an independent, contiguous run of digits to the answer. Converting a positive integer to its decimal string exposes that run in exactly the required left-to-right order, including any zeroes between nonzero digits. Iterate through `nums` in order, then iterate through each converted string and append the numeric value of every character.

This nested traversal does not imply quadratic work: the inner loop runs once for each emitted digit, so all inner-loop iterations together total $D$. Appending immediately also preserves both required orderings. Digits from one number cannot move past digits from another, and digits within a number are visited from most significant to least significant. The constructed list is therefore exactly the requested flattened digit sequence.

## Complexity detail

Let $D$ be the total number of decimal digits in the input. Converting and traversing all numbers takes $O(D)$ time. The returned list contains $D$ integers and therefore uses $O(D)$ space. Apart from that required output and each short temporary decimal representation, the algorithm uses constant additional state.

## Alternatives and edge cases

- **Arithmetic extraction:** Repeated division and remainder operations can avoid string conversion, but they discover digits from right to left and therefore require a stack, reversal, or a place-value calculation to restore the required order.
- **Repeated prepending:** Traversing all digits backward and assigning `[digit] + answer` reconstructs the right order, but every concatenation copies the accumulated suffix and makes the total work quadratic in $D$.
- **One-digit values:** A value from $1$ through $9$ contributes one unchanged element.
- **Embedded and trailing zeroes:** Values such as `100000` and `70` must contribute every zero; treating a number arithmetically must not discard zero positions before their digits are recorded.
