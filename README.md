# Portuguese Acoustic Model for CMU Sphinx

This is an attempt to train a CMU Sphinx acoustic model for Portuguese (pt-br) using the datasets found in [an ASR study for Brazillian Portuguese](https://github.com/igormq/asr-study). The resulting model is used in [Rhasspy](https://github.com/synesthesiam/rhasspy).

Following the [sphinxtrain tutorial](https://cmusphinx.github.io/wiki/tutorialam/), a continuous 200 senome acoustic model was train on approximately 8 hours of speech data. No attempt was made to validate or clean the data, since I don't know Portuguese. The trained model does poorly, as expected on so little data, but may be useful enough for a very constrained domain.
