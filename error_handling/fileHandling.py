file=open("order.txt","w")
# so that during the transition from ram to memory if the program crashes the file gets corrupted so to avoid finally close the file before exiting
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

# with operator does the above thing
# calls file.__enter__() and file.__exit__()
with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")