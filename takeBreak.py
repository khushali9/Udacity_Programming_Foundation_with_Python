#project to open browser and play video
import webbrowser
import time

total_breaks=4
break_count=0
print("This Program started on"+time.ctime())
while(break_count<total_breaks):
    time.sleep(10)#sec
    webbrowser.open("https://www.youtube.com/watch?v=NobzfIebbrE")
    break_count=break_count+1