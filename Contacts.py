class contacts:

    def __init__(self, name, surname, number, identification):
        self.name = name
        self.surname = surname
        self.number = number
        self.id = identification

    def readLast(filename):
        file = open(filename, "r")
        lastID = -1
        for f in file:
            lastID += 1
        file.close()
        return lastID

    def setClient(filename):
        file = open(filename, "r")
        identification = contacts.readLast(filename) + 1
        file.close()
        file = open(filename, "a")
        name = input("Please insert new client name\n")
        surname = input("Please insert new client surname\n")
        number = input("Please insert new client telephone number\n")
        file.write("\n" + str(identification) + " " + name + " " + surname + " " + number)
        file.close()
    
    def getClientList(filename):
        file = open(filename, "r")
        for l in file:
            print(l)
        file.close()

    def chargeClients(filename):
        clientstorage = []
        file = open(filename, "r")
        for l in file:
            clientstorage.append(l)
        file.close()
        return clientstorage

    def eraseClient(filename, backupfilename, clientstorage):
        backupfile = open(backupfilename, "w")
        for l in range(len(clientstorage)):
            backupfile.write(str(clientstorage[l]))
        eraseclientid = int(input("Please insert the identificaction number of the client you want to erase\n"))
        linetoerase = clientstorage[eraseclientid]
        clientstorage.remove(linetoerase)
        clientstorageorden = []
        for l in range(len(clientstorage)):
            n = str(l)
            linea = []
            linea = clientstorage[l]
            lineaordenada = linea.replace(linea[0], n)
            clientstorageorden.append(lineaordenada)
        clientstorage = []
        for l in range(len(clientstorageorden)):
            clientstorage.append(str(clientstorageorden[l]))
        file = open(filename, "w")
        for l in range(len(clientstorage)):
            file.write(str(clientstorage[l]))
        backupfile.close()
        file.close()

        return clientstorage

        
