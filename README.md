# mechanizedai-e2e

## Prerequisites

In order to run this framework properly the following parameters must be set, according to what's stated in the [env template file.](config/envs/dot-env-template)
```
export CONFIG_FILE=<name of the desired config file. For instance: env.local.json
export USERS_FILE=<name of the file to store user data. For instance: users.json
export GROUPS_FILE=<name of the file to store groups data. For instance: groups.json
export USERS_PER_GROUPS_FILE=<name of the file to store the relationship between Users and Groups. For instance: users_per_groups.json
```

**NOTE**: It's important to locate any file into the config folder in this project. The Loader functions are set in that way to make the parametrization easier.

## Project dependencies
[Pytest](https://docs.pytest.org/en/7.2.x/) Test Engine, in charge of all basic plumbering to make testing possible!

[PyHamcrest](https://pyhamcrest.readthedocs.io/en/latest/) Assertion library.
