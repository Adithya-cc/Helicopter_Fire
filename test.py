import subprocess

cmd = 'python logsys.py'
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
print(err)
print(out)