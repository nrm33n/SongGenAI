from transformers import TFGPT2LMHeadModel
from transformers import pipeline

# assuming you are in the folder with the json and p5 files
model = TFGPT2LMHeadModel.from_pretrained('./euromodel/') 
# now make a pipeline - the pipeline API is very easy to use
generator = pipeline('text-generation', model=model, tokenizer='distilgpt2')
# and generate.......... >:)
#print(generator("A little happy, a little sad ", max_length=30, num_return_sequences=5))
res = generator("A little happy, a little sad ", max_length=30, num_return_sequences=5)
print(res)
#just saving it out to a text file for later. make life a little easier :-)
with open('lyrics.txt', 'w') as f:
    for lyric in res:
        f.write(lyric['generated_text'] + "\n")
