from src.component import *

class Service_Person():
    def __init__(self, bike):
        self.bike = bike
    def order_parts(self):
        for comp in self.bike.components:
            if comp.current_state == "Broken":
                comp.current_state = "Pristine"
                comp.amount_of_uses = 0
                print(f"the {comp.component_name} has been replaced")
    def service_parts(self):
        for comp in self.bike.components:
            if comp.current_state == "Fragile":
                comp.current_state = "Good"
                comp.amount_of_uses = comp.max_lifespan * 0.1
                print(f"the {comp.component_name} has been serviced and is now in good condition")
    def oil(self):
        oil_parts = ["brake", "chain", "gear"]
        comps_names = [comp.component_name for comp in self.bike.components]
        if len([comp for comp in oil_parts if comp not in comps_names]) == 3:
            raise NoComponentThatCanBeOiled("there is no component that can be oiled present")
        for comp in self.bike.components:
            if comp.component_name in oil_parts and comp.current_state == "Good":
                comp.current_state = "Pristine"
                comp.amount_of_uses = 0
                print(f"the {comp.component_name} has been oiled and is now in pristine condition")
    def clean(self):
        clean_parts = ["frame", "seat", "handles", "pedals", "forks"]
        comps_names = [comp.component_name for comp in self.bike.components]
        if len([comp for comp in clean_parts if comp not in comps_names]) == 5:
            raise NoComponentThatCanBeCleaned("there is no component that can be cleaned present")
        for comp in self.bike.components:
            if comp.component_name in clean_parts and comp.current_state == "Good":
                comp.current_state = "Pristine"
                comp.amount_of_uses = 0
                print(f"the {comp.component_name} has been cleaned and is now in pristine condition")
    def pump_wheels(self):
        comps_names = [comp.component_name for comp in self.bike.components]
        if "tyre" not in comps_names:
            raise NoTyre("there is no tyre on the bike")
        for comp in self.bike.components:
            if comp.component_name == "tyre" and comp.current_state == "Good":
                comp.current_state = "Pristine"
                comp.amount_of_uses = 0
                print(f"the {comp.component_name} has been pumped up and is now in pristine condition")
    def fix_electronics(self):
        electronic_parts = ["lights"]
        comps_names = [comp.component_name for comp in self.bike.components]
        if len([comp for comp in electronic_parts if comp not in comps_names]) == len(electronic_parts):
            raise NoElectronicComponentFound("there is no electronic component on the bike")
        for comp in self.bike.components:
            if comp.component_name in electronic_parts and comp.current_state == "Good":
                comp.current_state = "Pristine"
                comp.amount_of_uses = 0
                print(f"the {comp.component_name} has been fixed and is now in pristine condition")
    def service_bike(self):
        self.service_parts()
        try:
            self.oil()
        except NoComponentThatCanBeOiled as err:
            print(err)
        try:
            self.pump_wheels()
        except NoTyre as err:
            print(err)
        try:
            self.clean()
        except NoFrame as err:
            print(err)
        for comp in self.bike.components:
                if comp.component_name == "bell":
                    comp.current_state = "Pristine"
                    comp.amount_of_uses = 0
    def check_safety(self):
        try:
            bell_test = self.bike.ring_bell()
            if bell_test == "Ring! Ring! Ring!":
                return "all components are either in good or pristine condition"
        except NoBell as err:
            print(err)
        for comp in self.bike.components:
            if comp.component_name == "brake" and comp.current_state in ["Good", "Pristine"]:
                return "the brake is in either good or pristine condition but other components are not"
        return "no brake on bike and other components could be damaged"
    def check_up(self):
        self.order_parts()
        self.service_bike()
        self.check_safety()

class NoComponentThatCanBeOiled(Exception):
    pass
class NoFrame(Exception):
    pass
class NoTyre(Exception):
    pass
class NoComponentThatCanBeCleaned(Exception):
    pass
class NoElectronicComponentFound(Exception):
    pass