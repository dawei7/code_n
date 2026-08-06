## Description

A subarray is a nonempty contiguous segment of the 0-indexed integer array
`nums`. For a subarray beginning at index $i$, form its alternating sum by
adding `nums[i]`, subtracting the next element, adding the following element,
and continuing with alternating signs through the chosen endpoint.

Consider every possible nonempty subarray. Return the greatest alternating sum
among them. The sign pattern always restarts with addition at the subarray's
left boundary; elements cannot be skipped, and the selected segment may have
either odd or even length.
