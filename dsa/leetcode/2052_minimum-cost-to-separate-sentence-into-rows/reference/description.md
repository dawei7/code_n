## Description

A sentence contains lowercase words separated by single spaces. Insert line breaks only between words so that every row contains at most `k` characters. Words must remain intact, appear exactly once in their original order, and retain one space between adjacent words placed on the same row; rows have no leading or trailing spaces.

For a non-final row of length $r$, pay $(k-r)^2$. The last row contributes no cost, regardless of its unused capacity. Return the minimum total cost over every valid placement of line breaks. Every individual word is guaranteed to fit within the row width.
