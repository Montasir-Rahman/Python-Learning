div_names = []
num_choice = int(input("Enter Number of divisions in Bangladesh: "))

for i in range(num_choice):
    div_names.append(input(f"Enter name of division {i}: "))
    
print(sorted(div_names))