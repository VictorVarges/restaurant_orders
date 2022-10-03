import csv
import os


def popular_food_by_person(data, name):
    customer_request = {}
    for request in data:
        if request[0] == name and request[1] not in customer_request:
            customer_request[request[1]] = 1
        elif request[0] == name and request[1] in customer_request:
            customer_request[request[1]] += 1
    return customer_request


def never_ordered_by_person(data, name):
    requests = set()
    for request in data:
        requests.add(request[1])
    requested_foods = popular_food_by_person(data, name)
    return requests.difference(requested_foods)


def days_never_visited(data, name):
    days = set()
    never_days = set()
    for request in data:
        days.add(request[2])
        if request[0] == name:
            never_days.add(request[2])
    return (days.difference(never_days))


def analyze_log(path_to_file):
    if ".csv" not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    with open(path_to_file, mode="r") as file:
        content = list(csv.reader(file))

        orders_maria = popular_food_by_person(content, "maria")
        more_orders_maria = max(orders_maria, key=orders_maria.get)

        orders_arnaldo = popular_food_by_person(content, "arnaldo")
        hamburguer_arnaldo = orders_arnaldo["hamburguer"]

        foods_never_ordered_by_joao = never_ordered_by_person(
            content, "joao"
        )
        days_never_visited_by_joao = days_never_visited(
            content, "joao"
        )

    with open("data/mkt_campaign.txt", mode="w") as file:
        answers = [
            f"{more_orders_maria}\n",
            f"{hamburguer_arnaldo}\n",
            f"{foods_never_ordered_by_joao}\n",
            f"{days_never_visited_by_joao}\n",
        ]
        for line in answers:
            file.writelines(line)