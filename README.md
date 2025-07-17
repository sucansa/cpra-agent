# cpra-agent
# 🛡️ CPRA Agentic AI Compliance System

**Automating Data Privacy Compliance Using AI Agents (Built with CrewAI)**

This project is a proof-of-concept AI agent workflow designed to automate the interpretation and enforcement of California Privacy Rights Act (CPRA) obligations. It was built over a weekend using open-source tools—demonstrating how agentic AI can make regulatory compliance faster, more scalable, and less dependent on manual legal interpretation.

---

## 🧠 What It Does

This multi-agent system reads CPRA legal text, identifies changes from previous versions, and translates them into actionable technical controls. It simulates how a compliance team might respond to regulatory updates—but entirely through autonomous AI agents.

---

## ⚙️ Architecture Overview

The system includes three AI agents:

| Agent | Role | Description |
|-------|------|-------------|
| 🧾 `Regulation Tracker` | Compliance Analyst | Compares new CPRA with the prior version and flags what changed |
| 📜 `Policy Converter` | Compliance Specialist | Translates changed clauses into internal governance policies |
| 🛠 `Control Designer` | Enterprise Architect | Suggests how to technically enforce each policy in cloud/data systems |

Agents are coordinated using the [CrewAI](https://docs.crewai.com/) framework.

---

## 🔧 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/cpra-agent.git
cd cpra-agent
