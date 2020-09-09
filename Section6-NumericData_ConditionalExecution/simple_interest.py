def calculate_simple_interest(principal, interest, duration):
    total_interest = interest * 0.01 * duration * principal
    total_amount = principal + total_interest
    return total_amount


print(calculate_simple_interest(10000, 5, 5))


def calculate_simple_interest2(principal, interest, duration):
    total_interest = interest * 0.01 * duration * principal
    return principal + total_interest


def calculate_simple_interest3(principal, interest, duration):
    return principal + interest * 0.01 * duration * principal

print(calculate_simple_interest3(20000, 6, 4))