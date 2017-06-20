import webbrowser
import time
alarm_HH = input("Enter the hour you want to wake up at")
alarm_MM = input("Enter the minute you want to wake up at")
now = time.localtime()
print(now)
if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
	webbrowser.open("https://www.youtube.com/watch?v=FX7MSDySYkY")

