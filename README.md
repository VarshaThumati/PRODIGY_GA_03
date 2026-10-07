# PRODIGY TASK 03 — Text Generation with Markov Chains

<p align="center">
  <b>A Simple Probabilistic Text Generation System using Markov Chains</b>
</p>

<p align="center">
  Generative AI Internship — Prodigy InfoTech
</p>

---

## 📌 Project Overview

This project implements a **text generation system using Markov Chains**, developed as part of the **Generative AI Internship at Prodigy InfoTech**.

The system learns statistical relationships between words from a given text corpus and uses those learned relationships to generate new text. Users can provide a starting word or phrase, after which the model generates multiple sentences based on the patterns learned from the corpus.

Unlike modern Large Language Models (LLMs), this project does not use neural networks or transformer-based architectures. Instead, it demonstrates the fundamental concept of **probabilistic text generation using Markov Chains**.

This project provides a simple and practical introduction to concepts such as:

- Markov Chains
- Probabilistic text generation
- Natural Language Processing
- Word relationships
- Predictive text generation
- Corpus-based learning

---

## 🎯 Objective

The primary objective of this project is to implement a simple text generation algorithm using **Markov Chains**.

### Key Objectives

- Understand the fundamentals of Markov Chains.
- Learn how text can be represented as probabilistic word relationships.
- Build a text generation model using an existing text corpus.
- Predict possible next words based on previously observed words.
- Generate new sentences using learned word patterns.
- Allow users to provide a starting word or phrase.
- Demonstrate the basic principles behind predictive text generation.
- Gain practical experience with Python-based Natural Language Processing.

---

## ✨ Key Features

### 🔹 Markov Chain Text Generation

The project uses a Markov Chain model to learn relationships between words in the training corpus and generate new text based on those patterns.

### 🔹 Custom Text Corpus

A custom text corpus containing content related to Artificial Intelligence, Machine Learning, Data Science, Python, NLP, and Generative AI is used as the training data.

### 🔹 User-Defined Starting Text

Users can enter a starting word or phrase, and the model attempts to generate sentences beginning with the provided input.

Example:

```text
Enter a starting word or phrase: artificial
```
---

## 🛠️ Technology Stack

### Programming Language
- **Python** — Used to implement the text generation system and handle the training corpus.

### Libraries
- **Markovify** — Used to build the Markov Chain text generation model.
- **Pathlib** — Used for handling file and directory paths.

### Development Tools
- **Visual Studio Code** — Used for project development and testing.
- **PowerShell** — Used for executing Python commands and managing the virtual environment.
- **Git** — Used for version control.
- **GitHub** — Used for source code management and project hosting.

### Core Concepts
- Markov Chains
- Probability-Based Text Generation
- Natural Language Processing (NLP)
- Predictive Text Generation
- Statistical Language Modeling
- Corpus-Based Learning

---

## 🔄 Project Flow

The complete workflow of the project is:

```text
                 ┌──────────────────────┐
                 │     Text Corpus      │
                 │      corpus.txt      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Load Training     │
                 │       Text          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Build Markov Chain │
                 │       Model         │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Learn Word-to-Word   │
                 │    Relationships     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   User Enters a     │
                 │ Starting Word/Phrase│
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Find Possible Next   │
                 │       Words          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Probabilistically    │
                 │ Select Next Word     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Generate Multiple    │
                 │     Sentences        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Display Generated    │
                 │       Text           │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Save Results to      │
                 │ generated_text.txt  │
                 └──────────────────────┘
