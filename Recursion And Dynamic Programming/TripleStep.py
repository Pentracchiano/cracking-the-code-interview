# 8.1 - A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def ways_to_climb_stairs(self, n: int) -> int:
    # O(n) and easily generalizable to k jumps

    last_numbers = [0, 1, 1]

    if n < 3:
        return last_numbers[n]

    current_sum = sum(last_numbers)
    for i in range(3, n):
        i %= len(last_numbers)
        previous_value = last_numbers[i]
        last_numbers[i] = current_sum
        current_sum += current_sum - previous_value

    return current_sum
