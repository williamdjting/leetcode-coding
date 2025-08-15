class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #my attempt
        # seen = set() # measures
        # # s = "a b c a b c b b"
        # lengthOfString = len(s) 
        # lengthOfLongestSubstring = 0

        # while lengthOfString > 0:
        # # create sliding window
        #     best = 0
        #     print("new round")

        #     slidingWindow = s[ :lengthOfString]


        #     for i in slidingWindow:

        #         if i not in seen:
        #             print("add i", i)
        #             seen.add(i)
        #             best += 1


        #         elif i in seen:
        #             print("contains duplicate", i)
        #             lengthOfString -= 1
        #             continue
        #         lengthOfLongestSubstring = max(best, lengthOfLongestSubstring)
        #         print("best", best, "lengthOfLongestSubstring", lengthOfLongestSubstring)

            
                
        # return lengthOfLongestSubstring

        # set based sliding window (expand right and shrink left)
        # seen = set()        # characters in current window
        # left = 0            # window start
        # best = 0

        # for right, ch in enumerate(s):
        #     # If ch is a duplicate, shrink from the left
        #     while ch in seen:
        #         seen.remove(s[left])
        #         left += 1

        #     # Now it's safe to include ch
        #     seen.add(ch)
        #     best = max(best, right - left + 1)

        # return best

        # dictionary based sliding window (jump left in one step)
        last_index = {}     # char -> last seen index
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= left:
                # Move left just past the previous occurrence of ch
                left = last_index[ch] + 1

            last_index[ch] = right
            best = max(best, right - left + 1)

        return best

s1 = "abcabcbb"
s2 = "pwwkew"
sol = Solution()
answer1 = sol.lengthOfLongestSubstring(s1)
print("answer1", answer1)
answer2 = sol.lengthOfLongestSubstring(s2)
print("answer2", answer2)
