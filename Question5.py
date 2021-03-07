# Nousheen Siddiqui
# Edited on 03/05/2021
# A function checks whether your game character has picked up all the items needed to perform certain tasks and checks against any status debuffs.
# Confirm checks with print statements.



def character(status_debufs,item_list):
    if "rope" in item_list and "coat" in item_list and "first_aid kit" in item_list and "slow" not in status_debufs:
        print("You can climb mountain")
    elif "pan" in item_list and "groceries" in item_list and "small" not in status_debufs:
        print("Can cook a meal")
    elif "pen" in item_list and "paper" in item_list and "idea" in item_list and "confusion" not in status_debufs:
        print("Write a book")
    else:
        print("No action")

items = ["pan", "paper", "idea", "rope", "groceries"]
status = ["slow"]

character(status, items)


