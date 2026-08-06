## Description

Given a string `s`, encode repeated text with the form `k[encoded_string]`. Here, `k` is a positive integer and
the bracketed text decodes to a substring that appears exactly `k` consecutive times. The text inside the brackets
may itself contain an encoding.

Return a valid representation of `s` having the shortest possible length. A substring must remain unencoded when
wrapping it would not make its representation shorter. If several valid encodings share the minimum length, any of
them may be returned.
