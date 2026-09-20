class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c=moves.count("_")
        l=moves.count("L")
        r=moves.count("R")
        return abs(l-r)+c

        