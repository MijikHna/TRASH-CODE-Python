import pytest
import psycopg2


@pytest.fixture()
def conn_mock_1(mocker):
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="test_db",
        user="test_user",
        password="password"
    )

    return mocker.patch('tests002.main.psycopg2.connect', return_value=conn)


@pytest.fixture()
def conn_mock_2(mocker):
    class ConnWithCursor:
        def __init__(self, conn) -> None:
            self.conn = conn
            self.cur = conn.cursor()

        def cursor(self):
            return self.cur

        def commit(self):
            pass

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="test_db",
        user="test_user",
        password="password"
    )

    return_obj = ConnWithCursor(conn)

    mocker.patch('tests002.main.psycopg2.connect', return_value=return_obj)

    yield return_obj

    conn.rollback()


@pytest.fixture()
def conn_commit_mock(mocker, conn_mock_2):
    return mocker.patch('tests002.main.commit')


@pytest.fixture()
def conn_mock_3(mocker):
    class FakeConnection:
        def __init__(self, conn) -> None:
            self.conn = conn,
            self.test = "test"

        def commit(self):
            pass

        def rollback(self):
            pass

        def cursor(self):
            return self.conn[0].cursor()

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="test_db",
        user="test_user",
        password="password"
    )

    return_obj = FakeConnection(conn)

    mocker.patch('tests002.main.psycopg2.connect', return_value=return_obj)

    yield return_obj

    conn.rollback()
