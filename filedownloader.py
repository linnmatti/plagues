import webbrowser
import time
fn = 'C:/Users/linn_/Dropbox/Locusts/Data/Raw DHS/url_list.txt'
f = open(fn, "r")
for item in f:
    print(item)
    webbrowser.open(item)
    time.sleep(25)
print('Done')


exit(0)