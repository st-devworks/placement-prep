# DAY 7 – Recursion

def show_numbers(n):
    if n == 0:          # base case
        return
    print(n)
    show_numbers(n - 1) # recursive call

show_numbers(5)