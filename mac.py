import subprocess
import re

global choice
choice = 0

def cmd(name):
	subprocess.run(name,shell=True, check=True)

def showmenu():
	print("\n")
	print("\t\t1. Показать ваш действующий MAC адрес")
	print("\t\t2. Сменить на рандомный")
	print("\t\t3. Сменить на конкретный адрес")
	print("\t\t4. Выйти")

def is_valid_mac(str):

	regex = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

	p = re.compile(regex)

	if(str == None):
		return False

	if(re.search(p, str)):
		return True
	else:
		return False

cmd("clear")
wl = input("Введите название сетевого интерфейса, MAC адрес,\nкоторого хотите изменить: ")

try:
	cmd("clear")
	cmd("sudo ifconfig "+wl+" down")

	while choice != 4: 
		if choice == 1:
			cmd("sudo macchanger -s "+wl)
		elif choice == 2:
			cmd("sudo macchanger -r "+wl)
		elif choice == 3:
			mac = input('Введите МАС адрес на который хотите сменить: ')
			if is_valid_mac(str(mac)):
				cmd("sudo ifconfig "+wl+" down")
				cmd("sudo macchanger -m "+mac+" "+wl)
				
			else:
				print("Вы ввели не валидный МАC адрес. Он должен соответствовать\n шаблону 00:00:00:00:00:00")
		else:
			print("Введите правильную цифру")

		showmenu()
		choice = int(input("\n\nВыберите опцию: "))

		cmd("clear")
		
	cmd("sudo ifconfig "+wl+" up")


except:
	print("\nMAC адрес не найден")



