# Very procedural code below! Comments should make things a bit more clear.

with open("input.txt", 'r') as data:
    list_of_foods = [line.split(" (contains ") for line in data.read().replace(")", "").split("\n")]

# PART 1
ingredients = set()
for food in list_of_foods:
    ingredients.update(food[0].split(" "))

# get map of allergen -> potential foods that can contain it
allergen_map = dict()
for food in list_of_foods:
    if len(food) > 1:
        allergens = food[1].split(", ")
        for allergen in allergens:
            if allergen not in allergen_map.keys():
                allergen_map[allergen] = set(food[0].split(" "))
            else:
                allergen_map[allergen] = allergen_map[allergen].intersection(food[0].split(" "))

# using that, get ingredients there are surely without allergens
ingredients_that_might_contain_allergen = set()
for ingredient_list in allergen_map.values():
    ingredients_that_might_contain_allergen.update(ingredient_list)
ingredients_that_cannot_contain_allergen = ingredients.difference(ingredients_that_might_contain_allergen)

# check how many times those ingredients occur in the list of foods
count = 0
for food in list_of_foods:
    for ingredient in food[0].split(" "):
        if ingredient in ingredients_that_cannot_contain_allergen:
            count += 1
print(count)

# PART 2
# We now have the allergen_map from which we can deduce the ingredient -> allergen mapping.
# Find allergens with only 1 ingredient -> choose it -> remove it for other allergens -> repeat until done

final_allergen_map = dict()
new_mapping_found = True
while new_mapping_found:
    new_mapping_found = False
    for allergen, ingredients in allergen_map.items():
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            new_mapping_found = True
            final_allergen_map[ingredient] = allergen
            for other_allergen in allergen_map.keys():
                if ingredient in allergen_map[other_allergen]:
                    allergen_map[other_allergen].remove(ingredient)

# Sort the ingredients to get the result
sorted_result = sorted(final_allergen_map.keys(), key=lambda x: final_allergen_map[x])
print(",".join(sorted_result))
