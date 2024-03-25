import pytest
import configparser

from src.rate_metrics import BaseAPI


@pytest.fixture
def mock_config():
    """Mocks configparser for testing."""
    mock_config = configparser.ConfigParser()
    mock_config.read = lambda path: None  # Avoid reading actual files
    mock_config["CONFIG"] = {
        "BASE_URL": "https://example.com/api/",
        "API_KEY": "TEST_API_KEY",
    }
    return mock_config


@pytest.fixture
def api_instance(mock_config):
    """Creates a BaseAPI instance for testing."""
    props = {
        "api_id": "test_api",
        "conf_path": r"C:\Users\sasid\OneDrive\Desktop\exchange_rate\ExchangeRate\src\tests",  # Adjust for test configuration path
        "test_api": {
            "BASE": "USD",
            "CURRENCY": "EUR",
        },
    }
    return BaseAPI('test_api', props, hist_date="2023-11-21")


class TestBaseAPI:
    def test_get_latest(self, api_instance, mock_config, mocker):
        expected_response = {
            "success": True,
            "timestamp": 1711324799,
            "historical": True,
            "base": "EUR",
            "date": "2024-03-24",
            "rates": {"AUD": 1.65867, "NZD": 1.804381},
        }
        mock_response = mocker.Mock(status_code=200, json=lambda: expected_response)
        mocker.patch("requests.get", return_value=mock_response)

        data = api_instance.get_latest()

        assert data == expected_response
        mock_response.raise_for_status.assert_called_once()

    def test_get_hist(self, api_instance, mock_config, mocker):
        hist_date = "2023-11-21"
        expected_response = {
            "success": True,
            "timestamp": 1711324799,
            "historical": True,
            "base": "USD",
            "date": hist_date,
            "rates": {"EUR": 0.98765},
        }
        mock_response = mocker.Mock(status_code=200, json=lambda: expected_response)
        mocker.patch("requests.get", return_value=mock_response)

        data = api_instance.get_hist()

        assert data == expected_response
