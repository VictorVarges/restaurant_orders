class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = []
        self.costs = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if not self.costs[ingredient]:
                return False
            self.costs[ingredient] -= 1
        self.inventory.append([customer, order, day])

    def get_quantities_to_buy(self):
        list_quantity = dict()
        for item in self.MINIMUM_INVENTORY:
            list_quantity.update({item: 0})
        list_products_to_buy = list_quantity
        for orders in self.inventory:
            products = orders[1]
            for item in self.INGREDIENTS[products]:
                list_products_to_buy[item] += 1

        return list_products_to_buy

    def get_available_dishes(self):
        result_dishes = set()
        for dish in self.INGREDIENTS:
            if self.costs[self.INGREDIENTS[dish][0]] > 1:
                result_dishes.add(dish)
        return result_dishes
