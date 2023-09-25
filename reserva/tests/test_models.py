import pytest
from model_bakery import baker
from reserva.models import Petshop, Reserva   

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva_fixture: Reserva):

    assert str(reserva_fixture) == 'Teste pytest: 2022-10-01 - Tarde'
    
@pytest.mark.django_db    
def test_petshop_qtd_reserva_deve_retornar_reservas(petshop: Petshop):
    quantidade = 3
    baker.make(Reserva, _quantity=quantidade, petshop=petshop)       
    
    assert petshop.qtd_reserva() == quantidade