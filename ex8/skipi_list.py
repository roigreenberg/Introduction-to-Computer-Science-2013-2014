################################################################
# FILE: skipi_list.py
# WRITER: Roi Greenberg + roigreenberg + 305571234
# EXERCISE : intro2cs ex8 2013-2014
# Description: implement a class for skipilist
# the class has the following functions:
# 0. __init__ - Constructs an empty SkipiList
# 1. add_first - add new node to the begining of the list
# 2. remove_first - remove the first node
# 3. add_last - add new node to the end of the list
# 4. remove_last - remove the last node
# 5. remove_node - remove the given node
# 6. getitem - return the data of the k'th element
################################################################

from sllist import SkipiNode as Node


class SkipiList:

    """
    This class represents a special kind of a doubly-linked list
    called a SkipiList. A SkipiList is composed of Nodes (SkipiNode from
    sllist).cIn addition to the data, each Node has one pointer to the
    next Node in the list, and another pointer to the prev-prev Node in the
    list (hence the name "skipi"). The only data members the class contains
    are the head and the tail of the list.
    """

    def __init__(self):
        """Constructs an empty SkipiList."""
        self.head = None
        self.tail = None

    def add_first(self, data):
        """
        Adds an item to the beginning of a list.
        data - the item to add
        """
        # define the head as the new Node
        self.head = Node(data, next=self.head)
        # if list was empty define th tail as the head
        if self.tail is None:
            self.tail = self.head
        # set the skip back pointer if needed
        if self.head.next is not None:
            if self.head.next.next is not None:
                self.head.next.next.skip_back = self.head             

    def remove_first(self):
        """
        Removes the first Node from the list and return its data.
        Returns that data of the removed node
        """
        # return None if there are no Nodes
        if self.head is None:
            return None
        # save and disconect the first Node from the list
        # and set the head to the next Node
        removed = self.head
        self.head = self.head.next
        removed.next = None
        # set the tail as None if list got empty
        if self.head is None:
            self.tail = None
        # remove the skip back pointer from the second Node if needed
        elif self.head.next is not None:
            self.head.next.skip_back = None
            
        return removed.data

    def add_last(self, data):
        """
        Adds an item to the end of a list.
        data - the item to add
        """
        # if list empty set head and tail as the new Node
        if self.head is None:
            self.tail = Node(data, next=None)
            self.head = self.tail
        # else set new tail
        else:
            self.tail.next = Node(data, next=None)
            # set the skip back pointer if needed
            if self.head != self.tail:
                if self.tail.skip_back is None:
                    self.tail.next.skip_back = self.head
                else:
                    self.tail.next.skip_back = self.tail.skip_back.next
            # set the tail to the new one
            self.tail = self.tail.next

    def remove_last(self):
        """
        Removes the last Node from the list and return its data.
        The data of the removed node
        """
        # return None if no Node to remove
        if self.tail is None:
            return None
        # save the tail
        removed = self.tail
        # set the new tail
        if self.tail != self.head:
            if self.tail.skip_back is None:
                self.tail = self.head
            else:
                self.tail = self.tail.skip_back.next
            self.tail.next = None
        else:
            self.tail = self.head = None

        return removed.data

    def remove_node(self, node):
        """
        Removes a given Node from the list, and returns its data.
        Assumes the given node is in the list. Runs in O(1).
        """
        # remove the first Node 
        if node == self.head:
            return self.remove_first()
        # remove the last Node
        elif node == self.tail:
            
            return self.remove_last()
        # set the skip back pointers after removing the Node and set the
        # preview Node to point on the next one(skip the removing node)
        if node.next != self.tail:
            if node.skip_back is not None:
                node.next.next.skip_back = node.skip_back.next
            else:
                node.next.next.skip_back = self.head
        if node.skip_back is not None:
            node.next.skip_back = node.skip_back
            node.skip_back.next.next = node.next
        else:
            self.head.next = node.next
            node.next.skip_back = None
        # disconnect the Node from the list
        node.next = None
        return node.data

    def __getitem__(self, k):
        """
        Returns the data of the k'th item of the list.
        If k is negative return the data of k'th item from the end of the list.
        If abs(k) > length of list raise IndexError.
        """
        # set a pinter
        # in case k non negetive
        if k >= 0:
            # set a pinter
            node = self.head
            # move the pointer to the right position
            for i in range(k):
                if node != self.tail:
                    node = node.next
                # raise an error if k > length of list 
                else:
                    raise IndexError
            return node.data
        # in case k negetive
        else:
            # set a pinter
            node = self.tail
            # move the pointer to the right position
            for i in range(-k // 2):
                if node is not None and node != self.head:
                    node = node.skip_back
                # raise an error if abs(k) > length of list    
                else:
                    raise IndexError
            # return the head if one if k is odd amd pointer move before head
            if node is None:
                if k % 2 == 0:
                    return self.head.data
                # raise an error if abs(k) > length of list
                else:
                    raise IndexError
            # move the pointer to the next one if k is odd
            if k % 2 == 0:
                node = node.next
            return node.data

