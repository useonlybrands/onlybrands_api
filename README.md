# OnlyBrands API

This is the backend of the OnlyBrands platform, just do database stuff so far
## Installation

TODO:
## Usage

- you will need to download and setup postgres locally
- create a virtual environment and install the dependencies with `make install`
- create a `.env` file in the root of the project with the following content:
```plaintext
MASTER_TOKEN=your_master_token
```
- run `make reset-db`, this resets the database
- run `make run`, this starts the server

## API Endpoints

### Influencer

- GET /influencers/ - Retrieve a list of influencers.
- GET /influencers/{influencer_id} - Retrieve a specific influencer by ID.
- POST /influencers/ - Create a new influencer.

### Brand

- POST /brands/ - Create a new brand.
- DELETE /brands/{brand_id} - Delete a specific brand by ID.

### Bid

- POST /bids/ - Create a new bid.
- DELETE /bids/{bid_id} - Delete a specific bid by ID.

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