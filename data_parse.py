import json

#load in dataset
with open('data/recipes_raw_nosource_ar.json') as f:
    data = json.load(f)

keys = list(data.keys())


def extract_ingredients(ingredients):
    """
    INPUT: ingredients
            -raw ingredient list from a recipe
           units
           -list of words used as units (ie. cup,teaspon,etc)
    OUTPUT: ingredients_cleaned
            -list of only ingredient names
    takes in a raw list of ingredients and returns a list
    of only ingredient names (skipping quantities/units)
    """
    units = [' cup',' teaspoon',' tablespoon',' pinch',' ounce',' pound',' can',' package',' slices',' jar','drop','dash','dashes']
    ingredients_cleaned = []
    for ingredient in ingredients:
        #get rid of ADVERTISEMENT strings
        ingredient = ingredient.replace("ADVERTISEMENT",'')
        #some ingredients have descriptions or instructions after a comma or in ()
        #we want to get rid of these
        if len(ingredient.split(','))>1:
            if len(ingredient.split(',')[0])>len(ingredient.split(',')[1]):
                ingredient = ingredient.split(',')[0]
        if '(' in ingredient:
            ingredient = ingredient.replace(')','(')
            if len(ingredient.split('('))>2:
                ingredient = ingredient.split('(')[0]+ingredient.split('(')[2]
            else:
                ingredient = ingredient.split('(')[0]
        #remove numbers and punctuation
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        ingredient = ''.join(filter(whitelist.__contains__, ingredient))
        #remove ingredient units
        for unit in units:
            if unit in ingredient:
                ingredient = ingredient.replace(unit+'s',' ')
                ingredient = ingredient.replace(unit,' ')
        #strip extra spaces and make everything lowercase
        ingredient = ingredient.lstrip(' ').rstrip(' ').lower()
        ingredient = ingredient.replace('  ',' ')
        #some ingredient lists include sections (ie. For the sauce:) we want to get rid of these
        if 'for ' not in ingredient:
            if ingredient != '' and ingredient != ' ':
                ingredients_cleaned.append(ingredient)
    return ingredients_cleaned


#store vocabulary of all ingredients seen
#store list of ingredient lists
ingredient_lists = {}
vocab = set()
for recipe in data:
    if 'ingredients' in data[recipe]:
        tmp_ingredients = extract_ingredients(data[recipe]['ingredients'])
        ingredient_lists[recipe] = tmp_ingredients
        vocab.update(tmp_ingredients)

with open('vocab.json','w') as json_file:
    json.dump(list(vocab),json_file)
