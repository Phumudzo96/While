# Ask user to enter numbers
number = int(input("Enter a number: "))

# Create a variable that will help count the numbers entered
number_sum = 0
number_count = 0
# Add the while loop to continuesly do the code till -1 is enter
while number != -1:
    print(number)
    number_sum += number
    number_count += 1
    number = int(input("Enter a number: "))
if number == -1:
    avarage = number_sum / number_count

# When -1 is entered this must be printed
print(f"-1 was added. The avarage is {avarage}")

