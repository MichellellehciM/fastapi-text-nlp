# 處理摘要 & 關鍵字提取

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

#  加載 NLP 模型
nlp = spacy.load("zh_core_web_sm")  # 支援中文
nlp_en = spacy.load("en_core_web_sm")  # 支援英文

def summarize_text(text: str):
    """ 使用 NLP 進行文本摘要 & 關鍵字提取 """
    doc = nlp(text) if any(ord(c) > 127 for c in text) else nlp_en(text)

    # 生成摘要
    sentences = [sent.text for sent in doc.sents]
    summary = " ".join(sentences[:min(3, len(sentences))])  # 取前三句作摘要

    # 提取關鍵字
    tfidf = TfidfVectorizer(stop_words="english" if doc.lang_ == "en" else None)
    vec = tfidf.fit_transform([text])
    keywords = np.array(tfidf.get_feature_names_out())[vec.toarray().argsort()[0, -5:]]  # 取前 5 個關鍵字

    return summary, keywords.tolist()
