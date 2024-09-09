import pytest
from auricular_inalambrico_class import Auricular_Inalambrico

# Fixture para crear un auricular de ejemplo
@pytest.fixture
def auricular():
    return Auricular_Inalambrico("Modelo X", 100, 10, 20, "MarcaY", "Negro")

# Test para verificar que los auriculares se inicializan correctamente
def test_inicializacion(auricular):
    assert auricular.get_modelo() == "Modelo X"
    assert auricular.get_precio() == 100
    assert auricular.get_rango_alcance_metros() == 10
    assert auricular.get_duracion_bateria() == 20
    assert auricular.get_marca() == "MarcaY"
    assert auricular.get_color() == "Negro"

# Test para verificar que los auriculares se encienden correctamente
def test_encender_auriculares(auricular):
    resultado = auricular.encender(5)
    assert resultado == "Modelo X encendido."
    assert auricular._encendido is True

# Test para verificar que los auriculares no se encienden si están fuera de alcance
def test_no_encender_fuera_de_alcance(auricular):
    with pytest.raises(ValueError, match="ya está encendido o fuera de alcance"):
        auricular.encender(15)

# Test para verificar que los auriculares se apagan correctamente
def test_apagar_auriculares(auricular):
    auricular.encender(5)
    resultado = auricular.apagar(5)
    assert resultado == "Modelo X apagado."
    assert auricular._encendido is False

# Test para verificar que los auriculares no se apagan si ya están apagados o fuera de alcance
def test_no_apagar_fuera_de_alcance_o_apagado(auricular):
    with pytest.raises(ValueError, match="ya está apagado o fuera de alcance"):
        auricular.apagar(15)

# Test para verificar el ajuste de volumen dentro del rango permitido
def test_ajustar_volumen_valido(auricular):
    resultado = auricular.ajustar_volumen(75)
    assert resultado == "Volumen ajustado a 75%."
    assert auricular._volumen == 75

# Test para verificar que no permite un volumen fuera de rango
def test_ajustar_volumen_invalido(auricular):
    with pytest.raises(ValueError, match="El volumen debe estar entre 0 y 100"):
        auricular.ajustar_volumen(110)

# Test para el uso de los auriculares y verificación de la batería restante
def test_usar_auriculares_bateria(auricular):
    auricular.encender(5)
    resultado = auricular.usar_auriculares(5)
    assert resultado == "Has usado los auriculares por 5 horas. Batería restante: 15 horas."
    assert auricular._bateria_restante == 15

# Test para verificar que no se puede usar los auriculares si están apagados
def test_no_usar_auriculares_apagados(auricular):
    with pytest.raises(ValueError, match="Los auriculares están apagados"):
        auricular.usar_auriculares(5)

# Test para verificar que el método __str__ devuelve la cadena correcta
def test_str(auricular):
    assert str(auricular) == "Auricular Modelo X, Marca: MarcaY, Precio: 100$, Color: Negro, Batería restante: 20 horas."
