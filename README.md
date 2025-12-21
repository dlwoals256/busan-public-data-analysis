# busan-public-data-analysis
An analysis of public data of Busan, Republic of Korea. With AI-ANT Inc.

# .env structure

```

DEBUG=True

# API Key
API_KEY=

# DB profile
DB_HOST_LOCAL=localhost
DB_HOST_DOCKER=db
DB_PORT=5432
DB_NAME=aiant_project_db
DB_USER=aiant
DB_PASSWORD=

```

- `DEBUG`: Debug mode toggle.
- `API_KEY`: Your API Key of the [data.go.kr](data.go.kr).
- `DB_HOST_LOCAL`: Local PostgreSQL URL. Set this as `localhost` if you use the local PostgreSQL.
- `DB_HOST_DOCKER`: PostgreSQL URL of the container 'db'. Which used by docker-compose. Leave it just as the first as `db`.
- `DB_NAME`: DB name. Leave it just as the first as `aiant_project_db`.
- `DB_USER`: DB user. Leave it just as the first as `aiant`.
- `DB_PASSWORD`: DB password. You can make your own.

# Bug note

## Inatall

### `psycopg2` raises `legacy install failure` on installing

- Install `psycopg2-binary` instead.

## API

### OpenAPI responses `Unauthorized`

- This can occur when you've requested just now. I prescribe you to wait for 15 minutes.