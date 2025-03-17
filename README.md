# AddrX

Python client for parsing address using Libpostal API service.

AddrX is a Python-based client for parsing addresses using the [libpostal](https://github.com/openvenues/libpostal) API service. This service can be used to parse single addresses or a list of addresses both synchronously and asynchronously.

## Features

- Parse single and multiple addresses in a list.
- Supports both synchronous and asynchronous execution.
- Inspired by the [Dripostal](https://github.com/dribia/dripostal) service.

## Installation

You can install AddrX via pip:

```sh
pip install addrx
```

## API Methods

- **`AddrX.single_parser(url: str, address: str, exclude_address_type: list[str] = None)`**

  - Parse a single address.
  - **Parameters**:

    - `url` - The API endpoint for the libpostal service.
    - `address` - Addresses to parse.
    - `exclude_address_type` - A list of address type that is not required | default None **Returns**: Parsed address.

- **`AddrX.parser(url: str, address_list: list[str], exclude_address_type: list[str])`**

  - Parses a list of addresses synchronously.
  - **Parameters**:

    - `url` - The API endpoint for the libpostal service.
    - `address_list` - A list of addresses to parse.
    - `exclude_address_type` - A list of address type that is not required | default None

  - **Returns**: List of parsed address.

- **`AddrX.async_parser(url: str, address_list: list[str], exclude_address_type: list[str])`**

  - Parses a list of addresses asynchronously.
  - **Parameters**:

    - `url` - The API endpoint for the libpostal service.
    - `address_list` - A list of addresses to parse.
    - `exclude_address_type` - A list of address type that is not required | default None

  - **Returns**: List of parsed address.

## License

This project is licensed under the MIT License.

--------------------------------------------------------------------------------

AddrX is built to simplify address parsing using Libpostal while offering both synchronous and asynchronous capabilities.

Happy coding!
