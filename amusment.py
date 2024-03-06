print("Welcome to my Amusement park rides")
height=int(input("Enter your height::"))
Bill=0

if height>=120:
  print("Aaajao Aapka Swagat Hai")
  age=int(input("Enter your age::"))
  if age<12:
    Bill=5
    print("Terese 5 rupay lunga")
  elif age<18:
    Bill=10
    print("Tu 10 Dega")
  elif age>=45 and age<=55:
    print("FREEEEE")
  else:
    Bill=20
    print("20 dede")

  photo=input("Do you want us to take a picture of you?, Y OR N:::")
  if photo=="Y":
    Bill+=3

else:
  print("Pehli Bus Pakad Ke Ghar ko Nikal")

print(f"Bill de {Bill}")