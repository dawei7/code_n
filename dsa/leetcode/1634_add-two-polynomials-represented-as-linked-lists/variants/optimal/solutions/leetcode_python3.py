class Solution:
    def addPoly(self, poly1: "PolyNode", poly2: "PolyNode") -> "PolyNode":
        dummy = PolyNode()
        tail = dummy

        while poly1 is not None and poly2 is not None:
            if poly1.power > poly2.power:
                tail.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            elif poly2.power > poly1.power:
                tail.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            else:
                coefficient = poly1.coefficient + poly2.coefficient
                if coefficient != 0:
                    tail.next = PolyNode(coefficient, poly1.power)
                poly1 = poly1.next
                poly2 = poly2.next
                if coefficient == 0:
                    continue
            tail = tail.next

        remaining = poly1 if poly1 is not None else poly2
        while remaining is not None:
            tail.next = PolyNode(remaining.coefficient, remaining.power)
            tail = tail.next
            remaining = remaining.next
        return dummy.next
