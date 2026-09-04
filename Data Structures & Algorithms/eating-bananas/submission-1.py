class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def compute_hours(speed: int) -> int:
            total = 0
            for pile in piles:
                total += (pile + speed - 1) // speed
            return total

        left, right = 1, max(piles)
        min_speed = float('inf')

        while (left <= right):
            cur_speed = (left + right) // 2

            hours = compute_hours(cur_speed)

            if hours > h:
                left = cur_speed + 1
            else:
                min_speed = cur_speed
                right = cur_speed - 1
        
        return min_speed



