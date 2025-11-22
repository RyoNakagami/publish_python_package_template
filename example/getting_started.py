from publish_python_package101.hallo_world import Greeter

def main():
    try:
        greeter = Greeter()
        message = greeter.hallo()
        print(message)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
