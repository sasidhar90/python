import webbrowser
import time

total_break=4
break_count=0
print("this program started on "+time.ctime())
while(break_count<total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=nPXfsewcPO8");
    break_count=break_count+1
