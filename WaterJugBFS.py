def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = [((0, 0), [])]
    while queue:
        current_state, path = queue.pop(0)
        visited.add(current_state)
        jug1_amount, jug2_amount = current_state
        if jug1_amount == target or jug2_amount == target:
            path.append(current_state)
            return path
        if jug1_amount < jug1_capacity:
            next_state = (jug1_capacity, jug2_amount)
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
        if jug2_amount < jug2_capacity:
            next_state = (jug1_amount, jug2_capacity)
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
        if jug1_amount > 0:
            next_state = (0, jug2_amount)
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
        if jug2_amount > 0:
            next_state = (jug1_amount, 0)
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
        if jug1_amount > 0 and jug2_amount < jug2_capacity:
            amount_to_pour = min(jug1_amount, jug2_capacity - jug2_amount)
            next_state = (jug1_amount - amount_to_pour, jug2_amount + amount_to_pour)
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
        if jug2_amount > 0 and jug1_amount < jug1_capacity:
            amount_to_pour = min(jug2_amount, jug1_capacity - jug1_amount)
            next_state = (jug1_amount + amount_to_pour, jug2_amount - amount_to_pour)
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
    return None
jug1_capacity = int(input("Enter the capacity of Jug 1: "))
jug2_capacity = int(input("Enter the capacity of Jug 2: "))
target_amount = int(input("Enter the target amount: "))

result = water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
if result:
    print(f"Steps to achieve {target_amount} liters using the jugs:")
    for i, state in enumerate(result):
        print(f"Step {i + 1}: Jug1={state[0]}, Jug2={state[1]}")
else:
    print(f"Target amount {target_amount} liters cannot be measured with the given jugs.")