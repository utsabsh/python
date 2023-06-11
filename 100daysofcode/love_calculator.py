name1 = input("enter first name: ")
name2 = input("enter second name:")
combined_name = name1+name2
count1=combined_name.lower().count("t")
count2=combined_name.lower().count("r")
count3=combined_name.lower().count("u")
count4=combined_name.lower().count("e")
counttrue = count1+count2+count3+count4
print(counttrue)
count5=combined_name.lower().count("l")
count6=combined_name.lower().count("o")
count7=combined_name.lower().count("v")
count8=combined_name.lower().count("e")
countlove = count5+count6+count7+count7
print(countlove)
total_count= int(str(counttrue)+str(countlove))

if total_count <10 or total_count>90:
    print(f"your score is {total_count}, you go together like coke and mentos.")
elif 50<total_count>40:
    print(f"your score is {total_count}, you are alright together.")
else:
    print(f"your score is {total_count}")
