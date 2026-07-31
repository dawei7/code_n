## General

**Reduce the target array to two chosen values**

The equality at distance two forces every even index to hold one common value
and every odd index to hold another. The adjacent-inequality condition says
those two chosen values must differ. Once a valid pair is fixed, every element
already equal to its parity's target remains unchanged and every other element
requires exactly one operation.

Thus minimizing replacements is the same as maximizing the number of retained
elements across a different-valued even target and odd target.

**Only two candidates from each parity can matter**

Count values independently at even and odd indices. If the most frequent even
value differs from the most frequent odd value, choosing both keeps as many
elements as any pair possibly can.

If the two modes are the same value, they cannot both be used. A valid optimum
must discard that shared mode on at least one side. On whichever side discards
it, the best replacement is that side's second-most-frequent value; choosing
anything ranked lower cannot retain more elements. Therefore only two pairs
need comparison:

- the even mode with the odd runner-up; and
- the even runner-up with the odd mode.

A missing runner-up receives frequency zero, representing any fresh positive
integer not used by the other side.

**Convert retained elements into operations**

Take the larger retained count from the valid candidate pair or pairs. Every
remaining position can be replaced directly with its parity target, so
subtracting that count from $n$ gives an achievable operation total. The
frequency argument proves no other different-valued pair retains more
positions, making the total minimal.

## Complexity detail

The two parity scans and frequency counts process $n$ elements in $O(n)$
expected time. Selecting the two largest entries from each hash map is linear
in the number of distinct values, which is at most $n$. The maps use $O(n)$
auxiliary space in the worst case.

The benchmark defines `size` as the array length $n$. Each tier gives both
parities a colliding mode, different runner-ups, and a number of distinct
values proportional to $n$. A correct method that repeatedly scans an entire
parity group to obtain every candidate frequency takes $O(n^2)$ time on these
inputs.

## Alternatives and edge cases

- **Sort the two parity groups:** Runs of equal values reveal their
  frequencies and still reduce to the top two candidates, but sorting takes
  $O(n\log n)$ time and copies or rearranges the groups.
- **Rescan for every candidate value:** This avoids storing a full frequency
  map but takes $O(n^2)$ time when the array contains many distinct values.
- A one-element array is already alternating because neither defining
  comparison has an applicable index.
- If both parity modes are equal, choosing that value for both sides is
  invalid even when it would retain the most elements.
- When one parity has only one distinct value, a fresh positive integer is a
  valid zero-frequency runner-up for that side.
- Odd-length arrays have one more even index; the frequency counts naturally
  preserve that asymmetry.
- Values selected as targets need only be positive and do not have to appear
  in the original array.
