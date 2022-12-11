def make_juice(fruit):
    return f"{fruit}+🍹"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

def make_perfect_juice(fruit):
    print(fruit)

    juice = make_juice(fruit)
    print(juice)

    cold_juice = add_ice(juice)
    print(cold_juice)
    
    perfect_juice = add_sugar(cold_juice)
    return perfect_juice

fruit = "🍉"
perfect_juice = make_perfect_juice(fruit)
print(perfect_juice)