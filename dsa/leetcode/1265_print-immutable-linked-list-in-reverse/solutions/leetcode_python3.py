# Definition for an ImmutableListNode.
# class ImmutableListNode:
#     def printValue(self) -> None: ...
#     def getNext(self) -> 'ImmutableListNode': ...

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        nodes = []
        current = head
        while current is not None:
            nodes.append(current)
            current = current.getNext()

        while nodes:
            nodes.pop().printValue()
