f = open('todolist.txt', 'w+' , encoding='utf-8')
f.write('go to eat\n')
f.write('go to work\n')
f.write('go to sleep')
t = f.tell()
print(t)
f.seek(0)
c = f.read()
print(c)
f.close()