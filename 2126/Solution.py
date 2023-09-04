import random

# Runtime: 905 ms
# Memory: 30.1 MB
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for asteroid in sorted(asteroids):
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
        return True

# test

mass = random.randint(1, 105)
asteroids_length = random.randint(1, 105)
asteroids = [random.randint(1, 105) for _ in range(asteroids_length)]

print(f"asteroidsDestroyed({mass}, {asteroids}): {Solution().asteroidsDestroyed(mass, asteroids)}")