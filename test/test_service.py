from src.service import (Service_Person)
from src.component import (Component, Bell, Chain, Brake, Tyre, Bike, Racing, BMX, Mountain, Street, Gear, Frame, )

def test_order_parts_replaces_broken_component_with_new_pristine():
    bell = Bell(10)
    brake = Brake(5)
    chain = Chain(10)
    tyre = Tyre(10)
    steet = Street(bell, brake, chain, tyre)
    steet.ride()
    steet.ride()
    steet.ride()
    steet.ride()
    steet.ride()
    frank = Service_Person(steet)
    frank.order_parts()
    expected = "Pristine"
    for comp in steet.components:
        if comp.component_name == "brake":
            assert comp.current_state == expected
def test_service_parts_changes_the_condition_of_any_fragile_parts():
    bell = Bell(10)
    brake = Brake(5)
    chain = Chain(10)
    tyre = Tyre(10)
    steet = Street(bell, brake, chain, tyre)
    steet.ride()
    steet.ride()
    steet.ride()
    steet.ride()
    frank = Service_Person(steet)
    frank.service_parts()
    expected = "Good"
    for comp in steet.components:
        if comp.component_name == "brake":
            assert comp.current_state == expected
def test_oil_changes_any_brakes_chains_or_gears_from_good_to_pristine():
    bell = Bell(10)
    brake = Brake(10)
    chain = Chain(10)
    gear = Gear(10)
    steet = Street(bell, brake, chain, gear)
    steet.ride()
    steet.ride()
    frank = Service_Person(steet)
    frank.oil()
    expected = "Pristine"
    for comp in steet.components:
        if comp.component_name == "brake":
            assert comp.current_state == expected
def test_clean_changes_condition_of_frame_from_good_to_pristine():
    frame = Frame(10)
    brake = Brake(10)
    chain = Chain(10)
    gear = Gear(10)
    steet = Street(frame, brake, chain, gear)
    steet.ride()
    steet.ride()
    frank = Service_Person(steet)
    frank.clean()
    expected = "Pristine"
    for comp in steet.components:
        if comp.component_name == "frame":
            assert comp.current_state == expected
def test_pump_wheels_changes_condition_of_tyre_from_good_to_pristine():
    frame = Frame(10)
    tyre = Tyre(10)
    chain = Chain(10)
    gear = Gear(10)
    steet = Street(frame, tyre, chain, gear)
    steet.ride()
    steet.ride()
    frank = Service_Person(steet)
    frank.pump_wheels()
    expected = "Pristine"
    for comp in steet.components:
        if comp.component_name == "tyre":
            assert comp.current_state == expected
def test_service_bike_calls_funcs_service_parts_oil_pump_wheels_clean():
    frame = Frame(10)
    tyre = Tyre(5)
    chain = Chain(10)
    gear = Gear(7)
    steet = Street(frame, tyre, chain, gear)
    steet.ride()
    steet.ride()
    steet.ride()
    steet.ride()
    frank = Service_Person(steet)
    frank.service_bike()
    expected = "Pristine"
    for comp in steet.components:
        assert comp.current_state == expected
def test_service_bike_does_not_fix_broken_components():
    frame = Frame(10)
    tyre = Tyre(5)
    chain = Chain(10)
    gear = Gear(7)
    steet = Street(frame, tyre, chain, gear)
    steet.ride()
    steet.ride()
    steet.ride()
    steet.ride()
    steet.ride()
    frank = Service_Person(steet)
    frank.service_bike()
    expected = "Broken"
    for comp in steet.components:
        if comp.component_name == "tyre":
            assert comp.current_state == expected
def test_check_safety_calls_ring_bell_func_and_checks_if_brakes_are_good_or_pristine():
    bell = Bell(10)
    brake = Brake(10)
    chain = Chain(10)
    tyre = Tyre(10)
    bmx = BMX(bell, brake, chain, tyre)
    bmx.ride()
    bmx.ride()
    frank = Service_Person(bmx)
    expected = "all components are either in good or pristine condition"
    result = frank.check_safety()
    assert result == expected
def test_check_up_calls_order_parts_service_bike_and_check_safety():
    bell = Bell(10)
    brake = Brake(5)
    chain = Chain(10)
    tyre = Tyre(3)
    bmx = BMX(bell, brake, chain, tyre)
    bmx.ride()
    bmx.ride()
    bmx.ride()
    frank = Service_Person(bmx)
    frank.check_up()
    expected = "Pristine"
    for comp in bmx.components:
        assert comp.current_state == expected