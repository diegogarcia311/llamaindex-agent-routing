# LlamaIndex Agent-Based Routing for NLP Tasks

This project demonstrates agent-based routing using LlamaIndex and a vector database for intelligent, category-specific NLP handling. It mimics real-world scenarios such as **automated expense classification**, where inputs are routed to specialized LLM chains based on semantic context and customer profile.

---

## 🔍 Use Case

A dynamic classification and reasoning system for expenses:
- Route based on semantic similarity and metadata
- Each route is backed by a vector store and specialized agent (e.g., Travel, Meals, Tech)
- Response outputs validated against safety/format constraints

---

## 🧱 Architecture Overview

```plaintext
          +--------------------+
Input --> | Expense Classifier | --+
          +--------------------+  |
                                  ↓
      +-------------------+   +------------------+
      | Travel Vector DB  |   | Tech Vector DB   |   ...
      +-------------------+   +------------------+
               ↓                     ↓
      [TravelAgent Chain]     [TechAgent Chain]
               ↓                     ↓
           Response Validator ----> Output
