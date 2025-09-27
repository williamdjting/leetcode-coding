from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        

        # store a cache of hashmap of a world and 
        # match it against any other, store in list    

        outputList : list[list[str]] = []

        seen = set()
        
        # outsideHashMap = { }
        outsideHashMap = defaultdict(lambda: defaultdict(int))
        n = len(strs) # length of strs
        

        # store each value of strs in a hashmap by index

        for i in range(n):    
            print("word is", strs[i],"\n")
            count = 0
            for index, letter in enumerate(strs[i]):
                print("letter", letter)
                
                outsideHashMap[strs[i]][letter] += 1

        # my attempt

        # check if each dictionary matches another, then store in same list
        # val = 0
        # while val < n:
        
        #     seen = set()
            
        #     for i in range(n): #index value 1,2,3,4,5
        #         localList = [] 
        #         if strs[i] not in seen:
                    
        #             localList.append(strs[i])
        #             seen.add(strs[i])
        #             for j in range(i+1, n):   # compare strs[i] vs strs[i+n]
        #                 if outsideHashMap[strs[i]] == outsideHashMap[strs[j]]:
        #                     localList.append(strs[j])
        #                     seen.add(strs[j])
        #         # else:
        #         #     localList.append(strs[i])
        #         print("localList", localList)   
        #         # outputList.append(localList)

        #     val += 1

        # chat gpt fix, accounts for singletons , skipping those letters already seen, avoiding duplicates


        for i in range(n):
            if strs[i] in seen:
                continue
            localList = [strs[i]]
            seen.add(strs[i])

            for j in range(i + 1, n):
                if strs[j] in seen:
                    continue
                if outsideHashMap[strs[i]] == outsideHashMap[strs[j]]:
                    localList.append(strs[j])
                    seen.add(strs[j])

            # Always append (whether singleton or group)
            # Convert to sorted list so duplicates collapse nicely
            localList = sorted(localList)

            if localList not in outputList:   # avoid duplicate sublists
                outputList.append(localList)

        print(outputList)
        return (outputList)


strs = ["eat","tea","tan","ate","nat","bat"]

sol = Solution()

answer = sol.groupAnagrams(strs)

print("answer", answer)