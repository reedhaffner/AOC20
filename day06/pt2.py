def remove_dups(ilist):
    removed = []
    for item in ilist:
        if item not in removed:
            removed.append(item)
    return removed


everyone_count = 0

with open("input.txt") as file:
    responses = file.read().split("\n\n")

for response in responses:
    individuals = response.split("\n")
    everyone_count += len(list(set(individuals[0]).intersection(*individuals)))

print(everyone_count)
