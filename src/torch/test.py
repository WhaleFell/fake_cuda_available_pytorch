class PyPackageTest(object):

    def __init__(self, name: str = "hyy", age: int = 90) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hello, my name is {self.name}, I am {self.age} years old. Modify in fake_cuda_available."
