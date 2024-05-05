import numpy as np
import csv
found=False
atom=input("Enter the name of the atom out of 118 element:")
with open('elements1.txt', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    data_array = np.array(data)
    for x in data_array:
     
            if atom.strip().lower()==x[0].lower():
                print(f"Element name is {x[0]}, Atomic Number is {x[1]} and Atomic Symbol is {x[2]}")
                found=True
                break
if found==False:
    print(f"Element {atom} not found in periodic Table") 
