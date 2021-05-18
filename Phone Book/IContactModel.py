from typing import List
from Contact import Contact

class IContactModel:
    def __init__(self) -> None:
        pass

    def getAllContacts(self) -> List[Contact]:
        pass
    
    def getContact(self, name: str) -> Contact:
        pass

    def addContact(self, contact: Contact) -> None:
        pass
    
    def deleteContact(self, name: str) -> None:
        pass

    def updateContact(self, contact: Contact) -> None:
        pass 