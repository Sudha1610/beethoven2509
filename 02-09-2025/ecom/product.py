#id, name, description, category, tags, stock, price
class Product:
    def __init__ (self,id,name,description, category, tags, stock, price):
        self.id =id 
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price
    def __str__(self):
        return f'[id={self.id}, name={self.name}, description={self.description}, category={self.category}, tags={self.tags}, stock={self.stock}, price={self.price}]'
    def __repr__(self):
        return self.__str__()
"""
mobile_vivo = product(1001,'vivo y12', 'good camera quality and bad call quality.', 'mobile', 'mobile,electronics smart phone',10, 25000 )
print(mobile_vivo)

mobile_oppo = product(id =1003, name='oppo y25',description= 'good camera quality.', category='mobile', tags='mobile,electronics smart phone',stock=10, price= 250000 )
print(mobile_oppo)
"""
    



