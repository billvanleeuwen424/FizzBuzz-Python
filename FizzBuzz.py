#FizzBuzz Program

counter = 1

#start loop
while counter < 100:

    #increase 
    counter += 1

    #enter into the fizz or buzz or fizzbuzz algorithm
    if counter % 5 == 0 or counter % 3 == 0:
        if counter % 5 == 0 and counter % 3 == 0:
            print("fizzbuzz")
            
        elif counter % 5 == 0:
            print("fizz")
        elif counter % 3 == 0:
            print("buzz")
    else:
        print(counter)
