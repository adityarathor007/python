# def fn1():
#     x=2;
#     def fn2():
#         x=3
#         print(f"Inner: {x}")
#     fn2()
#     print(f"Outer: {x}")

# fn1()
# x=5
# print(f"Global: {x}")


#non local if you want to access just above the current fn and global if you want to access a variable from global scope
def fn1():
    x=2;
    def fn2():
        nonlocal x
        global y
        x=3
        y=7
    fn2()
    print(f"Updated by inner: {x}")

y=2
fn1()
print(f"Updated the global scope: {y}")

#global should be avoided as it would modify the variable that someone else is using
