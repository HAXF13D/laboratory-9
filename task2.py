#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    some_dict = {
        1: "abc",
        2: "home",
        3: "test",
        4: "task"
    }
    print(f"Словарь до изменений:\n{some_dict}")
    dict_items = some_dict.items()
    changed_dict = {i: j for j, i in dict_items}
    print(f"Словарь после изменений:\n{changed_dict}")
