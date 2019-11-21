import time
import sys
import random
import os
import webbrowser


def set_alarm():
	
	
	#If less than 3 arguments (argv[0] is the name of the script), do not run script
	if len(sys.argv) < 4:
		print ("No arguments given or invalid format. Please enter a time. Format is HH MM SS (24hr). Example: alarm.py 19 30 00")
		print ("Current time is ", time.strftime("%H:%M:%S"))
		exit()
	
	#else convert the arguments into a single string that we can use to compare later
	else:
		alarm_hour = sys.argv[1]
		alarm_minute = sys.argv[2]
		alarm_second = sys.argv[3]
		alarm_time = "%s:%s:%s" % (alarm_hour, alarm_minute, alarm_second)
		print ("Alarm set for %s." % (alarm_time))
		
	
		#Set current_time to the current system time in the same format as the user provided time	
		current_time = time.strftime("%H:%M:%S")
		print ("Current time is %s." % (current_time))
		
	#infinite loop for alarm to keep going	
	while 1 == 1:
		#while it isn't time for alarm to go off, wait 1 second and check time again
		while current_time != alarm_time:
			time.sleep(1)
			current_time = time.strftime("%H:%M:%S")
		else:
			#open web browser window for youtube
			#call get_url function to pull video from txt file
			url = get_url()
			print (url)
			webbrowser.register('chrome', None)
			webbrowser.open(url)
			time.sleep(1)
			current_time = time.strftime("%H:%M:%S")
			
			
	else:
		exit()
			
		
#pulls a youtube URL from Videos.txt at random		
def get_url():
	f = open("Videos.txt", 'r')
	songs = []
	#add songs in list to songs[]
	for line in f:
		songs.append(line)
	#pick a random song and store it in song variable	
	song = songs[random.randint(0, len(songs) - 1)]
	f.close()
	#return URL of random song
	return song
	
set_alarm()