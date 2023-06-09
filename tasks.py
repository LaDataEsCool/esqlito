from invoke import task
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from langchain.prompts.prompt import PromptTemplate


@task
def bot(q, question="How many customers order more than 2 times?"):
    db = SQLDatabase.from_uri("clickhouse://default:@localhost/public",
                              include_tables=['customers', 'orders'],  # we include only one table to save tokens in the prompt :)
                              )
    llm = OpenAI(temperature=0, verbose=True)

    _DEFAULT_TEMPLATE = """
    Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
    Use the following format:

    Question: "Question here"
    SQLQuery: "SQL Query to run"
    SQLResult: "Result of the SQLQuery"
    Answer: "Final answer here"

    Only use the following tables:

    {table_info}

    Question: {input}
    """

    PROMPT = PromptTemplate(
        input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE
    )

    db_chain = SQLDatabaseChain.from_llm(llm, db, prompt=PROMPT, verbose=True, use_query_checker=True, return_intermediate_steps=True)
    result = db_chain(question)
