## Description

You are given two string arrays `creators` and `ids`, and an integer array `views`, all of length `n`. The `i^th` video on a platform was created by `creators[i]`, has an id of `ids[i]`, and has `views[i]` views.

The **popularity** of a creator is the **sum** of the number of views on **all** of the creator's videos. Find the creator with the **highest** popularity and the id of their **most** viewed video.

<ul>
	<li>If multiple creators have the highest popularity, find all of them.</li>
	<li>If multiple videos have the highest view count for a creator, find the lexicographically **smallest** id.</li>
</ul>

Note: It is possible for different videos to have the same `id`, meaning that `id`s do not uniquely identify a video. For example, two videos with the same ID are considered as distinct videos with their own viewcount.

Return* *a **2D array** of **strings** `answer` where `answer[i] = [creators_i, id_i]` means that `creators_i` has the **highest** popularity and `id_i` is the **id** of their most **popular** video. The answer can be returned in any order.
