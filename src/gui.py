# Import necessary modules
from PyQt5.QtWidgets import QMainWindow
import math
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import norm
from math import sqrt, comb, exp, factorial, ceil

class StatsCalculatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setup the GUI layout, menus, etc.
        # This method will be expanded to create the GUI interface
        pass

    # Combinations Calculator
    # Computes the number of combinations of choosing r items from n items
    def combinations(n, r):
        return math.comb(n, r)

    # Permutations Calculator
    # Computes the number of ways of arranging r items from n items
    def permutations(n, r):
        return math.perm(n, r)

    # Variance Calculator
    # Calculates the variance of a list of numbers
    def variance(data):
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)

    # Standard Deviation Calculator
    # Calculates the standard deviation of a list of numbers
    def standard_deviation(data):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    # Mean Calculator
    # Computes the arithmetic mean of a list of numbers
    def mean(data):
        return sum(data) / len(data)

    # Median Calculator
    # Finds the median value in a list of numbers
    def median(data):
        data_sorted = sorted(data)
        n = len(data_sorted)
        mid = n // 2

        if n % 2 == 0:
            return (data_sorted[mid - 1] + data_sorted[mid]) / 2
        else:
            return data_sorted[mid]

    # Mode Calculator
    # Identifies the mode(s) in a set of numbers
    def mode(data):
        count = Counter(data)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]

    # Probability Calculator
    # Computes the probability of an event
    def probability(success_outcomes, total_outcomes):
        return success_outcomes / total_outcomes

    # Z-Score Calculator
    # Calculates the Z-score of a data point
    def z_score(data_point, mean, standard_deviation):
        return (data_point - mean) / standard_deviation

    # T-Test Calculator
    # Performs a t-test to determine if there is a significant difference between the means of two groups
    def t_test(mean1, mean2, std1, std2, n1, n2):
        pooled_std = sqrt(((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / (n1 + n2 - 2))
        t_score = (mean1 - mean2) / (pooled_std * sqrt(1/n1 + 1/n2))
        return t_score

    # Chi-Square Test Calculator
    # Computes the chi-square statistic for given observed and expected frequencies
    def chi_square_test(observed, expected):
        chi_square = sum((o - e)**2 / e for o, e in zip(observed, expected))
        return chi_square

    # Linear Regression Calculator
    # Calculates the slope and intercept of a linear regression line
    def linear_regression(x, y):
        n = len(x)
        xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_x = sum(x)
        sum_y = sum(y)
        square_sum_x = sum(xi**2 for xi in x)

        slope = ((n * xy) - (sum_x * sum_y)) / ((n * square_sum_x) - (sum_x**2))
        intercept = (sum_y - (slope * sum_x)) / n

        return slope, intercept

    # ANOVA Calculator
    # Performs an ANOVA test for given groups of data
    def anova(*groups):
        k = len(groups)  # Number of groups
        n = sum(len(group) for group in groups)  # Total number of observations

        overall_mean = sum(sum(group) for group in groups) / n  # Overall mean

        # Between-group variability
        ss_between = sum(len(group) * (sum(group) / len(group) - overall_mean) ** 2 for group in groups)

        # Within-group variability
        ss_within = sum(sum((item - sum(group) / len(group)) ** 2 for item in group) for group in groups)

        # Mean sum of squares
        ms_between = ss_between / (k - 1)
        ms_within = ss_within / (n - k)

        # F-ratio
        f_ratio = ms_between / ms_within
        return f_ratio

    # Confidence Interval Calculator
    # Determines the confidence interval for a sample mean
    def confidence_interval(mean, std, n, confidence_level):
        z = norm.ppf(1 - (1 - confidence_level) / 2)
        margin_of_error = z * (std / (n ** 0.5))
        return (mean - margin_of_error, mean + margin_of_error)
    
    # Binomial Distribution Calculator
    # Computes probabilities for a binomial distribution
    def binomial_probability(n, k, p):
        return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    # Poisson Distribution Calculator
    # Calculates the probabilities for a Poisson distribution
    def poisson_probability(lambda_, k):
        return (lambda_ ** k) * exp(-lambda_) / factorial(k)

    # Normal Distribution Calculator
    # Provides probabilities for a normal distribution
    def normal_probability(mean, std, x):
        return norm.cdf(x, mean, std)

    # Sample Size Calculator
    # Determines the sample size needed for a survey or experiment
    def sample_size(margin_of_error, confidence_level, p_hat):
        z = norm.ppf(1 - (1 - confidence_level) / 2)
        return ceil((z**2 * p_hat * (1 - p_hat)) / margin_of_error**2)

    # Histogram Generator
    # Creates a histogram based on a set of data points
    def create_histogram(data, bins=None):
        plt.hist(data, bins=bins)
        plt.xlabel('Data')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.show()

    # Box-and-Whisker Plot Generator
    # Generates a box-and-whisker plot for a set of data
    def create_box_plot(data):
        plt.boxplot(data)
        plt.ylabel('Data')
        plt.title('Box-and-Whisker Plot')
        plt.show()
