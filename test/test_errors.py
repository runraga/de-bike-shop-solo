import pytest
from src.service import (Service_Person)
from src.component import (Bell, Brake, Chain, Tyre, Bike, BikeBrokenError,
                           NoBell, Frame, Gear, WrongComponentForBike, BMX, Exercise)

def test_ride_func_raises_correct_error():
    with pytest.raises(
        BikeBrokenError,
        match="cannot ride because the bell is broken"
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

def test_bmx_can_not_have_brakes():
    with pytest.raises(
        WrongComponentForBike,
        match="this type of bike cannot have this component"
        ):
        tyre = Tyre(5)
        chain = Chain(5)
        frame = Frame(5)
        brake = Brake(5)
        BMX(tyre, chain, frame, brake)

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
        Exercise(gear, tyre, chain, frame, brake)
