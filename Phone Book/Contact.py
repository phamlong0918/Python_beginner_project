class Contact:
    def __init__(self, name: str, phoneNumber: str) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber

    def name(self) -> str:
        return self.__name

    def phoneNumber(self) -> str:
        return self.__phoneNumber

    def setPhoneNumer(self, phoneNumber: str) -> None:
        self.__phoneNumber = phoneNumber