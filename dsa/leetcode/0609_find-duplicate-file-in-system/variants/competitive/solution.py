from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        by_content = {}

        for description in paths:
            parts = description.split()
            directory = parts[0]
            for file_record in parts[1:]:
                opening = file_record.index("(")
                filename = file_record[:opening]
                content = file_record[opening + 1 : -1]
                by_content.setdefault(content, []).append(directory + "/" + filename)

        return [group for group in by_content.values() if len(group) > 1]
