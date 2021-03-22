class Solution:
    
    def productExceptSelf(self, nums):
        
        N = len(nums)
        
        output = [0] * N
        left_to_right = [0] * N
        right_to_left = [0] * N
        
        left_to_right[0] = 1
        right_to_left[N-1] = 1
        
        for i in range(1, N):
            left_to_right[i] = left_to_right[i-1] * nums[i-1]
            
        for j in range(N-2, -1, -1):
            right_to_left[j] = right_to_left[j+1] * nums[j+1]
        
        for k in range(N):
            output[k] = left_to_right[k] * right_to_left[k]
            
        return output