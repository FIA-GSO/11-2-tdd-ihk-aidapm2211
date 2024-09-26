import pytest

from NotenBerechnung import berechne_prozentwert, ermittle_note


# Positive Tests for `berechne_prozentwert`
@pytest.mark.parametrize(
    "erreichte_punkte, maximale_punkte, expected",
    [
        (50, 100, 50.0),  # 50 von 100 Punkten -> 50%
        (75, 100, 75.0),  # 75 von 100 Punkten -> 75%
        (90, 90, 100.0),  # 90 von 90 Punkten -> 100%
        (0, 100, 0.0),  # 0 von 100 Punkten -> 0%
        (25, 50, 50.0),  # 25 von 50 Punkten -> 50%
    ]
)

def test_berechne_prozentwert(erreichte_punkte, maximale_punkte, expected):
    # Act
    result = berechne_prozentwert(erreichte_punkte, maximale_punkte)

    # Assert
    assert result == expected
@pytest.mark.parametrize(
    "prozentwert, expected_note",
    [
        (95.0, "sehr gut"),  # 95% -> sehr gut
        (92.0, "sehr gut"),  # 92% -> sehr gut (Grenzwert)
        (85.0, "gut"),  # 85% -> gut
        (81.0, "gut"),  # 81% -> gut (Grenzwert)
        (70.0, "befriedigend"),  # 70% -> befriedigend
        (67.0, "befriedigend"),  # 67% -> befriedigend (Grenzwert)
        (55.0, "ausreichend"),  # 55% -> ausreichend
        (50.0, "ausreichend"),  # 50% -> ausreichend (Grenzwert)
        (45.0, "ungenügend")  # 45% -> ungenügend
    ]
)
def test_ermittle_note_pos(prozentwert, expected_note):
    # Act
    result = ermittle_note(prozentwert)

    # Assert
    assert result == expected_note

# Negative Tests for `berechne_prozentwert` (ValueError and TypeError)
@pytest.mark.parametrize(
    "erreichte_punkte, maximale_punkte, expected_exception",
    [
        (-1, 100, ValueError),  # Negative erreichte Punkte
        (50, -1, ValueError),  # Negative maximale Punkte
        ("fünfzig", 100, TypeError),  # String statt Zahl bei erreichte_punkte
        (50, "einhundert", TypeError),  # String statt Zahl bei maximale_punkte
        (50, 0, ValueError),  # Maximale Punkte gleich 0
        (50, 49, ValueError)  # Maximale punkte kleiner als erreichte Punkte

    ]
)
def test_berechne_prozentwert_exceptions(erreichte_punkte, maximale_punkte, expected_exception):
    # Act & Assert
    with pytest.raises(expected_exception):
        berechne_prozentwert(erreichte_punkte, maximale_punkte)
