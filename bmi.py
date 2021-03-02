#zadanie bmi

masa = float(input("Podaj wagę [kg]: "))
wzrost = float(input("Podaj wzrost [m]: "))

bmi = masa/(wzrost**2)

print("BMI = {0}".format(bmi))

if(bmi < 18.5):
    print("Niedowaga.")
elif(bmi >= 18.5 and bmi < 25):
    print("Waga prawidłowa.")
elif(bmi >= 25 and bmi < 30):
    print("Nadwaga.")
elif(bmi >=30):
    print("Otyłość.")
input("Naciśnij enter, aby zakończyć ")