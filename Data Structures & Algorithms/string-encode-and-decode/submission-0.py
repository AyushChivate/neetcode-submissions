class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = f"{encoded}#{len(string)}#{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i <= len(s)-1:
            if s[i] == "#":
                numIndex = i + 1
                numStr = ""
                while s[numIndex] != "#":
                    numStr = numStr + s[numIndex]
                    numIndex += 1
                length = int(numStr)
                decoded.append(s[numIndex+1:numIndex+length+1])
                i = numIndex + length + 1
        print(decoded)
        return decoded

"""
#10#"He"l#2#lo#7#World!1#11#I--=`121`//

"""

"""

"He"l#2#lo

World!1

I--=`121`//


#10#"He"l#2#lo#7#World!1#11#I--=`121`//


"""