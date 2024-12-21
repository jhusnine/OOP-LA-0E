import turtles

  leo = turtles.Leonardo("Leonardo", "blue")
  gelo = turtles.Michelangelo("Michelangelo", "orange")
  tel = turtles.Donatello("Donatello", "violet")
  rap = turtles.Raphael("Raphael", "red")

  print(leo.alias)
  print(gelo.alias)
  print(tel.alias)
  print(rap.alias)

  if __name__ =="__main__":
      leo = turtles.Leonardo("Leon", "Le")
      print(leo.alias)
