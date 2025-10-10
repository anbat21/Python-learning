"""
Created on Jul 1 11:38:46 2025

@author: Vaishali Siddeshwar
"""
from transformers import pipeline

# ----------------------- Pipeline Initialization -----------------------

def get_pipeline(task: str, model: str = None):
    """Initialize and return a HuggingFace pipeline for a given task."""
    if model:
        return pipeline(task, model=model)
    return pipeline(task)


# ----------------------- Individual Tasks -----------------------

def perform_sentiment_analysis(text: str):
    classifier = get_pipeline("sentiment-analysis")
    return classifier(text)


def perform_batch_sentiment_analysis(texts: list):
    classifier = get_pipeline("sentiment-analysis")
    return classifier(texts)


def perform_text_generation(prompt: str, max_len=30, num_sequences=2):
    generator = get_pipeline("text-generation", model="mistralai/Ministral-8B-Instruct-2410")
    return generator(prompt, max_length=max_len, num_return_sequences=num_sequences)


def perform_summarization(text: str, max_len=130, min_len=30):
    summarizer = get_pipeline("summarization")
    return summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)

def perform_text_translation(text: str):
  en_fr_translator = pipeline("translation_es_to_en", model="Helsinki-NLP/opus-mt-es-en")
  return display_text_translation(en_fr_translator(text))


def generate_text_mistral():
    messages = [
        {"role": "user", "content": "Who are you?"},
    ]
    text_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")
    return display_text_mistral(text_pipeline(messages))


# ----------------------- Output Display Helpers -----------------------

def display_sentiment(result):
    for item in result:
        print(f"Sentiment: {item['label']}, Confidence: {round(item['score'], 2)}")


def display_batch_sentiment(texts, results):
    for text, prediction in zip(texts, results):
        print(
            f"Input Text: {text}\nPredicted Sentiment: {prediction['label']} (Confidence: {round(prediction['score'], 2)})\n")


def display_generated_text(results):
    for i, output in enumerate(results, 1):
        print(f"Generated #{i}: {output['generated_text']}")


def display_summary(summary_result):
    print("Summary:")
    print(summary_result[0]['summary_text'])


def display_text_translation(translations):
    print("Translated Text: ")
    print(translations[0]['translation_text'])


def display_text_mistral(response):
    print(response[-1]['generated_text'][-1]['content'])
    
# ----------------------- Main Execution -----------------------

def main():
    # 1. Sentiment Analysis
    text = "I've been waiting for a HuggingFace course my whole life."
    sentiment_result = perform_sentiment_analysis(text)
    display_sentiment(sentiment_result)

    # 2. Text Generation
    generated = perform_text_generation("Canada is a country in North America.")
    display_generated_text(generated)

    # 3. Summarization
    long_text = """Canada is a country in North America. Its ten provinces and three territories extend from the
    Atlantic Ocean to the Pacific Ocean and northward into the Arctic Ocean, making it the world's second-largest
    country by total area, with the world's longest coastline. Its border with the United States is the longest
    international land border. The country is characterized by a wide range of both meteorologic and geological
    regions. With a population of over 41 million, it has widely varying population densities, with the majority
    residing in urban areas and large areas of the country being sparsely populated. Canada's capital is Ottawa and
    its three largest metropolitan areas are Toronto, Montreal, and Vancouver. Indigenous peoples have continuously
    inhabited what is now Canada for thousands of years. Beginning in the 16th century, British and French
    expeditions explored and later settled along the Atlantic coast. As a consequence of various armed conflicts,
    France ceded nearly all of its colonies in North America in 1763. In 1867, with the union of three British North
    American colonies through Confederation, Canada was formed as a federal dominion of four provinces. This began an
    accretion of provinces and territories resulting in the displacement of Indigenous populations, and a process of
    increasing autonomy from the United Kingdom. This increased sovereignty was highlighted by the Statute of
    Westminster, 1931, and culminated in the Canada Act 1982, which severed the vestiges of legal dependence on the
    Parliament of the United Kingdom. Canada is a parliamentary democracy and a constitutional monarchy in the
    Westminster tradition. The country's head of government is the prime minister, who holds office by virtue of
    their ability to command the confidence of the elected House of Commons and is appointed by the governor general,
    representing the monarch of Canada, the ceremonial head of state. The country is a Commonwealth realm and is
    officially bilingual (English and French) in the federal jurisdiction. It is very highly ranked in international
    measurements of government transparency, quality of life, economic competitiveness, innovation, education and
    human rights. It is one of the world's most ethnically diverse and multicultural nations, the product of
    large-scale immigration. Canada's long and complex relationship with the United States has had a significant
    impact on its history, economy, and culture. A developed country, Canada has a high nominal per capita income
    globally and its advanced economy ranks among the largest in the world by nominal GDP, relying chiefly upon its
    abundant natural resources and well-developed international trade networks. Recognized as a middle power,
    Canada's support for multilateralism and internationalism has been closely related to its foreign relations
    policies of peacekeeping and aid for developing countries. Canada promotes its domestically shared values through
    participation in multiple international organizations and forums."""
    summary = perform_summarization(long_text)
    display_summary(summary)

    # 4. Batch Sentiment Analysis
    batch_texts = [
        "I've been waiting for a HuggingFace course my whole life.",
        "Python is good.",
        "C++ is outdated."
    ]
    batch_results = perform_batch_sentiment_analysis(batch_texts)
    display_batch_sentiment(batch_texts, batch_results)
    
    perform_text_translation("Este curso sobre LLMs se está poniendo muy interesante")
    
    generate_text_mistral()

if __name__ == "__main__":  
    
    main()


