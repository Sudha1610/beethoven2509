from product_manager import create_product,  read_all, read_by_id
from product_manager import  update, delete_by_id
from product import Product


def menu():

    message = '''
1- create product
2- read all products
3- read by id
4- update
5- delete 
6- exit / logout 
'''
    choice = int(input(message))
    if choice == 1:
        Name = input('name:')
        description = input('description:')
        category = input('category:')
        tags = input('tags:')
        stock = int(input('stock:'))
        price = int(input('price:'))
        id = -1

        product = Product(id,Name,description,category,tags,stock,price)
        
        create_product(product)
        print("product created sucessfully..")

    elif choice == 2:
        products = read_all()    
        print('products:')
        for product in products:
            print(product)

    elif choice == 3:
        id = int(input('id:'))
        product = read_by_id(id)
        if product == None:
            print('products not found')
        else:
            print(product)


    elif choice == 4:
        id = int(input('id:'))
        old_product = read_by_id(id)
        if old_product == None:
            print('product not found.')
        else:
            print(old_product)
        #name = input(f'name({old_product.name}):')
        Name = input('name:')
        description = input('description:')
        category = input('category:')
        tags = input('tags:')
        stock = int(input('stock:'))
        price = int(input('price:'))

        new_product = Product(id, Name, description,category, tags, stock, price)
        update(new_product)
        print("product updated sucessfully.")


        

    elif choice == 5:
        id = int(input('id:'))
        old_product = read_by_id(id)
        if old_product == None:
            print('product not found.')
        else:
            print('old_product')
            if input('are you sure to delete(y/n)?') == 'y':
                delete_by_id(id)
                print('product deleted sucessfully')
    return choice

    

def menus():
    print('products management app')
    choice = menu()
    while choice != 6:
        choice = menu()
    print('thank you for using app')
menus()












