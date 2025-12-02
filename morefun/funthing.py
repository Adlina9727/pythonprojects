class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year}{self.model}"
    
    def display_name(self):
        return f"Welcome {self.name}"