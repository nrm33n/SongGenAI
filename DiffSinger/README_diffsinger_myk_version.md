# How to run diffsinger


## Use the MYK sing.py script 

```
python sing.py
```

```
python sing.py --lyrics "and another one about liking flowers or not as the case may be" --notes A,B,C --dur 1
```

## Run the built in commands

Resynthesize 'I like flowers' without any pitch modulation:

```
python3 synthesize.py --text "I like flowers default" --restore_step 160000 --mode single -p config/LJSpeech/preprocess.yaml -m config/LJSpeech/model.yaml -t config/LJSpeech/train.yaml
```


```
python3 synthesize.py --text "I like flowers duration four" --restore_step 160000 --mode single -p config/LJSpeech/preprocess.yaml -m config/LJSpeech/model.yaml -t config/LJSpeech/train.yaml --duration_control 4.0
```



