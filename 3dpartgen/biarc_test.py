import numpy as np
import matplotlib.pyplot as plt

def generate_biarc(start_point, end_point, tangent_start, tangent_end, resolution=100):
    # Calculate the parameters for the biarc
    delta = end_point - start_point
    angle = np.arccos(np.dot(tangent_start, tangent_end))

    # Check if the points and tangents are collinear
    if np.isclose(angle, 0):
        # If collinear, return a straight line segment
        return np.linspace(start_point, end_point, resolution)
    
    # Calculate the intermediate point
    intermediate_point = start_point + delta / 2
    
    # Calculate the radii of the two arcs
    radius_1 = np.linalg.norm(delta) / (2 * np.sin(angle / 2))
    radius_2 = radius_1

    # Calculate the center points of the two arcs
    center_1 = intermediate_point + radius_1 * np.array([-tangent_start[1], tangent_start[0]])
    center_2 = intermediate_point + radius_2 * np.array([tangent_start[1], -tangent_start[0]])

    # Generate the parameter t from 0 to 1
    t = np.linspace(0, 1, resolution)

    # Calculate the angles for each point on the arcs
    theta_1 = np.arctan2(start_point[1] - center_1[1], start_point[0] - center_1[0])
    theta_2 = np.arctan2(end_point[1] - center_2[1], end_point[0] - center_2[0])

    # Generate the points on the first arc
    arc1_points = center_1 + radius_1 * np.array([np.cos(theta_1 + angle * t.reshape(-1, 1)), np.sin(theta_1 + angle * t.reshape(-1, 1))])

    # Generate the points on the second arc
    arc2_points = center_2 + radius_2 * np.array([np.cos(theta_2 - angle * (1 - t.reshape(-1, 1))), np.sin(theta_2 - angle * (1 - t.reshape(-1, 1)))])

    # Concatenate the two arcs and return the biarc
    return np.concatenate((arc1_points, arc2_points[:, ::-1]), axis=1)

# Example usage
start_point = np.array([0, 0])
end_point = np.array([5, 5])
tangent_start = np.array([1, 0])
tangent_end = np.array([0, 1])

biarc = generate_biarc(start_point, end_point, tangent_start, tangent_end)

# Plot the biarc
plt.plot(biarc[0], biarc[1])
plt.plot(start_point[0], start_point[1], 'ro', label='Start Point')
plt.plot(end_point[0], end_point[1], 'ro', label='End Point')
plt.axis('equal')
plt.legend()
plt.show()