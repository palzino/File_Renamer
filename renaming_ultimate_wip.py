import os

x = 1
working_dir = os.getcwd()
split = os.path.split(working_dir)
print(split[0], "break",split[1])
season = (f"Season {x}")
for f in os.listdir():
    if f == season:
        f_ep = 1
        os.chdir(os.path.join(working_dir, season))
        for x in os.listdir():
            print(x)
            
        x = + 1
    else:
        print("not here")