import time
import os

inventory = []

def mainmenu():
    print("Inventory")
    time.sleep(0.75)
    print("--------------")
    print("What do you want to do?")
    time.sleep(0.75)
    print("A : Add item")
    print("R : Remove item")
    print("I : Inventory")
    time.sleep(0.5)
    global select
    select = str(input("select : ").upper())

    def add_item():
        print("Inventory")
        time.sleep(0.75)
        print("--------------")
        print("Add item")
        item = str(input("Item : ").capitalize())
        print("Confirmation : Type \"1\" to confirm or type others to cancel (Type B to go back)")
        confirm = str(input(": "))
        if confirm == "1":
            inventory.append(item)
            time.sleep(0.5)
            print(item, "has been added to your inventory")
            time.sleep(3)
            os.system("cls")
            mainmenu()
        elif confirm == "B":
            time.sleep(0.25)
            os.system("cls")
            mainmenu()
        else:
            time.sleep(0.75)
            os.system("cls")
            add_item()

    def remove_item():
        print("Inventory")
        time.sleep(0.75)
        print("--------------")
        print("Remove item")
        item = str(input("Item : ").capitalize())
        print("Confirmation : Type \"1\" to confirm or type others to cancel (Type B to go back)")
        confirm = str(input(": "))
        if confirm == "1":
            if item in inventory:
                inventory.remove(item)
                time.sleep(0.5)
                print(item, "has been removed from your inventory")
                time.sleep(4)
                os.system("cls")
                remove_item()
            else:
                time.sleep(0.5)
                print("You dont have that item!")
                time.sleep(4)
                os.system("cls")
                remove_item()
        elif confirm == "B":
            time.sleep(0.25)
            os.system("cls")
            mainmenu()
        else:
            time.sleep(0.75)
            os.system("cls")
            remove_item()

    def view_inv():
        seen_inv = set(inventory)
        print("Inventory (Type B to go back)")
        time.sleep(0.75)
        print("--------------")
        print("Your items")
        for item in seen_inv:
            print(f"-{item} (x{inventory.count(item)})")
        back = str(input(": ").upper())
        if back == "B":
            time.sleep(0.25)
            os.system("cls")
            mainmenu()
        else:
            time.sleep(0.75)
            print("Your input was not in the option")

    if select == "A":
        os.system("cls")
        add_item()
    elif select == "R":
        os.system("cls")
        remove_item()
    elif select == "I":
        os.system("cls")
        view_inv()

mainmenu()