class GenerateParentheses:
    """
    Given n pairs of parentheses, 
    write a function to generate all combinations of well-formed parentheses.
    Ex)
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    """
    def generateParenthesis(self, n):
            res = {}
            seen = {}
            st = '()' * n
            self.heapsAlgo(res, st, len(st), seen)
            return res.keys()
        
    def heapsAlgo(self, res, st, n, seen):  
        if st in seen:
            return
        if n == 1:
            if self.validParentheses(st) and st not in res:
                res[st] = 0
            if st not in seen:
                seen[st] = 0
        for i in range(n):
            self.heapsAlgo(res, st, n - 1, seen)
            if i % 2 == 0:
                st = self.swap(st, 0, n - 1)
            else:
                st = self.swap(st, i, n - 1)
                
    def swap(self, st, i, j):
        s = list(st)
        s[i], s[j] = s[j], s[i]
        return ''.join(s)
    
    def validParentheses(self, st):
        stack = []
        for p in st:
            if p == '(':
                stack.append(1)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True