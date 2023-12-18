"""
Use Pick's and Shoelace

Shoelace gives you Area of shape
Pick's: Area of shape = # of lattice points inside + 1/2 of points on boundary - 1
Rearrange to get: Area of shape + 1 + 1/2 of points on boundary = # of lattice points in and on boundary

"""

steps = []

with open("input.txt") as fhand:
    for line in fhand:
        line = line.strip()
        dir, dis, colour = tuple(line.split(" "))
        colour = colour[1:-1]
        steps.append((dir, int(dis), colour))

def polygonArea(vertices):
  #A function to apply the Shoelace algorithm
  numberOfVertices = len(vertices)
  sum1 = 0
  sum2 = 0
  
  for i in range(0,numberOfVertices-1):
    sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
    sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
  
  #Add xn.y1
  sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
  #Add x1.yn
  sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   
  
  area = abs(sum1 - sum2) / 2
  return area
  
vertices = []
DIRS = {"R": (0,1), "L": (0,-1), "U": (-1,0), "D": (1,0)}
current = [0,0]
part_one_perim = 0

# every step creates a new vertex
for step in steps:
   dir, dis, colour = step
   dir = DIRS[dir]
   current[0] += (dir[0] * dis)
   current[1] += (dir[1] * dis)
   part_one_perim += dis
   new_current = [x for x in current]
   vertices.append(new_current)

part_two_vertices = []
current = [0,0]
part_two_perim = 0
DIRS = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}

for step in steps:
   dir, dis, colour = step
   dis = int(colour[1:6], 16)
   dir = DIRS[int(colour[-1])]

   current[0] += (dir[0] * dis)
   current[1] += (dir[1] * dis)
   part_two_perim += dis
   new_current = [x for x in current]
   part_two_vertices.append(new_current)

def part_one():
    print(polygonArea(vertices=vertices) + (part_one_perim / 2) + 1)

def part_two():
    print(polygonArea(vertices=part_two_vertices) + (part_two_perim / 2) + 1)

part_one()
part_two()
      
