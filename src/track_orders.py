from src.analyze_log import (
    never_ordered_by_person,
    days_never_visited
)


from collections import Counter

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        order = dict()
        for client, request, _ in self.orders:
            if client == customer:
                if request not in order:
                    order[request] = 0
                order[request] += 1
        return max(order, key=order.get)

    def get_never_ordered_per_customer(self, customer):
        return never_ordered_by_person(self.orders, customer)

    def get_days_never_visited_per_customer(self, customer):
        return days_never_visited(self.orders, customer)

    def get_busiest_day(self):
        list_days = list()
        for order in self.orders:
            list_days.append(order[2])
        return max(set(list_days), key=list_days.count)

    def get_least_busy_day(self):
        pass
