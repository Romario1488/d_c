from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

result = []


def index(request):
    result.clear()
    template = loader.get_template('myapp/index.html')
    if request.POST.get('calc'):
        print('calculated')
        birth_date = request.POST.get('birthdate', False)
        print(birth_date)
        if birth_date:
            start_engine(birth_date)
    print(result)
    first_num.clear()
    second_num.clear()
    third_num.clear()
    all_numbers.clear()
    destiny_number.clear()
    character.clear()
    energy.clear()
    interest.clear()
    health.clear()
    logic.clear()
    work.clear()
    luck.clear()
    debt.clear()
    memory.clear()
    print(result)
    counter = 0
    for i in result:
        if i == '':
            result[counter] = '—'
        counter+=1

    if len(result) >= 1:
        context = {
            'character': result[0],
            'energy': result[1],
            'interest': result[2],
            'health': result[3],
            'logic': result[4],
            'work': result[5],
            'luck': result[6],
            'debt': result[7],
            'memory': result[8],
            'ustremlennost': result[9],
            'family': result[10],
            'stability': result[11],
            'temperament': result[12],
            'bit': result[13],
            'destiny_number': result[14],
            'additional_numbers': additional_numbers[0],
            'habbits': result[15],
            'birth_date': birth_date,
        }
        additional_numbers.clear()
        return render(request, 'myapp/index.html', context=context)
    else:
        return render(request, 'myapp/index.html')


first_num = []

second_num = []

third_num = []

all_numbers = []

destiny_number = []

additional_numbers = []


def start_engine(birth_date):
    birth_date = birth_date.split('.')
    main(birth_date)


def get_destiny_number(birth_date):
    for days in birth_date[0]:
        destiny_number.append(int(days))

    for months in birth_date[1]:
        destiny_number.append(int(months))

    for years in birth_date[2]:
        destiny_number.append(int(years))
    get_addtitional_numbers(destiny_number, birth_date[0])
    return sum(destiny_number)


def get_addtitional_numbers(destiny_number, birth_date: int):
    birth_date = int(birth_date)
    first_num = sum(destiny_number)
    a = (first_num // 10)
    b = (first_num % 10)
    second_num = a + b
    first_birthdate_num = int(str(abs(birth_date))[0])
    third_num = first_num - 2 * first_birthdate_num

    a = (third_num // 10)
    b = (third_num % 10)
    fourth_number = a + b
    additional_number = str(first_num) + '.' + str(second_num) + '.' + str(third_num) + '.' + str(fourth_number)
    additional_numbers.append(additional_number)


def get_first_number(birth_date):
    for days in birth_date[0]:
        first_num.append(int(days))

    for months in birth_date[1]:
        first_num.append(int(months))

    for years in birth_date[2]:
        first_num.append(int(years))

    return sum(first_num)


def get_second_number(first_number):
    second_num.append(first_number // 10)
    second_num.append(first_number % 10)
    return sum(second_num)


def get_third_number(birth_date, first_number):
    for days in birth_date[0]:
        dig = int(days) * 2
        third_number = first_number - dig
        return third_number


def get_fourth_number(third_number):
    third_num.append(third_number // 10)
    third_num.append(third_number % 10)
    return sum(third_num)


def creating_character(birth_date, first_number, second_number, third_number, fourth_number):
    for days in birth_date[0]:
        all_numbers.append(int(days))

    for months in birth_date[1]:
        all_numbers.append(int(months))

    for years in birth_date[2]:
        all_numbers.append(int(years))

    if first_number >= 10:
        all_numbers.append(first_number // 10)
        all_numbers.append(first_number % 10)
    else:
        all_numbers.append(first_number)

    if second_number >= 10:
        all_numbers.append(second_number // 10)
        all_numbers.append(second_number % 10)
    else:
        all_numbers.append(second_number)

    if third_number >= 10:
        all_numbers.append(third_number // 10)
        all_numbers.append(third_number % 10)
    else:
        all_numbers.append(third_number)

    if fourth_number >= 10:
        all_numbers.append(fourth_number // 10)
        all_numbers.append(fourth_number % 10)
    else:
        all_numbers.append(fourth_number)

    for number in all_numbers:
        if number == 1:
            character.append('1')
        elif number == 2:
            energy.append('2')
        elif number == 3:
            interest.append('3')
        elif number == 4:
            health.append('4')
        elif number == 5:
            logic.append('5')
        elif number == 6:
            work.append('6')
        elif number == 7:
            luck.append('7')
        elif number == 8:
            debt.append('8')
        elif number == 9:
            memory.append('9')

    character_value = ''.join(character)
    energy_value = ''.join(energy)
    interest_value = ''.join(interest)
    health_value = ''.join(health)
    logic_value = ''.join(logic)
    work_value = ''.join(work)
    luck_value = ''.join(luck)
    debt_value = ''.join(debt)
    memory_value = ''.join(memory)
    destiny = get_destiny_number(birth_date)
    second_number = get_second_number(first_number)
    while int(destiny) >= 10 and int(second_number) != 11:
        first_d_number = int(destiny) // 10
        second_d_number = int(destiny) % 10
        destiny = first_d_number + second_d_number
    # print(f'Внутренний квадрат: \nХарактер: {character_value}\nЭнергия: {energy_value}\nИнтерес: {interest_value}'
    #       f'\nЗдоровье: {health_value}\nЛогика: {logic_value}\nТруд: {work_value}\nУдача: {luck_value}\nДолг: {debt_value}'
    #       f'\nПамять: {memory_value}\n\nВнешний квадрат:\nЦелеустремленность:{len(character) + len(health) + len(luck)}\n'
    #       f'Семья: {len(energy) + len(logic) + len(debt)}\n'
    #       f'Стабильность: {len(interest) + len(work) + len(memory)}\nТемперамент: {len(interest) + len(logic) + len(luck)}\n'
    #       f'Быт: {len(health) + len(logic) + len(work)}\nЧисло судьбы: {destiny}')

    result.append(character_value), result.append(energy_value), result.append(interest_value), \
    result.append(health_value), result.append(logic_value), result.append(work_value), result.append(luck_value), \
    result.append(debt_value), result.append(memory_value), result.append(len(character) + len(health) + len(luck)), \
    result.append(len(energy) + len(logic) + len(debt)), \
    result.append(len(interest) + len(work) + len(memory)), \
    result.append(len(interest) + len(logic) + len(luck)), \
    result.append(len(health) + len(logic) + len(work)), \
    result.append(destiny),
    result.append(len(interest) + len(work) + len(memory))


# Результат вышестоящей функции должен быть передан в качестве контекста, обработчика шаблонов.

character = []
energy = []
interest = []
health = []
logic = []
work = []
luck = []
debt = []
memory = []


def main(birth_date):
    first_number = get_first_number(birth_date)
    second_number = get_second_number(first_number)
    third_number = get_third_number(birth_date, first_number)
    fourth_number = get_fourth_number(third_number)

    creating_character(birth_date, first_number, second_number, third_number, fourth_number)
