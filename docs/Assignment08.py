# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudocode to start assignment 8
# James Henderson,08.30.2022,Modified class code
# James Henderson,08.31.2022,Modified main body to complete assignment 8
# ------------------------------------------------------------------------ #
import pickle

# Data - Start -------------------------------------------------------------------- #
FILE_NAME_STR = 'products.txt'  # The name of the data file
SUCCESS_STR = 'Success'  # String indicating a method completed successfully
FAIL_STR = 'Fail'  # String indicating a method failed to complete
status_str = ''  # String indicating method completion status
products_lst = []  # List to contain product objects


class Product:
    """Stores data about a product.:

    properties:
        product_name: (string) with the product's name  \n
        product_price: (float) with the product's standard price \n
        product_category: (string) with the product's category \n
        product_description: (string) with the product's description \n
    methods: to_string(): -> (string) with the product's details (name, price, category, and description） \n
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class  \n
        James Henderson,08.30.2022,Modified class code
    """
    # -- Attributes --
    __product_name_str = ''
    __product_price_flt = 0.00
    __product_category_str = ''
    __product_description_str = ''

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float, product_category: str, product_description: str):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category
        self.product_description = product_description

    # -- Properties --
    # product_name (string) with the product's  name
    @property
    def product_name(self):  # getter / accessor
        return str(self.__product_name_str).title()  # title case

    @product_name.setter
    def product_name(self, value: str):  # setter / mutator
        try:  # attempt to set the product name; catch ValueError exceptions
            str(value)
            self.__product_name_str = value
        except ValueError:
            pass

    # product_price (float) with the product's standard price
    @property
    def product_price(self):  # getter / accessor
        return self.__product_price_flt
        # return '${:,.2f}'.format(self.__product_price_flt)  # currency-formatted string

    @product_price.setter
    def product_price(self, value: float):  # setter / mutator
        try:  # attempt to set the product price; catch ValueError exceptions (i.e., if value isn't a number)
            float(value)
            self.__product_price_flt = value
        except ValueError:
            pass
        
    # product_category (string) with the product's category
    @property
    def product_category(self):  # getter / accessor
        return self.__product_category_str

    @product_category.setter
    def product_category(self, value: str):  # setter / mutator
        try:  # attempt to set the product category; catch ValueError exceptions
            str(value)
            self.__product_category_str = value
        except ValueError:
            pass
        
    # product_description (string) with the product's description
    @property
    def product_description(self):  # getter / accessor
        return self.__product_description_str

    @product_description.setter
    def product_description(self, value: str):  # setter / mutator
        try:  # attempt to set the product description; catch ValueError exceptions
            str(value)
            self.__product_description_str = value
        except ValueError:
            pass

    # explicit method of __str__
    def to_string(self):
        return self.__str__()

    # implicitly returns current product details
    def __str__(self):  # print the product's name, category, price and description
        formatted_price = str(f'${self.product_price:.2f}')  # format price - USD currency format
        return ','.join([self.product_name, formatted_price, self.product_category, self.product_description])


# Data - End -------------------------------------------------------------------- #


# Processing - Start  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        create_new_file(file_name): -> (status) \n
        save_data_to_file(file_name, list_of_product_objects) -> (status) \n
        read_data_from_file(file_name): -> (a list of product objects), (status) \n
        add_product_to_list(name, price, category, description, products): -> (a list of product objects), (status)
        remove_product_from_list(name, products): -> (a list of product objects), (status)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        James Henderson,08.30.2022,Modified class code
    """

    @staticmethod
    def create_new_file(file_name: str):
        """ Creates a new file with the specified name.

        :param file_name: (string) with name of file
        :return:
            status - (string) indicating function status
        """
        file = open(file_name, "wb")  # open the file in "binary write" mode
        file.close()  # close file to create it
        status = SUCCESS_STR  # set status to success String

        return status

    @staticmethod
    def save_data_to_file(file_name: str, products: list):
        """ Saves data to a text file in binary format using pickle.

        :param file_name: (string) with name of file
        :param products: (list) of product objects to write to file
        :return:
            menu - (list) of data rows |
            status - (string) indicating function status
        """
        with open(file_name, 'wb') as file:  # opens text file in "binary write" mode (saves & closes when done)
            pickle.dump(products, file)  # write the product data into the file
            status = SUCCESS_STR  # return success status message when completed

        return status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads binary data from a file that was stored using pickle.

        :param file_name: (string) with name of file
        :return:
            menu - (list) of data rows  |
            status - (string) indicating function status
        """
        with open(file_name, "rb") as file:  # opens text file in "binary read" mode (closes when done)
            try:
                products = (pickle.load(file))  # read the product data into a list
                status = SUCCESS_STR  # return success status message when completed
            except EOFError:
                products = []
                status = FAIL_STR

        return products, status

    @staticmethod
    def add_product_to_list(name: str, price: float, category: str, description: str, products: list):
        """ Adds a new product to the current list of products.

        :param name: (string) name of the product
        :param price: (float) item price (USD)
        :param category: (string) product category
        :param description: (string) product description
        :param products: (list) to which you want to add data
        :return:
            products - (list) of data rows
            status - (string) indicating function status
        """
        # add Dictionary representation of product to product list
        product = Product(name, price, category, description)
        products.append(product)

        # set status equal to a summary of what was added (String)
        status = str(f'{name} (${price:.2f}) was added to the {category} section of the product list.')
        return products, status

    @staticmethod
    def remove_product_from_list(name: str, products: list):
        """ Removes a product from a list of products.

        :param name: (string) name of the product
        :param products: (list) from which you want to remove data
        :return:
            products - (list) of data rows
            status - (string) indicating function status
        """
        if name:  # if the product name is not blank, check to remove product
            item_found = False
            for item in products:
                if item.product_name.lower() == name.lower():  # if matching product name was found, remove it
                    products.remove(item)
                    item_found = True  # stop searching for the product
                    break

            if item_found:  # set function status equal to status message
                status = str(f'{name.title()} was successfully removed from the product list.')
            else:
                status = str(f'{name} was not on the product list, so nothing was removed.')
        else:  # nothing was entered
            status = ''

        return products, status


# Processing - End  ------------------------------------------------------------- #


# Presentation (Input/Output) - Start  -------------------------------------------- #
class IO:
    """ Performs tasks related to the interactive portion of the program.

    methods:
        print_user_choice_menu() \n
        input_press_to_continue() \n
        input_user_menu_choice(): -> (user String input) \n
        input_yes_no_choice(message): -> (user String input) \n
        print_product_list(products, sort_by_key1, sort_by_key2) \n
        input_new_product(): -> (product name), (product_price), (product_category), (product_description) \n
        input_product_to_remove(): -> (product_name)
        create_new_file(file_name): -> (status) \n

    changelog: (When,Who,What)
        James Henderson,08.30.2022,Created class code
    """

    @staticmethod
    def print_user_choice_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new product
        2) Remove an existing product
        3) Save product list to file      
        4) Reload product list from file
        5) Exit program
        ''')

    @staticmethod
    def input_press_to_continue(optional_message: str = ''):
        """ Pause program and show a message before continuing.

        :param optional_message: (string) optional message to display to the user
        :return:
            None
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_user_menu_choice():
        """ Gets the menu choice from a user.

        :return:
            (String) of user input.
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()  # prompt user for choice
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(message: str):
        """ Gets a yes or no choice from the user.

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def print_product_list(products: list, sort_by_key1: str = '', sort_by_key2: str = ''):
        """ Shows the current product list.

        :param products: (list) of products
        :param sort_by_key1: (string) optional key to sort by: Name, Price, Category, etc.
        :param sort_by_key2: (string) optional 2nd key to sort by: Name, Price, Category, etc.
        :return:
            None
        """

        #  sort the products for display (or not) according to the sort key arguments
        try:
            if sort_by_key1 and not sort_by_key2:  # if only 1 sort key is present, sort the list on it
                sorted_products = sorted(products, key=lambda d: d[sort_by_key1])
            elif sort_by_key1 and sort_by_key2:  # if both sort keys are present, sort the list on both of them
                sorted_products = sorted(products, key=lambda elem: "%s %s" % (elem[sort_by_key1], elem[sort_by_key2]))
            else:  # if no sort keys were provided, do not sort the list
                sorted_products = products
        except Exception as e:  # if there was an error with the sort keys provided, raise an exception and don't sort
            print("The program tried to sort the products on a characteristic that doesn't exist. "
                  "A default sort order was applied.")
            sorted_products = products

        print("******* Here are our current products: *******")  # display product list
        category = ""
        for product in sorted_products:
            if category != product.product_category:  # print a category header for each new category encountered
                category = product.product_category
                print(category)
                print("*******************************************")

            print(product)  # print the Product's details - name, category, price (USD currency format) and description

        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product():
        """ Gets input from the user on a new product to add to the list.

        :return:
            - (string) product name
            - (float) product price
            - (string) product category
            - (string) product description
        """
        print("Please enter the new product details:")
        product_name = input("Name: ").title()  # product name, title case
        while True:
            try:  # continue to prompt the user for valid input if product price isn't a number
                product_price = float(input("Price: "))
                break
            except ValueError:
                print("Please enter a valid price (decimal number format).")
        product_category = input("Category: ").title()  # product category, title case
        product_description = input("Description: ").lower()  # product description, lowercase

        return product_name, product_price, product_category, product_description

    @staticmethod
    def input_product_to_remove():
        """ Gets input from the user on a product to remove.

        :return:
            - (string) product name
        """
        product_name = input('Which product would you like to remove? ')
        return product_name

    @staticmethod
    def create_new_file(file_name: str):
        """ Asks the user if they would like to create a new product list file with the specified name.

        :param file_name: (string) with name of file
        :return:
            status - (string) indicating function status
        """
        valid_choice = False  # initialize user choice validity variable
        choice = False  # initialize user choice variable
        while not valid_choice:  # prompt user on whether to create the text file if it does not yet exist
            choice = IO.input_yes_no_choice("The product file has not been created yet. "
                                            "Would you like to create it (y/n)? ")
            if choice == "y" or choice == "n":  # continue onwards if user made a valid choice
                valid_choice = True
            else:
                print("Please make a valid selection. ", end="")  # repeat request until user makes a valid choice
                continue

        if choice == "y":  # the user chose to create the menu file
            FileProcessor.create_new_file(file_name)
            print("File created successfully.")
            status = SUCCESS_STR
        else:  # the user did not choose to create a menu file yet
            status = FAIL_STR

        return status

# Presentation (Input/Output) - End  -------------------------------------------- #


# Custom Error Classes - Start  -------------------------------------------- #
class UserCancelledNewFileCreation(Exception):
    """ Custom error class for when user cancels new file creation.

    changelog: (When,Who,What)
        James Henderson,08.30.2022,Created class code
    """
    pass


class InvalidUserMenuChoice(Exception):
    """ Custom error class for when user enters an invalid menu choice.

    changelog: (When,Who,What)
        James Henderson,08.30.2022,Created class code
    """
    pass


class InvalidSaveChoice(Exception):
    """ Custom error class for when user enters an invalid save choice.

    changelog: (When,Who,What)
        James Henderson,08.30.2022,Created class code
    """
    pass

# Custom Error Classes - End  -------------------------------------------- #


# Main Body of Script - Start  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Step 1 - When the program starts, load data from the menu file
try:
    products_lst, status_str = FileProcessor.read_data_from_file(FILE_NAME_STR)  # read file data
    if status_str == SUCCESS_STR:
        IO.input_press_to_continue('Data loaded successfully.')
    else:
        IO.input_press_to_continue('No data loaded.')

except IOError:  # file does not exist
    try:  # ask the user if they want to create the file
        result = IO.create_new_file(FILE_NAME_STR)
        if result == FAIL_STR:  # if user chooses not to create a new file at the save location, move to error handling
            raise UserCancelledNewFileCreation("The user chose not to create the product list file.")
        else:
            pass

    except UserCancelledNewFileCreation as e:  # user chose not to create a product list file -> program ends
        print("\tBuilt-In Python error info: ")  # print exception details for the user to see
        print('\tName of the custom exception: ' + str(e), 'Exception docstring: ' + str(e.__doc__),
              'Type of the exception: ' + str(type(e)), sep='\n\t')
        IO.input_press_to_continue("No menu file was created. Thanks for running the program!")  # exit message
        exit()

# Show user a menu of options
while True:
    # Step 3 - Show current data
    IO.print_product_list(products_lst, "Category", "Name")  # Show current product list, sorted by category then name
    IO.print_user_choice_menu()  # Shows main menu

    try:
        choice_str = IO.input_user_menu_choice()  # Get user menu selection

        # Step 4 - Process user's menu selection
        if choice_str.strip() == '1':  # Add a new product
            product_name_str, product_price_flt, product_category_str, product_description_str = IO.input_new_product()
            products_lst, status_str = FileProcessor.add_product_to_list(product_name_str,
                                                                         product_price_flt,
                                                                         product_category_str,
                                                                         product_description_str,
                                                                         products_lst)
            IO.input_press_to_continue(status_str)
            continue  # to show the user menu

        elif choice_str == '2':  # Remove an existing product
            product_name_str = IO.input_product_to_remove()
            products_lst, status_str = FileProcessor.remove_product_from_list(product_name_str, products_lst)
            IO.input_press_to_continue(status_str)
            continue  # to show the user menu

        elif choice_str == '3':  # Save product list to file

            while True:  # prompt user to save the menu to the file or not
                try:
                    choice_str = IO.input_yes_no_choice("Save this menu to file (binary output)? (y/n) - ")
                    if choice_str == "y":  # user chooses to save
                        status_str = FileProcessor.save_data_to_file(FILE_NAME_STR, products_lst)
                        IO.input_press_to_continue(status_str)
                        break
                    elif choice_str == "n":  # user chooses not to save
                        IO.input_press_to_continue("Save cancelled!")
                        break
                    else:
                        raise InvalidSaveChoice("Invalid choice")  # go to error handling if user made an invalid choice

                except InvalidSaveChoice as e:  # prompt user to enter a valid choice, repeat prompt
                    print("Please enter a valid choice ('y' to save, 'n' to cancel).")

            continue  # to show the user menu

        elif choice_str == '4':  # Reload product list from file
            print("Warning: Unsaved Data Will Be Lost!")

            while True:  # prompt user to save the product list to the file
                try:
                    choice_str = IO.input_yes_no_choice("Are you sure you want to reload the last saved product list?"
                                                        " (y/n) - ")
                    if choice_str == "y":  # user chooses to reload from the file
                        products_lst, status_str = FileProcessor.read_data_from_file(FILE_NAME_STR)
                        IO.input_press_to_continue(status_str)
                        break
                    elif choice_str == "n":  # user chooses not to reload from the file -> cancel
                        IO.input_press_to_continue("File reload cancelled!")
                        break
                    else:
                        raise InvalidSaveChoice("Invalid choice")  # go to error handling if user made an invalid choice

                except InvalidSaveChoice as e:  # prompt user to enter a valid choice, repeat prompt
                    print("Please enter a valid choice ('y' to save, 'n' to cancel).")

            continue  # to show the user menu

        elif choice_str == '5':  # Exit Program
            print("Goodbye!")
            break  # and exit

        else:  # go to error handling - prompt the user for a valid menu choice if an invalid choice was entered
            raise InvalidUserMenuChoice("Invalid menu choice.")

    except InvalidUserMenuChoice:  # if invalid choice, let the user know; repeat prompt
        print("Please enter a valid choice [1-5].")

# Main Body of Script - End  ---------------------------------------------------- #
