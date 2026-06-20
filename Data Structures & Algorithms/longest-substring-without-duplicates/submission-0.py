class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        duplicates = set()
        r, l = 0, 0
        longest = 0

        while r < len(s):
            if s[r] not in duplicates:
                duplicates.add(s[r])
                longest = max(longest, len(duplicates))
                r += 1
            else:
                while l <= r:
                    if s[l] != s[r]:
                        duplicates.remove(s[l])
                    else:
                        l += 1
                        r += 1
                        break
                    l += 1
        return longest

        # both pointers start at beginning

        # while right is less than len string
        
        # right keeps advancing and adding to set until duplicate
            # keep taking max of set

        # when right finds duplicate, left keeps advancing and removing from set until duplicate



"""

zabcadabb

"""