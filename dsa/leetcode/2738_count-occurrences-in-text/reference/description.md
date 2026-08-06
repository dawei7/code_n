## Description

The `Files` table stores a unique file name and that file's text content. Determine how many files contain `bull` and how many contain `bear`, counting a file once for a word even if that word occurs several times in its content.

An occurrence is valid only when the exact lowercase word has a space immediately before and immediately after it. Embedded forms such as `bullet` and `bears`, punctuation-adjacent text such as `bull.`, and a target at the beginning or end of the content do not qualify. Return one row for each target word; row order is unrestricted.
