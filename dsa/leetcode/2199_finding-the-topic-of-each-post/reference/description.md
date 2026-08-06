## Description

The `Keywords` table associates topic IDs with words that express those topics. A topic may have several keywords, and the same word may belong to several topics. The `Posts` table stores each post's ID and text, which contains only English letters and spaces.

A post has a topic when one of that topic's keywords appears as a complete word in the post, compared case-insensitively. A shared prefix is not enough: for example, `war` does not match the word `warning`.

For every post, produce its distinct matching topic IDs in ascending numeric order, joined by commas. If no keyword matches, use the literal string `Ambiguous!`. Result rows may be returned in any order.
