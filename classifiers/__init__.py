from fastapi import APIRouter

from .llm import (
    gpt_classifier, 
    deberta_review_classifier,
    bert_sentiment_german,
    distilbert_stock_news_classifier
)

from .lookup_lists import lookup_list

from .dates_and_times import (
    workday_classifier,
)

from .sentiment import (
    textblob_sentiment,
    vader_sentiment_classifier,
)

from .similarity import (
    cosine_similarity,
)

from .spelling import (
    spelling_check,
)

from .text_analysis import (
    emotionality_detection,
    language_detection,
    profanity_detection,
    sentence_complexity,
    textblob_subjectivity,
)

from .spelling import (
    spelling_check,
)

router = APIRouter()

for module in [
    textblob_sentiment,
    spelling_check,
    vader_sentiment_classifier,
    gpt_classifier,
    lookup_list,
    cosine_similarity,
    emotionality_detection,
    language_detection,
    profanity_detection,
    sentence_complexity,
    textblob_subjectivity,
    distilbert_stock_news_classifier,
    workday_classifier,
    deberta_review_classifier, 
    bert_sentiment_german
]:
    module_name = module.__name__.split(".")[-1]
    model_name = (
        "".join([term.capitalize() for term in module_name.split("_")]) + "Model"
    )
    exec(
        f"""
@router.post("/{module_name}")
async def api_{module_name}(request: {module_name}.{model_name}):
    return {module_name}.{module_name}(request)
    """
    )
