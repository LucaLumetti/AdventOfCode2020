import numpy as np
import math
import re
f = open('input').read().rstrip().split('\n\n')
image_shape = int(math.sqrt(len(f)))

tiles = {}
for tile in f:
    spl = tile.split('\n')
    tiles[spl[0]] = np.array([ list(s) for s in spl[1:]])

def border_align(a,b):
    return a == b or a[::-1] == b

def find_right_partner(id, tile, tiles):
    right = tile[:,-1]
    for id_b,tile_b in tiles.items():
        if(id_b == id): continue
        top_b = tile_b[0,:]
        bottom_b = tile_b[-1,:]
        left_b = tile_b[:,0]
        right_b = tile_b[:,-1]
        if((top_b == right).all()):         return id_b, np.rot90(tile_b)
        if((top_b[::-1] == right).all()):   return id_b, np.rot90(tile_b[:,::-1])

        if((right_b == right).all()):       return id_b, np.rot90(tile_b[::-1,:],k=2)
        if((right_b[::-1] == right).all()): return id_b, np.rot90(tile_b,k=2)

        if((bottom_b == right).all()):      return id_b, np.rot90(tile_b,k=3)
        if((bottom_b[::-1] == right).all()):return id_b, np.rot90(tile_b[:,::-1], k=3)

        if((left_b == right).all()):        return id_b, tile_b
        if((left_b[::-1] == right).all()):  return id_b, tile_b[::-1,:]
    return False, None

def find_bottom_partner(id, tile, tiles):
    bottom = tile[-1,:]
    for id_b,tile_b in tiles.items():
        if(id_b == id): continue
        top_b = tile_b[0,:]
        bottom_b = tile_b[-1,:]
        left_b = tile_b[:,0]
        right_b = tile_b[:,-1]
        if((top_b == bottom).all()):         return id_b, tile_b
        if((top_b[::-1] == bottom).all()):   return id_b, tile_b[:,::-1]

        if((right_b == bottom).all()):       return id_b, np.rot90(tile_b)
        if((right_b[::-1] == bottom).all()): return id_b, np.rot90(tile_b[::-1,:])

        if((bottom_b == bottom).all()):      return id_b, np.rot90(tile_b[:,::-1],k=2)
        if((bottom_b[::-1] == bottom).all()):return id_b, np.rot90(tile_b, k=2)

        if((left_b == bottom).all()):        return id_b, np.rot90(tile_b,k=3)
        if((left_b[::-1] == bottom).all()):  return id_b, np.rot90(tile_b[::-1,:],k=3)
    return False, None

image = None
cut_image = None
image_id = None
for id, tile_t in tiles.items():
    combs = []
    combs.append(tile_t)
    combs.append(tile_t[:,::-1])
    combs.append(np.rot90(tile_t))
    combs.append(np.rot90(tile_t[:,::-1]))
    combs.append(np.rot90(tile_t,k=2))
    combs.append(np.rot90(tile_t[:,::-1],k=2))
    combs.append(np.rot90(tile_t,k=3))
    combs.append(np.rot90(tile_t[:,::-1],k=3))
    for n,tile in enumerate(combs):
        tiles_copy = tiles.copy()
        image = np.empty(shape=(image_shape,image_shape,10,10),dtype=object)
        image_id = []
        image[0,0] = tile
        image_id.append(id)
        restart = False
        next = None
        for i in range(image_shape):
            for j in range(image_shape):
                if(i == 0 and j == 0): continue
                partner = None
                if(j == 0):
                    partner, next = find_bottom_partner(image_id[(i-1)*image_shape+j], image[i-1,j], tiles_copy)
                else:
                    partner, next = find_right_partner(image_id[i*image_shape+j-1], image[i,j-1], tiles_copy)
                if(not partner):
                    restart = True
                    break
                image[i,j] = next
                image_id.append(partner)
                del tiles_copy[partner]
            if(restart):
                break
        if(not restart):
            break
    if(not restart):
        break

def remove_borders(tile):
    return tile[1:-1,1:-1]


image_id = [ int(s.split(' ')[1].replace(':','')) for s in image_id ]
result = np.array(image_id).reshape((image_shape,image_shape))
print(result[0,0]*result[0,-1]*result[-1,0]*result[-1,-1])

cut_image = np.empty(shape=(image_shape,image_shape,8,8),dtype=object)
for i in range(image_shape):
    for j in range(image_shape):
        cut_image[i,j] = image[i,j,:,:][1:-1,1:-1]
final_image = ""
for i in range(image_shape):
    for j in range(8):
        line = []
        for e in cut_image[i,:,j,:]:
            line.append(''.join([ ''.join(s) for s in e ]))
        final_image += ''.join(line) + "\n"

sea_monster = r"(?=#.{77}(#).{4}#{2}.{4}#{2}.{4}#{3}.{77}#.{2}#.{2}#.{2}#.{2}#.{2}#)"

final_image = np.array(list(final_image.replace('\n',''))).reshape((image_shape*8, image_shape*8))
combs = []
combs.append(final_image)
combs.append(final_image[:,::-1])
combs.append(np.rot90(final_image))
combs.append(np.rot90(final_image[:,::-1]))
combs.append(np.rot90(final_image,k=2))
combs.append(np.rot90(final_image[:,::-1],k=2))
combs.append(np.rot90(final_image,k=3))
combs.append(np.rot90(final_image[:,::-1],k=3))
for i,c in enumerate(combs):
    c = ''.join(c.reshape((-1,1)).squeeze())
    if(re.search(sea_monster, c)):
        print(c.count("#") - len(list(re.finditer(sea_monster, c)))*15)
