# Simpleweb

An example application to show how integrate [Spring Cloud Config](https://spring.io/projects/spring-cloud-config) with an python application.

### How to run

1. access your pivotal account;
2. provision a `Config Server` service;
3. clone this repo;
4. inside `simpleweb` directory deploy the application: `cf push simpleweb000`

#### Endpoints available

`/`
Hello World

`/config`
Show the configuration retrieved from Config Server.

`/config-keys`
Show the keys from a dictionary configuration retrieved.

#### Configuration Example

Available on: https://github.com/amenezes/spring_config

Configuration required to setup the service.

````json
{"git": {"uri": "https://github.com/amenezes/spring_config"}}
````