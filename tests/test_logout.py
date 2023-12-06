def test_logout(logout):
    assert "Login" in logout.page_source
