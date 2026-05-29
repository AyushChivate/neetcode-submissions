class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join([char for char in s if char.isalnum()]).lower()
        
        for f, b in zip(cleaned, reversed(cleaned)):
            if f != b:
                return False

        return True