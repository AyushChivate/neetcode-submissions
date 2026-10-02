class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)      

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.dic[key]

        l, r = 0, len(vals) - 1
        greatest_idx = None

        while l <= r:
            m = (l + r) // 2

            if vals[m][1] == timestamp:
                return vals[m][0]
            
            if vals[m][1] < timestamp:
                greatest_idx = m
                l = m + 1
            else:
                r = m - 1
                
        if greatest_idx is None:
            return ""
        return vals[greatest_idx][0]

        
