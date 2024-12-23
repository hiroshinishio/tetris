## Migration Guide: PyQt5 to PyQt6

This guide provides an overview of the changes made to transition the project from PyQt5 to PyQt6.

### Updated Dependencies

- The `requirements.txt` and `requirements.pytorch.txt` files have been updated to use `PyQt6`.

### Refactored Imports

- All import statements have been updated from `PyQt5` to `PyQt6`.

### Docker Configuration

- Dockerfiles have been checked to ensure they install `PyQt6`.

### Testing

- GitHub Actions workflows have been updated to use the updated dependencies.

For more details on PyQt6, refer to the [PyQt6 documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/).
