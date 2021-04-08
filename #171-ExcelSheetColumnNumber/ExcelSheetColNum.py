class Solution:
    
    def titleToNumber(self, columnTitle: str    ) -> int:
        val_map = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        columnTitle = list(columnTitle)
        columnTitle.reverse()
        res = 0
        for i, ch in enumerate(columnTitle):
            val = val_map.index(ch)
            power = i
            res += pow(26, power) * val
        return res