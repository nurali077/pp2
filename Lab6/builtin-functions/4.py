import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  
    return math.sqrt(number)

if __name__ == "__main__":
    number = float(input("Enter the number: "))
    delay = int(input("Enter the delay in milliseconds: "))
    result = delayed_sqrt(number, delay)
    print(f"Square root of {number} after {delay} milliseconds is {result}")