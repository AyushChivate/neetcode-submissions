class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''

        for s in strs:
            string += str(len(s)) + '#' + s
        
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        curlenstr = ''
        i = 0
        decodedstr = ''
        sol = []

        while i < len(s):
            print(i)
            while s[i] != '#':
                curlenstr += s[i]
                i += 1
                print(i)

            i += 1
            print(i)
            curlenint = int(curlenstr)
            while curlenint > 0:
                decodedstr += s[i]
                curlenint -= 1
                i += 1
                print(i)
                
            sol.append(decodedstr)
            curlenstr = ''
            decodedstr = ''

        return sol
