## Examples

**Example 1**

- Input: `target = "apple", dictionary = ["blade"]`
- Output: `"a4"`
- Explanation: The shortest abbreviation of "apple" is "5", but this is also an abbreviation of "blade". The next shortest abbreviations are "a4" and "4e". "4e" is an abbreviation of blade while "a4" is not. Hence, return "a4".

**Example 2**

- Input: `target = "apple", dictionary = ["blade","plain","amber"]`
- Output: `"1p3"`
- Explanation: "5" is an abbreviation of both "apple" but also every word in the dictionary. "a4" is an abbreviation of "apple" but also "amber". "4e" is an abbreviation of "apple" but also "blade". "1p3", "2p2", and "3l1" are the next shortest abbreviations of "apple". Since none of them are abbreviations of words in the dictionary, returning any of them is correct.

