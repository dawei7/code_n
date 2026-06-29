


def solve():
    '''
    	{
    		# Node Class
    		class Node:
    		    def __init__(self, data):   # data -> value stored in node
    		        self.data = data
    		        self.next = None
    	}
    '''

    def intersetPoint(head1,head2):
        #code here
        a_pointer, b_pointer = head1, head2
        while a_pointer != b_pointer:
            a_pointer = a_pointer.next if a_pointer else head2
            b_pointer = b_pointer.next if b_pointer else head1
        return a_pointer.data


if __name__ == "__main__":
    solve()
