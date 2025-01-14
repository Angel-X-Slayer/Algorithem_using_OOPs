# Method 1---------------------------------------------------------


# str = "Move-Hyphens-to-front"
# new_str = ""
# tmp = 0
# for i in range(len(str)):
#     if str[i] == "-":
#         tmp += 1
#         pass
#     else:
#         new_str += str[i]
# for i in range(tmp):
#     new_str = "-"+new_str
# print(new_str)


# -------------------------------END------------------------------------------


# Method 2---------------------------------------------------------------


str = "pig-pag"
char = list(str)
read = len(char)-1
write = len(char)-1
while read >= 0:
    if char[read] != "-":
        char[write] = char[read]
        write -= 1
        read -= 1
    else:
        read -= 1

for i in range(write+1):
    char[i] = "-"

print("".join(char))


# ------------------------------------------END--------------------------------
