def main():
    def quest1():
#Create a function in your program that counts from 0 to [NUMBER]
        def countup(num):
            for x in range(num+1):   #iterates from 0 to Number
                print (x)    #prints each number
        countup(18) #call function from 0 to 18


    def quest2():
#Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
        def i_hate_q():
            while(True):
                escape=input("Please press 'q' or 'Q' so I don't have to do this problem anymore. ")  #ask for input
                escape=escape.lower()    #lowercase the input
                if (escape == 'q'):       #allows user to escape if they press "q" or "Q"
                    print("Thank you!!!!")
                    break
                else:                       #otherwise you are stuck
                    print("GRRRRRRRRRR!!!")
        i_hate_q() #Calls function

    def quest3():
        def askforNum():
            num1 =int(input("Please enter your first number. "))    #ask for first number
            num2 = int(input("Please enter your your second number. "))   #ask for second number
            def add(num1,num2):  #add
                return num1+num2
            def sub(num1,num2):  #subtract
                return num1-num2
            def multi(num1,num2): #multiply
                return num1*num2
            def div(num1,num2): #divide
                return num1/num2


            print(add(num1,num2))   #displays returned function for all problems
            print(sub(num1,num2))
            print(multi(num1,num2))
            print(div(num1,num2))
        askforNum()

    def quest4():
        def askforNum():
            num1 =int(input("Please enter your first number. "))   #ask for first input
            num2 = int(input("Please enter your your second number. "))  #ask for second input
            operation = input("would you like to add, subtract, multiply or divide? ") #ask for operation
            operation=operation.lower()

            if operation == "add":                       #add
                return(f"{num1} + {num2} = {num1+num2}")
            elif operation == "subtract":                #sub
                return(f"{num1} - {num2} = {num1-num2}")
            elif operation == "multiply":                #multiply
                return(f"{num1} x {num2} = {num1*num2}")
            elif operation == "divide":                  #divide
                return(f"{num1} / {num2} = {num1/num2}")
            else:
                return("Invalid input")
        print(askforNum())





    #quest1()
    #quest2()
    #quest3()
    quest4()


if __name__ == '__main__':
    main()
