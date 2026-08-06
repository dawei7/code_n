## Description

You are given a binary array `pattern` and an `InfiniteStream` representing a 0-indexed, unending sequence of bits. The stream exposes only `next()`, which consumes and returns one bit. Earlier bits cannot be indexed, requested again, or recovered by rewinding the stream.

Return the first index at which all entries of `pattern` occur consecutively in the same order. The input guarantees that a matching start exists among the first $10^5$ stream positions, so a sequential algorithm will eventually reach the end of the first occurrence.
