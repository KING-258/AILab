def fractional_knapsack(items, capacity):
    n = len(items)
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    cost = 0
    bag = []
    for weight, value in sorted_items:
        if capacity == 0:
            break
        if weight <= capacity:
            bag.append((weight, value, 1))
            cost += value
            capacity -= weight
        else:
            ch = capacity / weight if weight != 0 else 0
            bag.append((capacity, ch * value, ch))
            cost += ch * value
            capacity = 0
    return cost, bag
def zero_one_knapsack(items, capacity):
    n = len(items)
    sorted_items = sorted(items, key=lambda x: x[0])
    capacity = int(capacity)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        weight_i, value_i = sorted_items[i - 1]
        for w in range(1, capacity + 1):
            if weight_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][int(w - weight_i)] + value_i)
            else:
                dp[i][w] = dp[i - 1][w]
    cost = dp[n][capacity]
    bag = []
    w = capacity
    for i in range(n, 0, -1):
        weight_i, value_i = sorted_items[i - 1]
        if dp[i][int(w)] != dp[i - 1][int(w)]:
            bag.append((weight_i, value_i))
            w -= weight_i
    return cost, bag
def main():
    num_items = int(input("Enter the number of items: "))
    items = []
    for i in range(num_items):
        weight = float(input(f"Enter weight of item {i+1}: "))
        value = float(input(f"Enter value of item {i+1}: "))
        items.append((weight, value))
    capacity = float(input("Enter the capacity of the knapsack: "))
    ch = int(input("Choose ch (0 for 0/1 Knapsack, 1 for Fractional Knapsack): "))
    if ch == 0:
        cost, bag = zero_one_knapsack(items, capacity)
    elif ch == 1:
        cost, bag = fractional_knapsack(items, capacity)
    else:
        print("Invalid input. Please choose either 0 or 1.")
        return
    print("Maximum value:", cost)
    print("Selected items:")
    for item in bag:
        if ch == 1:
            print(f"Weight: {item[0]}, Value: {item[1]}, Fraction: {item[2]}")
        else:
            print(f"Weight: {item[0]}, Value: {item[1]}")
if __name__ == "__main__":
    main()