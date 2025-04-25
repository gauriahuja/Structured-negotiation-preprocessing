# Structured-negotiation-preprocessing
Structuring negotiation dialogues to support agentic AI coaching, feedback generation, and healthcare simulation research
## Objective

This project parses and structures negotiation dialogues from the [End-to-End Negotiator dataset](https://github.com/facebookresearch/end-to-end-negotiator) to create clean, human-readable formats. These structured dialogues are intended for use in downstream agentic AI systems, including training negotiation feedback agents and decision support models, especially within healthcare AI research.

---

## Technologies Used

- **Python 3.9+**
- **Basic text parsing and string processing**
- **File handling with Python**

---

## Dataset Source

- **Dataset:** Deal or No Deal Negotiation Corpus
- **Original Repository:** [Facebook Research - End-to-End Negotiator](https://github.com/facebookresearch/end-to-end-negotiator)
- **Details:** Human-human negotiation dialogues involving division of hats, balls, and books, labeled with item values and agreed splits.

---

## Project Structure

```bash
structured-negotiation-preprocessing/
├── data/
│   ├── train.txt                 # Raw negotiation dialogue data
│
├── scripts/
│   ├── parse_negotiation.py     # Script to parse dialogues and format outputs
│
├── outputs/
│   ├── generated_script_output.txt  # Structured, human-readable negotiation dialogues
│
├── README.md
```

---

## Installation
**Install dependencies:**
   *(No external libraries required beyond standard Python 3.9+ libraries.)*


## How It Works

- **Step 1:** Read the raw `train.txt` dataset.
- **Step 2:** Extract fields such as `<input>`, `<dialogue>`, `<output>`, and `<partner_input>`.
- **Step 3:** Format dialogues into a clean, readable script.
- **Step 4:** Save structured outputs into `generated_script_output.txt`.

---

## Example Output

```
Your Inventory: 1 hat, 2 balls, 3 books
Your Goal Values: hats=3, balls=2, books=5

Dialogue:
Agent 1: I would like both books if possible.
Agent 2: Fine, then I will take the balls.
Agent 1: Sounds good.
...

Final Agreement: (item division details)
```

---

## Research Relevance

The structured outputs from this project support:
- AI agent negotiation training
- Feedback coaching model development
- Behavioral simulation for healthcare decision-making support
- Ethical negotiation modeling in agentic AI systems

---

## License
This project is intended for academic and research purposes under the University of Florida AI Systems Research Initiative.

---

## Author
**Gauri Ahuja**  
M.S. in Computer Science, University of Florida  
[LinkedIn](https://linkedin.com/in/gauri777) | [Email](mailto:ahujagauri@ufl.edu)
