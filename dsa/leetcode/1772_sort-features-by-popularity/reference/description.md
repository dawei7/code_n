## Description

An ordered array `features` lists distinct product features, and each string in `responses` contains space-separated words from one customer response.

A feature's popularity is the number of responses that mention it at least once. Repeating the same feature several times in one response still contributes only one mention.

Return all features in descending popularity. When two features have equal popularity, preserve their relative order from the original `features` array.
