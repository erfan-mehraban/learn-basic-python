a=input()
res = ""
for l in a:
    if l is 'a':
        res+="@"
    elif l is 'n':
        res+="$"
    elif l is 'e':
        res+="_"
    elif l is 'm':
        res+="^"
    else:
        res+=l
print(res)

