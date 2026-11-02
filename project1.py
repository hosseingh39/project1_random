
import random

print("Be Baziye Hadse Adad Khosh amadid")

while True:

   
    number = random.randint(1, 100)

   
    max_attempts = 5
    attempts = 0

    print("Yek adad bein 1 ta 100 entekhab shode ast.")
    print("Shoma 5 forsat baraye hads zadan darid.")

   
    while attempts < max_attempts:

        print("Talash", attempts + 1, "az 5")
        print("Jan baghimande:", max_attempts - attempts)

        try:
            guess = int(input("Adad morede nazar khod ra vared konid: "))

           
            if guess < 1 or guess > 100:
                print("Lotfan adadi bein 1 ta 100 vared konid.")
                continue

        except ValueError:
            print("Voroodi namotabar ast! Lotfan faghat adad vared konid.")
            continue
       
        attempts += 1
        difference = abs(number - guess)

        if guess == number:
            print("Afarin! Shoma barande shodid.")

            
            if attempts == 1:
                print("Rotbe shoma: Nemonei!")
            elif attempts == 2:
                print("Rotbe shoma: Besyar khob!")
            elif attempts == 3:
                print("Rotbe shoma: Khob!")
            elif attempts == 4:
                print("Rotbe shoma: Ghabool!")
            elif attempts == 5:
                print("Rotbe shoma: Ba shans bordi!")

            break

        elif guess > number:
            print("Adad koochaktari vared kon.")

        else:
            print("Adad bozorgtari vared kon.")
        
        if difference <= 5:
            print("Kheyli nazdiki!")
        elif difference <= 15:
            print("Nazdiki, vali hanooz fasele dari!")
        else:
            print("Kheyli doori!")

        print("Tedade forsat baghimande:",
              max_attempts - attempts)
   
    if attempts == max_attempts and guess != number:
        print("Moteasefane forsat haye shoma tamam shod!")
        print("Adad makhfi barabar bood ba:", number)
        print("Shoma bakhtid!")
   
    again = input("Aya mikhahid dobare bazi konid? (Bale/Kheir): ")

    if again.strip().lower() not in ["bale", "bali", "yes", "y"]:
        print("Mamnoon az baziye shoma!")
        print("Barname be payan resid.")
        break
