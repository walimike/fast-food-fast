"""
The models file provides aids the designing process for our API
"""


class OrderList(object):
    """A class for managing the order list for orders made"""

    order_list = []

    def __init__(self):
        pass

    def add_order(self, order,price):
        """This function is for adding orders to orderlist"""
        self.id = self.id_manager(OrderList.order_list)
        self.order = order
        self.price = price
        self.status = "No"
        new_order = self.asdict(self.id,self.order,self.price,self.status)
        OrderList.order_list.append(new_order)

    def asdict(self, id, order, price,status):
        """This function creates a dictionary for data to be added to list"""
        return {'orderid':id,'order':order,'price':price, 'completed_status':status}

    def id_manager(self,list):
        """This function prevents replication of IDs"""
        if len(list)==0:
            self.id = 1
        else:
            self.id = (list[-1]['orderid']) + 1
        return self.id

    def update_order(self,id,status):
        """This function is used to update the status of an order as yes/no"""
        order = [order for order in OrderList.order_list if order['orderid']== id]
        order[0]['completed_status'] = status.title()
        
    def id_limit(self):
        """This function checks for the ID limit to prevent user input from going beyond"""
        if OrderList.order_list == []:
            return 0
        return OrderList.order_list[-1]['orderid']

    def retrieve_order(self,id):
        """This function retrieves orders for the user"""
        order = [order for order in OrderList.order_list if order['orderid'] == id]
        if len(order)==1:
            return order[0]

