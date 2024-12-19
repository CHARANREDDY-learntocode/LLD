from error import error_code


class BaseAdminException(Exception):
    @staticmethod
    def get_error_msg_template(err_code):
        return getattr(error_code, err_code, error_code.ERROR_DEFAULT)

    def __init__(self, err_code, kwargs):
        self.__error_code = err_code
        self.__kwargs = kwargs

    def __str__(self):
        return self.get_error_msg_template(self.__error_code).format(**self.__kwargs)


class InvalidReputationValue(BaseAdminException):
    def __init__(self):
        super().__init__("ERROR_001", {})
