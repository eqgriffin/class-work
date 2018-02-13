fname = input('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    if fname.upper() == "na na boo boo":
        print("na na boo boo - You've been punked!")
    else:
        print("File cannot be opened: ", fname)
    exit()    
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print(count)