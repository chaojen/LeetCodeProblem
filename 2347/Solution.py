from collections import Counter
import random

# Runtime: 38 ms
# Memory: 16.18 MB
class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        suits_most_count = Counter(suits).most_common(1)[0][1]
        
        # [Flush]: Five cards of the same suit.
        if suits_most_count == 5:
            return "Flush"

        ranks_most_count = Counter(ranks).most_common(1)[0][1]

        # [Three of a Kind]: Three cards of the same rank.
        if ranks_most_count >= 3:
            return "Three of a Kind"

        # [Pair]: Two cards of the same rank.
        if ranks_most_count == 2:
            return "Pair"

        # [High Card]: Any single card.
        return "High Card"

# test
solution = Solution()

for time in range(1, 6):
    print(f"{time}.")
    ranks = [random.randint(1, 13) for _ in range(5)]
    suits = [random.choice('abcd') for _ in range(5)]
    bestHand = solution.bestHand(ranks, suits)
    print(f"ranks: {ranks}\nsuits: {suits}\nbestHand:{bestHand}")