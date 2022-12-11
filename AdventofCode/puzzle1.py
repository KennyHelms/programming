c = 0
x = 0 
r = 0
with open ('input.txt') as f:
    line = f.readline()
    r = 1
    c = c +1
    prev = line
    while line:
        line = f.readline()
        r = r +1
        #print(line)
        if line > prev:
            print(line + ' is greater than ' + prev )
            #prev = line
            c = c +1
        else:
            x = x +1
            print(line + 'lower ' + prev )
        prev = line
print(c)
print(x)
print(r)