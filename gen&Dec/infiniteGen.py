def infinite_chai():
    cnt=1
    while True:
        yield f"Refill #{cnt}"
        cnt+=1;

refill = infinite_chai()

# # this would run the infinite loop
# for get in refill:
#     print(get)

# we can controll cnt
for _ in range(3):
    print(next(refill))