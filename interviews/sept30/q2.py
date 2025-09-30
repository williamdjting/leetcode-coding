Q5: Write an algorithm
to sort a stack (largest
items on top) using at
most one additional
stack to hold items. You
may not copy elements
into other data
structures (ex. array).

-------------------------------


class Solution:

		def __init__ (self):
    		
    		return
	
  	def sortingStack(self, aStack : List[int]) -> List[int] #ordered stack
    		# aStack = [20, 10, 30]
        helperStack  : List[int] = []
    		for element in aStack: 
        	tmp = aStack.pop #30 , [20, 10], #20
          if tmp is in helperStack: 
          		continue

          if tmp > helperStack[-1]:
          		helperStack.append(tmp) #30 goes from aStack into helperStack, #20 > #30 , append else              
          else:
          		aStack.push(helperStack[-1])
              helperStack.append(tmp)
              
        return helperStack
  
sol = Solution()
aStack = [20, 10, 30]
answer = sol.sortingStack(aStack : List[int])
print(answer) # [10, 20 , 30] where [-1] is the top
assert answer is equal to [10,20,30]
    
    
    
