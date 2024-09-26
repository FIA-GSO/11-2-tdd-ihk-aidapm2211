import pytest

from NotenBerechnung import berechne_prozentwert


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
