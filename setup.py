from pydantic import BaseModel, Field
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

# This is schema for generating your dataset
# datasets = {
#     'example1': {
#         'outfile': 'example1',
#         'prompt': "Generate an address in a fictional town"
#     },
#     'example2': {
#         'outfile': 'example2',
#         'prompt': "Generate an address in a fictional town"
#     },
# }

model = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=1.0)
blacklist = []
quantity = 100

datasets = {
    'padded_armor': {
        'outfile': 'padded_armor',
        'prompt': "Generate a totally unique high fantasy name for padded armor",
    },
    'leather_armor': {
        'outfile': 'leather_armor',
        'prompt': "Generate a totally unique high fantasy name for leather armor",
    },
    'studded_leather_armor': {
        'outfile': 'studded_leather_armor',
        'prompt': "Generate a totally unique high fantasy name for studded leather armor",
    },
    'hide_armor': {
        'outfile': 'hide_armor',
        'prompt': "Generate a totally unique high fantasy name for hide armor",
    },
    'chain_shirt': {
        'outfile': 'chain_shirt',
        'prompt': "Generate a totally unique high fantasy name for chain shirt",
    },
    'scale_mail': {
        'outfile': 'scale_mail',
        'prompt': "Generate a totally unique high fantasy name for scale mail",
    },
    'breastplate': {
        'outfile': 'breastplate',
        'prompt': "Generate a totally unique high fantasy name for breastplate",
    },
    'half_plate': {
        'outfile': 'half_plate',
        'prompt': "Generate a totally unique high fantasy name for half plate",
    },
    'ring_mail': {
        'outfile': 'ring_mail',
        'prompt': "Generate a totally unique high fantasy name for ring mail",
    },
    'chain_mail': {
        'outfile': 'chain_mail',
        'prompt': "Generate a totally unique high fantasy name for chain mail",
    },
    'splint': {
        'outfile': 'splint',
        'prompt': "Generate a totally unique high fantasy name for splint",
    },
    'plate': {
        'outfile': 'plate',
        'prompt': "Generate a totally unique high fantasy name for plate",
    }
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