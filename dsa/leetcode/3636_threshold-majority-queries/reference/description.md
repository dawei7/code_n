## Description

You are given an integer array `nums` of length `n` and an array `queries`, where `queries[i] = [l_i, r_i, threshold_i]`.

Return an array of integers <code data-end="33" data-start="28">ans</code> where <code data-end="48" data-start="40">ans[i]</code> is equal to the element in the subarray <code data-end="102" data-start="89">nums[l_i...r_i]</code> that appears **at least** <code data-end="137" data-start="125">threshold_i</code> times, selecting the element with the **highest** frequency (choosing the **smallest** in case of a tie), or -1 if no such element *exists*.
