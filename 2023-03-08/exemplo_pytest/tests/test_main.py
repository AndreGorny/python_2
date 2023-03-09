import src.main as main


def test_main():
    assert hasattr(main, "main")


def test_validate_http_status(mock_get):

    mock_get.return_value.status_code = 200

    response = main.main()
    assert response["status_code"] == 200
