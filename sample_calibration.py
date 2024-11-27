from sense_hat import SenseHat
import subprocess

sense = SenseHat()

temp = round(sense.get_temperature(),2)
cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell= True)
cpu_temp = cpu_temp.decode("utf-8")
cpu_temp = float(cpu_temp.split('=')[1].split("'")[0])

updated_temp = round(temp - ((cpu_temp - temp)/1.051),1)
print(cpu_temp)
print(temp)
print(updated_temp)