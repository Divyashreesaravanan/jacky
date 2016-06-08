s="1234"
a=list(s)
a[::2],a[1::2]=a[1::2],a[::2]
print(''.join(a))
