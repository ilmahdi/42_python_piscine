# ft_package

`ft_package` is a simple Python package that provides a utility function to count occurrences of a value in a list.

## Installation

You can install the package locally using `pip` by specifying the `.tar.gz` or `.whl` file from the `dist` folder:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

After installing the package, you can import and use the `count_in_list` function in your scripts:

```python
from ft_package import count_in_list

# Example usage
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## Package Information

When installed, you can check the package details with the following command:

```bash
pip show -v ft_package
```

This will output information such as:
- Name
- Version
- Summary
- Home-page
- Author
- License
- Location
- Requires

## Development

This package was built using `setuptools` and `wheel`. To build the package locally:

1. Ensure you have the required build tools:
   ```bash
   python3 -m pip install --upgrade build
   ```

2. Build the package:
   ```bash
   python3 -m build
   ```

This will create the `.tar.gz` and `.whl` files in the `dist/` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Created by **il**  
Email: [il@42.fr](mailto:il@42.fr)  
GitHub: [https://github.com/il/ft_package](https://github.com/il/ft_package)
