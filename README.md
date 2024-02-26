# mechanizedai-e2e

## Prerequisites

In order to run this framework properly the following parameters must be set, according to what's stated in the [env template file.](config/envs/dot-env-template)

## How to run Tests

Simply go to the tests directory and invoke

```
$ pytest
```
Optionally the --target-env parameter can be added, by default its value is SANDBOX.

## Project dependencies
[Pytest](https://docs.pytest.org/en/7.2.x/) Test Engine, in charge of all basic plumbering to make testing possible!

[PyHamcrest](https://pyhamcrest.readthedocs.io/en/latest/) Assertion library.

[Python DotEnv](https://pypi.org/project/python-dotenv/) Employed to manage environment settings.

[WebDriver Manager](https://pypi.org/project/webdriver-manager/) Framework to manage interactions with the Web Application via WebDriver.
