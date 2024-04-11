# numbers.py

# Decorator to add additional text to the queue number message
def add_additional_text(func):
    def wrapper(area):
        number = func(area)
        yield f"Your number is {number}. Please wait and someone will be with you shortly."
    return wrapper

# Generator function for queue numbers for different areas
@add_additional_text  # Apply the decorator
def queue_numbers(area):
    count = 1
    while True:
        yield f"{area[0].upper()}-{count}"
        count += 1
