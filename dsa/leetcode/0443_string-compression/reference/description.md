## Description

Compress the character array `chars` by considering each maximal group of consecutive equal characters in order. A group of length one contributes only its character. A longer group contributes its character followed by the decimal representation of its length.

Store the compressed sequence at the beginning of the same input array instead of returning a separate string. If a group length has multiple digits, write each digit into its own array position. After modifying `chars`, return the length of the compressed prefix.

The compression must use only constant extra space.
