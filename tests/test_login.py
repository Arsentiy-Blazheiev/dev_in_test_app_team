def test_successful_login(login):
    assert "Welcome" in login.page_source


def test_failed_login(login):
    login.login("invalid login", "invalid password")
    assert "Invalid credentials" in login.page_source
