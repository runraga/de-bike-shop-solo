import pytest
from src.component import *

def test_has_current_state_property():
    component = Component(10)
    assert hasattr(component, 'current_state')

def test_has_max_lifespan_property():
    component = Component(10)
    assert hasattr(component, 'max_lifespan')

def test_has_check_condition_method():
    component = Component(10)
    assert hasattr(component, 'check_condition')

def test_check_condition_returns_component_state():
    expected = "Pristine"
    component = Component(10)
    result = component.check_condition()
    assert result == expected

def test_bell_has_same_attributed_as_component():
    bell = Bell(10)
    assert hasattr(bell, 'current_state')
    assert hasattr(bell, 'max_lifespan')
    assert hasattr(bell, 'check_condition')
    
def test_bell_has_usage_method():
    bell = Bell(10)
    assert hasattr(bell, 'usage')

def test_state_of_bell_decrease_with_usage():
    bell = Bell(10)
    bell.usage()
    bell.usage()
    expected = "Good"
    result = bell.current_state
    assert result == expected

def test_bell_cannot_be_used_if_broken():
    bell = Bell(10)
    for _ in range(10):
        bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    # bell.usage()
    expected = "Broken"
    result = bell.current_state
    assert result == expected
    
def test_brake_has_usage_method():
    brake = Brake(10)
    assert hasattr(brake, 'usage')

def test_state_of_brake_decrease_with_usage():
    brake = Brake(10)
    brake.usage()
    brake.usage()
    expected = "Good"
    result = brake.current_state
    assert result == expected

def test_brake_cannot_be_used_if_broken():
    brake = Brake(10)
    brake.usage()
    brake.usage()
    brake.usage()
    brake.usage()
    brake.usage()
    brake.usage()
    brake.usage()
    brake.usage()
    brake.usage()
    brake.usage()
    expected = "Broken"
    result = brake.current_state
    assert result == expected

def test_chain_has_usage_method():
    chain = Chain(10)
    assert hasattr(chain, 'usage')

def test_state_of_chain_decrease_with_usage():
    chain = Chain(10)
    chain.usage()
    chain.usage()
    expected = "Good"
    result = chain.current_state
    assert result == expected

def test_chain_cannot_be_used_if_broken():
    chain = Chain(10)
    chain.usage()
    chain.usage()
    chain.usage()
    chain.usage()
    chain.usage()
    chain.usage()
    chain.usage()
    chain.usage()
    chain.usage()
    chain.usage()
    expected = "Broken"
    result = chain.current_state
    assert result == expected

def test_tyres_has_usage_method():
    tyre = Tyre(10)
    assert hasattr(tyre, 'usage')

def test_state_of_tyres_decrease_with_usage():
    tyre = Tyre(10)
    tyre.usage()
    tyre.usage()
    expected = "Good"
    result = tyre.current_state
    assert result == expected

def test_tyres_cannot_be_used_if_broken():
    tyre = Tyre(10)
    tyre.usage()
    tyre.usage()
    tyre.usage()
    tyre.usage()
    tyre.usage()
    tyre.usage()
    tyre.usage()
    tyre.usage()
    tyre.usage()
    tyre.usage()
    expected = "Broken"
    result = tyre.current_state
    assert result == expected

def test_has_correct_attributes():
    bell = Bell(100)
    brake = Brake(50)
    chain = Chain(50)
    tyre = Tyre(30)
    bike = Bike(bell, brake, chain, tyre)
    assert hasattr(bike, 'components')

def test_ride_method_returns_correct_response_when_bike_is_broken():
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

def test_all_componenets_are_fine_or_pristine():
    bell = Bell(100)
    brake = Brake(100)
    chain = Chain(100)
    tyre = Tyre(100)
    bike = Bike(bell, brake, chain, tyre)
    expected = "a beautiful quality ride today"
    result = bike.ride()
    assert result == expected   

def test_when_a_component_is_fagile_none_broken():
    bell = Bell(10)
    brake = Brake(10)
    chain = Chain(10)
    tyre = Tyre(10)
    bike = Bike(bell, brake, chain, tyre)
    expected = "it was a bumpy ride today"
    bike.ride()
    bike.ride()
    bike.ride()
    bike.ride()
    bike.ride()
    result = bike.ride()
    assert result == expected       

def test_ring_bell_method_returns_correct_response_when_bike_is_broken():
    bell = Bell(0)
    brake = Brake(0)
    chain = Chain(0)
    tyre = Tyre(0)
    bike = Bike(bell, brake, chain, tyre)
    expected = "The bell fell off"
    result = bike.ring_bell()
    assert result == expected

def test_racing_bike_increase_tyre_and_chain_usage_correctly():
    bell = Bell(5)
    brake = Brake(5)
    chain = Chain(5)
    tyre = Tyre(5)
    racing = Racing(bell, brake, chain, tyre)
    racing.ride()
    for comp in racing.components:
        if comp.component_name == 'tyre':
            assert comp.amount_of_uses == 1.05
        if comp.component_name == 'chain':
            assert comp.amount_of_uses == 1.05

def test_BMX_bike_increase_tyre_and_chain_usage_correctly():
    bell = Bell(5)
    pedals = Pedals(5)
    chain = Chain(5)
    tyre = Tyre(5)
    bmx = BMX(bell, pedals, chain, tyre)
    bmx.ride()
    for comp in bmx.components:
        if comp.component_name == 'tyre':
            assert comp.amount_of_uses == 1.15
        

def test_mountain_bike_increase_tyre_and_chain_usage_correctly():
    bell = Bell(5)
    brake = Brake(5)
    chain = Chain(5)
    tyre = Tyre(5)
    mountain = Mountain(bell, brake, chain, tyre)
    mountain.ride()
    for comp in mountain.components:
        if comp.component_name == 'chain':
            assert comp.amount_of_uses == 0.85

def test_street_bike_increase_tyre_and_chain_usage_correctly():
    bell = Bell(5)
    brake = Brake(5)
    chain = Chain(5)
    tyre = Tyre(5)
    steet = Street(bell, brake, chain, tyre)
    steet.ride()
    for comp in steet.components:
        if comp.component_name == 'brake':
            assert comp.amount_of_uses == 1.05
