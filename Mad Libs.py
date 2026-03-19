"""Mad Libs"""
#to do: prompt user to fill missing words
text = "Roses are {color}, violets are {noun}, sugar is {adjective}, and so are you!"

color = input("Enter a color: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")

# to do: print the final text
print(text.format(color = color, noun = noun, adjective = adjective))