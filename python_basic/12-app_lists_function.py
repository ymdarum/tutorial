lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Jim"]
#friends.append(lucky_numbers) #add list as is
#friends.extend(lucky_numbers) #add to the current list
#friends.append("Creed") #add based on index
#friends.insert(1,"Kelly")
# friends.remove('Jim')
# friends.clear
# friends.pop()
#friends.insert(1,lucky_numbers)
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
friends2.sort()
print(friends2)
print(lucky_numbers)
#name = input("Enter Name: ")()
#print(name + " position is: " + str(friends.index(name)))
#print(name + " appear " + str(friends.count(name)) + " time")
