from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint



def make_data(day: datetime):
    first_day = day + timedelta(days=(7 - day.weekday()))
    return first_day
    

def transform_str_to_data(text: str):
    date_from_text = datetime.strptime(text, '%d.%m.%Y')
    return date_from_text.replace(year=datetime.now().year).date()


def birthday_func (_list: list):
    birthday_list = defaultdict(list)
    today = datetime.now()
    first_day = make_data(today).date() - timedelta(days=2)
    last_day = first_day + timedelta(days=6)
    happy_list = [man for man in _list if first_day <=
                  transform_str_to_data(man['birthday']) <= last_day]
    
    for man in happy_list:
        birthday = transform_str_to_data(man['birthday'])
        if birthday.weekday() in (5,6):
            birthday_list['Monday'].append(man['name'])
        else:
            birthday_list[birthday.strftime('%A')].append(man['name'])

    print(f'Start period = {first_day}, end period = {last_day}')
    return birthday_list


if __name__ == '__main__':

    users = [{'name': 'Stepfan Bendera', 'birthday': '26.03.1956'},
             {'name': 'Taras Shevchenko', 'birthday': '25.03.1816'},
             {'name': 'Volodymyr Zelensky', 'birthday': '30.03.1979'},
             {'name': 'Volodymyr Dunkin', 'birthday': '31.03.1985'}]



    pprint(birthday_func(users))
