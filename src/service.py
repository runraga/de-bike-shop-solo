from src.component import *

class Service_Person():
    def __init__(self, bike):
        self.bike = bike

    def order_parts(self):
        for comp in self.bike.components:
            if comp.get_current_state() == "Broken":
                comp.improve_state()
                print(f"the {comp.component_name} has been replaced")

    def service_parts(self):
        all_parts = [comp.component_name for comp in self.bike.components]
        self.bike.improve_part("Fragile", all_parts, "serviced")

    def oil(self):
        oil_parts = ["brake", "chain", "gear"]
        self.bike.improve_part("Good", oil_parts, "oiled")

    def clean(self):
        clean_parts = ["frame", "seat", "handles", "pedals", "forks"]
        print("cleaning the bike")
        self.bike.improve_part("Good", clean_parts, "cleaned")

    def pump_wheels(self):
        pump_wheels = ['tyre']
        self.bike.improve_part("Good", pump_wheels, "pumped up")

    def fix_electronics(self):
        electronic_parts = ["lights"]
        self.bike.improve_part("Good", electronic_parts, "serviced")

    def service_bike(self):
        self.service_parts()
        self.oil()
        self.pump_wheels()
        self.clean()

        bell = ["bell"]
        self.bike.improve_part("Good", bell, "serviced")

    def check_safety(self):
        try:
            bell_test = self.bike.ring_bell()
            if bell_test == "Ring! Ring! Ring!":
                return "all components are either in good or pristine condition"
        except NoBell as err:
            print(err)
        for comp in self.bike.components:
            if comp.component_name == "brake" and comp.get_current_state() in ["Good", "Pristine"]:
                return """the brake is in either good or
                         pristine condition but other components are not"""
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
