# 1) All strings of length n from {a,b}
def strings_ab(n: int = 2) -> list[str]:
    res: list[str] = []
    def backtrack(path: str):
        if len(path) == n:
            res.append(path)          # string is immutable → safe
            return
        backtrack(path + "a")
        backtrack(path + "b")
    backtrack("")
    return res


# 2) All binary strings of length n
def binary_strings(n: int) -> list[str]:
    res: list[str] = []
    def backtrack(path: str):
        if len(path) == n:
            res.append(path)          # string is immutable
            return
        backtrack(path + "0")
        backtrack(path + "1")
    backtrack("")
    return res


# 3) All subsets of [1..n]
def subsets(n: int) -> list[list[int]]:
    nums = list(range(1, n + 1))
    res: list[list[int]] = []
    def backtrack(i: int, path: list[int]):
        if i == len(nums):
            res.append(path[:])       # list is mutable → copy
            return
        # skip nums[i]
        backtrack(i + 1, path)
        # include nums[i]
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
    backtrack(0, [])
    return res


# 4) All permutations of [1..n]
def permutations(n: int) -> list[list[int]]:
    nums = list(range(1, n + 1))
    res: list[list[int]] = []
    used = set()
    path: list[int] = []

    def backtrack():
        if len(path) == n:
            res.append(path[:])       # snapshot
            return
        for num in nums:
            if num in used:
                continue
            path.append(num)
            used.add(num)
            backtrack()
            used.remove(num)
            path.pop()
    backtrack()
    return res


# Backtracking
print(strings_ab(2))             # ['aa','ab','ba','bb']
print(binary_strings(3))         # ['000','001','010','011','100','101','110','111']
print(subsets(3))                # order may vary; 8 subsets
print(permutations(3))           # 6 permutations





# # ---------- BACKTRACKING FUNDAMENTALS ----------

# # 1) All strings of length 2 from {a,b}
# # def strings_ab(n=2):
# #     res = []
# #     path = ""
# #     choices = ["a","b"]

# #     def backtrack(path):
# #         # TODO: base case length==n -> append string
# #         # TODO: try "a", try "b"
        


# #         if len(path) == n:

# #             if path not in res:
# #                 res.append(path[:])
# #             else:
# #                 path.pop()

# #         for choice in choices:

# #             path.append(choice)
            
# #             backtrack(path)

            

# #     backtrack(path)
# #     return res


# def strings_ab(n=2):
#     res = []
#     choices = ("a", "b")

#     def backtrack(path: str):
#         # base case
#         if len(path) == n:
#             res.append(path)   # strings are immutable; no need to copy
#             return

#         # try both choices
#         for ch in choices:
#             backtrack(path + ch)   # create a new string

#     backtrack("")
#     return res



# # 2) All binary strings of length n
# def binary_strings(n: int):
#     res = []

#     choices = ('0', '1')

#     def backtrack(path):
#         # TODO: base case length==n -> append

#         if len(path) == n:
#             res.append(path)
#             return

#         # TODO: branch with "0" and "1"
#         for choice in choices:
#             backtrack(path + choice)



#     backtrack("")

#     return res



# # 3) All subsets of [1..n]
# def subsets(n: int):
#     nums = list(range(1, n+1))
#     res = []

#     def backtrack(i, path):
#         # TODO: if i==len(nums): append copy
#         # TODO: branch skip or include nums[i]

#         #base case
#         if i == len(nums):
#             res.append(path[:])
#             return


        
#         # choice 1: skip nums[i]
#         backtrack(i + 1, path)

#         # choice 2: include nums[i]
#         path.append(nums[i])
#         backtrack(i + 1, path)
#         path.pop()   # undo choice (backtrack)


#     backtrack(0, [])
    
    
#     return res



# # 4) All permutations of [1 ... n]

# def permutations(n: int):
#     nums = list(range(1, n+1))
#     res = []
#     used = set()

#     def backtrack(path):
#         # base case: path has length n
#         if len(path) == n:
#             res.append(path[:])  # make a copy
#             return

#         # try every number not yet used
#         for num in nums:
#             if num in used:
#                 continue
#             # choose
#             path.append(num)
#             used.add(num)

#             # recurse
#             backtrack(path)

#             # undo choice (backtrack)
#             path.pop()
#             used.remove(num)

#     backtrack([])
#     return res



# if __name__ == "__main__":
#     print(strings_ab())        # ['aa','ab','ba','bb']
#     print(binary_strings(3))   # ['000','001','010','011','100','101','110','111']  
#     print(subsets(2))          # [[],[1],[2],[1,2]]
#     print(permutations(3))     # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]