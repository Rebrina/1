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
#print(cook_book)      

def get_shop_list_by_dishes(dishes, person_count):
    if dishes in cook_book:
        print(cook_book[dishes])
    return()
  

com = input('')

if com == 'Омлет':
    get_shop_list_by_dishes(com, 2)


  

