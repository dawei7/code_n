[TOC]

### Approach 1: Increment Pointer

#### Intuition

When reading from the `i`-th position, if $\text{bits}[i] = 0$, the next character must be at $i + 1$, because `0` is 1-bit; else if $\text{bits}[i] = 1$, the next character must be at $i + 2$, because `1` is only present in 2-bit characters `10` and `11`. We increment our read-pointer `i` to the start of the next character appropriately. At the end, if our pointer is at $\text{bits.length} - 1$, then the last character must have a size of 1 bit.

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
```

#### Complexity Analysis

* Time Complexity: $O(N)$, where $N$ is the length of `bits`.

* Space Complexity: $O(1)$, the space used by `i`.

---

### Approach 2: Greedy

#### Intuition

To find if the last character in the array is a one-bit character, we can use a parity-based approach. First, we remove the last element, which is the character we want to check. We then initialize a `parity` variable and iterate backward through the array. Each time we encounter a `1`, we toggle `parity` with $parity ^= 1$, effectively flipping its value. This toggle allows us to track whether the number of `1`s is odd or even.

At the end, if `parity` is `0`, it indicates the last character is a one-bit character; if `parity` is `1`, it’s part of a two-bit sequence.

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
```

#### Complexity Analysis

* Time Complexity: $O(N)$, where $N$ is the length of `bits`.

* Space Complexity: $O(1)$, the space used by `parity` (or `i`).