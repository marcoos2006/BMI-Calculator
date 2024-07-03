yes = "Y"

#start of calculating loop
while True:
    if yes == "Y":
        weight = float(input("BMI calculator\nPlease enter your weight: "))
        height = float(input("Please enter your height(cm): "))
        height2 = height/100
        bmi = float(height2)*float(height2)
        final_bmi = weight/float(bmi)
        print(f"Your BMI is {final_bmi:0.1f}")
        if final_bmi <= 18.4:
            print("You are Underweight")
            while True:
                #user input if they want to reset the calculator
                yes = input("Would u like to calculate another BMI? (Y/N): ")
                if yes == "Y":
                    print("----------------------------------------------------------")
                    break
                else:
                    exit()
        elif final_bmi <= 24.9:
            print("You are Normal Weight")
            while True:
                yes = input("Would u like to calculate another BMI? (Y/N): ")
                if yes == "Y":
                    print("----------------------------------------------------------")
                    break
                else:
                    exit()
        elif final_bmi <= 29.9:
            print("You are Overweight")
            while True:
                yes = input("Would u like to calculate another BMI? (Y/N): ")
                if yes == "Y":
                    print("----------------------------------------------------------")
                    break
                else:
                    exit()
        elif final_bmi <= 34.9:
            print("You are Obesity class 1")
            while True:
                yes = input("Would u like to calculate another BMI? (Y/N): ")
                if yes == "Y":
                    print("----------------------------------------------------------")
                    break
                else:
                    exit()
        elif final_bmi <= 39.9:
            print("You are Obesity class 2")
            while True:
                yes = input("Would u like to calculate another BMI? (Y/N): ")
                if yes == "Y":
                    print("----------------------------------------------------------")
                    break
                else:
                    exit()
        else:
            print("You are Obesity class 3")
            while True:
                yes = input("Would u like to calculate another BMI? (Y/N): ")
                if yes == "Y":
                    print("----------------------------------------------------------")
                    break
                else:
                    exit()