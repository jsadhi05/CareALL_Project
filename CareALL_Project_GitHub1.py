import weakref
import gc


Rid = 1000
RequestId = 0
Bid = 0
People = 0


from os import system, name
from time import sleep
# define our clear function
def clear():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')



class User:
    User_instances = []

    def __init__(self, u_id, password):
        self.__class__.User_instances.append((self))
        self.u_id = u_id
        self.password = password


class Review():

    Rating = 4.0
    number = 0
    Review_user = []

#    def __init__(self, u_id):
#    self.__class__.Review_instances.append((self))
#    self.u_id = u_id
#    self.number = 0

    def update_rating(self,new_rating, new_review):
        self.Rating = self.number*(self.Rating) + self.(new_rating)
        self.number = self.number + 2
        self.Rating = self.Rating*(self.number)
        self.Review_user.append(Rating)



def view_review(user_id):
    for obj9 in CareTaker.CareTaker_instances:
        if(obj9.u_id == user_id):
            print("Rating {} ".format(obj9.Rating))



class CareTaker(User, Review):
    CareTaker_instances = []

    def update_details(self, cust_name, adress, email, age):
        self.__class__.CareTaker_instances.append((self))
        self.cust_name = cust_name
        self.adress = adress
        self.email = email
        self.age = age

    def request_for_care(self):
        pass

    def select_bid(self):
        pass


class CareGiver(User, Review):
    CareGiver_instances = []

    def update_details(self, cgiver_name, adress, email, age):
        self.__class__.CareGiver_instances.append((self))
        self.cgiver_name = cgiver_name
        self.adress = adress
        self.email = email
        self.age = age
        self.care_takers_number = 0
        self.care_takers = []

    def view_requests(self):
        for instance in CareRequest.CareRequest_instances:
            if (instance.status == True):
                print(
                    " Request ID : {} -------- {} age {}, is looking a Caretaker at {} for a duration of {} months at a price range of {}".format(
                        instance.Rq_id, instance.name, instance.age, instance.adress, instance.duration,
                        instance.price_range))

    def place_bid(self, Rq_id, price):

        global Bid
        Bid = Bid + 1
        bid = 'bid' + str(Bid)
        bid = CareBids(Rq_id, price, self.u_id)

    def update_care_takers(self, do, user_id):
        if do == 'add':
            self.care_takers_number += self.care_takers_number
            self.care_takers.append(user_id)
        if do == 'remove':
            self.care_takers -= self.care_takers
            self.care_takers.remove(user_id)

    def view_care_takers(self):
        print("Your Rating is {}".format(self.Rating))
        for ids in self.care_takers:
            for x in gc.get_objects():
                if isinstance(x, CareTaker):
                    if x.u_id == ids:
                        print("Name : {} ".format(x.cust_name))
        #yorn = input("Do you want to rate your CareTaker ")



class CareRequest():
    CareRequest_instances = []

    # def __init__(self):

    def update_details(self, name, adress, age, price_range, duration, u_id):
        global Rid
        self.__class__.CareRequest_instances.append((self))
        self.name = name
        self.adress = adress
        self.age = age
        self.price_range = price_range
        self.duration = duration
        self.Rq_id = Rid
        Rid = Rid +1
        self.status = True
        self.u_id = u_id


    def view_bids(self):
        for instance in CareBids_instances:
            if instance.Rq_id == self.Rq_id:
                print("The person {} quoted a ammount of Rs.{}").format(instance.bidder_id, instance.price)

    def update_status(self, status, cg_id):
        self.status = status
        self.cgiver_id = cg_id


class CareBids:
    CareBids_instances = []

    def __init__(self, rq_id, price, bidder_id):
        self.__class__.CareBids_instances.append((self))
        self.Rq_id = rq_id
        self.price = price
        self.bidder_id = bidder_id



def login():

    global People
    print("""Hello
              1.CareTaker Login
              2.CareGiver Login
              3.Register""")
    choice = input("Enter your Preferance : ")
    print(type(choice))

    if choice == '1':
        user_id = input("Enter your User Id ")
        password = input("Enter your Password : ")
        for obj in User.User_instances:

            print(obj)
            if obj.u_id == user_id:
                if obj.password == password:
                    print("Login Success!")
                    print("Welcome {}!".format(obj.cust_name))
                    CareTaker_Portal(obj)
                else:
                    print("Login Failure!")
                    login()

    if choice == '2':
        user_id = input("Enter your User Id ")
        password = input("Enter your Password : ")
        for obj1 in CareGiver.CareGiver_instances:

            if obj1.u_id == user_id:
                if obj1.password == password:
                    print("Login Success!")
                    clear()
                    print("Welcome {}!".format(obj1.cgiver_name))
                    CareGiver_Portal(obj1)
                else:
                    print("Login Failure!")
                    login()

    if choice == '3':
        u_id = input("Enter your Desired User Id ")
        password = input("Enter your Desired Password ")

        name = 'A' + str(People)
        # name = User(u_id, password)
        People = People + 1
        choice_2 = input("1. Care Taker, 2. Care Giver ")
        if choice_2 == '1':
            cust_name = input("Enter your Name ")
            adress = input("Enter your Adress ")
            email = input("Enter your e-mail ID ")
            age = input("Enter your Age ")

            name = CareTaker(u_id, password)
            name.update_details(cust_name, adress, email, age)
            clear()
            login()

        if choice_2 == '2':
            cgiver_name = input("Enter your Name ")
            adress = input("Enter your Adress ")
            email = input("Enter your e-mail ID ")
            age = input("Enter your Age ")

            name = CareGiver(u_id, password)
            name.update_details(cgiver_name, adress, email, age)
            clear()
            login()


def CareTaker_Portal(obj2):
    global RequestId

    print("""" What do you want to do?
                1.Request for Care
                2.View bids for requested care
                3.Select a Bidder
                4.View and Rate your CareGiver
                5.Sign Out""")
    choice = input("Enter your preference : ")
    if choice == '2':
        name = 'R' + str(RequestId)
        RequestId += RequestId
        name = CareRequest()
        dur = input("Enter the duration of care required (in months)")
        price_r = input("Enter your desired price")
        name.update_details(obj2.cust_name, obj2.adress, obj2.age, price_r, dur, obj2.u_id)
        req_portal(obj2.u_id)
    if choice == '1':
        req_portal(obj2.u_id)
    if choice == '4':
        
        Rer_id = input("Enter the Request Id")
        b_id = input("Enter the Bidder Id")

        sel_bid(b_id, obj2.u_id, Rer_id)
    if choice == '3':
        print("Your Rating is {}".format(obj2.Rating))
        for obj12 in CareRequest.CareRequest_instances:
            if obj12.u_id == obj2.u_id:
                print("Your CareGiver id is {}".format(obj12.cgiver_id))
        yn = input("Do you want to Review your CareGiver? (Y/N)")
        if(yn == 'Y' or yn == 'y'):
            for obj11 in CareRequest.CareRequest_instances:
                if obj11.u_id == obj2.u_id:
                    new_rating = input("Give your Rating for the CareGiver of ID {}".format(obj11.cgiver_id))
                    new_review = input("Give your review ")
                    for obj13 in CareGiver.CareGiver_instances:
                        if obj13.u_id == obj11.cgiver_id:
                            obj13.update_rating(new_rating, new_review)




    if choice == '5':
        login()
    CareTaker_Portal(obj2)


def req_portal(user_id):
    for obj3 in CareRequest.CareRequest_instances:

        if (obj3.u_id == user_id):
            string = 'Active'
            if (obj3.status == True):
                print(" Request ID : {}   Status : {}".format(obj3.Rq_id, string))

    req_id = input("Enter the Request ID for more info.")

    """for obj4 in CareRequest.CareRequest_instances:

        if (obj4.Rq_id == str(req_id)):
            print("Your request of care for {} months for Rs {} has the following bidders".format(obj4.duration,
                                                                                                  obj4.price_range))"""

    for obj5 in CareBids.CareBids_instances:
        if(obj5.Rq_id == str(req_id)):
            print("Bidder ID : {}     Price : {}".format(obj5.bidder_id, obj5.price))


def sel_bid(b_id, user, request_id):
    for obj6 in CareGiver.CareGiver_instances:

        if (obj6.u_id == b_id):
            if (obj6.care_takers_number < 4):
                obj6.update_care_takers('add', user)
                for obj1 in CareRequest.CareRequest_instances:
                    if (obj1.Rq_id == int(request_id)):
                        obj1.update_status(False, b_id)
            else:
                print("Thar CareGiver is not available at this moment please choose another")


def CareGiver_Portal(obj7):

    print("""What would you like to do?
             1. See the number of people whom you are taking care of
             2.View Posted Requests
             3.Place a Bid
             4.Sign Out""")
    choice = input("Enter your Preference")
    if choice == '2':
        obj7.view_care_takers()
    if choice == '1':
        obj7.view_requests()
    if choice == '4':
        rq_id = input("Enter the Request ID")
        
        price = input("Enter the price you want to Bid")
        obj7.place_bid(rq_id, price)
    if choice == '3':
        login()
    CareGiver_Portal(obj7)


def main():
    pass


login()
