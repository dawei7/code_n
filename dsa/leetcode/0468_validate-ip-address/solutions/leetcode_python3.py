class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            parts = queryIP.split(".")
            if len(parts) == 4 and all(
                part
                and len(part) <= 3
                and part.isascii()
                and part.isdigit()
                and (len(part) == 1 or part[0] != "0")
                and int(part) <= 255
                for part in parts
            ):
                return "IPv4"
            return "Neither"

        if ":" in queryIP:
            parts = queryIP.split(":")
            hexadecimal = set("0123456789abcdefABCDEF")
            if len(parts) == 8 and all(
                1 <= len(part) <= 4 and all(character in hexadecimal for character in part)
                for part in parts
            ):
                return "IPv6"
        return "Neither"
