# Minimum Time Visiting All Points

def min_points(points):
    total_time = 0

    for i in range(len(points) - 1):

        # Get current point coordinates
        x1 = points[i][0]
        x2 = points[i][1]

        # Get next point coordinates         
        y1 = points[i + 1][0]
        y2 = points[i + 1][0]

        # Calculate horizontal distance
        horizontal = abs(x2 - x1)

        # Calculate vertical distance
        vertical = abs(y2 - y1)

        # Add minimum travel time
        time = max(horizontal,vertical)

        total_time += time

    return total_time

points = [[2, 4], [6, 7], [3, 1], [8, 5]]
print(min_points(points))