class GeneParenBacktracking:
    """
    Given n pairs of parentheses, 
    write a function to generate all combinations of well-formed parentheses.
    Ex)
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    """
    def generateParenthesis(self, n):

        res = []      # Stores results
        current = []  # Keeps track of current decision space

        def generate(l, r):
            
            # Base case
            st = ''.join(current)
            if len(st) == n*2:
                res.append(st)
                return
            
            # If we haven't used the max amount of '(' parens, (which will always be N),
            # put it in current[]
            if l < n:
                current.append('(')
                generate(l+1, r)
                current.pop()

            # We can only add a closing parentheses if the num of ')' is < num of '('
            if r < l:
                current.append(')')
                generate(l, r+1)
                current.pop()