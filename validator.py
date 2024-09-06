class Validator:
    """
    Class representing
    static functions of checking
    """

    @staticmethod
    def check_str_type_validation(str_to_check: str) -> bool:
        """
        the function gets a string value and checks if the string is a str type
        @param str_to_check: a string value
        @return: True if the parameter's type is str and else False
        """
        if type(str_to_check) != str:
            return False
        return True

    @staticmethod
    def check_product_code_length_validation(product_code: str) -> bool:
        """
        the function gets a string representing a product code
        and checks if the value of it is exactly 8 characters
        @param product_code: a string representing a product code
        @return: True if the parameter's value is exactly 8 characters and else False
        """
        if len(product_code) != 8:
            return False
        return True

    @staticmethod
    def check_product_code_value_validation(product_code: str) -> bool:
        """
        the function gets a string representing a product code and checks
        if the value in it contains only digits
        @param product_code: a string representing a product code
        @return: True if the parameter's value contains only digits and else False
        """
        if not product_code.isdigit():
            return False
        return True

    @staticmethod
    def check_product_name_length_validation(product_name: str) -> bool:
        """
        the function gets a string representing a product name and checks
        if the length of the value in it is between 3 and 20
        @param product_name: a string representing a product name
        @return: True if the parameter's value length is between 3 and 20 and else False
        """
        if len(product_name) < 3 or len(product_name) > 20 :
            return False
        return True

    @staticmethod
    def check_product_name_contains_alphabetical_characters_validation(product_name: str) -> bool:
        """
        the function gets a string representing a product name and checks
        if the parameter's value contains alphabetical characters
        @param product_name: a string representing a product name
        @return: True if the parameter's value contains alphabetical characters and else not
        """
        if not any(char.isalpha() for char in product_name):
            return False
        return True

    @staticmethod
    def check_value_is_int(number: int) -> bool:
        """
        the function gets an int value and checks if the parameter is an int type
        @param number: an int value
        @return: True if the parameter's type is int and else False
        """
        if type(number) != int:
            return False
        return True

    @staticmethod
    def check_int_not_negative(number: int) -> bool:
        """
        the function gets an int value and checks if the value is not negative
        @param number: an int value
        @return: True if the value is not negative and else False
        """
        if number < 0:
            return False
        return True

    @staticmethod
    def check_value_is_float(number: float) -> bool:
        """
        the function gets an int value and checks if the parameter is a float type
        @param number: a float value
        @return: True if the parameter's type is float and else False
        """
        if type(number) != float:
            return False
        return True

    @staticmethod
    def check_float_not_negative(number: float) -> bool:
        """
        the function gets a float value and checks if the value is not negative
        @param number: a float value
        @return: True if the value is not negative and else False
        """
        if number < 0:
            return False
        return True
