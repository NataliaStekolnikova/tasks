# Задание 2. Коллекции.
# Примечание: входные параметры ни в однй из задач не должны быть модифицированы.
# '''
from typing import Any, Dict, Iterable, List, Tuple
import copy
# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return list(args)

# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    return [arg for arg in args if isinstance(arg, int)]

# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    return [arg for arg in args if isinstance(arg, argument_type)]

# Сконструировать и вернуть список из переданных аргументов, тип которых входит в заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    return [arg for arg in args if type(arg) in set(argument_types)]

# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    return first + second

# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    result = []
    for lst in lists:
        result.extend(lst)
    return result

# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [value] * length

# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    new_list = []
    for value in values:
        if value != value_to_remove:
            new_list.append(value)
    return new_list

# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [value for value in values if value != value_to_remove]

# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x != value_to_remove, values))

# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    temp = []
    for x in values:
        if x not in set(values_to_remove):
            temp.append(x)
    return temp

# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [x for x in values if x not in set(value_to_remove)]

# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, values_to_remove: Iterable) -> List:
    return list(filter(lambda x: x not in set(values_to_remove), values))

# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    return list(set(values))

# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    return {key: value for key, value in kwargs.items() if isinstance(value, int)}

# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)

# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    result_dict = {}
    for key in values:
        result_dict[key] = copy.deepcopy(default)
    return result_dict

# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {index: value for index, value in enumerate(values)}

# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return dict(kws)

# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).
def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return dict(zip(keys, values))

# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    result = first.copy()
    result.update(second)
    return result

# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    dictionary.update(kwargs)
    return dictionary

# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    for key, value in kwargs.items():
        if key in dictionary:
            if isinstance(dictionary[key], list):
                dictionary[key].append(value)
            else:
                dictionary[key] = [dictionary[key], value]
        else:
            dictionary[key] = value
    return dictionary

# Объединить два словарь и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    merged_dict = first.copy()
    for key, value in second.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], list):
                merged_dict[key].append(value)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value
    return merged_dict

# Объединить два словарь и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    merged_dict = first.copy()
    for key, value in second.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], dict) and isinstance(value, dict):
                merged_dict[key] = deep_merge_two_dicts(merged_dict[key], value)
            elif isinstance(merged_dict[key], list) and isinstance(value, list):
                merged_dict[key].extend(value)
            elif isinstance(merged_dict[key], set) and isinstance(value, set):
                merged_dict[key].update(value)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value
    return merged_dict

# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    return list(dictionary.keys())

# Вернуть список, состоящий из значений, принадлежащих словарю.
def get_values(dictionary: Dict) -> List:
    return list(dictionary.values())

# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    return list(dictionary.items())

# Реверсировать и вернуть словарь.
def reverse_dict(dictionary: Dict) -> Dict:
    reversed_dict = {}
    for key, value in dictionary.items():
        reversed_dict[value] = key
    return reversed_dict

# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
def clear_dummy_elements(dictionary: Dict) -> Dict:
    return {key: value for key, value in dictionary.items() if value not in (None, '', [], {})}

# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    unique_items = dict()
    unique_items.update(clear_dummy_elements(dictionary))
    return unique_items

# Обменять в словаре ключи и значения
# (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    reversed_dict = dict()
    for key, value in dictionary.items():
        if isinstance(value, (bool, int, float, complex, str, tuple)):
            reversed_dict[value] = key
        else:
            reversed_dict[key] = value
    return reversed_dict

# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary):
    sorted_dict = {}
    keys = sorted(dictionary.keys())
    for key in keys:
        sorted_dict[key] = dictionary[key]
    return sorted_dict

# Вернуть словарь, отсортированный по ключу в обратном порядке.
# Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items(), key=lambda item: item[0], reverse=True))

# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
from collections import defaultdict
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    grouped_dict = defaultdict(list)
    for key, value in sorted(dictionary.items(), key=lambda x: (0 if isinstance(x[0], int) else 1 if isinstance(x[0], float) else 2)):
        grouped_dict[type(key).__name__].append((key, value))
    for key in grouped_dict:
        grouped_dict[key].sort(key=lambda x: x[0], reverse=True)
    return grouped_dict

# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> int:
    num_count = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)) and -10 <= value <= 25:
            num_count += 1
    return num_count

# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    result_dict = {}
    for index, key in enumerate(keys):
        if index < len(values):
            value = values[index]
        else:
            value = None
        result_dict[key] = value
    return result_dict

# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    result_dict = {}
    for key, value in zip(keys, copy.copy(values)):
        result_dict[key] = value
    return result_dict

# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    result_dict = {}
    for key in keys:
        value = next(values, None)
        result_dict[key] = value
    return result_dict
