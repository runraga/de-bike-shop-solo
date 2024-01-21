class Component:
    def __init__(self, max_lifespan, wear_per_use):
        self.component_name = self.__class__.__name__.lower()
        self.max_lifespan = max_lifespan
        self.amount_of_uses = 0
        self.wear_per_use = wear_per_use
        self.state_limits = {"Broken": 1, "Fragile": 0.5, "Good": 0.1, "Pristine": 0}

    def check_condition(self):
        print(f"""component state is currently {self.get_current_state()}
              and has a current life span of {self.max_lifespan - self.amount_of_uses} uses""")
        return self.get_current_state()

    def get_current_state(self):
        try:
            percent_max_use = self.amount_of_uses/self.max_lifespan
        except ZeroDivisionError:
            percent_max_use = 1

        state_names = list(self.state_limits)
        boundaries = list(self.state_limits.values())

        for i, boundary in enumerate(boundaries):
            if percent_max_use >= boundary:
                return state_names[i]

    def improve_state(self):
        state_names = list(self.state_limits)
        boundaries = list(self.state_limits.values())

        curr_state = self.get_current_state()

        i = state_names.index(curr_state)

        if i in (0, len(state_names) - 2):
            self.amount_of_uses = 0

        else:
            self.amount_of_uses = self.max_lifespan * boundaries[i+1]

    def use(self):
        if self.get_current_state() == "Broken":
            raise BikeBrokenError(f"cannot ride because the {self.__class__.__name__} is broken")
        self.amount_of_uses += self.wear_per_use

class Bell(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Gear(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Frame(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)
            
class Brake(Component):
    def __init__(self, max_lifespan,wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)
            
class Chain(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)
            
class Tyre(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Seat(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Handles(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Pedals(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Lights(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Forks(Component):
    def __init__(self, max_lifespan, wear_per_use = 1):
        super().__init__(max_lifespan, wear_per_use)

class Bike:
    def __init__(self, *args):
        self.components = list(args)

    def ride(self):
        comps_with_states = {comp.component_name:comp.get_current_state()
                             for comp in self.components}
        if "Broken" in comps_with_states.values():
            broken_name = list(comps_with_states.keys())[list(comps_with_states.values())
                                                         .index("Broken")]
            raise BikeBrokenError(f"cannot ride because the {broken_name} is broken")
        message = "a beautiful quality ride today"
        if "Fragile" in comps_with_states.values():
            message = "it was a bumpy ride today"
        for comp in self.components:
            comp.use()
        return message

    def ring_bell(self):
        comps_with_states = {comp.component_name:comp.get_current_state()
                             for comp in self.components}

        if "bell" not in comps_with_states.keys():
            raise NoBell("no bell found on bike")

        message = "Ring! Ring! Ring!"
        if "Broken" in comps_with_states.values():
            message = "The bell fell off"
            return message
        if "Fragile" in comps_with_states.values():
            message = "Ring! cling..."
        return message

    def improve_part(self, target_state, target_components, verb):

        for comp in self.components:
            if (comp.component_name in target_components 
                and comp.get_current_state() == target_state):
                comp.improve_state()
                print(f"""the {comp.component_name} has been {verb} and is now in
                     {comp.get_current_state()} condition""")

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
