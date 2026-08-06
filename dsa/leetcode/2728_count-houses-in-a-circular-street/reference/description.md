## Description

A circular street contains an unknown positive number $n$ of houses. Every house has one door, which may initially be open or closed, and the houses form a cycle: continuing in either direction eventually returns to the starting house. Your initial position and the initial door states are arbitrary.

You control a `Street` interface that can open or close the current door, report whether that door is open, and move one house to the left or right. A supplied bound `k` guarantees $n \le k$. Use only those operations and return the exact number of houses on the street.
