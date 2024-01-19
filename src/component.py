class Component:
    def __init__(self, max_lifespan, current_state="Pristine"):
        self.current_state = current_state
        self.max_lifespan = max_lifespan
        self.amount_of_uses = 0
        self.get_current_state()
        

    def check_condition(self):
        print(f"component state is currently {self.current_state} and has a current life span of {self.max_lifespan - self.amount_of_uses} uses")
        return self.current_state
    
    def get_current_state(self):
        if self.max_lifespan == 0:
            self.current_state = 'Broken'
            return
        percent_max_use = self.amount_of_uses/self.max_lifespan
        if percent_max_use >= 1:
            self.current_state = 'Broken'
            return
        if percent_max_use < 0.1:
            self.current_state = "Pristine"
        elif percent_max_use < 0.5:
            self.current_state = "Good"
        elif percent_max_use < 1:
            self.current_state = "Fragile"
        return

class Bell(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "bell"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("Bell is broken and cannot be used")
            return
        else:
            print("The bell goes ding")

class Gear(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "gear"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("Gear is broken and cannot be used")
            return
        else:
            print("The gears determines how hard you pedal")

class Frame(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "frame"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("frame is broken and cannot be used")
            return
        else:
            print("The frame holds the bike together")       
            
class Brake(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "brake"
        self.wear_per_use = 1
    def usage(self):
        
        self.amount_of_uses += self.wear_per_use
        print(self.amount_of_uses)
        self.get_current_state()
        if self.current_state == "Broken":
            print("brake is broken and cannot be used")
            return
        else:
            print("The brake stops the bike")
    
            
class Chain(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "chain"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("chain is broken and cannot be used")
            return
        else:
            print("The chain makes the wheels go around")
    
            
class Tyre(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "tyre"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("tyre is broken and cannot be used")
            return
        else:
            print("The tyre gives the grip")
class Seat(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "seat"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("seat is broken and cannot be used")
            return
        else:
            print("The seat is where you sit on")
class Handles(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "handles"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("handles are broken and cannot be used")
            return
        else:
            print("The handles let you steer the bike")
class Pedals(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "pedals"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("pedals are broken and cannot be used")
            return
        else:
            print("The pedals make the gears go round")
class Lights(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "lights"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("the lights are broken and cannot be used")
            return
        else:
            print("The lights allow you to see in the dark")
class Forks(Component):
    def __init__(self, max_lifespan):
        super().__init__(max_lifespan)
        self.component_name = "forks"
        self.wear_per_use = 1
    def usage(self):
        self.amount_of_uses += self.wear_per_use
        self.get_current_state()
        if self.current_state == "Broken":
            print("forks are broken and cannot be used")
            return
        else:
            print("The forks make the ride more smooth")
class Bike:
    def __init__(self, *args):
        self.components = list(args)
    def ride(self):
        message = "a beautiful quality ride today"
        for comp in self.components:
            if comp.current_state == "Broken":
                raise BikeBrokenError("cannot ride because it is broken")
            elif comp.current_state == "Fragile":
                message = "it was a bumpy ride today"    
        for comp in self.components:
            comp.usage()
        return message

    def ring_bell(self):
        comps_names = [comp.component_name for comp in self.components]
        if "bell" not in comps_names:
            raise NoBell("no bell found on bike")
        message = "Ring! Ring! Ring!"
        for comp in self.components:
            if comp.current_state == "Broken":
                message = "The bell fell off"
                return message
            elif comp.current_state == "Fragile":
                message = "Ring! cling..."   
        return message  
    
class Racing(Bike):
    def __init__(self, *args):
        super().__init__(*args)
        for comp in self.components:
            if comp.component_name == 'tyre':
                comp.wear_per_use = 1.05
            if comp.component_name == 'chain':
                comp.wear_per_use = 1.05

class BMX(Bike):
    def __init__(self, *args):
        super().__init__(*args)
        for comp in self.components:
            if comp.component_name == "brake":
                raise WrongComponentForBike("this type of bike cannot have this component")
            if comp.component_name == 'tyre':
                comp.wear_per_use = 1.15
            

class Mountain(Bike):
    def __init__(self, *args):
        super().__init__(*args)
        for comp in self.components:
            if comp.component_name == 'chain':
                comp.wear_per_use = 0.85
            
class Street(Bike):
    def __init__(self, *args):
        super().__init__(*args)
        for comp in self.components:
            if comp.component_name == 'brake':
                comp.wear_per_use = 1.05
class Exercise(Bike):
    def __init__(self, *args):
        super().__init__(*args)
        for comp in self.components:
            if comp.component_name == "tyre":
                raise WrongComponentForBike("this type of bike cannot have this component")
            if comp.component_name == 'seat':
                comp.wear_per_use = 1.15

class BikeBrokenError(Exception):
    pass
class NoBell(Exception):
    pass
class WrongComponentForBike(Exception):
    pass
