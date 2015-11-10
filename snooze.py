import subprocess
from crontab import CronTab

users_cron = CronTab(user='pi')
iter = users_cron.find_command('sudo python /home/pi/alarmpi/sound_the_alarm.py')
#disable the alarm
for job in iter:
	if job.is_enabled():
		job.enable(False)
	else:
		job.enable(True)
		subprocess.call('sudo python sound_the_alarm.py', shell=True)
users_cron.write()
