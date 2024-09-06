from validator import *


class Product:
    """
    Class represents a product
    """

    def __init__(self, product_code: str, product_name: str, product_month_sales: int, product_price: float):
        """
        Constructor which is used to define product's attributes
        @param product_code: the code of the product
        @param product_name: the name of the product
        @param product_month_sales: the monthly sales of the product
        @param product_price: the price of one product
        :raises ValueError - If one of the given arguments is invalid
        :raises TypeError - If one of the given arguments type is invalid
        """
        self.product_code = product_code
        self.product_name = product_name
        self.product_month_sales = product_month_sales
        self.product_price = product_price

    def __str__(self):
        """
        Method returns the object's attributes in string representation
        :return: String which contains all object's attributes
        """
        return f"Product : [Code : {self.product_code}, Name : {self.product_name}, Monthly selling Count : {self.product_month_sales}, Price : {self.product_price}]"

    @property
    def product_code(self) -> str:
        """
        Getter to return product's code
        :return: product's code
        """
        return self.__product_code

    @product_code.setter
    def product_code(self, product_code: str) -> None:
        """
        Product's code setter
        :param product_code: Value to set product's code with
        :raises TypeError -  if the given product's code is not a str
        :raises ValueError -  if the given product's code is not with length of 8 characters
        or, it contains not numbers characters
        :return: None
        """
        if not Validator.check_str_type_validation(product_code):
            raise TypeError("Wrong product code type")
        if not Validator.check_product_code_length_validation(product_code):
            raise ValueError("Product code length needs to be 8 characters")
        if not Validator.check_product_code_value_validation(product_code):
            raise ValueError("Product code contains not digits characters")
        self.__product_code = product_code

    @property
    def product_name(self) -> str:
        """
        Getter to return product's name
        :return: product's name
        """
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name: str) -> None:
        """
        Product's name setter
        :param product_name: Value to set product's code with
        :raises TypeError -  if the given product's code is not a str
        :raises ValueError -  if the given product's code is not between, 3 to 20 characters
        :return: None
        """
        if not Validator.check_str_type_validation(product_name):
            raise TypeError("Wrong product name type")
        if not Validator.check_product_name_length_validation(product_name):
            raise ValueError("Product name length needs to be between 3 to 20 characters")
        if not Validator.check_product_name_contains_alphabetical_characters_validation(product_name):
            raise ValueError("Product name should contain at least one alphabetical character")
        self.__product_name = product_name

    @property
    def product_month_sales(self) -> str:
        """
        Getter to return product's month sales
        :return: product's month sales
        """
        return self.__product_month_sales

    @product_month_sales.setter
    def product_month_sales(self, product_month_sales: int) -> None:
        """
        Product's month sales setter
        @param product_month_sales: Value to set product's month sales with
        :raises TypeError -  if the given product's name is not an int
        :raises ValueError -  if the given product's month sales is a negative number
        @return: None
        """
        if not Validator.check_value_is_int(product_month_sales):
            raise TypeError("The product month sales needs to be an int")
        if not Validator.check_int_not_negative(product_month_sales):
            raise ValueError("The product month sales needs to be positive")
        self.__product_month_sales = product_month_sales

    @property
    def product_price(self) -> str:
        """
        Getter to return product's price
        :return: product's price
        """
        return self.__product_price

    @product_price.setter
    def product_price(self, product_price: float) -> None:
        """
        Product's price setter
        @param product_price: Value to set product's price with
        :raises TypeError -  if the given product's price is not a float
        :raises ValueError -  if the given product's price is a negative number
        @return: None
        """
        if not Validator.check_value_is_float(product_price):
            raise TypeError("The product price needs to be a float")
        if not Validator.check_float_not_negative(product_price):
            raise ValueError("The product price needs to be positive")
        self.__product_price = product_price
