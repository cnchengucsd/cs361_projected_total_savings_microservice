import sys

def calculate_projected_savings(total_savings, average_savings, months):
    try:
        total_savings = float(total_savings)
    except ValueError:
        return "Error: Invalid input for totalSavings. Please ensure it is a number."

    try:
        average_savings = float(average_savings)
    except ValueError:
        return "Error: Invalid input for averageSavings. Please ensure it is a number."

    try:
        months = int(months)
    except ValueError:
        return "Error: Invalid input for months. Please ensure it is an integer."

    project_savings = (average_savings * months) + total_savings
    return project_savings

if __name__ == "__main__":
    if len(sys.argv) == 4:
        total_savings_arg = sys.argv[1]
        average_savings_arg = sys.argv[2]
        months_arg = sys.argv[3]
        result = calculate_projected_savings(total_savings_arg, average_savings_arg, months_arg)
        print(result)
    else:
        print("Error: Three arguments required - totalSavings, averageSavings, and months.")


