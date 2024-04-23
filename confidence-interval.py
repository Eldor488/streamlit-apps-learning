import math 

# Function to calculate the confidence interval when we do not know the margin error 
# x = number of people in the sample 
# n = number of people in the sample who satifisfied the condition

def calculate_confidence_interval():
    n = input("Enter the number of people in the sample: ")
    x = input("Enter the number of people in the sample who satisfied the condition: ")
    n = int(n)
    x = int(x)

    p_hat1 = x/n 
    p_hat2 = 1/math.sqrt(n)
# Confidence interval
    confidence_interval_positive = p_hat1 + p_hat2
    confidence_interval_negative = p_hat1 - p_hat2
    print(f"The confidence interval is: {round(confidence_interval_negative, 2)} to {round(confidence_interval_positive, 2)}")
    return confidence_interval_positive, confidence_interval_negative
    

calculate_confidence_interval()
