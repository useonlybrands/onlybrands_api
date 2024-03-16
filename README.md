# OnlyBrands API

![backend_logo](https://github.com/useonlybrands/onlybrands_api/blob/main/onlybrands_api.png?raw=true)
This is the backend of the OnlyBrands platform, just do database stuff so far

## Usage

- you will need to download and setup postgres locally (look at below)
- create a virtual environment and install the dependencies with `make install`
- create a `.env` file in the root of the project with the following content:
```plaintext
MASTER_TOKEN=your_master_token
```
- run `make reset-db`, this resets the database
- run `make run`, this starts the server
- you can now access the API at `http://locahost:8000/docs`
- you can use the master token to access the API, or create a new user and use the token generated for that user

### Dev

- todo: tests
- We use [Ruff](https://github.com/astral-sh/ruff) to lint and format
- run `make lint` to lint the code
- run `make format` to format the code

### Endpoints

Here are some of the main endpoints of the application:

- `POST /create_bid/`: Create a new bid. Requires `BidCreate` data and the `current_user` token.
- `POST /accepted_bid/`: Accept a bid. Requires `Bid` data and the `current_user` token.
- `POST /complete_bid/`: Complete a bid. Requires `Bid` data and the `current_user` token.
- `DELETE /delete_bid/`: Delete a bid. Requires `Bid` data and the `current_user` token.
- `POST /create_influencer/`: Create a new influencer. Requires `InfluencerCreate` data and the `current_user` token.
- `DELETE /delete_influencer/`: Delete an influencer. Requires `Influencer` data and the `current_user` token.
- `POST /create_brand/`: Create a new brand. Requires `BrandCreate` data and the `current_user` token.
- `DELETE /delete_brand/`: Delete a brand. Requires `Brand` data and the `current_user` token.


## Database Structure

### Influencer

- id: Integer, Primary Key
- name: String
- email: String
- created_at: DateTime

### Brand

- id: Integer, Primary Key
- name: String
- email: String
- created_at: DateTime

### Bid

- id: Integer, Primary Key
- influencer_id: Integer, Foreign Key (Influencer)
- brand_id: Integer, Foreign Key (Brand)
- created_at: DateTime
- status: String



## Setup Postgres
install postgres server dev
```
sudo apt install postgresql-server-dev-all
```
you can check the version
```
psql --version
```

login to postgres
```
sudo -u postgres psql postgres
```

you might have to login to the postgres user first
```
psql
CREATE USER postgres;
ALTER USER postgres WITH SUPERUSER;
```

change your password for postgres
```
\password postgres
```
(then enter "waffle" twice) or whatever you want the password to be

exit the postgres user
```
\q
```

You can avoid having to enter the password for postgres by setting up a default password
```
echo "localhost:5432:*:postgres:waffle" >> .pgpass
chmod 600 .pgpass
```

you can then connect to the database like this
```
psql -h localhost -U postgres
\q
```
`