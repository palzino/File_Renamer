import os
while True:
    selection = input("input 1 to run the program and 2 to quit")
    if selection == "1":
        series_name = input("Input the name of the series")
        season_number = input("input season number")
        f_ep = 1
        mylist = []
        working_dir = input("input directory")
        for f in os.listdir():
            file_name, file_ext = os.path.splitext(f)
            if file_ext == ".py":
                continue
            else:
                ep_format = (f"S{season_number}ep{f_ep}")
                f_ep = f_ep + 1
                new_name = ('{}{}{}'.format(series_name + " ", ep_format, file_ext))
                os.rename(f, new_name)
    elif selection == "2":
        break
    else:
        print("enter a valid response")
            
       
