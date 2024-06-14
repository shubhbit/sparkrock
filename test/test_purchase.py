import pytest

@pytest.mark.purchase
class TestPurchase:

    @pytest.mark.positive
    def test_purchase_end_to_end(self):
        pytest.purchase_instance.add_item_to_cart()
        pytest.purchase_instance.checkout()
        pytest.purchase_instance.fill_details("user_djjdj", "djdjdjjdj", "dhdhdhdh")
        pytest.purchase_instance.finish()
        assert "Thank you for your order!" in pytest.purchase_instance.verify_success()
        pytest.purchase_instance.back_home()
