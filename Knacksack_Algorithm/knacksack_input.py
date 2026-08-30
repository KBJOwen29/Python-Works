# function for running the algorithm
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill dp table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity], dp

# Main System
def main():
    print("=== 0/1 Knapsack Problem Solver ===")
    print("This program uses dynamic programming to solve the 0/1 Knapsack Problem.")
    print("You will be asked to enter:")
    print("- The number of items")
    print("- The value and weight of each item")
    print("- The capacity of the knapsack\n")

    try:
        n = int(input("Enter number of items: "))
        values = []
        weights = []

        for i in range(n):
            print(f"\n--- Item {i + 1} ---")
            val = int(input("Enter value: "))
            wt = int(input("Enter weight: "))
            values.append(val)
            weights.append(wt)

        capacity = int(input("\nEnter the capacity of the knapsack: "))
        max_value, dp_table = knapsack(values, weights, capacity)

        print("\nDP Table:")
        for row in dp_table:
            print(row)

        print(f"\nMaximum value that can be carried: {max_value}")

    except ValueError:
        print("Invalid input. Please enter integers only.")
# Calls Main System
if __name__ == "__main__":
    main()
