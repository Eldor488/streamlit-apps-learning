import math

# Function to calculate the confidence interval
def calculate_confidence_interval(p_hat, n, confidence_level):
    # Convert confidence level to Z-score
    # Common confidence levels and their corresponding Z-scores
    z_scores = {90: 1.645, 95: 1.96, 99: 2.576}
    z = z_scores[confidence_level]
    
    # Calculate standard error
    SE = math.sqrt(p_hat * (1 - p_hat) / n)
    
    # Calculate margin of error
    margin_error = z * SE
    
    # Calculate confidence interval
    lower_bound = p_hat - margin_error
    upper_bound = p_hat + margin_error
    
    # Round the results to one decimal place
    lower_bound_rounded = round(lower_bound, 2)
    upper_bound_rounded = round(upper_bound, 2)
    
    return lower_bound_rounded, upper_bound_rounded

# Input from user
p_hat = float(input("Enter sample proportion (as a decimal): "))
n = int(input("Enter sample size: "))
confidence_level = int(input("Enter confidence level (90, 95, 99): "))

# Calculate confidence interval
lower_bound, upper_bound = calculate_confidence_interval(p_hat, n, confidence_level)

# Print result
print(f"The {confidence_level}% confidence interval is: {lower_bound} to {upper_bound}")
