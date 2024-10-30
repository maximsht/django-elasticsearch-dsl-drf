from elasticsearch_dsl import analyzer

__all__ = (
    'html_strip',
)

# The ``standard`` filter has been removed in Elasticsearch 7.x.
_filters = ["standard", "lowercase", "stop", "snowball"]

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=_filters,
    char_filter=["html_strip"]
)
