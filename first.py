# Day 1: Python Fundamentals & Ubuntu Setup

# 1. Variables and Reserved Keywords
# Learned: Cannot use 'break' as a variable name
my_progress = "Day 1 of 100" 

# 2. Numbers and Binary Formatting
# Using the format(num, 'b') concept
decimal_num = 10
binary_str = format(decimal_num, 'b')

# 3. F-Strings (Evaluated at runtime)
print(f"Status: {my_progress}")
print(f"Decimal {decimal_num} in binary is: {binary_str}")

# 4. Lists (Dynamic Arrays)
topics_learned = ["Variables", "Strings", "Binary", "Lists"]
print(f"I practiced these {len(topics_learned)} concepts: {topics_learned}")
