#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# variant 6

import sys
from datetime import datetime


if __name__ == '__main__':
    trains = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            destination = input("Название пункта назначения? ")
            number = int(input("Номер поезда? "))
            time = input("Время отправления ЧЧ:ММ? ")
            time = datetime.strptime(time, '%H:%M')
            train = {
                'destination': destination,
                'number': number,
                'time': time,
            }
            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 28,
                '-' * 14,
                '-' * 19
            )
            print(line)
            print(
                '| {:^4} | {:^28} | {:^14} | {:^19} |'.format(
                    "No",
                    "Название пункта назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)
            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<28} | {:<14} | {:>19} |'.format(
                        idx,
                        train.get('destination', ''),
                        train.get('number', ''),
                        train.get('time', 0).strftime("%H:%M")
                    )
                )
            print(line)

        elif command.startswith('select '):
            count = 0
            parts = command.split(' ', maxsplit=1)
            time = datetime.strptime(parts[1], '%H:%M')
            for train in trains:
                if train.get("time") > time:
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(
                            count,
                            train.get('destination', ''),
                            train.get("number")
                        )
                    )
            if count == 0:
                print("Отправлений позже этого времени нет.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить отправление;")
            print("list - вывести список отправлений;")
            print("select <ЧЧ:ММ> - вывод на экран информации о "
                  "поездах, отправляющихся после этого времени;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
