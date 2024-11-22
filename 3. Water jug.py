from collections import deque

def is_measurable(jug1_capacity, jug2_capacity, target_amount):
    if target_amount > jug1_capacity + jug2_capacity:
        return False
    if target_amount % gcd(jug1_capacity, jug2_capacity) != 0:
        return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve_water_jug(jug1_capacity, jug2_capacity, target_amount):
    if not is_measurable(jug1_capacity, jug2_capacity, target_amount):
        print("No solution exists")
        return

    visited = set()
    queue = deque([(0, 0)])  # starting point (0, 0)
    steps = []

    while queue:
        jug1, jug2 = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        steps.append((jug1, jug2))

        if jug1 == target_amount or jug2 == target_amount or jug1 + jug2 == target_amount:
            for step in steps:
                print(f"Jug1: {step[0]} liters, Jug2: {step[1]} liters")
            return

        # Fill Jug1
        if (jug1_capacity, jug2) not in visited:
            queue.append((jug1_capacity, jug2))
        # Fill Jug2
        if (jug1, jug2_capacity) not in visited:
            queue.append((jug1, jug2_capacity))
        # Empty Jug1
        if (0, jug2) not in visited:
            queue.append((0, jug2))
        # Empty Jug2
        if (jug1, 0) not in visited:
            queue.append((jug1, 0))
        # Pour Jug1 to Jug2
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        if (jug1 - pour_to_jug2, jug2 + pour_to_jug2) not in visited:
            queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        # Pour Jug2 to Jug1
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        if (jug1 + pour_to_jug1, jug2 - pour_to_jug1) not in visited:
            queue.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

    print("No solution exists")

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2
solve_water_jug(jug1_capacity, jug2_capacity, target_amount)
