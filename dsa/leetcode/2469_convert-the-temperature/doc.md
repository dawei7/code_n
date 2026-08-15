# Convert the Temperature

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2469 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-the-temperature/) |

## Problem Description

### Goal

You are given a nonnegative floating-point value `celsius`, rounded to two decimal places, representing a temperature measured in Celsius.

Convert that temperature to Kelvin and Fahrenheit. Return the two converted values in the fixed order `[kelvin, fahrenheit]`. A result is accepted when each value is within $10^{-5}$ of its exact conversion.

Use the conversion formulas

$$
\text{kelvin}=\text{celsius}+273.15
$$

and

$$
\text{fahrenheit}=1.8\cdot\text{celsius}+32.
$$

### Function Contract

**Inputs**

- `celsius`: A Celsius temperature rounded to two decimal places.

The constraint is $0\le\texttt{celsius}\le1000$.

**Return value**

- A two-element floating-point array containing the Kelvin value first and the Fahrenheit value second.

### Examples

#### Example 1

- **Input:** `celsius = 36.50`
- **Output:** `[309.65000, 97.70000]`
- **Explanation:** Adding $273.15$ gives $309.65$ Kelvin, while applying the Fahrenheit formula gives $97.70$.

#### Example 2

- **Input:** `celsius = 122.11`
- **Output:** `[395.26000, 251.79800]`
- **Explanation:** The same two direct conversions give $395.26$ Kelvin and $251.798$ Fahrenheit.
