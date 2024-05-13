class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        A = []
        while nums:
            alice_move = nums.pop(0)
            bob_move = nums.pop(0)
            A.append(bob_move)
            A.append(alice_move)
        return A    
