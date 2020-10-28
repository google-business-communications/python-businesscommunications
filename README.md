# [Google's Business Communications: Python Client](https://github.com/google-business-communications/python-businesscommunications)

[Business Communications](https://developers.google.com/business-communications/business-messages/reference/business-communications/rest) is an API for creating, managing, and launching agents for Google's Verified SMS and Business Messages platforms.

## Documentation

The documentation for the Business Commmunications API can be found [here](https://developers.google.com/business-communications/business-messages/reference/business-communications/rest).

## Supported Python Versions

Python 3.5, 3.6 and 3.7, and 3.8 are fully supported and tested.



## Quickstart

### Before you begin

1.  [Register with Business Messages](https://developers.google.com/business-communications/business-messages/guides/set-up/register).
1.  Once registered, follow the instructions to [enable the APIs for your project](https://developers.google.com/business-communications/business-messages/guides/set-up/register#enable-api).

### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. virtualenv is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With virtualenv, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

### Mac/Linux

```
pip install virtualenv
python -m venv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install
```

### Windows

```
pip install virtualenv
python -m venv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install
```

### Using the client library

```python
from oauth2client.service_account import ServiceAccountCredentials
from businesscommunications.businesscommunications_v1_client import BusinesscommunicationsV1
from businesscommunications.businesscommunications_v1_messages import (
    Brand)

SCOPES = ['https://www.googleapis.com/auth/businesscommunications']

# Initialize the API authentication credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'your-service-account-key-file-location', scopes=SCOPES)

# Create the client
client = BusinesscommunicationsV1(credentials=credentials)

# Create the service for brands
brands_service = BusinesscommunicationsV1.BrandsService(client)

# Create a new brand with the name "Test Brand" 
brand = brands_service.Create(Brand(displayName='Test Brand'))

# Print created brand object
print(brand)
```

## Samples

See [code examples](https://github.com/google-business-communications/bc-bm-python-command-line-examples) to see example
usage for most API features. The samples' `README.md` has instructions for running the samples.

| Sample                      | Source Code                       |
| --------------------------- | --------------------------------- |
| Brand CRUD Operations | [source code](https://github.com/google-business-communications/bc-bm-python-command-line-examples/blob/master/brand_sample.py) |
| Agent CRUD Operations | [source code](https://github.com/google-business-communications/bc-bm-python-command-line-examples/blob/master/agent_sample.py) |
| Location CRUD Operations | [source code](https://github.com/google-business-communications/bc-bm-python-command-line-examples/blob/master/location_sample.py) |

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/google-business-communications/python-businesscommunications/CONTRIBUTING.md).

## License

Apache Version 2.0

See [LICENSE](https://github.com/google-business-communications/python-businesscommunications/LICENSE)
