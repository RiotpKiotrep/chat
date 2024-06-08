import subprocess as sub

p=sub.Popen(('sudo','tcpdump','port','8000','-i','lo','-l','-v'), stdout=sub.PIPE)
for row in iter(p.stdout.readline, b''):
    print(row.rstrip().decode())