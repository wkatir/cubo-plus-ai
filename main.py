def calculate(amount, anual_interest, years):
    anual_interest = anual_interest / 100
    capital = (amount * anual_interest) * years
    return capital


amount = float(input("Amount to invest (USD): "))
anual_interest = float(input("Anual interest (percentaje %): "))
years = float(input("Years to invest: "))

capital = calculate(amount,anual_interest,years)
print(f"The return obtaind according to the info provided amount: {amount} (USD), anual interest: {anual_interest}% and years of investment {years} is : {capital} (USD)")

