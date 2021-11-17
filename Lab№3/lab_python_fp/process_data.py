import json
import sys
# Сделаем другие необходимые импорты
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1

path = "D:\P1\RIP\Lab№3\lab_python_fp\data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    wait = input("PRESS ENTER TO CONTINUE.")
    return sorted([unique_prof for unique_prof in Unique([prof for prof in field(arg, 'job-name')], ignore_case=True)])


@print_result
def f2(arg):
    wait = input("PRESS ENTER TO CONTINUE.")
    return list(filter(lambda x: x.startswith('Программист'), arg))


@print_result
def f3(arg):
    wait = input("PRESS ENTER TO CONTINUE.")
    return list(map(lambda x: x + " c опытом Python", arg))


@print_result
def f4(arg):
    wait = input("PRESS ENTER TO CONTINUE.")
    return [f"{prof}, зарплата {salary} руб." for prof, salary in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
wait = input("PRESS ENTER TO CONTINUE.")