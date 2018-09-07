import datetime
print('{:+f}; {:+f}'.format(3.14,3.14))
print('{: f}; {: f}'.format(3.14,-3.14))
print('{:-f}; {:-f}'.format(3.14,-3.14))
print('int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(42))
print('int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}'.format(42))
print('{:,}'.format(1234567890))
points = 19
total = 22
print('Correct answer: {:.2%}'.format(points/total))
d = datetime.datetime(2010,7,4,12,15,58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

for align,text in zip('<^>',['left','center','right']):
    print('{0:{fill}{align}16}'.format(text,fill=align,align=align))

octets = [192,168,0,1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))
#print(int(_,16))
width = 5
for num in range(5,12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num,base=base,width=width),end=' ')
    print()

