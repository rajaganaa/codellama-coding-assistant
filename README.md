# 🦙 CodeLlama Coding Assistant

> Fine-tuned CodeLlama-7B with QLoRA on CodeAlpaca-20K | Deployed on AWS SageMaker

## 🚀 Live Demo
👉 **[Try it here](https://huggingface.co/spaces/RajGana/codellama-demo)**

## 🤗 Model on HuggingFace
👉 https://huggingface.co/RajGana/codellama-coding-assistant

## 📌 What it does
- ✅ **Complete** — Auto-completes Python functions
- 🐛 **Debug** — Finds and fixes bugs with explanation  
- 📖 **Explain** — Explains code in plain English

## 🛠 Tech Stack
| Component | Technology |
|-----------|-----------|
| Base Model | CodeLlama-7B (Meta) |
| Fine-tuning | QLoRA (4-bit quantization) |
| Dataset | CodeAlpaca-20K |
| Training | AWS SageMaker ml.g4dn.xlarge |
| Storage | S3 + HuggingFace Hub |
| Inference | Groq API (Llama-3.1-8b-instant) |
| UI | Gradio on HuggingFace Spaces |

## 🏗 Architecture
SageMaker Training → S3 → HuggingFace Hub → Gradio Space → Groq Inference API

## 📊 Training Details
- Epochs: 3
- LoRA rank: 16
- Batch size: 4
- Quantization: 4-bit (bitsandbytes)
- Base model: codellama/CodeLlama-7b-hf
