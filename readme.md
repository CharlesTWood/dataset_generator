# Software Create for free and open use by the public.
-----------------------------------------------------
The original use case for this script was to generate
datasets for shop names in a database for role playing games.
But it's up to your creativity and the quality of your 
prompt to create the outcome you are looking for.

### Here's a list of blacksmith shop names generated by this script:
   
> - The Shivering Forge
> - The Fiery forge
> - The Smithy
> - The Hammer and Anvil Forge
> - The Shimmering Anvil
> - The Anvil
> - The burning hammer
> - The Dark Forge
> - The Forge
> - The Ember Forge
> - The Iron Anvil
> - Back Alley Blacksmith
> - The Olden Hammer

# Usage

    python main.py 'outfile' 'prompt' datacounter

**outfile** ~ my_dataset
> The file containing the data
**NOTE** .txt is appended to the end of the file name.
The name of the file you want to save the dataset to.
You can also use this to append to an existing file if it already exists.
You don't have to create a new file for each dataset since the script will
handle that for you.

**prompt** ~ 'Return a name for a blacksmith shop in a medieval fantasy setting'
> The prompt you want to use to generate the dataset.

**datacounter** ~ 100
> The number of items you want to generate.
The script will stop when it reaches 0 or when the script is terminated.

**NOTE** The script will not generate duplicates of the same response
so the larger the datacounter, the longer it will take to generate the dataset
since duplicate items will be discarded and another request will need ot be 
made which can build up api costs. Average cost for 2000 davici 
requests(high quality) is around $3.00.

# Output

The script will create a new file in the datasets folder with the name you provided.
e.g datasets/my_dataset.txt. If the file already exists, it will append to the file.

# Setup

        pip3 install -r requirements.txt
        export OPENAI_API_KEY=*yourkey*
