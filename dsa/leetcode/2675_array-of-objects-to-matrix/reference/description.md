## Description

Convert an array `arr` of JSON objects or arrays into a rectangular matrix. Items may be nested to any depth and their leaves may be numbers, strings, Booleans, or `null`. A leaf's column name is its complete property path, with successive object keys or array indices joined by periods.

The first matrix row lists every distinct leaf path found anywhere in `arr`, sorted in lexicographically ascending order. Each later row represents the corresponding item from `arr`: put its leaf value under the matching column, and use an empty string when that item has no value at that path. Empty objects and arrays contribute no columns.
