# Game Design Documentation

## State Model
The game state is maintained in a single in-memory dictionary that persists across turns.  
It tracks the following:

- Current round
- Maximum rounds
- User and bot scores
- Bomb usage for each player
- Game-over flag

This design ensures:

- The game never exceeds three rounds
- Each player can use their bomb only once
- No reliance on prompt-based memory or external storage

---

## Agent / Tool Design
The chatbot follows an agent-style architecture with explicit tool-like functions:

1. **validate_move** – Handles intent validation and rule enforcement  
2. **resolve_round** – Applies game logic and determines the winner  
3. **update_game_state** – Mutates the game state and controls game progression  

The main loop acts as the controller, coordinating:

- User input
- Tool execution
- Response generation  

This clean separation mirrors ADK principles of:

- Intent understanding
- Logic execution
- Response synthesis

---

## Trade-offs Made
- LLM-based referee responses were initially considered but removed due to restricted and inconsistent model availability.  
- Rule-based responses were used instead to ensure **reliability** and **deterministic behavior**.  
- Priority was given to **correctness** and **architectural clarity** over conversational richness.

---

## Improvements with More Time
With additional time or broader API access, the system could be extended with:

1. LLM-generated referee commentary  
2. Multiple agents (referee and opponent)  
3. Structured JSON outputs for each round  
4. Unit tests for game logic  
5. Configurable difficulty levels for the bot





