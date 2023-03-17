# This program is meant to mass remove DID #'s from Genesys Cloud

## Configuring the .env file.

```
token="" # Example of a bearer token 'KGM0NDUwZDUzLTVkNjgtNDMyNy1iNmQ5LTY4MWMzNzZlNDRhYzo2ZmRjMjc0Ni01MDcyLTRhZWQtYjM1YS1mYWMyMTZkMTE2ODEp'
division="" # Example of a division 'Azure'
presence="" # Example of presnece 'MicrosoftTeams' Possible Values: MicrosoftTeams, ZoomPhone, EightByEight
state="" # Example of state 'any' Possible Values: active, inactive, deleted, any
```

Once you proivde a values for the following fields then program is ready to be run.

Python 3.10 was used to build this application, download URL can be found here ==> https://www.python.org/downloads/release/python-31010/