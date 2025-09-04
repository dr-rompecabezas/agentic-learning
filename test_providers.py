#!/usr/bin/env python3
"""
Test script to verify LLM providers work correctly
"""

from llm_providers import create_provider, AnthropicProvider, OpenAIProvider


def test_provider_creation():
    """Test that providers can be created successfully"""
    print("Testing provider creation...")

    # Test Anthropic provider
    try:
        anthropic_provider = create_provider("anthropic")
        print(f"✅ Anthropic provider created: {type(anthropic_provider).__name__}")
    except Exception as e:
        print(f"❌ Anthropic provider failed: {e}")

    # Test OpenAI provider
    try:
        openai_provider = create_provider("openai")
        print(f"✅ OpenAI provider created: {type(openai_provider).__name__}")
    except Exception as e:
        print(f"❌ OpenAI provider failed: {e}")

    # Test direct instantiation
    try:
        direct_anthropic = AnthropicProvider()
        print(f"✅ Direct Anthropic provider: {type(direct_anthropic).__name__}")
    except Exception as e:
        print(f"❌ Direct Anthropic failed: {e}")

    try:
        direct_openai = OpenAIProvider()
        print(f"✅ Direct OpenAI provider: {type(direct_openai).__name__}")
    except Exception as e:
        print(f"❌ Direct OpenAI failed: {e}")


def test_simple_api_calls():
    """Test simple API calls to both providers"""
    print("\nTesting simple API calls...")

    test_messages = [{"role": "user", "content": "Say hello in exactly 3 words."}]

    # Test Anthropic
    try:
        anthropic_provider = create_provider("anthropic")
        response = anthropic_provider.make_call(test_messages, max_tokens=50)
        print(f"✅ Anthropic response: {response[:50]}...")
    except Exception as e:
        print(f"❌ Anthropic API call failed: {e}")

    # Test OpenAI
    try:
        openai_provider = create_provider("openai")
        response = openai_provider.make_call(test_messages, max_tokens=50)
        print(f"✅ OpenAI response: {response[:50]}...")
    except Exception as e:
        print(f"❌ OpenAI API call failed: {e}")


if __name__ == "__main__":
    test_provider_creation()
    test_simple_api_calls()
