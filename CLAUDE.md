# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

**Environment Setup:**

```bash
uv sync  # Install dependencies and sync environment
```

**Running the Application:**

```bash
# Use default provider (Anthropic Claude)
uv run python main.py

# Specify provider via CLI
uv run python main.py --provider openai
uv run python main.py --provider anthropic

# Specify provider via environment variable
LLM_PROVIDER=openai uv run python main.py
```

**Development Tools:**

```bash
# Code formatting
uv run black .

# Test provider functionality
uv run python test_providers.py
```

## Architecture Overview

### Core Components

**main.py** - Primary application with `CustomerServiceTrainer` class containing:

- Comprehensive scenario briefing system with business context
- CLI-based training interface with coaching system
- Conversation state management and feedback generation

**llm_providers.py** - Provider abstraction layer featuring:

- Abstract `LLMProvider` base class for consistent API interface
- `AnthropicProvider` using Claude Sonnet models via `messages.create()`
- `OpenAIProvider` using GPT models via `responses.create()` endpoint
- Factory function `create_provider()` for configuration-based instantiation

**test_providers.py** - Provider validation utilities for testing both API integrations

### Provider Pattern Architecture

The system uses a provider pattern to abstract LLM APIs:

1. **Configuration**: Providers selected via CLI flag `--provider` or `LLM_PROVIDER` environment variable
2. **Instantiation**: Factory pattern creates appropriate provider instance
3. **Usage**: All providers implement consistent `make_call(messages, max_tokens)` interface
4. **Extension**: New providers easily added by implementing `LLMProvider` abstract class

### Training Flow Architecture

1. **Briefing Phase**: Displays comprehensive scenario context including company details, policies, and customer background
2. **Roleplay Phase**: AI customer (Sarah Chen) interacts with trainee, maintaining character consistency
3. **Coaching System**: Optional real-time hints via conversation analysis (toggleable with `coach` command)
4. **Feedback Phase**: Post-scenario performance analysis using conversation history

## API Requirements

**Anthropic (default)**: Requires `ANTHROPIC_API_KEY` environment variable
**OpenAI**: Requires `OPENAI_API_KEY` environment variable

## Key Implementation Notes

- OpenAI integration uses the `responses.create()` API (not chat completions)
- Conversation history maintained as list of message dictionaries with `role` and `content` keys  
- Provider switching preserves full functionality without code changes
- All LLM calls go through the provider abstraction - never call APIs directly
- Training scenarios include detailed business context to prevent knowledge gaps from interfering with skill development
