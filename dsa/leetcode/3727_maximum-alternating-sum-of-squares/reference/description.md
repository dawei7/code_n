## Description

You are given an integer array `nums`, and you may rearrange its elements in any order.

For an array `arr`, the alternating score is defined by squaring every element and alternating between addition and subtraction from index zero onward:

$$
\operatorname{score}(\texttt{arr})
= \texttt{arr}[0]^2 - \texttt{arr}[1]^2
+ \texttt{arr}[2]^2 - \texttt{arr}[3]^2 + \cdots
$$

Return the maximum alternating score that can be obtained by rearranging `nums`.
