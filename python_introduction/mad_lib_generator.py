# Mad Libs Story Generator with Conditional Touches

# Prompt user for input
weather = input("What is the weather like today (e.g., sunny, rainy, stormy)? ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter a final adjective: ")
animal1 = input("Enter an animal: ")
animal2 = input("Enter another animal: ")
verb = input("Enter a verb (e.g., jump, run, dance): ")
snack = input("Enter your favorite snack: ")
color = input("Enter a color: ")

# Conditional variation: choose a reaction based on the weather
if weather.lower() in ["sunny", "clear"]:
    mood = "excited and ready for adventure"
elif weather.lower() in ["rainy", "stormy"]:
    mood = "a bit nervous but still curious"
else:
    mood = "not sure what to expect, but hopeful"

# Build the story
story = f"""
On a {adjective1} {weather} day, I went to the zoo feeling {mood}.
I saw a {adjective2} {animal1} {verb}ing from tree to tree.
Then, I noticed a {adjective3} {animal2} relaxing in the shade, munching on a {snack}.
Suddenly, a zookeeper wearing a {color} uniform shouted, “Watch out!”
Turns out the animals were planning a {adjective4} escape!

What a wild and unforgettable zoo trip!
"""

# Display the final story
print("\n--- Your Mad Libs Story ---")
print(story)