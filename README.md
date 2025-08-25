# AI Roleplay Trainer

## Overview

AI Roleplay Trainer is a CLI tool for practicing customer service skills through AI-powered roleplay scenarios. The tool simulates realistic customer interactions and provides feedback to help users improve their communication, empathy, and problem-solving abilities.

## Features

- Interactive CLI for customer service training
- Realistic scenario: Billing Dispute with a mildly frustrated customer
- AI-powered roleplay using Anthropic Claude
- Feedback and performance analysis after each scenario
- Easy-to-extend for new scenarios

## Scenario Example

**Scenario:** Billing Dispute - Unexpected Charge

- Customer: Sarah Chen, loyal for 2 years, confused about a $45 charge
- Your goal: Resolve the issue, demonstrate empathy, and communicate clearly

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/dr-rompecabezas/ai-roleplay-trainer.git
    cd ai-roleplay-trainer
    ```

2. **Install dependencies with [uv](https://github.com/astral-sh/uv):**

    ```sh
    uv sync
    ```

    Or use another modern Python tool (e.g. pipx, poetry) with Python 3.13+

3. **Set your Anthropic API key:**

    ```sh
    export ANTHROPIC_API_KEY='your-api-key-here'
    ```

Replace `'your-api-key-here'` with your actual API key from Anthropic.

## Usage

Run the CLI tool:

```sh
python main.py
```

Follow the prompts to start a scenario, respond to the customer, and receive feedback.

### Commands

- `start`: Begin the customer service scenario
- `coach`: Toggle coaching hints on/off
- `ref`: Show quick reference to scenario details
- `end`: Finish and receive feedback
- `quit`: Exit the program

## Requirements

- Python 3.13+
- API key for Anthropic Claude (set up as required by the `anthropic` Python package)

## Project Structure

- `main.py`: CLI tool and scenario logic
- `pyproject.toml`: Project metadata and dependencies
- `README.md`: Project documentation
- `ROADMAP.md`: Future development plans

## License

MIT License
