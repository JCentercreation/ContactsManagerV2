import UserOption
from Contacts import contacts


useropti = 0
filename = "Clients.txt"
backupfilename = "ClientsBackUp.txt"
while useropti == 0:
    useropti = UserOption.pullUserOpt()
    clientstorage = []
    if useropti == 1:
        clientstorage = contacts.chargeClients(filename)
        contacts.getClientList(filename)
        useropti = 0        
    elif useropti == 2:
        clientstorage = contacts.chargeClients(filename)
        contacts.setClient(filename)
        useropti = 0
    elif useropti == 3:
        clientstorage = contacts.chargeClients(filename)
        contacts.eraseClient(filename, backupfilename, clientstorage)
        useropti = 0
    elif useropti == 4:
        print("Thanks for using clients contact manager app\n")
    else:
        print("Please select a valid option\n")
        useropti = 0



