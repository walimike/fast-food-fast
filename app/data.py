food_catalogue = [{"food":"matooke","price":5000}]

#returns price of food if food exists in catalogue and none in case food not found
def check_catalogue(food):
    order = [order for order in food_catalogue if order['food'] == food]
    if len(order)==1:
        return order[0]["price"]
