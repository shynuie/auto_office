import pickle
import os


class Staff:
    
    def __init__(self):
        self.name = 'default'
        self.email = 'default'
        self.phone_no = 'default'
        self.purchaser = 1
        self.contact = 1
        self.receiver = 1
        self.tag = []
        self.shipping_address = []


    def setting(self):

        self.name = input('Enter staff name : ')
        self.email = input('Enter email : ')
        self.phone_no = input('Enter Phone no : ')
        print('responsible to?')
        while True:
            try:
                self.contact = int(input('Contact? (1/0) :'))
                self.purchaser = int(input('Purchaser? (1/0) :'))
                self.receiver = int(input('Receiver? (1/0) :'))
                break
            except:
                continue
        while True:
            tag = input('Adding tag? (q for quit)').lower()
            if tag == 'q':
                break
            self.tag.append(tag)


class Client:

    def __init__(self):
        self.name = 'default'
        self.id = 'default'
        self.address = Location()
        self.shipping_address = []
        self.contact = []
        self.purchaser = []
        self.receiver = []


    def setting(self):
        self.name = input('Please set client name : ')
        self.id = input('Please set client id : ').upper()
        self.address.setting()
        self.shipping_address.append(self.address)


    def add_staff(self):
        print('\nAdding staff\n')
        staff = Staff()
        staff.setting()
        if staff.purchaser == 1:
            self.purchaser.append(staff)
        if staff.contact == 1:
            self.contact.append(staff)
        if staff.receiver == 1:
            self.receiver.append(staff)


    def add_shipping_address(self):
        location = Location()
        location.setting()
        self.shipping_address.append(location)
        

class Location:

    def __init__(self):
        self.country = 'default'
        self.city = 'default'
        self.street1 = 'default'
        self.street2 = ''
        self.zipcode = ''
        self.fulladdress = ''
    

    def setting(self):
        self.country = input('Please enter the country name:')
        self.city = input('Please enter the city name:')
        self.street1 = input('Please enter the street1:')
        self.street2 = input('Please enter the street2:')
        self.zipcode = input('Please enter the zipcode:')
        self.fulladdress = self.street2 + ', ' + self.street1 + ', ' + self.city + ', ' + self.zipcode + ', ' + self.country


def add_client(clients_dic):
    client = Client()
    client.setting()
    client.add_staff()
    clients_dic[client.id] = client
    return clients_dic


def home_action_page(clients_dic):
    while True:
        action = input('What do you want to do? \n(type in v for view / a for add / e for edit) :')
        if action == 'v':
            view_clients(clients_dic)
        elif action == 'a':
            clients_dic = add_client(clients_dic)
        else:
            return clients_dic


def view_clients(clients_dic):
    print(clients_dic.keys())
    choice = input('Pls enter the clients\' id: ').upper()
    client = clients_dic[choice]
    print('\n**********************************************************************\n')
    print('Name: ' + client.name)
    print('Address: \n' +client.address.fulladdress)
    for contact in client.contact:
        print('Contact name: ' +contact.name)
        print('Contact phone: ' +contact.phone_no)
        print('Contact email: ' +contact.email)
        print('\n**********************************************************************')


def loading():
    try:
        with open('clients.pickle','rb') as f:
            clients_dic = pickle.load(f)
            return clients_dic
    except:
        print('Can not find the data, will create new one.')
        clients_dic = {}
        return clients_dic


def saving(clients_dic):
    while True:
        saving_action = input('Saving the data? (y/n)')
        if saving_action == 'y':
            with open('./clients.pickle','wb') as f:
                pickle.dump(clients_dic,f)
            print('Saving file successfully, good bye~')
            break
        elif saving_action == 'n':
            print('Good bye~')
            break


def main():
    clients_dic = loading()
    clients_dic = home_action_page(clients_dic)
    saving(clients_dic)


main()


