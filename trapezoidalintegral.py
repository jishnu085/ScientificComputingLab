from numpy import*
def trapezoidal_rule(func, a, b, n):
    """
    Compute the integral of a function using the trapezoidal rule.

    :param func: The function to be integrated.
    :param a: Lower limit of integration.
    :param b: Upper limit of integration.
    :param n: Number of subintervals (must be even for the trapezoidal rule).
    :return: Approximation of the integral.
    """
    # Step size
    h = (b - a) / n

    # Initialize sum
    integral = 0.5 * (func(a) + func(b))

    # Add the contributions from the interior points
    for i in range(1, n):
        integral += func(a + i * h)

    # Multiply by the step size
    integral *= h

    return integral

# Define the function to be integrated
def f(x):
    return 3 * x ** 4 + 5

# Define the limits of integration
a = -3
b = 3

# Define the number of subintervals
n = 1000  # Choose an appropriate number of subintervals

# Compute the integral using the trapezoidal rule
integral = trapezoidal_rule(f, a, b, n)

print("Approximation of the integral using the trapezoidal rule:", integral)
