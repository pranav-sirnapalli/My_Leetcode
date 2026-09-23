class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total = 0
        points_len = len(points)
        curr_x = points[0][0]
        curr_y = points[0][1]

        for i in range(1, len(points)):
            x_val = points[i][0]
            y_val = points[i][1]

            abs_x = abs(x_val - curr_x)
            abs_y = abs(y_val - curr_y)
            total = total + max(abs_x, abs_y)
            curr_x = x_val
            curr_y = y_val
        return total

