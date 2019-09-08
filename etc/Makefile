.PHONY: fileids transcription

all: fileids transcription

fileids: pt-synesthesiam.fileids
	./make_train_test.py pt-synesthesiam_train.fileids pt-synesthesiam_test.fileids $<

transcription: pt-synesthesiam.transcription
	./make_train_test.py pt-synesthesiam_train.transcription pt-synesthesiam_test.transcription $<
