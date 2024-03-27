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
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    bag = [0] * len(items)

    for index in range(len(sorted_items)):
        weight, value = sorted_items[index]
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
            original_index = items.index((weight, value))
            bag[original_index] = 1
    return total_value, bag
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
        total_value, bag = zero_one_knapsack(items, capacity)
    elif ch == 1:
        total_value, bag = fractional_knapsack(items, capacity)
    else:
        print("Invalid input. Please choose either 0 or 1.")
        return
    print("Maximum value:", total_value)
    print("Selected items:")
    if ch == 1:
        for item in bag :
            print(f"Weight: {item[0]}, Value: {item[1]}, Fraction: {item[2]}")
    else:
        for index, is_selected in enumerate(bag):
            if is_selected == 1:
                item = items[index]
                print(f"Weight: {item[0]}, Value: {item[1]}")
if __name__ == "__main__":
    main()