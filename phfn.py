try:
	from prettytable import PrettyTable
	from os import system, name
except ImportError:
	print('Подождите устанавливаем библиотеки')
	import pip
	pip.main(['install', '--user', 'prettytable', 'os'])

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

info_table = PrettyTable()

op = 'None'
country = 'Украина'
#            киевстар[0]                       водафон[1]                  лайфселл[2]       интертелеком[3]  3mob[4]  пиплнет[5]    городские[6] 																																																					Платный номер[7]	
op_list = [['068','067','096','097','098'], ['050','066','095','099'], ['063','093','073'], ['094','089'],   ['091'],  ['092'],     ['031', '032', '033', '034', '035', '036', '037', '038', '041', '042', '043', '044', '045', '046', '047', '048', '049', '051', '052', '053', '054', '055', '056', '057', '058', '059', '061', '062', '064', '065', '069'], ['070','080','090'] ]
clear()
phone = '+380684537720'

while True:
	#phone = input(colors.OKCYAN+colors.BOLD +f'Привет это распознатель кодов операторов напиши свой номер: '+colors.ENDC)
	if phone[0:1]!='+':
		clear()
		print(colors.FAIL+colors.BOLD+'Введите правильный номер например (+380195863364)'+colors.ENDC)
	elif phone[0:2]=='+7':
		clear()
		pass
		print('Hohoho. . . No')
	elif len(phone)<13:
		print(colors.FAIL+colors.BOLD+'Введите номер правильной длины'+colors.ENDC)
	else:
		if phone[3:6] in op_list[0]:
			op = 'КиевСтар'
		elif phone[3:6] in op_list[1]:
			op = 'ВодаФон'
		elif phone[3:6] in op_list[2]:
			op = 'ЛайфСелл'
		elif phone[3:6] in op_list[3]:
			op = 'ИнтерТелеком'
		elif phone[3:6] in op_list[4]:
			op = '3mob'
		elif phone[3:6] in op_list[5]:
			op = 'ПиплНет'
		elif phone[3:6] in op_list[6]:  
			op = 'Городской Номер'
		elif phone[3:6] in op_list[7]:
			op = 'Платные Номера если позвонить спишуться деньги!'



		print(op[0:3])
		info_table.field_names = [colors.HEADER+colors.BOLD+'Информация'+colors.ENDC]
		if op[0:3]=='Пла':
			info_table.add_row([f'{op}'])
		else:
			info_table.add_row([f'Оператор: {op}'])
		info_table.add_row([f'Страна: {country}'])

		print(f'''
{info_table}

		''')
		break