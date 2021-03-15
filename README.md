# Run

```
make
```

# Environment variables

Variable                  | Usage                                                             | Default value
------------------------- | ----------------------------------------------------------------- | -----------------
TARGET_PROJECT_LOCAL_PATH | Local path of the target project to be scanned (Please change it) | "/tmp"
SONAR_PROJECT_KEY         | Snarqube project key (If not set it will take the default value)  | "generic-project"
SONAR_PROJECT_TOKEN       | Snarqube project token (If not set it will be generated for you)  | `None`
SONAR_PASSWORD            | Sonar `admin` user password                                       | `password`

# Rerun on new containers

```
make reset
```

# Remove local images and config

```
make rmi
```