# 🧠 Agentic Design: Trolley Problem Simulation with GPT

This project explores **agentic design** through an interactive and morally complex simulation of the Trolley Problem. Using **OpenAI's GPT**, the simulation tests how an AI agent navigates difficult ethical decisions when faced with uncertain outcomes and morally ambiguous traits.

---

## 🚇 Project Summary

A trolley is heading down a track and must choose between two groups of people. Each group contains individuals with different **traits**, some of which impact their **chance of escape** (e.g. age, physical conditions), and others that are purely **moral dimensions** (e.g. profession, criminal record).

The twist:  
**ChatGPT is the one making the decisions** — and it doesn’t know the actual escape chances, only the visible traits.

---

## 🧩 How It Works

- Each scenario generates two random tracks (`track_A` and `track_B`) filled with unique **bystanders**.
- Each bystander has a set of given traits (e.g., `"doctor"`, `"athlete"`, `"elderly"`).
- GPT receives the traits and must decide which group should be sacrificed.
- The system records each decision and builds a **moral values index** over time, showing which traits GPT tends to save or sacrifice.

---

## ✨ Features

- 🤖 **GPT-powered decision-making**
- ⚖️ **Trait-based moral simulation**
- 📊 **Quantitative moral index tracking**
- 🔍 **Hidden escape probabilities** (not visible to GPT)
- 📝 **Decision logging for ethical analysis**

---

## 📦 Tech Stack

- Python 3.9+
- OpenAI GPT (via `openai` API)


---

## 🔧 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mathuebra/Trolley-AI-Problem.git
cd trolley-gpt-simulation
```

### 2. Install dependencies

```bash
pip install openai
pip install matplotlib
pip install seaborn
pip install pandas
```

### 3. Set your OpenAI API key

Create a `.env` file or set it in your environment:

```bash
export OPENAI_API_KEY="your-api-key"
```
Or inside the code:

```bash
import openai
openai.api_key = "your-api-key"
```

### 4. Run the simulation

```bash
python final.py
```

