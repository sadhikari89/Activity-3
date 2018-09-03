# display a program heading or any welcome message
print("ISQA 4900 Letter Grade Calculator")
print()

# initialize variable
# while loop

choice = "y"
while choice.lower() == "y":
    # get input from the user
         pointsEarned = float(input("Enter total number of points earned:\t"))

    # if, elif and else boolean expressions
         if 970 <= pointsEarned <= 1000:
            print("Letter grade: A+")

         elif 930 <= pointsEarned <= 969:
             print("Letter grade: A")

         elif 900 <= pointsEarned <= 929:
          print("Letter grade: A-")

         elif 870 <= pointsEarned <= 899:
             print("Letter grade: B+")

         elif 830 <= pointsEarned <= 869:
            print("Letter grade: B")

         elif 800 <= pointsEarned <= 829:
            print("Letter grade: B-")

         elif 770 <= pointsEarned <= 799:
            print("Letter grade: C+")

         elif 730 <= pointsEarned <= 769:
            print("Letter grade: C")

         elif 700 <= pointsEarned <= 729:
            print("Letter grade: C-")

         elif 670 <= pointsEarned <= 699:
           print("Letter grade: D+")

         elif 630 <= pointsEarned <= 669:
           print("Letter grade: D")

         elif 600 <= pointsEarned <= 629:
           print("Letter grade: D-")

         elif 0 <= pointsEarned <= 599:
            print("Letter grade: F")

         else:
            print("Invalid entry. Try again!!")

         print()
    # know whether users wants to continue or leave
         choice = input("Continue (y/n):\t")
         print()
    # runs when user inputs n or loop ends
print("Bye!")
