import numpy as np


def linear_regression(x1, x2, y):
    # Check if there are enough data points
    if len(x1) < 2 or len(x2) < 2 or len(y) < 2 or len(x1) != len(x2) or len(x1) != len(y):
        print("Insufficient data for linear regression.")
        return None, None, None

    # Calculate the coefficients (a1, a2, and b)
    a1 = ((y[1] - y[0]) / (x1[1] - x1[0])) if (x1[1] - x1[0]) != 0 else 0
    a2 = ((y[1] - y[0]) / (x2[1] - x2[0])) if (x2[1] - x2[0]) != 0 else 0
    b = y[0] - a1 * x1[0] - a2 * x2[0]

    return a1, a2, b

# Example usage:
x1 = [1, 3, 5, 7, 9]
x2 = [2, 4, 6, 8, 10]
y = [3, 7, 11, 15, 19]

# Call the function
slope1, slope2, intercept = linear_regression(x1, x2, y)

if slope1 is not None and slope2 is not None and intercept is not None:
    print(f"Slope for x1 (a1): {slope1}")
    print(f"Slope for x2 (a2): {slope2}")
    print(f"Intercept (b): {intercept}")

    # Test for new values
    new_x1 = 11
    new_x2 = 10
    new_y = slope1 * new_x1 + slope2 * new_x2 + intercept
    print(f"Prediction for x1={new_x1}, x2={new_x2}: {new_y}")
