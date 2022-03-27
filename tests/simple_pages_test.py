"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">Pylint</a>' in response.data
    assert b'<a class="nav-link" href="/page2">AAA Testing</a>' in response.data
    assert b'<a class="nav-link" href="/page3">OOP</a>' in response.data
    assert b'<a class="nav-link" href="/page4">SOLID</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"My Site" in response.data
