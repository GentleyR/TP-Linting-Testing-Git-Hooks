from app import items, delete_item, app

def test_delete_item_removes_correct_index():
    items[:] = ["a", "b", "c"]

    with app.test_request_context():
        delete_item(1)

    assert items == ["a", "c"]