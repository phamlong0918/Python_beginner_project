from typing import List
from Contact import Contact
from PhoneBook import PhoneBook
from PhoneBook import DatabaseError
from CsvContactModel import CsvContactModel

class PhoneBookScreen:
    def __init__(self) -> None:
        self.__isRunning = True
        self.__phoneBook = PhoneBook(CsvContactModel())

    def showMainMenu(self) -> None:
        while self.__isRunning == True:
            print("Select one option below:")
            print("\t1. Add contact")
            print("\t2. Show all contacts")
            print("\t3. Update contact")
            print("\t4. Delete contact")
            print("\t5. Quit")

            key = input()
            if key == "1":
                self.__showAddContactScreen()
            elif key == "2":
                self.__showAllContactsScreen()
            elif key == "3":
                self.__showUpdateContactsScreen()
            elif key == "4":
                self.__showDeleteContactScreen()
            elif key == "5":
                self.__quit()
            else:
                print("Invalid input, please enter again!")


    def __showAllContactsScreen(self) -> None:
        try:
            allContacts: List[Contact] = self.__phoneBook.getAllContacts()
        except DatabaseError:
            print("Cannot connect to Database")
            return
        
        #if no exeption occurs, print all contact
        print("All contacts:", "\n")
        for index in range(len(allContacts)):
            print(f"Contact {index + 1}:")
            print(f"\tName: {allContacts[index].name()}")
            print(f"\tPhone number: {allContacts[index].phoneNumber()}")
            print("")


    def __showAddContactScreen(self) -> None:
        while True:
            print("Enter name: ", end="")
            name: str = input()
            if self.__phoneBook.isContactExist(name) == True:
                print("This user already exist, please enter the other name!")
            else:
                break

        print("Enter phone number: ", end="")
        phoneNumber: str = input()
        newContact: Contact = Contact(name, phoneNumber)       
        self.__phoneBook.addContact(newContact)
        return None

    def __showUpdateContactsScreen(self) -> None:
        print("Please enter user need to be updated: ", end="")
        name = input()
        if self.__phoneBook.isContactExist(name) == False:
            print("There is no contact with that name")
        else:
            print("New phone number: ")
            phoneNumber:str = input()
            self.__phoneBook.updateContact(Contact(name, phoneNumber))

    def __showDeleteContactScreen(self) -> None:
        print("Please enter user need to be deleted: ", end="")
        name = input()
        if self.__phoneBook.isContactExist(name) == False:
            print("There is no contact with that name")
        else:
            self.__phoneBook.deleteContact(name)

    def __quit(self) -> None:
        self.__isRunning = False
        return None