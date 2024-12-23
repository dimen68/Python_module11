# Создать персональную функции для подробной интроспекции объекта
import inspect
from pprint import pprint


def introspection_info(obj):
    info_dict = {}
    info_dict['type'] = type(obj)
    attr_list = []
    metod_list = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            metod_list.append(attr)
        else:
            attr_list.append(attr)
    info_dict['attributes'] = attr_list
    info_dict['methods'] = metod_list
    info_dict['module'] = inspect.getmodule(obj)
    return info_dict


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(f'Для объекта number_info получена следующая информация:')
    pprint(number_info)
    input('Для продолжения в окне консоли нажмите клавишу ENTER')

    str_info = introspection_info('Hello!!!')
    print(f'Для объекта str_info получена следующая информация:')
    pprint(str_info)
    input('Для продолжения в окне консоли нажмите клавишу ENTER')

    def_info = introspection_info(introspection_info)
    print(f'Для объекта introspection_info получена следующая информация:')
    pprint(def_info)
    input('Для продолжения в окне консоли нажмите клавишу ENTER')

    inspect_info = introspection_info(inspect)

    print(f'Для объекта introspection_info получена следующая информация:')
    pprint(inspect_info)
    input('Для продолжения в окне консоли нажмите клавишу ENTER')

    list_info = introspection_info([42, 'Hello!!!', True])
    print(f'Для объекта list_info получена следующая информация:')
    pprint(list_info)
