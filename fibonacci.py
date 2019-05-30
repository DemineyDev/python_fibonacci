# Program that generates fibonacci sequence to a user generated number

print('***HELLO USER***')
print("Let's generate a fibonacci sequence to your chosen number")
user_input = input('Please enter a number: ')    # Get number from user

def generate_fibonacci(user_input):
    nums = [0, 1]     # Initialize first two values of fibonacci sequence
    while nums[-1] < int(user_input):   #While loop to loop while number less than users number
        nums.append(nums[-1] + nums[-2])   #Apend to list
    for num in nums:     # Iterate through list printing the numbers, excluding last which is larger than user's number
        if num < int(user_input):
            print(num)



generate_fibonacci(user_input)
