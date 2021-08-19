#PYTHON FUNCTIONS


# function to check if string is palindrome or not

def isPalindrome(word):
    #  Using inBuilt function to reverse and join a string
    # Checking if both string are equal or not
    rev_word = ''.join(reversed(word))

    if (word == rev_word):
        print("The word is a palindrome")
    else:
        print("The word is not a Palindrome")
isPalindrome("madam")
isPalindrome("dad")


# Function that takes an array of numbers and returns a new array where every element of the original array is multiplied by 2
def doubler(arr):
    # Initiase an Empty array to append to later
    # loops through the length of the array and multiply each element by 2
    #append and increment by 1, the return the Output
  doubled_arr = []
  i = 0
  while i < len(arr) :
    Input_arr = arr[i]
    Output_arr = Input_arr* 2
    doubled_arr.append(Output_arr)

    i += 1
  return doubled_arr

print(doubler([2, 4, 3]))


# Function that returns the average of three numbers
def average(n1, n2, n3): 
	total = int(n1) + int(n2) + int(n3) 
	Avg = total/3 
	print(Avg)

average(1, 2, 3)

# Function that takes in a string name and returns a string saying bye to that name

def Goodbye(name):
    str_name = "Goodbye" + " " + name

    return str_name

print(Goodbye("Zaza"))


# A method that takes in a number max and returns an array containing all numbers greater than 0 and less than max
#  that are divisible by either 4 or 6, but not both.

def fizz_buzz(max):
    Max_arr = []
    for i in range(0, max):
        if((i % 4 == 0 and i % 6 != 0) or (i % 6 == 0 and i % 4 != 0)):
            Max_arr.append(i)

            i += 1
    return Max_arr

print(fizz_buzz(15))
print(fizz_buzz(30))