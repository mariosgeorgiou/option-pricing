import math
from scipy.stats import norm
import sys


def calculate_put_price(S0, K, T, r, sigma):
    # Calculate d1 and d2
    d1 = (math.log(S0 / K) + (r + (sigma**2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Calculate put option price using Black-Scholes formula
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return put_price


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python put_option_pricer.py <strike_price>")
        sys.exit(1)

    S0 = 167  # Current stock price
    T = 874 / 365  # Time to expiration in years (874 days)
    r = 0.0420  # Risk-free interest rate
    sigma = 0.2738  # Implied volatility (27.38%)

    try:
        K = float(sys.argv[1])  # Strike price from command-line argument
    except ValueError:
        print("Invalid strike price. Please enter a numerical value.")
        sys.exit(1)

    put_price = calculate_put_price(S0, K, T, r, sigma)
    print(
        f"The price of the put option with strike price ${K} is approximately ${put_price:.2f}"
    )
