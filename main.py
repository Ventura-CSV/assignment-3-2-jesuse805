def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    """
    #Calculate Minimum
    # The "If" statements calulate the smallest number within the program
    if num1 <= num2 and num1 <= num3:
        minval = num1
    elif num2 <= num1 and num2 <= num3:
        minval = num2
    else:
        minval = num3
        
    #Calculate Maximum
    # The "If" statements are the complete opposite of the previous statements
    # Thus, Calculates the Maximum number in the program
    if num1 >= num2 and num1 >= num3:
        maxval = num1
    elif num2 >= num1 and num2 > num3:
        maxval = num2
    else:
        maxval = num3
    
    #Calculate Median
    # The "If" statement calculates whether num1 is the median with 2 and statements and an or statement
    if (num1 <= num2 and num1 >= num3) or (num1 >= num2 and num1 <= num3):
        median = num1 
    # The "elif" statement calculates whether num2 is the median, replicating num 1 statements
    elif (num2 <= num1 and num2 >= num3) or (num2 >= num1 and num2 <= num3):
        median = num2
    # If num1 and num2 arent the median, thus num3 is the median
    else:
        median = num3
    
    
    """
    ########################################
    """

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
