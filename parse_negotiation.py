import re

def parse_train_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()

    # Use regex to find all full dialogue blocks in the file
    pattern = r"<input>.*?</input>.*?<dialogue>.*?</dialogue>.*?<output>.*?</output>.*?<partner_input>.*?</partner_input>"
    matches = re.findall(pattern, text)

    dialogue_blocks = []

    for match in matches:
        input_match = re.search(r"<input>(.*?)</input>", match)
        dialogue_match = re.search(r"<dialogue>(.*?)</dialogue>", match)
        output_match = re.search(r"<output>(.*?)</output>", match)
        partner_input_match = re.search(r"<partner_input>(.*?)</partner_input>", match)

        if input_match and dialogue_match and output_match and partner_input_match:
            dialogue_blocks.append({
                "input": input_match.group(1).strip(),
                "dialogue": dialogue_match.group(1).strip(),
                "output": output_match.group(1).strip(),
                "partner_input": partner_input_match.group(1).strip()
            })

    return dialogue_blocks

# === File path ===
file_path = r"E:\RESEARCH WORK\Dataset 3\train.txt"

# === Parse the file ===
dialogues = parse_train_file(file_path)

# === Summary ===
print(f"\n Loaded {len(dialogues)} dialogues from train.txt")

if len(dialogues) == 0:
    print(" No dialogues found. Please check if the tags are formatted correctly.")
else:
    print("\n Sample Dialogues (First 3):\n")
    for i, d in enumerate(dialogues[:3]):
        print(f"🔹 Dialogue {i+1}")
        print("Input:         ", d["input"])
        print("Dialogue:      ", d["dialogue"])
        print("Output:        ", d["output"])
        print("Partner Input: ", d["partner_input"])
        print("-" * 50)

        # === Create a conversation script from all dialogues ===
script_lines = []

for i, d in enumerate(dialogues[:50]):  # change 50 to 100 or more if needed
    script_lines.append(f"Dialogue {i+1}")
    script_lines.append(f"INPUT VALUES: {d['input']}")
    script_lines.append(f"CONVERSATION: {d['dialogue']}")
    script_lines.append(f"OUTPUT: {d['output']}")
    script_lines.append(f"PARTNER INPUT: {d['partner_input']}")
    script_lines.append("-" * 80)

# Join into a single script
final_script = "\n".join(script_lines)

# === Save the script to a .txt file ===
output_txt_path = r"E:\RESEARCH WORK\Dataset 3\generated_script_output.txt"

with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write(final_script)

print(f"\n Full script saved to: {output_txt_path}")
