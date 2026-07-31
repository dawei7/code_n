## General

**Separate a number's digit and place-value information.** For one positive integer, the encrypted result depends on only two facts: its largest decimal digit and its digit count. A right-to-left digit scan obtains the next digit with `number % 10` and removes it with `number //= 10`. Maintain `largest_digit` as the maximum digit seen so far.

At the same time, maintain `repeated_ones`, initially zero. For every scanned digit, update it with `repeated_ones = repeated_ones * 10 + 1`. After scanning $d$ digits, this value is the $d$-digit repunit

$$
R_d = \underbrace{11\ldots1}_{d\text{ digits}}.
$$

If the largest digit is $m$, replacing all $d$ original digits by $m$ produces exactly $mR_d$. Add that product to the running answer and repeat independently for every element of `nums`.

The digit scan considers every digit of a number, so `largest_digit` equals its true maximum when the loop ends. The repunit has exactly the original number's digit count, and multiplying it by a single decimal digit places that digit in every position without carrying. Thus each contribution is precisely the required encryption, and summing all contributions returns the requested total.

## Complexity detail

Using $D$ as defined in the function contract, every decimal digit is processed once, so the running time is $O(D)$. The scan stores only the current number, a maximum digit, a repunit, and the total; therefore the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **String conversion:** Convert each number to text, take its maximum character, repeat that character to the same length, and parse the result. This is concise and still takes $O(D)$ time, but it allocates a temporary string proportional to the current digit count.
- **Counting distinct values with repeated list scans:** Encrypting each distinct value once and multiplying by `nums.count(value)` is correct, but repeated full-list counts make the worst-case time quadratic when the values are distinct.
- **Single-digit values:** Their repunit is `1`, so they remain unchanged.
- **Embedded zeros:** Zero digits do not receive special treatment; they are replaced by the number's largest digit like every other position.
- **Value `1000`:** This is the only legal four-digit input. Its largest digit is `1`, so it encrypts to `1111` rather than `1000`.
- **Positive-input guarantee:** No element is zero, so every number contributes at least one digit iteration.
