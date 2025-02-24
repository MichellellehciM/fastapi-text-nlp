import spacy
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
import jieba.analyse  # 讓 `TextRank` 更準確

#  加載 NLP 模型
nlp = spacy.load("zh_core_web_sm")  # 支援中文
nlp_en = spacy.load("en_core_web_sm")  # 支援英文

# 自訂中文停用詞
STOP_WORDS = {"的", "是", "在", "和", "有", "可以", "進行", "使用", "來", "說", "這個", "但", "也"}

def extract_keywords(text, num_keywords=5):
    """ NLP 提取關鍵字（TextRank for 中文, TF-IDF for 英文） """
    
    # 如果是英文，使用 TF-IDF 來提取關鍵字
    if all(ord(c) < 127 for c in text):  # 判斷是否為純英文
        tfidf = TfidfVectorizer(stop_words="english")
        vec = tfidf.fit_transform([text])
        keywords = np.array(tfidf.get_feature_names_out())[vec.toarray().argsort()[0, -num_keywords:]]
        return keywords.tolist()
    
    # 如果是中文，使用 TextRank 來提取關鍵字
    return jieba.analyse.textrank(text, topK=num_keywords, withWeight=False)


def summarize_text(text: str, num_sentences=None, num_keywords=5):
    """ NLP 自動摘要 (LexRank) + 精準關鍵字提取 (TextRank) """
    doc = nlp(text) if any(ord(c) > 127 for c in text) else nlp_en(text)
    sentences = [sent.text.strip() for sent in doc.sents]  # 去除空白 & 確保句子完整

    if not sentences:
        return "", []  # 避免處理空內容時報錯

    # **根據文章長度動態調整摘要長度**
    if num_sentences is None:
        num_sentences = max(3, len(sentences) // 4)  # 文章長度越長，摘要句數越多

    # **生成摘要 (LexRank，類似 TextRank 但更適合長文)**
    tfidf = TfidfVectorizer()
    sentence_vectors = tfidf.fit_transform(sentences).toarray()
    similarity_matrix = np.dot(sentence_vectors, sentence_vectors.T)

    # **使用 LexRank 計算句子權重**
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)

    # **依據分數排序並選擇重要句子**
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary_sentences = [s for _, s in ranked_sentences[:num_sentences]]

    # **將摘要變成條列式**
    summary = "\n- " + "\n- ".join(summary_sentences)

    # **提取關鍵字 (使用 TextRank)**
    keywords = extract_keywords(text, num_keywords)

    return summary, keywords


# # 測試
# text = "你的新聞文章..."
# summary = summarize_text(text)
# keywords = extract_keywords(text)
# print("📌 摘要：", summary)
# print("🔑 關鍵字：", keywords)