import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


#na video aula não precisou do decorator, aqui só rodou com ele
@pytest.mark.django_db
def test_reserva_view_deve_retornar_template():
    client = Client()  # Crie o objeto Client
    response = client.get('/reserva/criar/')
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')