# AI Roleplay Trainer

## Overview

AI Roleplay Trainer is a CLI tool for practicing customer service skills through AI-powered roleplay scenarios. The tool simulates realistic customer interactions and provides feedback to help users improve their communication, empathy, and problem-solving abilities.

## Features

- Interactive CLI for customer service training
- Realistic scenario: Billing Dispute with a mildly frustrated customer
- **Multi-provider AI support**: Choose between Anthropic Claude or OpenAI GPT
- Feedback and performance analysis after each scenario
- Configurable coaching hints during conversations
- Easy-to-extend for new scenarios and providers

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

3. **Set your API key(s):**

    For Anthropic Claude (default):

    ```sh
    export ANTHROPIC_API_KEY='your-anthropic-key-here'
    ```

    For OpenAI GPT:

    ```sh
    export OPENAI_API_KEY='your-openai-key-here'
    ```

## Usage

Run the CLI tool with your preferred AI provider:

```sh
# Use Anthropic Claude (default)
uv run python main.py

# Use OpenAI GPT
uv run python main.py --provider openai

# Or set via environment variable
LLM_PROVIDER=openai uv run python main.py
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
- API key for your chosen provider:
  - Anthropic Claude: `anthropic` Python package
  - OpenAI GPT: `openai` Python package (v1.105.0+)

## Project Structure

- `main.py`: CLI tool and scenario logic
- `llm_providers.py`: Multi-provider AI abstraction layer
- `test_providers.py`: Provider testing utilities
- `pyproject.toml`: Project metadata and dependencies
- `README.md`: Project documentation
- `ROADMAP.md`: Future development plans

## License

MIT License
