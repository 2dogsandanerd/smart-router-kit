# Smart Router Kit

**Stop sending every query to every data source.** A lightweight, production-ready RAG routing toolkit that uses an LLM to intelligently route user queries to the right tool or data source.

*Extracted from a battle-tested, production RAG platform.*

---

### ✨ This is the second pillar of a bigger vision.

This router is a core component of a much larger, **private-by-design AI platform** I'm building. First, we ingest data intelligently (`smart-ingest-kit`), now we query it intelligently.

If you believe in building efficient, scalable, and private AI systems, follow the journey.

➡️ **[Get early access and join the Private AI Lab here](https://mailchi.mp/38a074f598a3/github_catcher)** ⬅️

---

## 🤔 Why a Smart Router?

Standard RAG pipelines are dumb. They treat every user question the same and throw it against all available data. This is slow, expensive (multiple API calls), and often leads to inaccurate answers when data sources conflict.

A smart router acts like an intelligent switchboard. It analyzes the user's intent *before* the search.

## ✅ Features

*   **LLM-as-a-Router:** Uses a small, local LLM to classify the user's query.
*   **Intent-Based Routing:** Understands whether the user wants to:
    *   `query` a specific knowledge base (e.g., "What does the legal doc say?").
    *   `summarize` a document.
    *   `compare` information across multiple sources.
*   **Dynamic Tool Selection:** Can route queries to different vector stores, traditional keyword search, or even a SQL database based on the query's nature.
*   **Reduces Costs & Latency:** Avoids unnecessary API calls and searches, leading to faster and cheaper responses.
*   **Increases Accuracy:** Prevents context collision by only searching in the most relevant data source.

## 🚀 Quick Start

(Coming soon - I'm working on making this a pip-installable package!)

## 🤝 Contributing

This is a new open-source project and I'm open to any ideas or contributions. Feel free to open an issue or a pull request.
