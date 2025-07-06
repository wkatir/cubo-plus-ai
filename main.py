def calculate(amount, anual_interest, years):
    anual_interest = anual_interest / 100
    capital = (amount * anual_interest) * years
    return capital


amount = float(input("Amount to invest: "))
anual_interest = float(input("Anual interest (percentaje %): "))
years = float(input("Years to invest: "))


print(calculate(amount,anual_interest,years))

