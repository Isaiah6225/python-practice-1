class calculate_average:
    
    

    def average(list):
        total = sum(list)
        average = total/len(list)

        print("Average of list: ", average)
            
    ages = [] 
    for x in range(0,3):
        age = int(input("Enter age: "))
        ages.append(age)
        

    average(ages)
        