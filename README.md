**Design Explanation**

**State Model**
The game state is maintained in a single in-memory dictionary that persists across turns.
It tracks the current round, maximum rounds, user and bot scores, bomb usage for each player, and a game-over flag.
This approach ensures the game never exceeds three rounds, enforces one-time bomb usage, and avoids relying on prompt-based memory or external storage.

**Agent / Tool Design**
The chatbot follows an agent-style architecture with explicit tool-like functions:
i. validate_move handles intent validation and rule enforcement.
ii. resolve_round applies game logic and determines the winner.
iii. update_game_state mutates state and controls game progression.

The main loop acts as the controller, coordinating user input, tool execution, and response generation.
This clean separation mirrors ADK principles of intent understanding, logic execution, and response synthesis.

**Tradeoffs Made**
Although LLM-based referee responses were initially considered, they were removed due to restricted and inconsistent model availability in the execution environment.
To ensure reliability and deterministic behavior, rule-based responses were used instead.
This prioritizes correctness and architectural clarity over conversational richness.

**Improvements with More Time**
With more time or broader API access, the system could be extended with:
i. LLM-generated referee commentary
ii. Multiple agents (referee and opponent)
iii. Structured JSON outputs for each round
iv. Unit tests for game logic
v. Configurable difficulty levels for the bot

Unit tests for game logic

Configurable difficulty levels for the bot
