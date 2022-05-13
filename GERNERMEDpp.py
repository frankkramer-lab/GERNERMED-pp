#!/usr/bin/env python3
import spacy
import os, sys

dpath = os.path.dirname(__file__)
model_dir = os.path.join(dpath, "model")

def main():
    if not os.path.exists(model_dir) or not os.path.isdir(model_dir):
        print(f"Model not found at: {os.path.abspath(model_dir)}", file=sys.stderr)
        sys.exit(-1)

    nlp = spacy.load(model_dir)
    sample_sentence = "Zur weiteren Bekämpfung der Symptomatik wird die Einnahme von täglich 100mg Cortison als Tablette empfohlen."
    doc = nlp(sample_sentence)

    print(f"Sample sentence: {sample_sentence}")
    for e in doc.ents:
        print(f"[{e.label_}]: {e.text} ({e.start_char}, {e.end_char})")

if __name__ == "__main__":
    main()