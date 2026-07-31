## Description

Design a reversible codec that converts a list of strings into one string for transmission across a network, then reconstructs the original list at the receiver.

The sending machine provides an encoding function:

```cpp
string encode(vector<string> strs) {
    return encoded_string;
}
```

The receiving machine provides the inverse function:

```cpp
vector<string> decode(string s) {
    return strs;
}
```

The sender computes `string encoded_string = encode(strs)`. After that value is transmitted, the receiver computes `vector<string> strs2 = decode(encoded_string)`. The reconstructed `strs2` must contain exactly the same strings, in the same order, as the sender's `strs`.

Implement both `encode` and `decode`. Built-in serialization mechanisms such as `eval` may not be used to solve the problem.
