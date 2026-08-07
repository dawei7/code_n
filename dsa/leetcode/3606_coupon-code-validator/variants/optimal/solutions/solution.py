from typing import List


class Solution:
    def validateCoupons(
        self,
        code: List[str],
        businessLine: List[str],
        isActive: List[bool],
    ) -> List[str]:
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }
        valid = []

        for coupon, business, active in zip(code, businessLine, isActive):
            if (
                active
                and business in priority
                and coupon
                and all(character.isalnum() or character == "_" for character in coupon)
            ):
                valid.append((priority[business], coupon))

        valid.sort()
        return [coupon for _, coupon in valid]
