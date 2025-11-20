a = float(input("Enter the first term (a): "))
d = float(input("Enter the common difference (d): "))
n = int(input("Enter the term number (n): "))
nth_term = a + (n - 1) * d
sum_n = (n / 2) * (2 * a + (n - 1) * d)
print("The", n, "th term of the AP is:", nth_term)
print("The sum of first", n, "terms is:", sum_n)
