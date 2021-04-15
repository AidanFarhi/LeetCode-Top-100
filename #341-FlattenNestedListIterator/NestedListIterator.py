# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    """
    You are given a nested list of integers nestedList. 
    Each element is either an integer or a list whose elements may also be integers or other lists. 
    Implement an iterator to flatten it.
    Implement the NestedIterator class:

    NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    int next() Returns the next integer in the nested list.
    boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

    Example 1:

    Input: nestedList = [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext returns false, 
    the order of elements returned by next should be: [1,1,2,1,1].
    Example 2:

    Input: nestedList = [1,[4,[6]]]
    Output: [1,4,6]
    Explanation: By calling next repeatedly until hasNext returns false, 
    the order of elements returned by next should be: [1,4,6].
    """
    
    def __init__(self, nestedList):
        self.flattened = []
        self.i = 0
        self.size = 0
        for nestedInt in nestedList:
            self.flattenList(nestedInt)
    
    def next(self) -> int:
        if self.hasNext():
            data = self.flattened[self.i]
            self.i += 1
            return data
    
    def hasNext(self) -> bool:
        return True if self.i < self.size else False
    
    def flattenList(self, nl):
        if nl.isInteger():
            self.flattened.append(nl.getInteger())
            self.size += 1
        else:
            arr = nl.getList()
            for num in arr:
                if type(num) != int:
                    self.flattenList(num)
                else:
                    self.flattened.append(num)
                    self.size += 1