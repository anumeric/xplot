'''
Problem 1: Plot Bar
'''
# TEST CASE GENERATOR # DO NOT MODIFY # 
inputs_list = [["A", 627.2],["B", 38.9],["C", 11.3]]
inputs_dict = {"A": 627.2, "B": 38.9,"C": 11.3}

# SOLUTION

def barGraph1(inputs_list):
  max_val = max(inputs_list, key=lambda x: x[1])[1]
  for element in inputs_list:
      print(element[0],int((element[1]/max_val)*50)*"#")

# Now, with a dict ...
def barGraph2(inputs_dict):
  max_val = max(inputs_dict.items(), key=lambda x: x[1])[1]
  for key,val in inputs_dict.items():
      print(key,int((val/max_val)*50)*"#")

barGraph1(inputs_list)      
barGraph1(inputs_dict)    

    
'''
Problem 2: PlotX
'''

# TEST CASE GENERATOR # DO NOT MODIFY # 
import random
qty_points = random.randint(0,10)
scale = random.randint(1,30)
charmap = {1:"X ",0: ". "}
input_coords = [[random.uniform(0.0,100.0) for _ in range(2)] for _ in range(qty_points)]   

# SOLUTION
def printGrid(input_coords,scale,charmap):
    grid = [[charmap[0] for _ in range(scale)] for _ in range(scale)]
    if not input_coords:
      return grid
    x_max =  max(map(lambda x: x[0], input_coords))
    y_max =  max(map(lambda x: x[1], input_coords))
    new_coords=   [[int( (input_coords[i][0]/x_max)*(scale-1) ),int( (input_coords[i][1]/y_max)*(scale-1) ) ] for i in range(len(input_coords))      ]
    for i in range(0,len(new_coords)):
        grid[new_coords[i][1]][new_coords[i][0]]= charmap[1]
    for i in range(len(grid)-1,-1,-1):
        print(''.join(grid[i]))

printGrid(input_coords,scale,charmap)
