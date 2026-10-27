import time

def main():
    print("Hello from inside your Docker container!")
    print(f"The current timestamp is: {time.time()}")

if __name__ == "__main__":
    main()
