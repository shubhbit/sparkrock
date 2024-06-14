import pytest

@pytest.mark.login
class TestLogin:

    @pytest.mark.positive
    def test_user_login_valid_credentials(self):
        user_name = pytest.config['user_name']
        password = pytest.config['password']
        pytest.login_instance.enter_user_name(user_name)
        pytest.login_instance.enter_user_password(password)
        pytest.login_instance.click_login()
        assert "inventory.html" in pytest.login_instance.verify_login_success(), "login unsuccessful"

    @pytest.mark.negative
    @pytest.mark.parametrize('user,password',[("hfhfh","jdjdhd"), ("","")])
    def test_login_invalid_creds(self, user, password):
        pytest.login_instance.enter_user_name(user)
        pytest.login_instance.enter_user_password(password)
        pytest.login_instance.click_login()
        assert not "inventory.html" in pytest.login_instance.verify_login_success(), "login unsuccessful"
        pytest.is_user_logged = False
