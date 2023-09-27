"""
IndoNLU: Benchmark and Resources for Evaluating Indonesian Natural Language Understanding
https://aclanthology.org/2020.aacl-main.85/

Classification, sentiment analysis, and NER tasks in Bahasa Indonesia.

Homepage:
"""
import numpy as np
from lm_eval.base import MultipleChoiceTask


_CITATION = """
@inproceedings{wilie-etal-2020-indonlu,
    title = "{I}ndo{NLU}: Benchmark and Resources for Evaluating {I}ndonesian Natural Language Understanding",
    author = "Wilie, Bryan  and
      Vincentio, Karissa  and
      Winata, Genta Indra  and
      Cahyawijaya, Samuel  and
      Li, Xiaohong  and
      Lim, Zhi Yuan  and
      Soleman, Sidik  and
      Mahendra, Rahmad  and
      Fung, Pascale  and
      Bahar, Syafri  and
      Purwarianti, Ayu",
    booktitle = "Proceedings of the 1st Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing",
    month = dec,
    year = "2020",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.aacl-main.85",
    pages = "843--857",
    abstract = "Although Indonesian is known to be the fourth most frequently used language over the internet, the research progress on this language in natural language processing (NLP) is slow-moving due to a lack of available resources. In response, we introduce the first-ever vast resource for training, evaluation, and benchmarking on Indonesian natural language understanding (IndoNLU) tasks. IndoNLU includes twelve tasks, ranging from single sentence classification to pair-sentences sequence labeling with different levels of complexity. The datasets for the tasks lie in different domains and styles to ensure task diversity. We also provide a set of Indonesian pre-trained models (IndoBERT) trained from a large and clean Indonesian dataset (Indo4B) collected from publicly available sources such as social media texts, blogs, news, and websites. We release baseline models for all twelve tasks, as well as the framework for benchmark evaluation, thus enabling everyone to benchmark their system performances.",
}
"""

SENTIMENTS = ["sadness", "anger", "love", "fear", "happy"]


class IndoNLUBenchmark(MultipleChoiceTask):
    VERSION = 0
    DATASET_PATH = "indonlp/indonlu"
    DATASET_NAME = "emot"

    def has_training_docs(self):
        return True

    def has_validation_docs(self):
        return True

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self._training_docs is None:
            self._training_docs = list(map(self._process_doc, self.dataset["train"]))
        return self._training_docs

    def validation_docs(self):
        return list(map(self._process_doc, self.dataset["validation"]))

    def test_docs(self):
        return list(map(self._process_doc, self.dataset["test"]))

    def _process_doc(self, doc):
        return {
            "query": f"""Does this text's sentiment match sadness, anger, love, fear, or happy?
{doc["tweet"]}\nAnswer:""",
            "choices": SENTIMENTS,
            "gold": doc["label"],
        }

    def doc_to_text(self, doc):
        return doc["query"]
