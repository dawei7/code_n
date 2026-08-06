## Description

The `user_content` table stores a unique `content_id` and a text value `content_text` for each row. Transform every word in each text so that its first letter is uppercase and every remaining letter is lowercase. A word begins at the start of the text or immediately after a space.

Existing spaces are data and must remain unchanged, including leading spaces, trailing spaces, and multiple consecutive spaces. The text contains no special characters. Return one row per source record with its identifier, the untouched source text named `original_text`, and the transformed text named `converted_text`.
