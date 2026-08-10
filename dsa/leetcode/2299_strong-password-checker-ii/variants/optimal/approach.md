## General

**Reject insufficient length before scanning categories**

A strong password needs at least eight characters. The method checks `len(password) < 8` first and immediately returns false.

No combination of character categories can repair a short password, so early rejection is both correct and avoids unnecessary work.

**Encode four required categories as bits**

`mask` begins at zero. Four bits represent whether the scan has seen:

- bit one, value `1`: a lowercase letter;
- bit two, value `2`: an uppercase letter;
- bit three, value `4`: a digit;
- bit four, value `8`: a special character.

Bitwise OR sets a category bit without clearing bits already found. Repeated characters from the same category leave the mask unchanged.

All four bits set produce `1+2+4+8=15`, so the final comparison `mask == 15` requires every category.

**Reject adjacent duplicates during the same pass**

At index `i>0`, the code compares the current character with `password[i-1]`. Equality causes immediate false.

Only adjacent equality is forbidden. A character may reappear after another character, so `"aba"` passes this condition while `"aab"` fails.

Checking adjacency before category classification is safe: once a violation exists, no remaining suffix can remove it.

**Classify the current character**

The `if/elif` chain tests `islower`, `isupper`, and `isdigit` in sequence. If none is true, the `else` branch sets the special-character bit.

Under the input guarantee, every character is an English letter, digit, or one of the listed special characters. Therefore, “none of the first three categories” is exactly “allowed special character.” No separate membership check is needed for valid inputs.

The chain is mutually exclusive, so each character sets one category bit.

**Why the mask is an exact summary**

After processing a prefix, a bit is set if and only if at least one character from its category has appeared. OR never creates an unrelated bit and never loses a discovered category.

If the scan finishes without an adjacency failure, `mask==15` is true exactly when all four existence requirements hold. Combined with the initial length check, this covers every strength criterion.

**Trace a successful password**

For `"IloveLe3tcode!"`, uppercase `I` sets value two, lowercase letters set value one, digit `3` sets value four, and `!` sets value eight. No adjacent pair is equal and length exceeds eight.

The accumulated mask is 15, so the method returns true.

**Trace multiple failures**

`"Me+You--IsMyDream"` has adjacent hyphens. The second hyphen triggers immediate false, even though some categories have already been found. It also lacks a digit, but finding one decisive failure is sufficient.

`"1aB!"` includes all four categories but fails before scanning because its length is four. All conditions are mandatory, not alternatives.

**Why a set is unnecessary**

The algorithm needs only four yes-or-no facts, not the actual characters seen. A four-bit integer is constant-size and makes the final conjunction a single equality.

The preceding-character lookup similarly avoids storing a set or frequency map for adjacency, because only the immediately previous character matters.

## Complexity detail

Let `n` be password length. After the constant-time length test, the loop processes at most `n` characters once. Character classification and bit operations are constant time for the allowed single characters, so time is `O(n)`.

`mask`, the index, and current character use `O(1)` auxiliary space. The input string is not modified.

Early failures can finish sooner, but the worst case scans the whole password.

## Alternatives and edge cases

- **Four Boolean variables:** They express the same state and complexity; the bit mask packages them compactly.
- **Regular expressions:** Separate searches can verify categories and adjacency but may scan the string multiple times and obscure the one-pass invariant.
- **Set of categories:** It works but allocates a dynamic object for four fixed facts.
- **Explicit special-character membership:** It is safer if arbitrary input characters are allowed; the source guarantee makes the `else` branch exact.
- **Exactly eight characters:** Length passes because the test rejects only values below eight.
- **All categories but too short:** The early length condition still returns false.
- **Long enough but one category missing:** The final mask differs from 15.
- **Adjacent repeated special character:** It fails just like repeated letters or digits.
- **Nonadjacent repeated character:** It is allowed.
- **First character:** The `if i` guard prevents an invalid negative-index adjacency comparison.
- **Repeated category:** OR is idempotent and retains the bit once set.
- **Allowed character domain:** It is what makes every classification exhaustive.
- **Input preservation:** The method performs read-only checks.
- **Special-character list:** Every punctuation character permitted by the contract reaches the same `else` branch and sets bit eight.
- **Adjacent equality is case-sensitive:** `'a'` and `'A'` are different characters, so they do not violate adjacency.
- **Unicode method concern:** `islower` and related methods recognize more than ASCII in general, but the input contract restricts characters to the specified ASCII domain.
- **Mask cannot exceed 15:** Only the four designated bits are ORed, so equality with 15 is a complete all-flags test.
- **Failure order:** Length and adjacency may return early; the method is not required to report which or how many rules failed.
- **Digit classification:** Each allowed decimal digit sets bit four regardless of its numeric value.
