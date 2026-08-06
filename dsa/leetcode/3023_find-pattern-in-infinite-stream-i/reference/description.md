## Description

You are given a binary array `pattern` and an `InfiniteStream` representing a 0-indexed, unending sequence of bits. The stream exposes only `next()`, which consumes and returns the next bit; it does not support indexing or rewinding.

Return the first index at which the complete `pattern` begins in the stream. The input guarantees that such a starting position exists among the first $10^5$ stream indices, so a correct sequential search eventually finds it.
