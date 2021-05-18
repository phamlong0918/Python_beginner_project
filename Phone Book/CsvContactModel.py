from typing import List
import csv, os
from Contact import Contact
from IContactModel import IContactModel

class CsvContactModel(IContactModel):
    def __init__(self) -> None:
        super().__init__()



    def getAllContacts(self) -> List[Contact]:
        lstContact: List[Contact] = []
        with open("contacts.csv", "r") as myContactsFile:
            contactsReader = csv.DictReader(myContactsFile)
            for row in contactsReader:
                lstContact.append(Contact(row["name"], row["phone number"]))

        return lstContact
                


    def getContact(self, name: str) -> Contact:
        allContacts = self.getAllContacts()
        for contact in allContacts:
            if contact.name() == name:
                return contact
        
        return None



    def addContact(self, contact: Contact) -> None:
        with open("contacts.csv", "r") as inFile:
            reader = csv.reader(inFile)
            with open("contacts_tmp.csv", "w") as outFile:
                writer = csv.writer(outFile)

                for line in reader:
                    writer.writerow(line)
                writer.writerow([contact.name(), contact.phoneNumber()])
        os.remove("contacts.csv")
        os.rename("contacts_tmp.csv", "contacts.csv")


    def deleteContact(self, name: str) -> None:
        with open("contacts.csv", "r") as myContactsFile:
            contactsReader = csv.DictReader(myContactsFile)

            with open("contacts_tmp.csv", "w") as outFile:
                writer = csv.writer(outFile)
                writer.writerow(contactsReader.fieldnames)
                for row in contactsReader:
                    if row["name"] == name:
                        continue
                    writer.writerow([row["name"], row["phone number"]])

        os.remove("contacts.csv")
        os.rename("contacts_tmp.csv", "contacts.csv")




    def updateContact(self, contact: Contact) -> None:
        with open("contacts.csv", "r") as myContactsFile:
            contactsReader = csv.DictReader(myContactsFile)

            with open("contacts_tmp.csv", "w") as outFile:
                writer = csv.writer(outFile)
                writer.writerow(contactsReader.fieldnames)
                for row in contactsReader:
                    if row["name"] == contact.name():
                        writer.writerow([contact.name(), contact.phoneNumber()])
                        continue
                    writer.writerow([row["name"], row["phone number"]])
                    
        os.remove("contacts.csv")
        os.rename("contacts_tmp.csv", "contacts.csv")
