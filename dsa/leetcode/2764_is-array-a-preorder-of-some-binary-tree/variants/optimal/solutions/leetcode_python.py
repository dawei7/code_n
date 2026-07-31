class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        if nodes[0][1] != -1:
            return False

        ancestors = [nodes[0][0]]

        for node_id, parent_id in nodes[1:]:
            while ancestors and ancestors[-1] != parent_id:
                ancestors.pop()

            if not ancestors:
                return False

            ancestors.append(node_id)

        return True
