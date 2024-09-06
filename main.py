from product import *
from datetime import datetime


def print_products(products_list: list) -> None:
    """
    the function gets a list of products and prints them
    @param products_list: list of products
    @return: None
    """
    print("The list of products :")
    if len(products_list) > 0:
        for product in products_list:
            print(product)
        print()
    else:
        print("The products list is empty")


def print_unsold_products(products_list: list) -> None:
    """
    the function gets a list of products and adds to a new list
    the unsold products in this month and prints them
    @param products_list: a list of products
    @return: None
    """
    if len(products_list) > 0:
        unsold_products = []
        print("The list of unsold Products is :")
        for product in products_list:
            if product.product_month_sales == 0:
                unsold_products.append(product)
        print_products(unsold_products)
    else:
        print("The products list is empty")


def print_the_most_selling_product(products_list: list) -> None:
    """
    the function gets a products list and check which product sold the most
    in month and prints it
    @param products_list: a list of products
    @return: None
    """
    if len(products_list) > 0:
        highest_sells = 0
        most_selling_product = None
        for product in products_list:
            products_sales = product.product_price * product.product_month_sales
            if products_sales > highest_sells:
                highest_sells = products_sales
                most_selling_product = product
        print(f"The most selling Product this month is : {most_selling_product}")
    else:
        print("The products list is empty")


def print_sum_month_sales_from_all_products(products_list: list) -> None:
    """
    the function gets a list of products and print the sum of all the sales
    from the products in the list of products
    @param products_list: list of products
    @return: None
    """
    if len(products_list) > 0:
        sum_products_sales = 0
        for product in products_list:
            sum_products_sales += product.product_price * product.product_month_sales
        print(f"The monthly sales of all of the Products is : {sum_products_sales} Shekels")
    else:
        print("The products list is empty")


def log_error(message, file_path = 'errors.log') -> None:
    """
    the function gets an error message and adds it to errors.log file
    @param message: an error message
    @param file_path: the path of th file
    @return: None
    """
    with open(file_path, 'a') as file:
        file.write(message + '\n')


def read_file(file_path) -> list:
    """
    The function gets a file path, and from it,
    it reads the products data and adds it to a list and returns it.
    @param file_path: the path of the products.txt file.
    :raises ValueError: If one of the given arguments is invalid.
    :raises TypeError: If one of the given arguments type is invalid.
    @return: a list of products.
    """
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_datetime = datetime.now()
        for line in lines:
            elements = line.strip().split(" , ")
            if len(elements) != 4:
                error = f'At : {current_datetime}, Invalid line: {line.rstrip()}, you need to have exactly 4 parameters'
                log_error(error)
                raise ValueError(error)
            try:
                product_code = elements[0]
                product_name = elements[1]
                selling_month_count = int(elements[2])
                product_price = float(elements[3])
            except ValueError as value_error:
                error = f"At : {current_datetime}, Invalid line: {line.rstrip()}, {value_error}"
                log_error(error)
                raise ValueError(error)

            try:
                product = Product(product_code, product_name, selling_month_count, product_price)
                data.append(product)
            except ValueError as value_error:
                error = f"At : {current_datetime}, Invalid line: {line.rstrip()}, {value_error}"
                log_error(error)
                raise ValueError(error)
            except TypeError as type_error:
                error = f"At : {current_datetime}, Invalid line: {line.rstrip()}, {type_error}"
                log_error(error)
                raise TypeError(error)

    return data


def main():
    try:
        path = 'products.txt'
        products = read_file(path)

        while True:
            print("\nPlease type the number of the option you want to choose:")
            print("1. Display the list of products")
            print("2. Display the sum of monthly sales from all products")
            print("3. Display the most selling product")
            print("4. Display unsold products")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print_products(products)
            elif choice == '2':
                print_sum_month_sales_from_all_products(products)
            elif choice == '3':
                print_the_most_selling_product(products)
            elif choice == '4':
                print_unsold_products(products)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                raise ValueError("Invalid choice. Please enter a number between 1 and 5.")

    except TypeError as t:
        print(t)
    except ValueError as v:
        print(v)
    except FileNotFoundError:
        print("The specified file doesn't exist")
    except PermissionError:
        print("You don't have permission to read from the file")


if __name__ == '__main__':
    main()
