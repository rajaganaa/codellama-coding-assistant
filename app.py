from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

def generate(prompt, max_tokens=300):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=max_tokens, do_sample=False)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result.split("### Response:")[-1].strip()

@app.post("/complete")
def complete(req: CodeRequest):
    prompt = f"### Instruction:\nComplete this code\n\n### Input:\n{req.code}\n\n### Response:\n"
    return {"completion": generate(prompt)}

@app.post("/debug")
def debug(req: CodeRequest):
    prompt = f"### Instruction:\nFix the bug\n\n### Input:\n{req.code}\n\n### Response:\n"
    return {"fixed_code": generate(prompt)}

@app.post("/explain")
def explain(req: CodeRequest):
    prompt = f"### Instruction:\nExplain this code\n\n### Input:\n{req.code}\n\n### Response:\n"
    return {"explanation": generate(prompt)}
