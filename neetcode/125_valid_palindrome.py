class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ''

        for letter in s:
            if letter.isalnum():
                newStr += letter.lower()
        
        return newStr == newStr[::-1]
        
        # checks if each letter is an alphanumeric value, if yes
        # adds to new str

        # checks newstr againsts its reverse self [start:stop:step]
        # not specifying a start implies, start from end
        # not specifying a stop imples end at beginning
        # -1 step means go backwards by 1 (reverse order)