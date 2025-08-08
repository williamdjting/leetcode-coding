import heapq

# class KthLargest:

#     def __init__(self, k: int, nums: list[int]):
#         self.k = k
#         self.nums = nums
    
#     def add(self, val: int) -> int:
        

#         self.nums.append(val)
#         self.nums.sort()
#         # print(self.nums)
#         valueAtK = 0
#         for num in range(k):
#             valueAtK = self.nums[num]

#         return valueAtK
        

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # turn list into a min-heap

        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add the new value
        heapq.heappush(self.heap, val)

        # If heap grows beyond size k, remove smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # The smallest in heap is the k-th largest overall
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:

k = 3
nums = [4,5,8,2]

val = 3

obj = KthLargest(k, nums)

# print(obj)

obj.add(3)
obj.add(5)
obj.add(10)
obj.add(9)
obj.add(4)
# print(param_1)

print(obj)