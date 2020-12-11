print("\tWELCOME TO WRECK STORES...")

phone_cat= ("Samsung, \tIphone, \tInfinix")
infinix_cat=("Note 7 -  100,000 \nHot 9 - 70,000 \nHot 8 - 85,000")
iphone_cat=("Iphone X -  250,000  \nIphone Xr - 200,000 \nIphone 11 - 300,000")
samsung_cat=("S10 -   150,000 \nS20 Ultra - 250,000 \nGalaxy Z Flip - 400,000")

shoes_cat=("Nike,  \tAdidas, \tPuma")
nike_cat=("Air Jordans -  50,000 \nLow Sb - 30,000  \nAir Max - 25,000")
adidas_cat=("Stan Smiths - 70,000 \nYeezy's - 60,000 \nBoost - 40,000")
puma_cat=("Classic - 35,000 \nIgnite - 45,000 \nTazon - 50,000")

laptops_cat=("HP, \tMacbook, \tDell")
hp_cat=("Elite Book - 400,000 \nSpectre - 750,000 \nPavillon - 500,000")
macbook_cat=("Air - 700,000 \nPro - 900,000 \nTouch - 500,000")
dell_cat=("Inspiron - 400,000 \nLatitude - 600,000 \n Xps - 800,000")

speakers_cat=("Bose, \tJBL, \tNova")
bose_cat=("Soundlink - 50,000 \nWave System - 20,000 \n Microlink - 15,000")
jbl_cat=("Flip - 60,000 \nXtreme - 45,000 \nCharge - 75,000")
nova_cat=("J12 - 30,000 \nGear - 50,000 \nBox- 40,000")

watches_cat=("Casio, \tHugo, \tSkone")
casio_cat=("G-shock - 10,000 \nEdifice - 35,000 \nIlluminator - 55,000")
hugo_cat=("Black Dial - 25,000 \nBlue Plated - 40,000 \nChronograph - 35,000")
skone_cat=("Corsham - 40,000 \nClapham - 50,000 \nWest Minister- 70,000")

name=(input("Enter Your Name: "))
print(f"Hy {name.upper()}, choose a category, you would like to shop from.")
category=("1.Phones \n2.Shoes \n3.Laptops \n4.Speakers \n5.Wrist-Watches")
print(category)

select=(int(input("(Please select with 1,2,3,4,5): ")))
if select==1:
    print(phone_cat)

    phone_brand=(input("Select a brand: "))
    if phone_brand.lower()=="samsung":
        print(samsung_cat)
    elif phone_brand.lower()=="iphone":
        print(iphone_cat)
    elif phone_brand.lower()=="infinix":
        print(infinix_cat)
    else:
        print("We do not have your specified brand")

    phone_model=(input("Choose a model: "))
    cart=(input("Add to cart(Y/N): "))
    if cart.lower()=="y" or cart.lower()=="yes":
        print("Purchase Successful")
    else:
        print("Oops, pick another model")

if select==2:
    print(shoes_cat)

    shoes_brand=(input("Select a brand: "))
    if shoes_brand.lower()=="nike":
        print(nike_cat)
    elif shoes_brand.lower()=="adidas": 
        print(adidas_cat)  
    elif shoes_brand.lower()=="puma": 
        print(puma_cat)
    else:
        print("We do not have your preferred brand")

    shoe_model=(input("Choose a model: "))
    cart=(input("Add to cart(Y/N): "))
    if cart.lower()=="y" or cart.lower()=="yes":
        print("Purchase Successful")
    else:
        print("Oops, pick another model")

if select==3:
    print(laptops_cat)

    laptops_brand=(input("Select a brand: "))
    if laptops_brand.lower()=="hp":
        print(hp_cat)
    elif laptops_brand.lower()=="macbook":
        print(macbook_cat)
    elif laptops_brand.lower()=="dell":
        print(dell_cat)
    else:
        print("Your preffered brand is not in stock")

    laptops_model=(input("Choose a model: "))
    cart=(input("Add to cart(Y/N): "))
    if cart.lower()=="y" or cart.lower()=="yes":
        print("Purchase Successful")
    else:
        print("Oops, pick another model")

if select==4:
    print(speakers_cat)
    speakers_brand=(input("Select a brand: "))
    if speakers_brand.lower()=="bose":
        print(bose_cat)
    if  speakers_brand.lower()=="jbl":
        print(jbl_cat)
    if speakers_brand.lower()=="nova":
        print(nova_cat)

    speakers_model=(input("Choose a model: "))
    cart=(input("Add to cart(Y/N): "))
    if cart.lower()=="y" or cart.lower()=="yes":
        print("Purchase Successful")
    else:
        print("Oops, pick another model")

if select==5:
    print(watches_cat)
    watches_brand=(input("Select a brand: "))
    if watches_brand.lower()=="casio":
        print(casio_cat)
    if watches_brand.lower()=="hugo":
        print(hugo_cat)
    if watches_brand.lower()=="skone":
        print(skone_cat)

    watches_model=(input("Choose a model:"))
    cart=(input("Add to cart(Y/N): "))
    if cart.lower()=="y" or cart.lower()=="yes":
        print("Purchase Successful")
    else:
        print("Oops, pick another model")
else:
    print("Sorry, we do not sell the specified product.")
