class Carshowroom:
    def _init_(self):
        self.company_name = ""
        self.model_name = ""
        self.showroom_price=""

    def Company(self,company):
        self.company_name=company
         
        print("Welcome to", self.company_name, "company")

    def Model(self):
            if self.company_name == "Toyota":
                 models = ["Camry", "Corolla", "Rav4"]

            elif self.company_name == "Honda":
                 models = ["Civic", "Accord", "CR-V"]
            
            elif self.company_name == "Ford":
                 models = ["Fusion", "Escape", "Explorer"]
                
                
            else:
               print("Invalid company name")
               return
            print("Models available for", self.company_name, ":", models)  
            self.model_name = input("Select a model: ")

    def Price(self):
        if self.company_name=="Toyota" and self.model_name=="camry":
            self.showroom_price=25000
        elif self.company_name=="Toyota" and self.model_name=="Corolla":
            self.showroom_price=26000
        elif self.company_name=="Honda" and self.model_name=="Civic":
            self.showroom_price=27000
        elif self.company_name=="Honda" and self.model_name=="Accord":
            self.showroom_price=28000
        elif self.company_name=="Ford"and self.model_name=="Fusion":
            self.showroom_price=29000
        elif self.company_name=="Ford" and self.model_name=="Escape":
            self.showroom_price=30000
        else:
            print("invalid")
            return
        gst_tax = 0.05 * self.showroom_price
        cgst_tax = 0.05 * self.showroom_price
        road_price = self.showroom_price + gst_tax + cgst_tax
        print("Road price for", self.company_name, self.model_name, "is:", road_price)

car_showroom = Carshowroom()
comp = input("Enter Company Name")
car_showroom.Company(comp)
car_showroom.Model()
car_showroom.Price()
