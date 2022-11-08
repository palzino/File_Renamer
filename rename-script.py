import os
s = 1
split = os.path.split(os.getcwd())
series_name = split[1]
for f in os.listdir():
    season = ("Season {0}".format(s))
    if f == season:
        x_ep = 1
        os.chdir(os.path.join(os.getcwd(), season))
        for x in os.listdir():
            file_name, file_ext = os.path.splitext(x)
            if file_ext == ".py" or file_ext ==".srt":
                continue
            else:
                ep_format = (f"S{s:02d} EP{x_ep:02d}")
                x_ep = x_ep + 1
                new_name = ('{}{}{}'.format(series_name + " ", ep_format, file_ext))
                os.rename(x, new_name)
        os.chdir(os.path.pardir)
        s = s + 1  
    else:
        continue