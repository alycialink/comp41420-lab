import time
import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class AddressService(addressbook_pb2.EarlyAdopterGreeterServicer):
    
    def SendAddressEntry(self, personEntry, context):
        return addressbook_pb2.AddressBook

    def serve():
        server = addressbook_pb2.early_adopter_create_Greeter_server(AddressService(), 50051, None, None)
        server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
                server.stop()
                        
if __name__ == '__main__':
    serve()