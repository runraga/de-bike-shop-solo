import pytest
from src.component import ( Tyre, Bell, Brake, Chain, Bike, Racing, BikeBrokenError, Pedals, BMX, Mountain, Street)

def test_has_max_lifespan_property():
    component = Tyre(10)
    assert hasattr(component, 'max_lifespan')

def test_has_check_condition_method():
    component = Tyre(10)
    assert hasattr(component, 'check_condition')

def test_check_condition_returns_component_state():
    expected = "Pristine"
    component = Tyre(10)
    result = component.check_condition()
    assert result == expected

def test_bell_has_same_attributes_as_component():
    bell = Bell(10)
    assert hasattr(bell, 'max_lifespan')
    assert hasattr(bell, 'check_condition')
    
def test_bell_has_use_method():
    bell = Bell(10)
    assert hasattr(bell, 'use')

def test_state_of_bell_decrease_with_use():
    bell = Bell(10)
    bell.use()
    bell.use()
    expected = "Good"
    result = bell.get_current_state()
    assert result == expected

def test_bell_cannot_be_used_if_broken():
    bell = Bell(10)
    for _ in range(10):
        bell.use()

    expected = "Broken"
    result = bell.get_current_state()
    assert result == expected
    
def test_brake_has_use_method():
    brake = Brake(10)
    assert hasattr(brake, 'use')

def test_state_of_brake_decrease_with_use():
    brake = Brake(10)
    brake.use()
    brake.use()
    expected = "Good"
    result = brake.get_current_state()
    assert result == expected

def test_brake_cannot_be_used_if_broken():
    brake = Brake(10)
    brake.use()
    brake.use()
    brake.use()
    brake.use()
    brake.use()
    brake.use()
    brake.use()
    brake.use()
    brake.use()
    brake.use()
    expected = "Broken"
    result = brake.get_current_state()
    assert result == expected

def test_chain_has_use_method():
    chain = Chain(10)
    assert hasattr(chain, 'use')

def test_state_of_chain_decrease_with_use():
    chain = Chain(10)
    chain.use()
    chain.use()
    expected = "Good"
    result = chain.get_current_state()
    assert result == expected

def test_chain_cannot_be_used_if_broken():
    chain = Chain(10)
    chain.use()
    chain.use()
    chain.use()
    chain.use()
    chain.use()
    chain.use()
    chain.use()
    chain.use()
    chain.use()
    chain.use()
    expected = "Broken"
    result = chain.get_current_state()
    assert result == expected

def test_tyres_has_use_method():
    tyre = Tyre(10)
    assert hasattr(tyre, 'use')

def test_state_of_tyres_decrease_with_use():
    tyre = Tyre(10)
    tyre.use()
    tyre.use()
    expected = "Good"
    result = tyre.get_current_state()
    assert result == expected

def test_tyres_cannot_be_used_if_broken():
    tyre = Tyre(10)
    tyre.use()
    tyre.use()
    tyre.use()
    tyre.use()
    tyre.use()
    tyre.use()
    tyre.use()
    tyre.use()
    tyre.use()
    tyre.use()

    expected = "Broken"
    result = tyre.get_current_state()
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
        match="cannot ride because the bell is broken"
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

def test_racing_bike_increase_tyre_and_chain_use_correctly():
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

def test_BMX_bike_increase_tyre_and_chain_use_correctly():
    bell = Bell(5)
    pedals = Pedals(5)
    chain = Chain(5)
    tyre = Tyre(5)
    bmx = BMX(bell, pedals, chain, tyre)
    bmx.ride()
    for comp in bmx.components:
        if comp.component_name == 'tyre':
            assert comp.amount_of_uses == 1.15

def test_mountain_bike_increase_tyre_and_chain_use_correctly():
    bell = Bell(5)
    brake = Brake(5)
    chain = Chain(5)
    tyre = Tyre(5)
    mountain = Mountain(bell, brake, chain, tyre)
    mountain.ride()
    for comp in mountain.components:
        if comp.component_name == 'chain':
            assert comp.amount_of_uses == 0.85

def test_street_bike_increase_tyre_and_chain_use_correctly():
    bell = Bell(5)
    brake = Brake(5)
    chain = Chain(5)
    tyre = Tyre(5)
    steet = Street(bell, brake, chain, tyre)
    steet.ride()
    for comp in steet.components:
        if comp.component_name == 'brake':
            assert comp.amount_of_uses == 1.05
