
users = ['juan', 'paco', 'mat', 'dogda', 'admin']

for user in users:
    if user == 'admin':
        print(f'Bienvenido admin ¿Quieres ver un informe de estado?')
    else:
        print(f'Bienvenido {user}')

if users == []:
    print('Necesitamos usuarios')


print('\n*************************************************\n')

current_users = ['Juan', 'paco', 'mat', 'dogda', 'admin']
new_users = ['juan', 'Paco', 'lix', 'lorence', 'fagboy', 'datadog']

lower_current_users = [user_lower.lower() for user_lower in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f'El nombre {new_user} ya está en uso, porfa cambialo')
    else:
        print(f'{new_user} está disponible para su uso')


print('\n*************************************************\n')


num_list = [num for num in range(1, 10)]

for num in num_list:
    if num == num_list[0]:
        print(f'{num}: 1st')
    elif num == num_list[1]:
        print(f'{num}: 2nd')
    elif num == num_list[2]:
        print(f'{num}: 3rd')
    elif num == num_list[3]:
        print(f'{num}: 4th')
    elif num == num_list[4]:
        print(f'{num}: 5th')
    elif num == num_list[5]:
        print(f'{num}: 6th')
    elif num == num_list[6]:
        print(f'{num}: 7th')
    elif num == num_list[7]:
        print(f'{num}: 8th')
    elif num == num_list[8]:
        print(f'{num}: 9th')
