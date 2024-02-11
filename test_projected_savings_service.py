import subprocess

def call_projected_savings_service(total_savings, average_savings, months):
    process = subprocess.run(
        ["python", "projected_savings_service.py", str(total_savings), str(average_savings), str(months)],
        capture_output=True, 
        text=True
    )
    return process.stdout.strip()

def main():
    # Test cases
    test_cases = [
        (1000, 200, 6),  # Normal case
        (1000, 200, 0),  # Zero months
        (-1000, 200, 6), # Negative total savings
        (1000, -200, 6), # Negative average savings
        (1000000, 50000, 12), # Large numbers
        (1000, 200, "six"),  # Non-integer months
        ("one thousand", "two hundred", 6)  # String inputs
    ]

    for total_savings, average_savings, months in test_cases:
        print(f"Testing with: Total Savings={total_savings}, Average Savings={average_savings}, Months={months}")
        result = call_projected_savings_service(total_savings, average_savings, months)

        # Saving the result in a variable
        projected_savings_result = result

        # Now you can use this variable for further processing or checking
        print(f"Result: {projected_savings_result}\n")


if __name__ == "__main__":
    main()
