## Description

Start with the positive integer represented by the decimal string `num` and write that integer as an uppercase hexadecimal string. In this representation, replace each hexadecimal digit `0` with the letter `O` and each digit `1` with the letter `I`. The hexadecimal letters `A` through `F` remain unchanged.

The result is valid Hexspeak exactly when every converted character is one of `A`, `B`, `C`, `D`, `E`, `F`, `I`, or `O`. Return the converted representation when it is valid. If the hexadecimal expansion contains any digit from `2` through `9`, return `"ERROR"`.
