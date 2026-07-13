from collections import Counter
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = Counter()
        for entry in cpdomains:
            count_text, domain = entry.split()
            count = int(count_text)
            while True:
                visits[domain] += count
                dot = domain.find(".")
                if dot == -1:
                    break
                domain = domain[dot + 1 :]
        return [f"{count} {domain}" for domain, count in visits.items()]
