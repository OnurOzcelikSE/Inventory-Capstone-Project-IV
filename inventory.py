from tabulate import tabulate

# this Shoe class defines the attributes country, code, product, cost and quantity
class Shoe:
    # this method defines the item details in the Shoe Class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # this method returns the cost of the shoes
    def get_cost(self):
        return self.cost

    # this method returns the quantity of the shoes
    def get_quantity(self):
        quantity()
        return self.quantity

    # this method returns a string representation of the class
    def __str__(self):
        return f"""\
Country:  {self.country}
Code:     {self.code}
Product:  {self.product}
Cost:     {self.cost}
Quantity: {self.quantity}
        """

#=============Global lists===========

# shoe list includes all the details of the valid and added shoes in the inventory.txt file
shoe_list = []

# quantity list is created to access only quantity details to find min and max quantities
quantity_list = []

#==========Functions outside the class==============

# this function reads the data from the inventory.txt file
def read_shoes_data():
    while True:
        try:
            # reads the data from the inventory.txt file
            with open("inventory.txt", "r", encoding="utf-8") as file:
                file.readline()

                # splits the data in the inventory.txt
                data = [line.strip("\n").split(",") for line in file]

                # first row is seperated to print out the headers
                first_row = ["Country", "Code", "Product", "Cost", "Quantity"]

                # displays the data in tabulate mode
                print(tabulate(data, headers=first_row, tablefmt="fancy_grid"))

                # adds the details from inventory.txt to the shoe_list
                shoe_list.append(data)
                file.close()
            break

        # error handling if the txt file's directory is wrong
        except FileNotFoundError:
            print("Your file couldn't be found. Please make sure if it is in the same folder!")
            continue

def capture_shoes():

    while True:
        # asks the user either if the user wants to add a new item to the list or not
        new_item = str(input("\nWould you like to add a new item to the list? "
                             "Please enter Y for Yes or N for No: \n")).lower()
        new_item_country = ""
        new_item_code = ""
        new_item_name = ""
        new_item_cost = ""
        new_item_quantity = ""

        # if user choses yes requests the data of the new item
        if new_item == "y":
            while True:
                try:
                    new_item_name = str(input("Please enter the product name: "))
                    new_item_code = str(input("What is the code of this product?: "))
                    new_item_country = str(input("Which country branch has this product?: "))
                    new_item_cost = int(input("How much does this product cost?: "))
                    new_item_quantity = int(input(f"How many does {new_item_country} has this item?: "))
                    break

                # error handlings if user enters a wrong type, value, etc
                except TypeError:
                    print("\nPlease make sure you entered the values in the right type!\n"
                          "Product Name, Product Code and Country must be string!\n"
                          "Cost and Quantity values must be integers!\n")
                    continue

                except ValueError:
                    print("\nPlease make sure you entered the values in the right type!\n"
                          "Product Name, Product Code and Country must be string!\n"
                          "Cost and Quantity values must be integers!\n")
                    continue

            # new line including the new item to add the list
            add_new_shoe = "\n" + new_item_country + "," + new_item_code + "," + new_item_name + "," + \
                           str(new_item_cost) + "," + str(new_item_quantity)

            # adds the new line to the shoe_list
            shoe_list.append(add_new_shoe)

            print(f"\n{new_item_name} added to the list successfully")

            while True:
                try:
                    # adds new item to the inventory.txt file
                    with open("inventory.txt", "a+", encoding="utf-8") as file:
                        file.write(add_new_shoe)
                        file.close()
                        view_all()
                    break

                # error handlings if the txt file is not at the same folder
                except FileNotFoundError:
                    print("Your file couldn't be found. Please make sure if it is in the same folder!")
                    continue
            break
        # if user chooses not to add a new item
        elif new_item == "n":
            break
            # if user enters a data except Y or N returns the request
        else:
            print("You entered an invalid value! Please enter Y or N")
            continue

    return main()

# this function displays all of the information about the shoes
def view_all():
    read_shoes_data()

    # refreshs the shoe_list to the updated status
    shoe_list.clear()

    return main()

# this function gives the user the option to search the details of the shoe by entering the code
def search_shoe():
    read_shoes_data()

    while True:
        # requests the product code from the user to find the details of a specific shoe
        search = str(input("Please enter the code of the product that you are looking for: ")).upper()

        # this for loop parses the elements in the nested list to search the shoe code
        # and if shoe is in the list, valid value stores the details of the shoe to print to the screen
        for sublist in shoe_list:
            for shoe in sublist:
                if search in shoe:
                    # shoe[0] = Country
                    # shoe[1] = Code
                    # shoe[2] = Product
                    # shoe[3] = Cost
                    # shoe[4] = Quantity
                    valid = (f"\n{shoe[2]} model is available in the {shoe[0]} branch\n"
                             f"There are {shoe[4]} shoes in stock. Price of that model is {shoe[3]} per unit.")
                    break

        # if the shoe is found in the list prints out the details
        if search in shoe:
            print(valid)
            break

        # if the shoe is not found in the list returns the request of the code
        else:
            print("This shoe code isn't valid in the list. Please make sure you entered the right code!")
            continue

    return main()

# this function calculates and prints out the value of all the items separately
def value_per_item():
    read_shoes_data()

    for sublist in shoe_list:
        for shoe in sublist:
            shoe_model = shoe[2]
            shoe_price = int(shoe[3])
            shoe_quantity = int(shoe[4])
            print(f"\n☑ We have '{shoe_model}' model worth '{shoe_price * shoe_quantity}' in stock")

        # this break stops re-printing the result if user enters vpi for several times
        break

    return main()

# this function returns the quantity details of the shoes in stock
def quantity():
    read_shoes_data()

    # refreshes the list after re-stock orders
    quantity_list.clear()

    # this for loop splits the quantity information of the shoes and adds them to a separate list called quantity_list
    for sublist in shoe_list:
        for shoe in sublist:
            quantities = int(shoe[4])

            # adds the quantity of the shoes in the integer type to the quantity list
            quantity_list.append(int(shoe[4]))
            if int(shoe[4]) in shoe_list:
                return shoe

# this function finds the shoe that has the maximum quantity in stock
def highest_qty():
    quantity()

    # finds the shoe model which has the maximum quantity in stock / quantity list
    maximum_quantity = max(quantity_list)

    # finds the index of the most stocked shoe
    # this helps us to match it in the shoe_list and get the information of that shoe to print out the details
    index_of_max_quantity = quantity_list.index(maximum_quantity)

    # finds the data of the shoe which has max quantity in stocks
    # gets the country, code, product, cost and quantity data from the shoe_list
    maximum = shoe_list[0][int(index_of_max_quantity)]

    # maximum[0] displays the branch of the shoe which has the most stocked
    # maximum[1] displays the code of the shoe which has the most stocked
    # maximum[2] displays the name of the shoe which has the most stocked
    # maximum[3] displays the cost of the shoe which has the most stocked
    # maximum[4] displays the quantity of the shoe which has the most stocked

    print(f"\nThe {maximum[2]} model shoe has the maximum quantity in our stocks.\n"
          f"It's available in {maximum[0]} branch. {maximum[3]} is each and we have {maximum[4]} units in stock.\n"
          f"{maximum[1]} is its product code")

    return main()

# this function finds the shoe that has the lowest quantity in stock
# and gives an option to order to re-stock that product to the user
def re_stock():
    quantity()

    # finds the shoe model which has the lowest quantity in stock / quantity list
    minimum_quantity = min(quantity_list)

    # finds the index of the shoe that has lowest quantity
    # this helps us to match it in the shoe_list and get the information of that shoe to print out the details
    index_of_min_quantity = quantity_list.index(minimum_quantity)

    # finds the data of the shoe which has lowest quantity in stocks
    # gets the country, code, product, cost and quantity data from the shoe_list
    minimum = shoe_list[0][int(index_of_min_quantity)]

    # minimum[0] displays the branch of the shoe which has the lowest quantity
    # minimum[1] displays the code of the shoe which has the lowest quantity
    # minimum[2] displays the name of the shoe which has the lowest quantity
    # minimum[3] displays the cost of the shoe which has the lowest quantity
    # minimum[4] displays the quantity of the shoe which has the lowest quantity

    while True:
        # asks the user if they want to re-stock the least number of shoes in stock
        order = str(input(f"\nThe {minimum[2]} model of shoes are almost out of stock\n"
                          f"We have only {minimum[4]} units in our {minimum[0]} stock.\n\n"
                          f"Would you like to re-stock it? Please enter Y for yes or N for no: ")).upper()

        # if user chooses to re-stock
        if order == "Y":
            while True:
                try:
                    # requests the number of the order to re-stock
                    re_stock = int(input(f"\nHow many would you like to order from the main warehouse?\n"))
                    break

                except TypeError:
                    print("\nPlease enter a integer!\n")
                    continue
                except ValueError:
                    print("\nPlease enter a integer!\n")
                    continue

            # returns the quantity that we already have in stock
            in_stock = int(minimum[4])

            # adds the number of quantity of the order to the lowest quantity
            re_stocked = int(in_stock) + int(re_stock)

            # updates the quantity of the shoe that has the lowest quantity in the shoe list
            shoe_list[0][int(index_of_min_quantity)][4] = int(re_stocked)

            # updates the quantity of the shoe that has the lowest quantity in the quantity list
            # quantity_list[index_of_min_quantity][4] = re_stocked

            # defined the updated list
            updated_list = shoe_list[0]

            # updates the inventory.txt file, writes the new number of shoes (ordered + in stock)
            with open("inventory.txt", "w+", encoding="utf-8") as updated:
                
                # prints out the headers separetely
                first_row = "Country, Code, Product, Cost, Quantity\n"
                updated.writelines(first_row)

                for line, overwrite in enumerate(updated_list):
                    updated_txt = f"{overwrite[0]},{overwrite[1]},{overwrite[2]},{overwrite[3]},{overwrite[4]}"

                    # in the updated list we need to print each item to new line, but not the last
                    # I used if contiditon to stop adding "\n" in the last line
                    if line < len(updated_list) - 1:
                        updated_txt += "\n"
                    updated.writelines(updated_txt)

            updated.close()

            print(f"\n{re_stock} units of {minimum[2]} has been successfully ordered to be re-stocked.\n"
                  f"And lists are updated!\nYou can see the updated list below\n")

            view_all()

            break

        # if user doesn't prefer to order
        if order == "N":
            pass
            break

        # if user enters an invalid value returns the request
        else:
            print("Invalid value! Please enter Y or N!\n")
            continue

    return main()

# if user wants to exit from the application
def quit():
    print("Goodbye!")
    exit()

#==========Main Menu=============

# this function gives options to the user to choose what they want to do
def main():
    print("\n✔✔✔ Welcome to Nike Store Manager Interface ✔✔✔")

    while True:
        menu = str(input("""
Please enter one of the options below\n
va  - to view all shoes model datas in the list
ss  - to search shoe by the code number
vpi - to calculate the total value for each item
hq  - to find the shoe with the highest quantity
rs  - to re-stock the shoes with the lowest quantity in stock
cs  - to capture data about a spesific shoe model
q   - to quit
:""")).lower()

        # forwards the user to the related menu up to user's entry
        try:
            if menu == "va":
                view_all()
                break

            if menu == "ss":
                search_shoe()
                break

            if menu == "vpi":
                value_per_item()
                break

            if menu == "hq":
                highest_qty()
                break

            if menu == "rs":
                re_stock()
                break

            if menu == "cs":
                capture_shoes()
                break

            if menu == "q":
                quit()

            else:
                print("Invalid value! Please enter one of the options below:\n")
                continue

        # error handlings if user enters a wrong type, value, etc
        except TypeError:
            print("You entered a wrong answer! Please enter one of the options below:\n")
            continue
        except ValueError:
            print("Please enter cs - va - rs - ss - vi  or hq!\n")
            continue
main()