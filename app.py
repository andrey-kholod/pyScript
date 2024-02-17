import os

count = int(input('Как сильно вы хотите нагрузить пеку?\n(Не более 25) ---> '))



with open('./virus.py', 'w') as f:
    command = ''

    if os.name == 'posix':
        for i in range(count):
            command += 'gnome-terminal\n'
    elif os.name == 'nt':
        for i in range(count):
            command += 'start cmd\n'

    f.write(f"""
import os
            
os.system('''{command}''')            
""")

os.system('python virus.py')
print(f'Ваша платформа {os.name} была нагружена {count} раз.')

os.system('rm app.py')
