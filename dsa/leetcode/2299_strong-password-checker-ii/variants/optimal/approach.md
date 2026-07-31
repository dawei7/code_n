## General

**Track every required category**

Reject immediately when the length is below eight. Otherwise scan the password
once while maintaining four Boolean flags: lowercase, uppercase, digit, and
allowed special character.

At each index after the first, compare the current character with its immediate
predecessor. Equal adjacent characters violate the contract, so the password
can be rejected immediately. After the scan, accept only if all four category
flags are true.

The length check enforces the first rule. Every character contributes to the
exact category flags it satisfies, so a true flag is equivalent to the
existence of that required type. Comparing every adjacent pair enforces the
last rule. Therefore the final conjunction is true exactly for strong
passwords.

## Complexity detail

Let $n = \lvert\texttt{password}\rvert$. The scan visits each character once,
so it takes $O(n)$ time. The fixed special-character set and four Boolean
flags use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Separate full scans:** Running one search for every rule is still $O(n)$ because the number of rules is fixed, but it repeats work.
- **Regular expressions:** Multiple expressions can express the categories and adjacency constraint, though the direct scan makes every rule explicit.
- **Repeated whole-password validation per index:** Redundant rescanning is correct but can take $O(n^2)$ time.
- **Exactly eight characters:** The boundary length is valid when all other rules hold.
- **Adjacent duplicate:** Any duplicated letter, digit, or special character causes rejection.
- **Separated duplicate:** Reuse is valid when another character lies between the occurrences.
- **Special set:** Only characters from `"!@#$%^&*()-+"` satisfy the special-character requirement.
- **Several failures:** The function still returns one Boolean; identifying one violation is enough to reject.
