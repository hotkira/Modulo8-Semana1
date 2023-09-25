import pytest
from datetime import date, timedelta
from reserva.forms import ReservaForm


@pytest.fixture
def test_formulario_reserva_validacao_dados_validos_fixture():
    data_futuro = date.today() + timedelta(days=1)
   
    form_data = {
        'nome': 'Teste pytest',
        'email': 'teste@example.com',
        'nome_pet': 'Meu Pet',
        'data': data_futuro,
        'turno': 'tarde',
        'tamanho': 1,
        'petshop': 1,
        'observacoes': 'Observações',
    }
    
    form = ReservaForm(data=form_data)
    
  
    print(form.errors) 
    assert form.is_valid()
    
    import pytest
from datetime import date, timedelta
from reserva.forms import ReservaForm

@pytest.fixture
def test_formulario_reserva_validacao_dados_invalidos_fixture():
    data_futuro = date.today() + timedelta(days=1)
   
    
    form_data = {
        'nome': 'Teste pytest',
        # Campo de email vazio (inválido)
        'email': '',  
        'nome_pet': 'Meu Pet',
        'data': data_futuro,
        'turno': 'tarde',
        'tamanho': 1,
        'petshop': 1,
        'observacoes': 'Observações',
    }
    
    form = ReservaForm(data=form_data)
    # Verifica se o formulário é inválido devido ao campo de email vazio
    print(form.errors) 
    assert not form.is_valid()  
