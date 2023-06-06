# Задание № 1
# Создаем ф-цию, которая читает файл с рецептами и преобразовывает в требуемый вид
def cook(file):

   with open('dishes_recipes.txt', 'r', encoding='utf-8') as dishes_recipes:

        cook_book = {}
        for dish in dishes_recipes:
            quantity_of_ingredients = int(dishes_recipes.readline())
            recipe_list = []
            for i in range(quantity_of_ingredients):
                ingredient_name, quantity, measure = dishes_recipes.readline().strip().split(' | ')
                recipe_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})

            dishes_recipes.readline()

            cook_book[dish.strip()] = recipe_list

   return cook_book

# Задание № 2
# Cоздаем функцию, вычисляющую необходимые для приобретения ингридиенты (внутри нее будем вызывать функцию cook(), возвращающую книгу рецептов cook_book)
# Обратите, пожалуйста, внимание, что в блюдо "Запеченный картофель" (в файл dishes_recipes.txt) намеренно добавлен ингредиент "Помидор",
# чтобы проверить, правильно ли программа посчитает кол-во ингридиентов, если они повторяются в блюдах
def get_shop_list_by_dishes(dishes, person_count):

    from pprint import pprint

    list_of_ing = []

    for dish in dishes:
        if dish in cook('dishes_recipes.txt').keys():
            list_of_ing.append(cook('dishes_recipes.txt')[dish])
        else:
            print(f'Ошибка: блюда "{dish}" нет в книге рецептов.\n')

    res = {}

    for el in list_of_ing:
        for el_ in el:
            el_['quantity'] = el_['quantity'] * person_count
            if el_['ingredient_name'] not in res.keys():
                res[el_['ingredient_name']] = {'measure': el_['measure'], 'quantity': el_['quantity']}
            else:
                res[el_['ingredient_name']]['quantity'] += el_['quantity']

    if res:
        pprint(res)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 2)








