COLOR_TO_NAME = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarincrimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                 "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff"}

color_code = input("Enter color: ").lower()
while color_code != "":
    if color_code in COLOR_TO_NAME:
        print(COLOR_TO_NAME[color_code])
    else:
        print("Invalid color")
    color_code = input("Enter color: ")
