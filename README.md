# SongGenAI

This is a pop music generator using transformer networks. It consists of 3 parts:  
* a lyric generator using the GPT-2 transformer model 
* singing voice synthesis using the DiffSinger model with a HifiGan deep learning based vocoder translate control data and convert synthesis model into audio. 
The specific vocoder used is by Kong, J., Kim, J., & Bae, J. from the 2020 paper Hifi-gan: Generative adversarial networks for efficient and high fidelity speech. 
It also uses an LJS speech model. 
* a music generator using the Music-VAE auto-encoder model. 

The latent space takes in a 2 or 16 bar musical sequence with multiple parts (e.g. 1-melody, 3-bass, melody, drums trio). 
It encodes to a 256 or 512 D latent vector. You can analyse the type of sound Music-VAE generates using the midi_analyser.py and midi_note_extractor.py files in the analyse-and-mix folder.

The kind of output it produces looks like this:
![midi_analyser](https://user-images.githubusercontent.com/84393679/224991460-574f4983-63eb-44e1-9c81-82d20a087517.jpg)
![midi_note_extractor](https://user-images.githubusercontent.com/84393679/224991479-990f7e6a-3121-41a8-adb5-6854bf5b50f7.jpg)



