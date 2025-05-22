from pprint import pprint


def read_recipes(file_name):
    cook_book = {}
    with open(file_name, encoding="utf-8") as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient = file.readline().strip().split(" | ")
                ingredients.append(
                    {
                        "ingredient_name": ingredient[0],
                        "quantity": int(ingredient[1]),
                        "measure": ingredient[2],
                    }
                )
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book


def print_cook_book(cook_book):
    for dish, ingredients in cook_book.items():
        print(dish)
        for ingredient in ingredients:
            print(
                f"  {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}"
            )


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] in shop_list:
                    shop_list[ingredient["ingredient_name"]]["quantity"] += (
                        ingredient["quantity"] * person_count
                    )
                else:
                    shop_list[ingredient["ingredient_name"]] = {
                        "measure": ingredient["measure"],
                        "quantity": ingredient["quantity"] * person_count,
                    }
    return shop_list


cook_book = read_recipes("recipes.txt")
print_cook_book(cook_book)
shop_list = get_shop_list_by_dishes(["Запеченный картофель", "Омлет", "Фахитос"], 3)
print()
pprint(shop_list)
