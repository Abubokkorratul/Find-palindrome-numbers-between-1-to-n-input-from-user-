n = int(input("Enter a number (n): "))
print("Palindrome numbers between 1 and", n, ":")
for num in range(1, n + 1):
    if str(num) == str(num)[::-1]:
        print(num, end=" ")
