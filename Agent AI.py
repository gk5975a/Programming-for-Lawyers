import os

counter = 0
while counter < 10: 
  with open(" contract.txt", "w") as f:
    f.write(f" a shortmemo {counter})
            
counter = counter + 1

filenames = os.listdir(".")

counter= 0
for filename in filenames:
 counter = counter + 1

 Print (counter)

 number_of_files = len(filenames)
 print(number_of_files)
