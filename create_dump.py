import subprocess

username = 'Andres'
password = 'andres'
database = 'biobio_test'

with open('biobio_test_dump.sql','w') as output:
    c = subprocess.Popen(['mysqldump', '-u',username,'-p%s'%password,database],stdout=output, shell=True)