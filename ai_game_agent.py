import random

# ---------------------------------------------------------
# 1. GAME STATE (SOURCE OF TRUTH)
# ---------------------------------------------------------

game_state = {
    "round": 0,
    "max_rounds": 3,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "game_over": False,
}

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

# ---------------------------------------------------------
# 2. TOOLS (EXPLICIT GAME LOGIC)
# ---------------------------------------------------------

def validate_move(move: str):
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move. Round wasted."}

    if move == "bomb" and game_state["user_bomb_used"]:
        return {"valid": False, "reason": "Bomb already used. Round wasted."}

    return {"valid": True, "move": move}


def resolve_round(user_move: str):
    if not game_state["bot_bomb_used"] and random.random() < 0.2:
        bot_move = "bomb"
    else:
        bot_move = random.choice(["rock", "paper", "scissors"])

    if user_move == bot_move:
        winner = "draw"
    elif user_move == "bomb":
        winner = "user"
    elif bot_move == "bomb":
        winner = "bot"
    else:
        wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        winner = "user" if wins[user_move] == bot_move else "bot"

    return {
        "user_move": user_move,
        "bot_move": bot_move,
        "winner": winner,
    }


def update_game_state(result):
    game_state["round"] += 1

    if result["winner"] == "user":
        game_state["user_score"] += 1
    elif result["winner"] == "bot":
        game_state["bot_score"] += 1

    if result["user_move"] == "bomb":
        game_state["user_bomb_used"] = True
    if result["bot_move"] == "bomb":
        game_state["bot_bomb_used"] = True

    if game_state["round"] >= game_state["max_rounds"]:
        game_state["game_over"] = True

# ---------------------------------------------------------
# 3. REFEREE RESPONSE (DETERMINISTIC)
# ---------------------------------------------------------

def referee_response(round_no, result):
    lines = [
        f"Round {round_no}/3",
        f"You played {result['user_move']}, bot played {result['bot_move']}."
    ]

    if result["winner"] == "draw":
        lines.append("It’s a draw!")
    elif result["winner"] == "user":
        lines.append("You win this round!")
    else:
        lines.append("Bot wins this round!")

    return "\n".join(lines)

# ---------------------------------------------------------
# 4. GAME LOOP (CONTROLLER)
# ---------------------------------------------------------

def main():
    print("""
🎮 Rock–Paper–Scissors–Plus
• Best of 3 rounds
• Moves: rock, paper, scissors, bomb
• Bomb usable once
• Bomb beats everything
""".strip())

    while not game_state["game_over"]:
        user_input = input(f"\nRound {game_state['round'] + 1}/3 > ")

        validation = validate_move(user_input)

        if not validation["valid"]:
            print(f"❌ {validation['reason']}")
            game_state["round"] += 1
            continue

        result = resolve_round(validation["move"])
        update_game_state(result)

        print("\n📢 Round Result")
        print(referee_response(game_state["round"], result))

        print(
            f"Score → You: {game_state['user_score']} | "
            f"Bot: {game_state['bot_score']}"
        )

    print("\n🏁 FINAL RESULT")
    if game_state["user_score"] > game_state["bot_score"]:
        print("🎉 You win!")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("🤖 Bot wins!")
    else:
        print("🤝 It's a draw!")

# ---------------------------------------------------------
# 5. ENTRY POINT
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
