def remove_dups(ilist):
    removed = []
    for item in ilist:
        if item not in removed:
            removed.append(item)
    return removed


with open("input.txt") as file:
    responses = file.read().split("\n\n")

responses = [response.replace("\n", "") for response in responses]

responses = ["".join(remove_dups(response)) for response in responses]

print(len("".join(responses)))
