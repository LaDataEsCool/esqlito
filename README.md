# esqlito

esqlite (Read Eseculito :peach:)  is an AI Assistant for Data-Driven

Discover how a customizable BOT-assisted BI tool can transform the way you analyze data, make informed decisions, and maximize efficiency.

## Clickhouse

Download and install Clickhouse, open a terminal and run.

```
mkdir db && \
cd db && \
curl https://clickhouse.com/ | sh
```

then serve it and keep open the terminal.
```
cd db && \
./clickhouse server
```

## Install dependencies

Create a new virtual environment and install the dependencies of the project.

You can execute the `make install` command and it will install everything for you.

This command does the following:

```bash
python3 -m venv .venv && \
.venv/bin/activate && \
python3 -m pip install --upgrade pip && \
pip3 install --upgrade setuptools &&  \
pip install  invoke && \
pip install -r requirements.txt
```



## dbt

We are going to use the Jaffle Shop dbt template  project.  For running this project open a new terminal window.

- First be sure to install dbt using

```
dbt --version
```

- Clone the Jaffle Shop repository.

```
git clone https://github.com/dbt-labs/jaffle_shop.git
```

- Set up a profile called jaffle_shop to connect to Clickhouse by following these instructions from the command line.

```
cp profiles.yml jaffle_shop/profiles.yml
cd jaffle_shop
dbt debug
```

Ensure your profile is setup correctly.

- Load the CSVs with the demo data set. This materializes the CSVs as tables in your target schema. Note that a typical dbt project does not require this step since dbt assumes your raw data is already in your warehouse.

```
dbt seed
```

- Run the models
```
dbt run
```

NOTE: If this steps fails, it might mean that you need to make small changes to the SQL in the models folder to adjust for the flavor of SQL of your target database. Definitely consider this if you are using a community-contributed adapter.


## OpenAI

[OpenAI API Keys](https://platform.openai.com/account/api-keys)
```
export OPENAI_API_KEY='<YOUR OPENAI_API_KEY>'
```

- Invoke the bot

```
invoke bot --question='How many customers?'
```
