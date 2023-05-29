import numpy as np
import matplotlib.pyplot as plt
from Bezier import Bezier

def calculate_intercept(segment1, segment2):
    """
    Calculates the intercept point of two line segments.

    Arguments:
    segment1 -- NumPy array of shape (2, 2) representing the first line segment.
    segment2 -- NumPy array of shape (2, 2) representing the second line segment.

    Returns:
    intercept -- NumPy array of shape (2,) representing the intercept point. None if no intercept exists.
    """

    # Extract segment coordinates
    (x1, y1), (x2, y2) = segment1
    (x3, y3), (x4, y4) = segment2

    # Calculate the slopes of the line segments
    slope1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else np.inf
    slope2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else np.inf
    print(slope1)
    print(slope2)

    # Check if the lines are parallel
    if slope1 == slope2:
        return None

    # Calculate the x-coordinate of the intercept point
    if slope1 == np.inf:
        x = x1
    elif slope2 == np.inf:
        x = x3
    else:
        x = (y3 - y1 + slope1 * x1 - slope2 * x3) / (slope1 - slope2)

    # Calculate the y-coordinate of the intercept point
    if slope1 == np.inf:
        y = slope2 * (x - x3) + y3
    else:
        y = slope1 * (x - x1) + y1

    # Check if the intercept point lies within the line segments
    # if (x1 <= x <= x2 or x2 <= x <= x1) and (y1 <= y <= y2 or y2 <= y <= y1) and \
    #         (x3 <= x <= x4 or x4 <= x <= x3) and (y3 <= y <= y4 or y4 <= y <= y3):
    intercept = np.array([x, y])
    return intercept

    # return None

seg1 = np.array([[0,1],[2,1]]) # start a, end b
seg2 = np.array([[9,6],[10,10]]) # start c, end d, connect b and c

# seg1 = np.array([[0,1],[2,1]]) # start a, end b
# seg2 = np.array([[3,3],[5,10]]) # start c, end d, connect b and c

interpoint = calculate_intercept(seg1, seg2)
print(interpoint)


t_points = np.arange(0, 1, 0.01) #................................. Creates an iterable list from 0 to 1.
points1 = np.array([seg1[1], interpoint, [5,6], seg2[0]]) #.... Creates an array of coordinates.
curve1 = Bezier.Curve(t_points, points1) #......................... Returns an array of coordinates.

import matplotlib.pyplot as plt

plt.figure()
plt.plot(
	curve1[:, 0],   # x-coordinates.
	curve1[:, 1]    # y-coordinates.
)
plt.plot(
	points1[:, 0],  # x-coordinates.
	points1[:, 1],  # y-coordinates.
	'ro:'           # Styling (red, circles, dotted).
)
plt.plot([seg1[0][0], seg1[1][0]], [seg1[0][1], seg1[1][1]], color='blue', label='Line Segment 1')
plt.plot([seg2[0][0], seg2[1][0]], [seg2[0][1], seg2[1][1]], color='red', label='Line Segment 2')
plt.grid()
plt.show()