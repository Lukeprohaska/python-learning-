
# Problem 1 - Compound Interest Calculator 

principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))

balance = principal

for year in range(1, years +1):
    balance = balance * (1 + rate / 100)
    print(f"year {year}: ${balance:.2f}")

total_interest = balance - principal
print(f"Total interest earned ${total_interest:.2f}")


# Problem 2 - Caesar Cipher Encoder

def caesar_encode(text, shift):
    result = ""
    for char in text:

        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')     

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result  += new_char
        else:
            result += char
    return result

print(f"Test 1: {caesar_encode('Hello, World!', 3)}")
print(f"Test 2: {caesar_encode('abc xyz', 2)}")
print(f"Test 3: {caesar_encode('Python 3', 5)}")
    
        
# Problem 3 - Matrix Transpose

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

m1 = [[1,2,3,], [4,5,6]]
print(f"Transpose of m1: {transpose(m1)}")

m2 = [[1,2], [3,4], [5, 6]]
print(f"Transpose of m2: {transpose(m2)}")
    