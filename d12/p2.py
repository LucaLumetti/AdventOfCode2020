f = [ [l[0],int(l[1:-1])] for l in open('input','r').readlines()]

waypoint = complex(10, 1)
pos = complex(0,0)
for d,i in f:
    pos += waypoint*i*(d == 'F')
    waypoint += complex(0,i)*(d == 'N')
    waypoint += complex(i,0)*(d == 'E')
    waypoint -= complex(0,i)*(d == 'S')
    waypoint -= complex(i,0)*(d == 'W')
    waypoint *= complex(0,1)**((i/90)*(d == 'L'))
    waypoint /= complex(0,1)**((i/90)*(d == 'R'))

print(abs(pos.real)+abs(pos.imag))
