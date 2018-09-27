"""
This contains a list of the food on the food catalogue that serves two purposes;
1. A user can only order for food that is here.
2. It provides matching for the unit price of each food item.
"""

food_catalogue = [{"food":"matooke","price":5000},
                  {"food":"posho","price":2500},
                  {"food":"rice","price":3000}
]
def check_catalogue(food):
    """This function returns price of food if food exists in catalogue and none in case food 
    not found"""
    order = [order for order in food_catalogue if order['food'] == food]
    if len(order)==1:
        return order[0]["price"]
