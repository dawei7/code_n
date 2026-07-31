## General

Split `s` at index `k`. Reverse the prefix `s[:k]` and concatenate it with the suffix `s[k:]` in its existing order.

The split assigns every index below `k` to the prefix and every index from `k` onward to the suffix. Reversing the first part therefore changes exactly the characters required by the contract, while concatenating the second part without transformation preserves every remaining position. The two slices cover the input once without overlap, so their concatenation has the same characters and length as `s` and is precisely the required result.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Creating the reversed prefix, copying the suffix, and constructing the result together take $O(N)$ time. Python strings are immutable, so the returned string and its temporary slices require $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Two pointers on a character array:** Swap positions at the two ends of the prefix until they meet, then join the array. This is also $O(N)$ time and $O(N)$ space in Python because the string must first become mutable.
- **Repeated string prepending:** Building the reversed prefix one character at a time with immutable concatenation can take $O(k^2)$ time.
- **`k = 1`:** A one-character prefix reverses to itself, so the entire string is unchanged.
- **`k = N`:** The suffix is empty and the complete string is reversed.
- **Repeated characters:** Equal letters may make some positions look unchanged, but the operation still reverses all positions in the selected prefix.
