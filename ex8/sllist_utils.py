################################################################
# FILE: sllist_utils.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex8 2013-2014
# Description: implement some function for a linked lists
# 1. reverse - reverse the list
# 2. merge_lists - merge to lists into one
# 3. contains_cycle - check if list have a cycle
# 4. get_item - return the data of the k'th element
# 5. is_palindrome - check if list s palindrome
# 6. have_intersection - check if 2 lists connect in same point
# 7. slice - slice the list according to the given arguments
# 8. merge_sort - sort a list in merge_sort algorithem
################################################################

from sllist import List, Node


def list_len(sll):
    """ function recieve a list and return the number of node in the list
    """
    # set pointer to the head
    node = sll.head
    # reset a counter
    counter = 0
    # run until point to None and count every run
    while node is not None:
        counter += 1
        node = node.next
    return counter


def reverse(sll):
    """
    Reverses the given list (so the head becomes the last element, and every 
    element points to the element that was previously before it). Runs in O(n). 
    No new object is created.
    """
    # set first pointer to the head
    node1 = sll.head
    # stop the function in no Nodes
    if node1 is None:
        return None
    # set second pointer to the second Node and set thr first Node to point to
    # None as the end of the list
    if node1.get_next() is not None:
        node2 = node1.get_next()
        node1.next = None
    # stop the function in only one Node
    else:
        return None
    # run until reach the end of the list
    while node2.get_next() is not None:
        # set third pointer to the next Node
        node3 = node2.get_next()
        # set the second node to point to the first one
        node2.next = node1
        # move the first and second pointers to the next one's
        node1, node2 = node2, node3
    # set the head to the last Node
    sll.head = node2
    # set the new head to point to his preview Node
    sll.head.next = node1


def merge_lists(first_list, second_list):
    """
    Merges two sorted (in ascending order) lists into one new sorted list in 
    an ascending order. The resulting new list is created using new nodes 
    (copies of the nodes of the given lists). Assumes both lists are sorted in 
    ascending order. The original lists should not be modified.
    """
    # create a new list
    new_list = List()
    # set pointers to the head of the lists
    fnode = first_list.head
    snode = second_list.head
    # run until both pointer reach the end of the lists
    while fnode is not None or snode is not None:
        # add the new list node with the data from the first list node
        # and move the pointer forword
        if fnode is not None and (snode is None or\
                                  fnode.get_data() < snode.get_data()):
            new_list.add_first(fnode.get_data())
            fnode = fnode.get_next()
        # add the new list node with the data from the second list node
        # and move the pointer forword
        elif snode is not None and (fnode is None or\
                                    snode.get_data() < fnode.get_data()):
            new_list.add_first(snode.get_data())
            snode = snode.get_next()
        # add the new list nodes with the data from both lists nodes
        # and move the pointers forword
        elif snode.get_data() == fnode.get_data():
            new_list.add_first(fnode.get_data())
            new_list.add_first(snode.get_data())
            fnode = fnode.get_next()
            snode = snode.get_next()
    # reverse the list so it be in ascending order
    reverse(new_list)
    return new_list


def contains_cycle(sll):
    """
    Checks if the given list contains a cycle. 
    A list contains a cycle if at some point a Node in the list points to 
    a Node that already appeared in the list. Note that the cycle does not 
    necessarily contain all the nodes in the list. The original list should 
    not be modified.
    Returns true iff the list contains a cycle
    Return False if any Node point to None
    """
    # set the slow moving node as the head
    if sll.head is not None:
        slow_node = sll.head
    else:
        return False
    # set the fast moving node as the head.next
    if sll.head.get_next() is not None:
        fast_node = sll.head.get_next()
    else:
        return False
    # run until the 2 pointers point to the same one or point to None
    while slow_node != fast_node:
        # move the slow node in 1 move and the fast in 2
        slow_node = slow_node.get_next()
        if fast_node.get_next() is not None:
            if fast_node.next.get_next() is not None:
                fast_node = fast_node.next.get_next()
            else:
                return False
        else:
            return False
    return True


def get_item(sll, k):
    """
    Returns the k'th element from of the list. 
    If k > list_size returns None, if k<0 returns the k element from the end.
    """
    # set a variables so the phrase in the range be accurate
    absolute = 1
    correction = 0
    # if k negetive reverse the list and change the variables so it be same as
    # positive k
    if k < 0:
        reverse(sll)
        absolute = -1
        correction = 1
    # set pointer to the head of the list
    node = sll.head
    # None if list empty
    if node is None:
        return None
    # run until reach the k'th element or return None if reach the end of the
    # list
    for node_num in range(absolute*k - correction):
        if node.get_next() is None:
            # reverse the list back to original in k negetive
            if k < 0:
                reverse(sll)
            return None
        node = node.get_next()
    # reverse the list back to original in k negetive
    if k < 0:
        reverse(sll)
    return node.get_data()        


def is_palindrome(sll):
    """
    Checks if the given list is a palindrome. A list is a palindrome if 
    for j=0...n/2 (where n is the number of elements in the list) the 
    element in location j equals to the element in location n-j. 
    Note that you should compare the data stored in the nodes and 
    not the node objects themselves. The original list should not be modified.
    Returns true iff the list is a palindrome
    """
    # set pointers to head
    head = node_from_end = node = sll.head
    # return True if list empty
    if node is None:
        return True
    # find the list length
    length = list_len(sll)
    # move node_from_end pointer to the last Node and set the list head to the
    # middle
    for node_pos in range(length - 1):
        if node_pos == (length//2 - 1):
            sll.head = node_from_end.get_next()
        node_from_end = node_from_end.get_next()
    # reverse the second half of the list
    reverse(sll)
    # compare the first half and the reversed second half
    for node_pos in range(length // 2):
        # in case list isn't palindrome reset the list to the original state
        if node.get_data() != node_from_end.get_data():
            reverse(sll)
            sll.head = head
            return False
        # move the pointers forward
        node, node_from_end = node.get_next(), node_from_end.get_next()
    # reset the list to the original state
    reverse(sll)
    sll.head = head
    return True


def have_intersection(first_list, second_list):
    """
    Checks if the two given lists intersect. 
    Two lists intersect if at some point they start to share nodes. 
    Once two lists intersect they become one list from that point on and 
    can no longer split apart. Assumes that both lists does not contain cycles. 
    Note that two lists might intersect even if their lengths are not equal. 
    No new object is created, and niether list is modified.
    Returns true iff the lists intersect.
    """
    # reverse the first list, set pointer to the last Node and reverse back
    reverse(first_list)
    node1 = first_list.head
    reverse(first_list)
    # reverse the second list, set pointer to the last Node and reverse back
    reverse(second_list)
    node2 = second_list.head
    reverse(second_list)
    # return True if bose pointer are identiacal and not None
    if node1 == node2 and node1 is not None and node2 is not None:
        return True
    return False


def slice(sll, start, stop=None, step=1):
    """ Returns a new list after slicing the given list from start to stop
    with a step.
    Imitates the behavior of slicing regular sequences in python.
    slice(sll, [start], stop, [step]):
    With 4 arguments, behaves the same as using list[start:stop:step],
    With 3 arguments, behaves the same as using list[start:stop],
    With 2 arguments, behaves the same as using list[:stop],
    """
    # create a new list
    new_list = List()
    # set a variable to know if stop if before the head of the list
    stop_beyond_first = 0
    
    # if only 2 arguments given, set the start as 0 and stop as the second
    # argument
    if stop is None:
        start, stop = 0, start
        
    # set the start and stop to a non negetive point if needed and return empty
    # list if start,stop and step giving no range of nodes
    if stop < 0:
        stop = list_len(sll) + stop
        if stop < 0:
            stop = 0
            stop_beyond_first = 1
    if start < 0:
        start = list_len(sll) + start
        if start < 0:
            start = 0
            stop_beyond_first = 0
    if start <= stop and stop <= 0 and step < 0 and stop_beyond_first == 0:
        return new_list
    if start >= stop and step > 0:
        return new_list
    if stop > list_len(sll):
        stop = list_len(sll)
    if start >= list_len(sll) and step < 0:
        start = list_len(sll)-1
    if start == 0 and stop == -1:
        return new_list

    # calculte the number of steps needed to do in the list
    step_div = (stop-start-stop_beyond_first) / step
    step_mod = (stop-start-stop_beyond_first) // step
    if step_div > step_mod:
        steps = step_mod + 1
    else:
        steps = step_mod

    # add new Nodes with the data from the given list in the right places
    for i in range(steps):
        data = get_item(sll, start + i*step)
        if data is not None:
            new_list.add_first(get_item(sll, start + i*step))

    # reverse the list to be in the right direction
    reverse(new_list)
    return new_list

    
def merge_sort(sll):

    """
    Sorts the given list using the merge-sort algorithm. 
    Resulting list should be sorted in ascending order. Resulting list should 
    contain the same node objects it did originally, and should be stable, 
    i.e., nodes with equal data should be in the same order they were in in the 
    original list. You may create a constant number of new to help sorting.
    """

    def length_from_node(head):
        """the function recieve a Node and return the length of the list
        from the Node to the end of the list
        """
        # set a counter
        counter = 0
        # count until reach the end of the list
        while head is not None:
            counter += 1
            head = head.next
        return counter

    # return None if list length >= 1    
    if sll.head is None:
        return None
    if sll.head.next is None:
        return None

    # create new Node to point on the sorted list
    new_node = Node(None)
    
    def spliter(head):
        """Sorts the given list using the merge-sort algorithm. 
        Resulting list should be sorted in ascending order."""

        # take the length of the list
        length = length_from_node(head)
        # set pointer to the head
        node = head

        # return the head if list length == 1
        if length == 1:
            return head
        # move the pointer to the middle
        for i in range(length//2 - 1):
            node = node.next
        if length % 2 == 1:
            node = node.next
        # set pointers to head and middle of the list and disconnect the halves
        left = head
        right = node.next
        node.next = None

        # continue spliting the halves        
        left = spliter(left)
        right = spliter(right)

        # set pointer for the sorted list
        sort_node = new_node

        # merge the nodes in ascending order
        while left and right:
            if left.data <= right.data:
                sort_node.next = left
                left = left.next
            else:
                sort_node.next = right
                right = right.next
            sort_node = sort_node.next
        # if only one head remained, add him to the sorted pointer
        sort_node.next = right if right else left

        # return the head of the sorted nodes 
        return new_node.next
    # set the head to point on the sorted list
    sll.head = spliter(sll.head)
    
