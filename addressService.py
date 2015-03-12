import addressbook_pb2
import sys

def InsertNewPerson(person):
    person.name = raw_input("Enter person's name: ")
    person.id = int(raw_input("Enter person's ID: ")
    email = raw_input("Enter email: ")
    if email != "":
        person.email = email
                    
    homeNumberInput = raw_input("Enter home phone number: ")
    if homeNumberInput != "":
        homeNumber = person.phone.add()
        homeNumber.number = homeNumberInput
        homeNumber.type = addressbook_pb2.Person.HOME
                    
    mobileNumberInput = raw_input("Enter mobile phone number: ")
    if mobileNumberInput != "":
        mobileNumber = person.phone.add()
        mobileNumber.number = mobileNumberInput
        mobileNumber.type = addressbook_pb2.Person.MOBILE
                    
    workNumberInput = raw_input("Enter work phone number: ")
    if workNumberInput != "":
        workNumber = person.phone.add()
        workNumber.number = mobileNumberInput
        workNumber.type = addressbook_pb2.Person.WORK
        
    
def DisplayAllPeople(address_book):
                    for person in address_book.person:
    print "Name: ", person.name
    print "ID: ", person.ID
    
    if person.HasField('email'):
        print "Email: ", person.email
    
    for phone in person.phone:
        if person.phone.type == addressbook_pb2.Person.HOME:
            print "Home number: ", person.phone.number
        if person.phone.type == addressbook_pb2.Person.MOBILE:
            print "Mobile number: ", person.phone.number
        if person.phone.type == addressbook_pb2.Person.WORK:
            print "Work number: ", person.phone.number

                    
address_book = addressbook_pb2.AddressBook()
     
#read
ab = open(sys.argv[1], "rb")
address_book.ParseFromString(ab.read())
ab.close()

#functions
InsertNewPerson(address_book.person.add())
DisplayAllPeople(address_book)

#write
ab = open(sys.argv[1], "wb")
ab.write(address_book.SerializeToString())
ab.close()