from pydantic import BaseModel, Field
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

# This is schema for generating your dataset
datasets = {
    'example1': {
        'outfile': 'example1',
        'prompt': "Generate an address in a fictional town"
    },
    'example2': {
        'outfile': 'example2',
        'prompt': "Generate an address in a fictional town"
    },
}

# Define your desired data structure.
class Item(BaseModel):
    name: str = Field(description="names of the item")

# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=Item)

prompt = PromptTemplate(
    template="Generate a name for an item.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)