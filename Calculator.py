
class calculator:
    def add_1(self,num_1,num_2):
        sum = num_1 + num_2
        return sum

    def substract_2(self,num_1,num_2):
        sum = num_1 - num_2
        return sum

    def multiply_3(self,num_1,num_2):
        sum = num_1 * num_2
        return sum

    def divide_4(self,num_1,num_2):
        sum = num_1 / num_2
        return sum

mycalculator = calculator()

while True:

    print(" 1 :--> ADD\n 2 :--> SUBSTRACT\n 3 :--> MULTIPLY\n 4 :--> DIVIDE\n * :--> EXIT")
    print("-----------------------------------------")
    x = input("SELECT OPERATION : ")

    if x == "1" or x == "2" or x=="3" or x=="4":
        number_1 = int(input("ENTER FIRST NUMBER : "))
        number_2 = int(input("ENTER SECOND NUMBER : "))

        if x=="1":
            print("SUMMATION IS -------->", mycalculator.add_1(number_1, number_2))

        elif x=="2":
            print("ABSTRACT IS -------->", mycalculator.substract_2(number_1, number_2))

        elif x=="3":
            print("MULTIPLY IS -------->", mycalculator.multiply_3(number_1, number_2))

        elif x=="4":
            if number_2 == 0:
                print("DIVIDE IS --------> ",number_1)

            else:
                print("DIVIDE IS -------->", mycalculator.divide_4(number_1, number_2))

    elif x=="*":
            break

    else:
        continue





