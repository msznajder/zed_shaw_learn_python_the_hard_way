zoo_relations = {
"antelope": ["grass"],
"big-fish": ["little-fish"],
"bug": ["leaves"],
"bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
"chicken": ["bug"],
"cow": ["grass"],
"fox": ["chicken", "sheep"],
"giraffe": ["leaves"],
"lion": ["antelope", "cow"],
"panda": ["leaves"],
"sheep": ["grass"],
}

def who_eats_who(zoo):
    animals = zoo.split(",")
    idx = 0
    res = [zoo] # !!!
    
    while True:
        if len(animals) == 1 or idx >= len(animals):
            res.append(",".join(animals))
            break

        if idx-1 >= 0 and animals[idx-1] in zoo_relations.get(animals[idx], []):
            res.append("{} eats {}".format(animals[idx], animals[idx-1]))
            del animals[idx-1]
            idx = 0
        elif idx+1 < len(animals) and animals[idx+1] in zoo_relations.get(animals[idx], []):
            res.append("{} eats {}".format(animals[idx], animals[idx+1]))
            del animals[idx+1]
            idx = 0
        else:
            idx += 1

    return res

# print(who_eats_who("chicken,fox,leaves,bug,grass,sheep"))
# print(who_eats_who("fox,bug,chicken,grass,sheep"))
print(who_eats_who("fox,chicken,tree,chicken,bug,banana,bug,bear"))



# ["fox,bug,chicken,grass,sheep", 
#             "chicken eats bug", 
#             "fox eats chicken", 
#             "sheep eats grass", 
#             "fox eats sheep", 
#             "fox"]