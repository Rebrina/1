i = 0
cook_book = {}
cook_book2 = {}
with open('cookbook.txt') as f:  
  for line in f:   
      recipe_id = line.strip()
      i = int(f.readline())      
      cook_book[recipe_id] = list()       
      while i > 0:
          ingridients = f.readline().strip()                  
          ingridients_list = ingridients.split(' | ')          
          cook_book2 = {'ingridient_name': ingridients_list[0], 'quantity':ingridients_list[1], 'measure':ingridients_list[2]}              
          cook_book[recipe_id].append(cook_book2)    
          i -= 1   
      f.readline()
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    total_ingrigients = {}
    i = 0
    while i < len(cook_book):
        dish = dishes[i]
        print(dish)
        j = 0
        if dish in cook_book:
            while j < len(cook_book[dish]):
                new_key = cook_book[dish][j]['ingridient_name']
                print(new_key)
                if new_key in total_ingrigients:
                    total_ingrigients[new_key]['quantity'] = total_ingrigients[new_key]['quantity'] + int(
                        cook_book[dish][j]['quantity']) * person_count
                else:
                    total_ingrigients[new_key] = {'measure': cook_book[dish][j]['measure'],
                                                  'quantity': int(cook_book[dish][j]['quantity']) * person_count}
                j += 1
        i += 1
        print(i)
    print(total_ingrigients)
    return (total_ingrigients)


# задание2
print('#########################')
dishes = []
a = ''
cook_book2 = cook_book
for keys in cook_book2:
    a = keys
    # a = cook_book2.pop(keys)
    dishes.append(a)

print(dishes)

person_count = int(input('Введите кол-во персон'))

get_shop_list_by_dishes(dishes, person_count)

