import pytest 
from src.service import *
from src.component import *

def test_ride_func_raises_correct_error():
    with pytest.raises(
        BikeBrokenError,
        match="cannot ride because it is broken"
    ):
        bell = Bell(0)
        brake = Brake(0)
        chain = Chain(0)
        tyre = Tyre(0)
        bike = Bike(bell, brake, chain, tyre)
        bike.ride()
def test_ring_bell_func_raises_correct_error():
    with pytest.raises(
        NoBell,
        match="no bell found on bike"
    ):
        frame = Frame(0)
        brake = Brake(0)
        chain = Chain(0)
        tyre = Tyre(0)
        bike = Bike(frame, brake, chain, tyre)
        bike.ring_bell()
def test_oil_func_raises_correct_error():
    with pytest.raises(
        NoComponentThatCanBeOiled,
        match="there is no component that can be oiled present"
    ):
        frame = Frame(0)
        bell = Bell(0)
        tyre1 = Tyre(0)
        tyre2 = Tyre(0)
        bike = Bike(frame, bell, tyre1, tyre2)
        frank = Service_Person(bike)
        frank.oil()
def test_clean_func_raises_correct_error():
    with pytest.raises(
        NoComponentThatCanBeCleaned,
        match="there is no component that can be cleaned present"
    ):
        gear = Gear(0)
        bell = Bell(0)
        tyre1 = Tyre(0)
        tyre2 = Tyre(0)
        bike = Bike(gear, bell, tyre1, tyre2)
        frank = Service_Person(bike)
        frank.clean()
def test_pump_tyre_func_raises_correct_error():
    with pytest.raises(
        NoTyre,
        match="there is no tyre on the bike"
    ):
        gear = Gear(0)
        bell = Bell(0)
        chain = Chain(0)
        frame = Frame(0)
        bike = Bike(gear, bell, chain, frame)
        frank = Service_Person(bike)
        frank.pump_wheels()
def test_service_bike_func_catches_correct_error_and_carries_out_rest_of_function():
    gear = Gear(5)
    bell = Bell(5)
    chain = Chain(5)
    frame = Frame(5)
    bike = Bike(gear, bell, chain, frame)
    bike.ride()
    bike.ride()
    bike.ride()
    frank = Service_Person(bike)
    frank.service_bike()
    expected = "Pristine"
    for comp in bike.components:   
        assert comp.current_state == expected
def test_check_safety_func_catches_correct_error_and_gives_correct_response():
        gear = Gear(5)
        tyre = Tyre(5)
        chain = Chain(5)
        frame = Frame(5)
        bike = Bike(gear, tyre, chain, frame)
        bike.ride()
        bike.ride()
        bike.ride()
        frank = Service_Person(bike)
        expected = "no brake on bike and other components could be damaged"
        result = frank.check_safety()
        assert result == expected
def test_BMX_can_not_have_brakes():
    with pytest.raises(
        WrongComponentForBike,
        match="this type of bike cannot have this component"
        ):
            tyre = Tyre(5)
            chain = Chain(5)
            frame = Frame(5)
            brake = Brake(5)
            bmx = BMX(tyre, chain, frame, brake)
def test_exercise_bike_raises_error_if_given_tyre():
    with pytest.raises(
        WrongComponentForBike,
        match="this type of bike cannot have this component"
    ):
        gear = Gear(5)
        tyre = Tyre(5)
        chain = Chain(5)
        frame = Frame(5)
        brake = Brake(5)
        ex_bike = Exercise(gear, tyre, chain, frame, brake)
def test_fix_electronic_func_raises_correct_error():
    with pytest.raises(
        NoElectronicComponentFound,
        match="there is no electronic component on the bike"
    ):
        gear = Gear(5)
        tyre = Tyre(5)
        chain = Chain(5)
        frame = Frame(5)
        brake = Brake(5)
        bike = Bike(gear, tyre, chain, frame, brake)
        frank = Service_Person(bike)
        frank.fix_electronics()