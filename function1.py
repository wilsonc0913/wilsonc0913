innum = 0
list1 = []
while(innum != -1):
    innum = int(input("Please input an inerger: "))
    list1.append(innum)
list1.pop()
print("Total interger : %d" % len(list1))
print("Max interger : %d" % max(list1))
print("Min interger : %d" % min(list1))
print("Sum of intergers : %d" % sum(list1))
print("Sorted of intergers : {}".format(sorted(list1, reverse=True)))
