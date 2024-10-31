from transformers import pipeline

# Create NER pipeline
ner_pipeline = pipeline("ner", grouped_entities=True)

# Perform NER on text
text = "My name is Wolfgang and I live in Berlin"
results = ner_pipeline(text)

print(results)