class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        rate = (low+high) // 2
        while low <= high:
            mid = (low+high) // 2
            hours = 0
            for i in range(len(piles)):
                if piles[i] <= mid: #smaller or equal so would only take an hour per rate
                    hours += 1
                elif piles[i] > mid:
                    hours += math.ceil(piles[i]/mid)
            if hours <= h:
                rate = mid
                high = mid - 1
            elif hours > h:
                low = mid + 1     
        return rate
