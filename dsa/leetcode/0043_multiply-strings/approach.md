## General

**Recreate multiplication without converting the whole inputs**

The restriction forbids turning `num1` and `num2` into built-in integers and multiplying them directly. It does not forbid converting one digit character at a time. The solution therefore reproduces grade-school multiplication: multiply every digit of the first number by every digit of the second, place each partial product according to decimal position, and propagate carries.

Let $m$ and $n$ be the input lengths. The product of an $m$-digit number and an $n$-digit number has at most $m + n$ digits. It can have $m + n - 1$ digits, but allocating `m + n` slots covers both possibilities and leaves room for a leading carry.

`arr` stores digits in normal most-significant-to-least-significant order. During the first phase its entries are not yet restricted to 0 through 9; they are buckets accumulating all raw products that belong at the same decimal position.

**Why a pair contributes to `i + j + 1`**

Digit `num1[i]` is $m - 1 - i$ positions from the right, while `num2[j]` is $n - 1 - j$ positions from the right. Their product belongs

$$
(m - 1 - i) + (n - 1 - j)
$$

positions from the right of the answer. In a length-$(m+n)$ array, that decimal position corresponds to array index `i + j + 1`. The slot immediately to its left, `i + j`, is where a carry from that position will eventually go.

This explains the otherwise mysterious extra `+ 1`. For `123 * 456`, the product of the rightmost digits `3 * 6` goes to the final slot because `i = 2`, `j = 2`, and `i + j + 1 = 5` in a six-slot array. The product `1 * 4` goes to index 1, leaving index 0 available if carry makes the final answer six digits.

**Accumulate before carrying**

The nested loops run from right to left, although accumulation correctness would also hold in another order because addition is commutative. For each pair, the source converts the two characters separately and adds `a * b` to `arr[i + j + 1]`.

No carry is performed inside these loops. Several products may make a bucket much larger than 9, and that is intentional. Separating multiplication from carry propagation keeps each phase simple: first place every pairwise contribution at its correct power of ten, then normalize the entire representation.

For example, the tens-position bucket may receive contributions from the units digit of one input times the tens digit of the other and vice versa. Adding both before carrying is exactly what written multiplication does when its shifted partial rows are summed.

**Normalize from right to left**

The second loop starts at the last array slot and stops after processing index 1. For a bucket `arr[i]`, integer division `arr[i] // 10` is the amount belonging one decimal place to the left, and `arr[i] % 10` is the digit that remains at the current place. The code adds the carry to `arr[i - 1]` and replaces `arr[i]` with its remainder.

Right-to-left order is essential. A carry added to `arr[i - 1]` must be included when that position is normalized on a later iteration. Processing left to right would normalize a position before receiving all carries from its right.

After the loop, every slot from index 1 onward is a valid decimal digit. Index 0 is also a valid leading digit for the mathematical product: the inputs have at most $m$ and $n$ digits, so the product fits in the allocated $m+n$ decimal positions and cannot require another carry beyond the array.

**Remove exactly one optional leading zero**

If neither input is zero, the product has either $m+n$ or $m+n-1$ digits. Therefore, a length-$(m+n)$ array has at most one unused leading slot. The expression `i = 0 if arr[0] else 1` includes index 0 when it is nonzero and otherwise starts from index 1.

The early check for `"0"` is important. Without it, an all-zero array would need more general leading-zero handling. The input contract forbids leading zeros except for the single string `"0"`, so testing equality with that representation catches every zero operand and returns the canonical result `"0"`.

The final generator converts each normalized array digit back to a string and `join` concatenates them. Converting individual digits respects the restriction because the full input strings are never interpreted as built-in integers.

**Why the arithmetic is exact**

Every pair of input digits contributes its product to the slot representing the sum of their decimal exponents. This is precisely the distributive expansion of the two numbers. The carry sweep does not change the represented value: replacing a bucket $x$ with remainder $x \bmod 10$ and adding $\lfloor x/10 \rfloor$ to the next-left bucket preserves the total weighted sum.

After all buckets are normalized, `arr` is a valid base-10 representation of the exact product. Removing an unused leading zero changes only formatting, not value. This proves that the returned string is the correct product.

## Complexity detail

The nested loops execute once for every pair of input digits, for $mn$ single-digit multiplications and additions. The carry pass and final string construction each process at most $m+n$ slots. Total time is therefore $O(mn + m + n)$, customarily simplified to $O(mn)$ for positive lengths.

The result bucket array has $m+n$ entries, and the returned string has at most that many characters. Auxiliary construction space is $O(m+n)$, matching the manifest. The scalar indices and digit variables use constant space. The generator passed to `join` is lazy, though the final output string itself necessarily occupies linear space.

## Alternatives and edge cases

- **Carry after every digit multiplication:** A destination slot can be normalized immediately and its carry added leftward. This uses the same array and bounds but intertwines accumulation with normalization, making ordering harder to reason about.
- **Reverse both input strings:** Reversed digits let index `i + j` directly represent the power of ten. The result must then be normalized and reversed back, which is equally valid but adds reversal steps.
- **Build shifted partial strings:** This mirrors paper multiplication visually, but storing and summing all partial rows uses more intermediate space and more complicated string addition.
- **Convert whole strings with `int`:** It is concise in Python but explicitly violates the problem's restriction and hides the intended arbitrary-precision arithmetic.
- **Either operand is `"0"`:** The early return supplies one canonical zero rather than an empty string or many leading zeros.
- **Single-digit operands:** The same bucket and carry logic works; for `9 * 9`, the two slots normalize to `"81"`.
- **Maximum carry chains:** Right-to-left normalization propagates carries through as many positions as necessary because each left bucket is processed only after all rightward carries have reached it.
- **No leading zeros in inputs:** This guarantee justifies removing at most one unused result slot after excluding zero operands.
- **Inputs remain unchanged:** Strings are immutable and the algorithm only reads their characters.
