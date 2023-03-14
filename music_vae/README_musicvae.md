# How to run musicvae js scripts

## Serve the models directory with a local web server on port 8081

The scripts have to download the music vae models from a web server.
They expect the following address to serve a folder containing a model:

http://127.0.0.1:8081/models/multitrack_chords/

In my case, I run:

```
./node_modules/http-server/bin/http-server -p8081 ./
```
in the top level directory which contains the models folder. 

## Install node modules (already available in the Coursera lab)

In the folder that contains the package.json file, run this command:

```
npm install 
```

## Run a script

Now you are ready to run a script:

```
node 1_vae_simplest.js
```

## Render a midi file to a wav

Some of the scripts output a midi file. E.g.:

```
node 3_vae_to_phrase_midi.js
```
This will output a file called phrase.mid. If you want to be able to hear the music, you need to render the midi file to audio.

You can do this with the fluidsynth program. There is a script to help you:

```
. midi_to_wav.sh phrase.mid 
```

This should render a wav file called phrase.mid.wav. Download it and play it!


