# Practical 7: Inheritance, Composition & Packaging

## Design Note

This application demonstrates inheritance and composition through a small staff-management example. The IS-A relationship is represented by the class hierarchy `Person → Employee → Developer`. An Employee is a Person, and a Developer is an Employee. This hierarchy allows child classes to reuse parent functionality and be used wherever the parent class is expected.

The HAS-A relationship is represented by `Employee` containing a `Department` object. An employee belongs to a department, but a department is not a type of employee. Composition models this relationship without creating an unnecessary inheritance link and keeps the two classes independently reusable.

The `super()` function calls the parent class constructor so that shared attributes are initialized without repeating code. The `describe()` method is overridden in `Employee` and `Developer` to provide details appropriate to each class while keeping a consistent method interface. The `Developer` implementation also uses `super().describe()` to retain the employee description.

The `salary` property controls access to the internal `_salary` attribute. Its setter rejects negative values with a `ValueError` and converts valid amounts to a float. This protects the object's data from invalid updates.

Finally, the package separates department and people classes into modules. The `__init__.py` file exposes the main classes, allowing `run.py` to import them cleanly from `staff_app`. This structure makes the application easier to maintain and extend.
