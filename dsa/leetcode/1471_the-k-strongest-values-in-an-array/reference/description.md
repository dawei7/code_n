## Description

Given an array of integers `arr` and an integer `k`.

A value $\text{arr}[i]$ is said to be stronger than a value $\text{arr}[j]$ if $|\text{arr}[i] - m| > |\text{arr}[j] - m|$ where `m` is the **centre** of the array.

If $|\text{arr}[i] - m| = |\text{arr}[j] - m|$, then $\text{arr}[i]$ is said to be stronger than $\text{arr}[j]$ if $\text{arr}[i] > \text{arr}[j]$.

Return *a list of the strongest `k`* values in the array. Return the answer **in any arbitrary order**.

The **centre** is the middle value in an ordered integer list. More formally, if the length of the list is n, the centre is the element in position $((n - 1) / 2)$ in the sorted list **(0-indexed)**.

- For `arr = [6, -3, 7, 2, 11]`, $n = 5$ and the centre is obtained by sorting the array `arr = [-3, 2, 6, 7, 11]` and the centre is $\text{arr}[m]$ where $m = ((5 - 1) / 2) = 2$. The centre is `6`.

- For `arr = [-7, 22, 17, 3]`, $n = 4$ and the centre is obtained by sorting the array `arr = [-7, 3, 17, 22]` and the centre is $\text{arr}[m]$ where $m = ((4 - 1) / 2) = 1$. The centre is `3`.

<div class="simple-translate-system-theme" id="simple-translate">
<div>
<div class="simple-translate-button isShow" style="background-image: url("moz-extension://8a9ffb6b-7e69-4e93-aae1-436a1448eff6/icons/512.png"); height: 22px; width: 22px; top: 266px; left: 381px;"> </div>

<div class="simple-translate-panel " style="width: 300px; height: 200px; top: 0px; left: 0px; font-size: 13px;">
<div class="simple-translate-result-wrapper" style="overflow: hidden;">
<div class="simple-translate-move" draggable="true"> </div>

<div class="simple-translate-result-contents">

</div>
</div>
</div>
</div>
</div>
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

```
**Input:** arr = [1,2,3,4,5], k = 2
**Output:** [5,1]
**Explanation:** Centre is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also **accepted** answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.
```
#### Example 2

- **Input:** `arr = [1,1,3,5,5], k = 2`
- **Output:** `[5,5]`
- **Explanation:** Centre is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].
#### Example 3

- **Input:** `arr = [6,7,11,7,6,8], k = 5`
- **Output:** `[11,8,6,6,7]`
- **Explanation:** Centre is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is **accepted**.
### Constraints

- $1 \le \text{arr.length} \le 10^{5}$

- $-10^{5} \le \text{arr}[i] \le 10^{5}$

- $1 \le k \le \text{arr.length}$