"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution():
	def __init__(self,input):
		self.input = input
		self.result = []
	def permutations(self):
		for i in range(len(self.input)):
			self.helper([self.input[i]],self.input[:i]+self.input[i+1:])
	def helper(self,main,rem):
		if len(main) == len(self.input):
			self.result.append(main)
		for i in range(len(rem)):
			self.helper(main+[rem[i]],rem[:i]+rem[i+1:])
obj = Solution([1,2,3])
obj.permutations()
print(obj.result)