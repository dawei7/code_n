## Description

Given a string `s`, determine the greatest number of consecutive characters that can be selected without any character appearing more than once. Return that maximum length rather than the characters themselves.

A substring is contiguous: it keeps every character between its chosen endpoints. Characters may not be skipped as they could be in a subsequence, so deleting an interior duplicate does not preserve the same candidate.

Every character participates in the duplicate rule, including uppercase and lowercase letters, digits, spaces, and symbols. The input may be empty; in that boundary case, no non-empty substring exists and the required length is zero.
