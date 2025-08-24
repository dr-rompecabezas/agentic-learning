#!/usr/bin/env python3
"""
Customer Service Training CLI Prototype
A simple CLI tool to practice customer service skills with AI roleplay
"""

import anthropic
import json
import requests
import sys


client = anthropic.Anthropic()

class CustomerServiceTrainer:
    def __init__(self):
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.conversation_history = []
        self.scenario_active = False
        
        # Scenario setup
        self.scenario = {
            "title": "Billing Dispute - Unexpected Charge",
            "context": """
You are training to handle customer service calls. In this scenario, you'll practice 
resolving a billing dispute with a mildly frustrated customer.

CUSTOMER BACKGROUND:
- Name: Sarah Chen
- Has been a customer for 2 years
- Usually pays bills on time
- Noticed an unexpected $45 charge on her account
- Feels confused and slightly frustrated
- Wants a clear explanation and resolution
            """,
            "customer_prompt": """
You are Sarah Chen, a customer calling about a billing issue. You have these characteristics:

PERSONALITY & TONE:`
- Mildly frustrated but reasonable
- Direct communicator who wants clear answers
- Willing to work with customer service if treated respectfully
- Gets more frustrated if you feel dismissed or not heard

YOUR SITUATION:
- You've been a loyal customer for 2 years
- You just received your bill with an unexpected $45 "Service Enhancement Fee"
- You never signed up for any service enhancement
- You want to understand what this charge is and get it removed if it's a mistake

CONVERSATION RULES:
- Stay in character as Sarah Chen throughout the entire conversation
- Only discuss this billing issue - if the human asks about anything else (travel, other topics, personal advice), respond with something like "I'm sorry, but I'm calling about my billing issue. Can we please focus on resolving this charge?"
- Be persistent about getting answers but remain civil
- Show appreciation when the representative is helpful
- Your goal is to understand the charge and get it resolved

IMPORTANT: You are ONLY Sarah Chen calling about a billing issue. Do not break character or discuss anything unrelated to customer service.

Start the conversation by explaining your billing concern.
            """
        }

    def make_api_call(self, messages, max_tokens=1000):
        """Make a call to the Claude API using anthropic client"""
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=max_tokens,
                messages=messages
            )
            # The response object from anthropic client contains 'content' as a list of dicts with 'text'
            if response and hasattr(response, 'content') and response.content:
                return response.content[0].text
            else:
                return "API Error: No content returned."
        except Exception as e:
            return f"Error making API call: {str(e)}"

    def start_scenario(self):
        """Initialize the customer service scenario"""
        print("=" * 60)
        print("CUSTOMER SERVICE TRAINING - BILLING DISPUTE SCENARIO")
        print("=" * 60)
        print(self.scenario["context"])
        print("\nPress Enter when ready to start the roleplay...")
        input()
        
        # Initialize conversation with customer
        initial_message = [{"role": "user", "content": self.scenario["customer_prompt"]}]
        customer_response = self.make_api_call(initial_message)
        
        print("\n" + "="*60)
        print("CUSTOMER CALLING...")
        print("="*60)
        print(f"Customer: {customer_response}")
        
        # Store the conversation
        self.conversation_history = [
            {"role": "user", "content": self.scenario["customer_prompt"]},
            {"role": "assistant", "content": customer_response}
        ]
        
        self.scenario_active = True
        return customer_response

    def handle_user_response(self, user_input):
        """Process user's customer service response"""
        if not self.scenario_active:
            return "Please start a scenario first."
        
        # Add user response to conversation
        self.conversation_history.append({
            "role": "user", 
            "content": f"""
Continue playing Sarah Chen, the customer with the billing issue. 
The customer service representative just said: "{user_input}"

Remember:
- Stay in character as Sarah Chen
- Focus only on the billing dispute
- If they ask about anything unrelated, redirect back to your billing issue
- React appropriately to their response (appreciative if helpful, more frustrated if dismissed)
"""
        })
        
        # Get AI customer response
        customer_response = self.make_api_call(self.conversation_history)
        
        # Add AI response to history
        self.conversation_history.append({"role": "assistant", "content": customer_response})
        
        return customer_response

    def end_scenario_with_feedback(self):
        """Generate feedback on the user's performance"""
        if not self.conversation_history:
            return "No conversation to analyze."
        
        # Create feedback prompt
        feedback_prompt = f"""
Analyze this customer service conversation and provide constructive feedback:

CONVERSATION:
{self.format_conversation_for_review()}

Please provide feedback on the customer service representative's performance:

1. STRENGTHS: What did they do well?
2. AREAS FOR IMPROVEMENT: What could they have done better?
3. SPECIFIC SUGGESTIONS: Concrete advice for handling similar situations
4. OVERALL RATING: Rate their performance from 1-5 with brief explanation

Focus on:
- Empathy and active listening
- Problem-solving approach
- Communication clarity
- De-escalation techniques
- Professional tone

Keep feedback constructive and specific.
        """
        
        feedback_messages = [{"role": "user", "content": feedback_prompt}]
        feedback = self.make_api_call(feedback_messages, max_tokens=1500)
        
        return feedback

    def format_conversation_for_review(self):
        """Format conversation history for feedback analysis"""
        formatted = []
        is_customer = True  # First message is always customer
        
        for i, msg in enumerate(self.conversation_history[1:], 1):  # Skip system prompt
            if is_customer:
                formatted.append(f"Customer: {msg['content']}")
            else:
                formatted.append(f"Representative: {msg['content']}")
            is_customer = not is_customer  # Alternate between customer and rep
            
        return "\n\n".join(formatted)

    def run(self):
        """Main CLI loop"""
        print("Welcome to Customer Service Training!")
        print("Type 'start' to begin a scenario, 'end' to finish and get feedback, or 'quit' to exit.")
        
        while True:
            command = input("\n> ").strip().lower()
            
            if command == 'quit':
                print("Thanks for training! Goodbye.")
                break
                
            elif command == 'start':
                if self.scenario_active:
                    print("Scenario already active. Type 'end' to finish current scenario first.")
                    continue
                self.start_scenario()
                
            elif command == 'end':
                if not self.scenario_active:
                    print("No active scenario to end.")
                    continue
                    
                print("\nGenerating feedback on your performance...")
                feedback = self.end_scenario_with_feedback()
                print("\n" + "="*60)
                print("PERFORMANCE FEEDBACK")
                print("="*60)
                print(feedback)
                
                # Reset for next scenario
                self.conversation_history = []
                self.scenario_active = False
                print("\nScenario complete! Type 'start' to try again or 'quit' to exit.")
                
            elif command.startswith('help'):
                print("\nCommands:")
                print("- start: Begin customer service roleplay")
                print("- end: Finish scenario and get feedback")
                print("- quit: Exit the program")
                print("- During roleplay: Type your customer service responses naturally")
                
            elif self.scenario_active:
                # User is responding to customer during active scenario
                print("\nProcessing your response...")
                customer_response = self.handle_user_response(command)
                print(f"\nCustomer: {customer_response}")
                print("\nYour response:")
                
            else:
                print("Unknown command. Type 'help' for available commands.")

if __name__ == "__main__":
    trainer = CustomerServiceTrainer()
    trainer.run()