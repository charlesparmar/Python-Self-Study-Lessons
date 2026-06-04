print("Welcome to the game of finding out what fruit Charles likes\n"
      "There is a list of fruits:\n"
      "The program will print each fruit and then below it will also print Charles' likes or dislike")

fruits = ["Apple", "Peach", "Pear", "Mango", "Banana"]

for like in fruits:
    print(like)
    if like == "Mango":
        print(f"Charles loves {like}")
    elif like == "Banana":
        print(f"Charles likes {like}")
    else:
        print(f"Charles does not like {like}")