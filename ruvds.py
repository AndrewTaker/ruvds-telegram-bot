import requests

BASE_URL: str = "https://api.ruvds.com"


def generic_get_request(url: str, token: str) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def get_paid_untill(token: str, server_id: str) -> dict:
    url = f"{BASE_URL}/v2/servers/{server_id}/paid_till"
    return generic_get_request(url, token)


def get_balance(token: str) -> dict:
    url = f"{BASE_URL}/v2/balance"
    return generic_get_request(url, token)


def get_server_cost(token: str, server_id: str):
    url = f"{BASE_URL}/v2/servers/{server_id}/cost"
    return generic_get_request(url, token)
