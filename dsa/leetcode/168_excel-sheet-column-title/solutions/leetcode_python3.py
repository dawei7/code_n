class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            title.append(chr(ord("A") + remainder))
        return "".join(reversed(title))
