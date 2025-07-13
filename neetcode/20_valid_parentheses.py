class Solution:
    def isValid(self, s: str) -> bool:

        # stack based
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        # return True if not stack else False
        if not stack:
            return True
        else:
            return False


        # brute force

        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''
        





        # curved = [ "(", ")"]
        # square = [ "[", "]"]
        # curly = [ "{", "}"]

        # stackList1 = []
        # stackList2 = []
        # stackList3 = []        

        # for letter in s:
        #     if letter == curved[0]:
        #         stackList1.append(letter)
        #     elif letter == square[0]:
        #         stackList2.append(letter)
        #     elif letter == curly[0]:
        #         stackList3.append(letter)

        #     if letter == curved[1]:
        #         if stackList1.pop() == curved[0]:
        #             stackList1.pop()
        #         else:
        #             return False
        #     if letter == square[1]:
        #         if stackList2.pop() == square[0]:
        #             stackList2.pop()
        #         else:
        #             return False
        #     if letter == curly[1]:
        #         if stackList3.pop() == curly[0]:
        #             stackList3.pop()
        #         else:
        #             return False
        

        # return True