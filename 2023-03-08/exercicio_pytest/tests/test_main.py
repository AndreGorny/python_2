import src.main as main


def test_main():
    assert hasattr(main, "main")


def test_http(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value.__getitem__.return_value = {
        'Nome': 'Andre',
        'Endereço': 'Rua A, 32'
        }

    response = main.main()

    assert response["status_code"] == 200
    assert response["args"] == {
        "Nome": "Andre",
        "Endereço": "Rua A, 32"
    }
