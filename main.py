
def file_open():
    i = 0
    cook_book = {}
    with open('cookbook.txt', encoding="utf-8") as f:
      for line in f:
          recipe_id = line.strip()
          i = int(f.readline())
          cook_book[recipe_id] = list()
          while i > 0:
              ingridients = f.readline().strip()
              ingridients_list = ingridients.split(' | ')
              cook_book[recipe_id].append({'ingridient_name':ingridients_list[0], 'quantity':ingridients_list[1], 'measure':ingridients_list[2]})
              i -= 1
          f.readline()
    return(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    total_ingrigients = {}
    i = 0
    cook_book2 = file_open()
    while i < len(dishes):
        dish = dishes[i]
        print(dish)
        j = 0
        if dish in cook_book2:
            while j < len(cook_book2[dish]):
                new_key = cook_book2[dish][j]['ingridient_name']
                print(new_key)
                if new_key in total_ingrigients:
                    total_ingrigients[new_key]['quantity'] = total_ingrigients[new_key]['quantity'] + int(cook_book2[dish][j]['quantity']) * person_count
                else:
                    total_ingrigients[new_key] = {'measure': cook_book2[dish][j]['measure'], 'quantity': int(cook_book2[dish][j]['quantity']) * person_count}
                j += 1
        i += 1
        print(i)
    print(total_ingrigients)
    return (total_ingrigients)

#Задание 1
print(file_open())

# задание2
d_list = input('Введите список блюд через запятую', )

dishes = d_list.split(', ')

person_count = int(input('Введите кол-во персон'))

get_shop_list_by_dishes(dishes, person_count)

