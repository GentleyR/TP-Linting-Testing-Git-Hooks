from app import items

def test_add_item_shows_up_in_list(client):
    items.clear()

    response = client.post("/add", data={"item": "Buy milk"}, follow_redirects=True)

    assert response.status_code == 200
    assert b"Buy milk" in response.data
