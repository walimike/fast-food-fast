
class OrderList(object):
    """A class for managing orders made"""

    order_list = []

    def __init__(self):
        pass

    def add_order(self, order):
        self.id = self.id_manager(OrderList.order_list)
        self.order = order
        self.price = price
        new_order = self.asdict(self.id,self.order,self.price)
        OrderList.order_list.append(new_order)

    def asdict(self, id, order, price):
        return {'orderid':id,'order':order,'price':price}

    def id_manager(self,list):
        if len(list)==0:
            self.id = 1
        else:
            self.id = (list[-1]['orderid']) + 1
        return self.id

    def update_order(order,id):
        pass

    def valid_order(self,order):
        pass

    def retrieve_order(self,id):
        pass
