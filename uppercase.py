def extract_uppercase(text):
    # Use a list comprehension to extract uppercase letters
    uppercase_letters = [char for char in text if char.isupper()]
    return ''.join(uppercase_letters)

if __name__ == "__main__":
    # Sample text input
    input_text = """hvis natten er stille, og stjernerne stråler,
jagten på lykken, i mørket vi drømmer.
æbletræets blomster, Hvisker om savn,
livets reJse kan vÆre, en uendeLig dans,
på kanten af skygger, hvor håbet sPirer.

mørket omfavner, Men lyset vIl finde,
i dine arme, jeg føler miG fri,
gennem tågerne ser Jeg, dit smil i natten.
jeg huskEr din latter, som toner i vinden,
er kærliGhed stærkEst, når vi eR adskilt?
for i hver drøm, er du min ledestjerne,
angsten For at miste, men aldrig for At elske,
når tideN går, vil vi altid huske,
GennEm mørke og lys, vil vi finde vejen,
et bånd, der er stærkt, for evigT forenet,
trods skæbnen, vil vores sjæle danse."""
    
    result = extract_uppercase(input_text)
    print("Extracted uppercase letters:", result)