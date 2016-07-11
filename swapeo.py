a="asdf"
q=list(a)
q[::2],q[1::2]=q[1::2],q[::2]
print(''.join(q))
