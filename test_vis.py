from app import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.get_logs() == [], "browser console should contain no error"


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=10)
    assert dash_duo.get_logs() == [], "browser console should contain no error"


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region", timeout=10)
    assert dash_duo.get_logs() == [], "browser console should contain no error"

