## Description

You are given two integers `n` and `k`.

A **positive** integer `x` is called **compatible** if it satisfies both of the following conditions:

<ul>
    <li>`abs(n - x) <= k`</li>
    <li>`(n & x) == 0`</li>
</ul>

Return the sum of all **compatible** integers `x`.

**Note**:

<ul>
    <li>Here, `&` denotes the **bitwise AND** operator.</li>
    <li>The **absolute** difference between integers `i` and `j` is defined as `abs(i - j)`.</li>
</ul>
