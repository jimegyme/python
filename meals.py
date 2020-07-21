ingredients = []

#Takes in user input#
ingredients = [item for item in input("Enter the list items : ").split()]

print(ingredients)
#Converts ingredients to all lower case#
for i in range(len(ingredients)):
    ingredients[i] = ingredients[i].lower()


amount = len(ingredients)


recipe1 = ["salt","pepper","cheese"]
recipe2 = ["salt","pepper"]
Recipebook = [("Sandwich","salt", "pepper","cheese"),("Spice Mix","salt","pepper"),('yellow', 3), ('blue', 4), ('red', 1)]
print (Recipebook[1][1])
#availablerecipes = []
print (len(Recipebook[0]))
for i in range(len(ingredients)):
    for q in range(len(Recipebook)):
        for w in range(1,len(Recipebook[q])):
            if ingredients[i] == Recipebook[q][w]:
                print("Ingredient", i+1,ingredients[i] , "matches with recipe", q+1,Recipebook[q][0])
