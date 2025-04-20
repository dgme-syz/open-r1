from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "/home/syz/projects/open-r1/data/Qwen2.5-0.5B-Open-R1-SFT"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="cuda"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "the area of square $\mathrm{ABCD}$ is 196 square centimeters, and it contains two partially overlapping smaller squares. The larger of the two smaller squares has an area that is 4 times the area of the smaller one, and the overlapping area of the two squares is 1 square centimeter. Therefore, the area of the shaded part is $\qquad$ square centimeters."
messages = [
    {"role": "system", "content": "You are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: <think>\n...\n</think>\n<answer>\n...\n</answer>"},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

print(model_inputs)
# generated_ids = model.generate(
#     **model_inputs,
#     max_new_tokens=1024 
# )
# generated_ids = [
#     output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
# ]

# response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
# print(response)
