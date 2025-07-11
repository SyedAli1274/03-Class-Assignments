# 🧳 AI Travel Designer Agent

## Overview
Plan a full travel experience by coordinating between specialized agents:
- Suggests destinations based on mood or interests
- Uses Tool: get_flights(), suggest_hotels() with mock data
- Hands off between:
  - DestinationAgent (finds places)
  - BookingAgent (simulates travel booking)
  - ExploreAgent (suggests attractions & food)

## Features
- OpenAI Agent SDK + Runner
- Tools: Travel Info Generator, Hotel Picker
- Handoff: Between Destination, Booking, and Explore Agents

## Setup
1. Clone the repository or copy the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=sk-...
   ```
4. Run the main program:
   ```bash
   python main.py
   ```

## Project Structure
- `agents/` - Contains agent logic
- `tools/` - Contains mock tools for flights and hotels
- `main.py` - Orchestrates the agent handoff and user interaction

## Notes
- This project uses mock data for flights and hotels.
- Agent handoff and tool usage are demonstrated for learning purposes. 