class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age > 60:
            return 100
        else:
            return "Invalid age"

# Testing the Zoo class
if __name__ == "__main__":
    zoo = Zoo()
    print("Zoo Ticket Prices:")
    print(f"Age -10: {zoo.get_ticket_price(-10)}")  
    print(f"Age 0: {zoo.get_ticket_price(0)} THB") 
    print(f"Age 13: {zoo.get_ticket_price(13)} THB")  
    print(f"Age 21: {zoo.get_ticket_price(21)} THB")  
    print(f"Age 61: {zoo.get_ticket_price(61)} THB")    

