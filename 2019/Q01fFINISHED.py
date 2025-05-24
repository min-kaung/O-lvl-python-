# Q01f

list_1f =[(2010,8), (4800, 11), (2011,4), (5000,9)]
assistantSalary = 1000.00

for pair in list_1f:
    shopIncome = pair[0]
    assistantSales = pair[1]
    print ("Shop income :", shopIncome, "Assistant sales ", assistantSales)

    if (shopIncome > 5000 or assistantSales >= 10):
        print ("Assistant bonus = ", assistantSalary * 0.1)

    elif (shopIncome >= 2000 and assistantSales >= 5):
            print("Assistant bonus = ", assistantSalary * 0.05)

    else:
        print("Assistant bonus = ", 0)