class Department:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Department name cannot be blank")
        self.name = name

    def __str__(self):
        return self.name
