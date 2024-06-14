num = int(input("Enter the number"))
if num>1:
    for i in range(2,int(num/2)+1):
        if(num%i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is prime number")
else:
    print(num,"is not a prime number")



list1 = [10,20,30,40,50,18,29,45,1]
print(f"Displaying the list elements:- {list1}")
list1.append(72)
print(f"Adding element to the list:- {list1}")
list1.pop()
print(f"Deleting element from the list:- {list1}")
list1.sort()
print(f"Sorting list elements{list1}")
list1.reverse()
print(f"Reversing of a list:- {list1}")
print(f"Max element in the list :{max(list1)}")
print(f"Min element in the list :{min(list1)}")
list1.clear()
print(f"clear the list:- {list1}")


