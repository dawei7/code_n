class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space_count = text.count(" ")

        if len(words) == 1:
            return words[0] + " " * space_count

        between, trailing = divmod(space_count, len(words) - 1)
        return (" " * between).join(words) + " " * trailing
