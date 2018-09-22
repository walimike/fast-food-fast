
class OrderList(object):
    """A class for managing orders made"""

    order_list = []

    def __init__(self):
        pass

    def add_order(self, order,price):
        self.id = self.id_manager(OrderList.order_list)
        self.order = order
        self.price = price
        self.status = "No"
        new_order = self.asdict(self.id,self.order,self.price,self.status)

        """This loop prevents replication of orders"""
        if not len(OrderList.order_list) == 0 and OrderList.order_list[-1]["order"] == self.order:
            return
        OrderList.order_list.append(new_order)

    def asdict(self, id, order, price,status):
        return {'orderid':id,'order':order,'price':price, 'completed_status':status}

    def asdict(self, id, order, price):
        return {'orderid':id,'order':order,'price':price}

    def id_manager(self,list):
        if len(list)==0:
            self.id = 1
        else:
            self.id = (list[-1]['orderid']) + 1
        return self.id

    def update_order(self,id,status):
        order = [order for order in OrderList.order_list if order['orderid']== id]
        order[0]['completed_status'] = status.title()
        
    def id_limit(self):
        return OrderList.order_list[-1]['orderid']

    def retrieve_order(self,id):
        order = [order for order in OrderList.order_list if order['orderid'] == id]
        if len(order)==1:
            return order[0]
