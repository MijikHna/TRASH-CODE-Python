import pytest

from mock import Mock, MagicMock

import main


@pytest.fixture()
def mock_get_two_objects(mocker):
    class1 = Mock()
    class1.get_attr1 = Mock(return_value=30)

    class2 = Mock()

    mocker.patch('main.get_two_objects', return_value=(class1, class2))


def test_main(mock_get_two_objects):
    # arrange

    # act
    main()
    # assert
    assert result == 30
