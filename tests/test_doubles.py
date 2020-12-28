class NerModelTestDouble:
    """
    Test Double for spaCy NLP model
    """
    def __init__(self, model):
        self.model = model
    
    def return_doc_ents(self, ents):
        self.ents = ents 

    def __call__(self, sent):
        return DocTestDoubles(sent, self.ents)

class DocTestDoubles:
    """
    Test double for spaCy Doc
    """
    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]
    
    def patched_method(self, attr, return_value):
        def patched(): return return_value
        setattr(self, attr, patched)
        return self
    
class SpanTestDouble:
    """
    Test double for spaCy Span
    """

    def __init__(self, text, label ):
        self.text = text
        self.label_ = label