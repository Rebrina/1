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
    if dishes in cook_book:
        i = 0
        while i <= len(cook_book):
            for dishes, i in cook_book.items():
                new_key = cook_book[dishes][i]['ingridient_name']
                print(new_key)
                quantuty_for_all = int(cook_book[dishes][i]['quantity']) * person_count
                total_ingrigients[new_key] = {'measure': cook_book[dishes][i]['measure'],
                                              'quantity': int(cook_book[dishes][i]['quantity']) * person_count}
                i += 1
                # total_ingrigients[new_key] = list()
        # temp = {'measure': cook_book[dishes][0]['measure'], 'quantity': cook_book[dishes][0]['quantity']*person_count}
        # total_ingrigients[new_key].append(temp)
        print(total_ingrigients)
    return (total_ingrigients)


com = input('Введите блюдо')
com2 = int(input('Введите количество персон'))

if com and com2:
    get_shop_list_by_dishes(com, com2)

  

