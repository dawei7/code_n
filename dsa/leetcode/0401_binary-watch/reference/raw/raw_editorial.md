### Approach 1: Enumerating Hours and Minutes

#### Intuition

From the problem statement, we know that the hour is represented using 4 bits and the minute is represented using 6 bits. A bit value of `0` indicates that the light is off, while a bit value of `1` indicates that the light is on.

We can enumerate all possible hour values in the range $[0, 11]$ and all possible minute values in the range $[0, 59]$. For each combination, we compute the total number of `1`s in their binary representations. If this total equals $\textit{turnedOn}$, we add the corresponding time to the answer.

#### Implementation


```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans
```


### Approach 2: Binary Enumeration

#### Intuition

Another way to enumerate valid times is to consider all $2^{10} = 1024$ possible configurations of the lights. Each configuration can be represented by a 10-bit binary number, where the higher 4 bits represent the hour and the lower 6 bits represent the minute.

For each configuration, we extract the hour and minute values using bitwise operations. If both values fall within their valid ranges and the total number of `1`s in the binary representation equals $\textit{turnedOn}$, we add the corresponding time to the answer.

#### Implementation


```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for i in range(1024):
            h, m = (
                i >> 6,
                i & 0x3F,
            )  # Extract the high 4 bits and low 6 bits using bitwise operations
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans
```


#### Complexity Analysis

- Time complexity $O(1)$.
  
  The total number of enumerations is constant and independent of the input.

- Space complexity: $O(1)$.
  
  Only constant extra space is used. The space required for the output is not counted toward the space complexity.

There is also an approach that uses bit manipulation to directly enumerate binary numbers with exactly $\textit{turnedOn}$ bits set, but it is beyond the scope of this solution. Interested readers may explore related materials for further details.

---