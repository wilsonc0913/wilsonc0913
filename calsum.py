def calsum(*params):
    total = 0
    for param in params:
        total += param
    return total

print("2 params: calsum(4,5) = %d " % calsum(4,5))
print("3 params: calsum(4,5,12) = %d" % calsum(4,5,12))
print("4 params: calsum(4,5,12,8) = %d" % calsum(4,5,12,8))
    


def scope():
    var1 = 1
    return var1, var2

    var1 = 10
    var2 = 20
    x, y = scope()
    print(x, y)
    print(var1, var2)
