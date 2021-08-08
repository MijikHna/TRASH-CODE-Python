from datetime import datetime

from main import execute_simple_select, execute_simple_insert


def test_execute_simple_select(conn_mock_2):
    test1 = conn_mock_2.conn
    test2 = conn_mock_2.cur

    execute_simple_select()

    assert 1 == 1


def test_execute_simple_insert(conn_mock_3):
    execute_simple_insert()
