import os
s = 1
series_name = os.path.split(os.getcwd())[1]
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
                os.rename = (x, '{}{}{}'.format(series_name + " ", ep_format, file_ext))
        os.chdir(os.path.pardir)
        s = s + 1
