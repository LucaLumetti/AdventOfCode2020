f = [ [l[0],int(l[1:-1])] for l in open('input','r').readlines()]

pos = complex(0,0)
facing = complex(1,0)

for d,i in f:
    pos += facing*i*(d == 'F')
    pos += complex(0,i)*(d == 'N')
    pos += complex(i,0)*(d == 'E')
    pos += complex(0,-i)*(d == 'S')
    pos += complex(-i,0)*(d == 'W')
    facing *= complex(0,1)**((i/90)*(d == 'L'))
    facing /= complex(0,1)**((i/90)*(d == 'R'))

print(abs(pos.real)+abs(pos.imag))
