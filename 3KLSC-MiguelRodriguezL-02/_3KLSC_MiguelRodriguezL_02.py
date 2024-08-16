NUM = 8
nums=[0]*NUM
total=0
for i in range(NUM):
    nums[i]=int(input("ingrese numero"))
    total+=nums[i]
    print("El resultado es: ", total)
