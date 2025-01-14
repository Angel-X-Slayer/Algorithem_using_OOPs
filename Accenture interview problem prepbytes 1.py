str = "0C1A1B1C1C1B0A0"
ans = int(str[0])
for i in range(2, len(str), 2):
    if str[i-1] == "A":
        ans &= int(str[i])
    elif str[i-1] == "B":
        ans |= int(str[i])
    elif str[i-1] == "C":
        ans ^= int(str[i])
print(ans)
