## Description

There is a hotel with `n` rooms. The rooms are represented by a 2D integer array `rooms` where `rooms[i] = [roomId_i, size_i]` denotes that there is a room with room number `roomId_i` and size equal to `size_i`. Each `roomId_i` is guaranteed to be **unique**.

You are also given `k` queries in a 2D array `queries` where `queries[j] = [preferred_j, minSize_j]`. The answer to the `j^th` query is the room number `id` of a room such that:

<ul>
	<li>The room has a size of **at least** `minSize_j`, and</li>
	<li>`abs(id - preferred_j)` is **minimized**, where `abs(x)` is the absolute value of `x`.</li>
</ul>

If there is a **tie** in the absolute difference, then use the room with the **smallest** such `id`. If there is **no such room**, the answer is `-1`.

Return *an array *`answer`* of length *`k`* where *`answer[j]`* contains the answer to the *`j^th`* query*.
