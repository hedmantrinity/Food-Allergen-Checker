from retrieve_data import get_data

# THIS is the throwaway CLI wrapper
user_input = input("Enter ingredients: ")
ingredients = [i.strip() for i in user_input.split(',')]
results = get_data(ingredients)

# Display (also throwaway)
for r in results:
    print(f"{r['display_name']} ({r['frequency']})")