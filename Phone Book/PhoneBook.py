from typing import List
from Contact import Contact
from IContactModel import IContactModel
from CsvContactModel import CsvContactModel

class PhoneBook:
    def __init__(self, contactModel: IContactModel) -> None:
        self.__contactModel: IContactModel = contactModel

    #--------------------------------------------------------------------
    def getAllContacts(self) -> List[Contact]:
        return self.__contactModel.getAllContacts()

    #--------------------------------------------------------------------
    def getContact(self, name: str) -> Contact:
        return self.__contactModel.getContact(name)

    #--------------------------------------------------------------------
    def isContactExist(self, name) -> bool:
        allContacts: List[Contact] = self.__contactModel.getAllContacts()
        for contact in allContacts:
            if contact.name() == name:
                return True
        else:
            return False

    #--------------------------------------------------------------------
    def addContact(self, newContact: Contact) -> None:
        self.__contactModel.addContact(newContact)

    #--------------------------------------------------------------------
    def deleteContact(self, name: str) -> None:
        self.__contactModel.deleteContact(name)

    #--------------------------------------------------------------------
    def updateContact(self, updateContact: Contact) -> None:
        self.__contactModel.updateContact(updateContact)

class DatabaseError(Exception):
    """Cannot connect to database"""
    pass