temp = 36
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("There is no party")
else :
    print("The party is on")

    temp = 25
    is_sunny = True

    if temp >= 28 and is_sunny:
        print("It is HOT outside")
        print("It is SUNNY")
    elif temp <= 0 and is_sunny:
        print("It is COLD outside")
        print("It is WINDY")
    elif 28 >= 28 and not is_sunny:
        print("It is Hot outside")
        print("It is cloudy")
