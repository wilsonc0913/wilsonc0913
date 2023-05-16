score = range(85, 101, 5)
subject = ["Chinese", "Math", "English", "History"]
#print(list(score))
n = 0
for s in score:
    print(subject[n],"= %d" % s)
    n += 1
#print("Chinese : %d" % score[0])
#print("Math : %d" % score[1])
#print("English : %d" % score[2])

r1 = range(3, 8)
print(list(r1))

r2 = range(3, 8, 2)
print(list(r2))

r3 = range(8, 3, -1)
print(list(r3))

list1 = ["Banana", "Apple", "Orange"]
for s in list1:
    print(s, end=",")

for i in range(1,31):
    print(i)
