def calculate(amount, anual_interest, years):
    anual_interest = anual_interest / 100
    capital = (amount * anual_interest) * years
    return capital


amount = float(input("Amount to invest (USD): "))
anual_interest = float(input("Anual interest (percentaje %): "))
years = float(input("Years to invest: "))

capital = calculate(amount,anual_interest,years)
print("------------------------------------------------------------------------------------")
print(f"Amount: {amount}: {capital} (USD)")
print(f"(USD), anual interest: {anual_interest} %")
print(f"Years of investment {years}")
print("------------------------------------------------------------------------------------")
print(f"The Captital according to the info provided is : {capital}")
print("------------------------------------------------------------------------------------")

