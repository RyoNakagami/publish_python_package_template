from publish_python_package101.hallo_world import Greeter

def test_hallo():
    greeter = Greeter()
    result = greeter.hallo()
    assert result == "Hallo from publish_python_package101!"
