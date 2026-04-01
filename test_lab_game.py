from unittest.mock import Mock
from lab_game import get_random_item, award_badge

def test_get_random_item():
    desig_rand = Mock()
    desig_rand.choice.return_value = "potion"
    result = get_random_item("Biruk", desig_rand)
    assert result == "Biruk found a potion"


def test_award_badge():
    notifier = Mock()
    result = award_badge("Biruk", "distinction", notifier)
    notifier.log.assert_called_once_with("Biruk earned distinction")
