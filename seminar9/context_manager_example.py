class MyContextManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, "rw")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        pass


try:
    with MyContextManager("/Users/maliimregergely/mig/seminar-fp/concerts.txt"):
        print("Inside")
        # raise ValueError
        print("After")
    print("Outside")
except ValueError:
    print("After from except")
