## General

**Convert jewel types into a membership set**

Each character in `jewels` names one stone type that should be counted. The question for every owned stone is simply whether its character belongs to that collection.

The solution creates

`s = set(jewels)`.

Set membership is expected constant time, so the jewel description is processed once instead of rescanned for every stone.

**Count stones, not distinct types**

The generator tests every character `c` in `stones` independently:

`c in s`.

If three owned stones have jewel types, all three must count even if some share the same character. This is why `stones` itself is not converted to a set.

**Sum Boolean results**

Membership returns `True` for a jewel and `False` otherwise. Python treats these as one and zero in arithmetic. `sum` therefore adds one for every jewel stone and zero for every ordinary stone.

The generator is lazy, so it does not allocate a list of Boolean values.

**Case sensitivity is preserved**

No lowercasing or uppercasing occurs. Python string characters `"a"` and `"A"` are distinct set keys.

For `jewels = "aA"` and `stones = "aAAbbbb"`, one lowercase `a` and two uppercase `A` stones match, producing three.

For `jewels = "z"` and `stones = "ZZ"`, neither uppercase character equals lowercase `z`, so the result is zero.

**Why unique jewel characters simplify construction**

The input guarantees jewel characters are unique, though `set` would remove duplicates even without that guarantee. The set contains exactly one entry per jewel type.

**Why a frequency map is unnecessary**

We do not need to know how often a type appears in the jewel definition; it is a yes-or-no classification. The occurrences that matter are in `stones`, and scanning them directly counts each physical stone.

**Set construction does not change case**

A Python set hashes characters exactly as they occur. It does not perform cultural case folding or alphabet normalization. This behavior matches the contract without extra code.

The jewel string contains only English letters, so each character is one complete type. There are no multi-character jewel names to tokenize.

**Trace the computation**

Suppose `jewels = "bC"` and `stones = "bbccdC"`. The membership set is `{"b", "C"}`.

The first two `b` characters contribute two. Lowercase `c` characters do not match uppercase `C`. `d` does not match. The final uppercase `C` contributes one, giving three.

**The invariant**

After processing the first `i` stone characters, the partial sum equals the number among those `i` whose types occur in the jewel set. The next Boolean adds exactly the contribution of the next stone, preserving the invariant.

After all stones are processed, the partial sum covers the entire owned collection.

**Why the result is an integer rather than a collection**

The problem asks only for how many owned stones are jewels, not which positions or types qualify. The generator can discard each membership result immediately after contributing it to the running sum.

If the caller later needed the matching stones themselves, a filtered list would be appropriate, but it would use output space proportional to the number of matches. This exact task needs only the scalar counter.

**A direct comparison with linear membership**

Using `c in jewels` would also be correct because strings support membership. However, that search may inspect the jewel string repeatedly for every stone. Converting once to a set moves that repeated work into a one-time preprocessing step and makes the intended constant-time classification explicit.

**Why duplicates in `jewels` would not hurt**

Although uniqueness is guaranteed, even a repeated jewel character would still describe the same type. Set conversion would collapse it, which is semantically appropriate. The guarantee mainly makes the input definition unambiguous.

**Empty cases outside the formal constraints**

The constraints make both strings nonempty. If either were empty in a broader interface, the same code would still behave sensibly: an empty jewel set yields zero, and an empty stone sequence contributes nothing.


The set contains all and only jewel types. Each stone contributes one precisely when its type is in that set. Summing those exact individual indicators yields exactly the number of stones that are jewels, with duplicates counted and case preserved.

## Complexity detail

Let `j` be the jewel-string length and `slen` the stone-string length. Building the set takes expected `O(j)` time, and scanning stones takes expected `O(slen)`. Total expected time is `O(j + slen)`.

The set stores `O(j)` characters. Since English letters form a fixed alphabet, it is also bounded by a small constant, but `O(j)` describes the direct input relationship. The generator uses `O(1)` additional space.

## Alternatives and edge cases

- **Nested scans:** Check each stone against every jewel character. This costs `O(jslen)` and repeats work.

- **Frequency counter for stones:** Count every stone type, then sum jewel frequencies. It is correct but stores more information than necessary.

- **Convert stones to a set:** This is incorrect because repeated physical stones must each count.

- **Normalize case:** This violates the case-sensitive contract.

- **No matching stones:** Every Boolean is false and the sum is zero.

- **Every stone is a jewel:** The result equals `len(stones)`.

- **Repeated stones:** Each occurrence is processed separately.

- **Unique jewel guarantee:** Set construction remains straightforward and deterministic.
