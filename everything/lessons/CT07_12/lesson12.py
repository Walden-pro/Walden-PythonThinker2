import random
# Functions
def print_title():
    print("""
     ██████╗ ██████╗   ██████╗  ███████╗  ██████╗  ██╗   ██╗ ███████╗ ███████╗ ████████╗
    ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔════╝ ██╔═══██╗ ██║   ██║ ██╔════╝ ██╔════╝ ╚══██╔══╝
    ██║      ██║   ██║ ██║  ██║ █████╗   ██║   ██║ ██║   ██║ █████╗   ███████╗    ██║   
    ██║      ██║   ██║ ██║  ██║ ██╔══╝   ██║▄▄ ██║ ██║   ██║ ██╔══╝   ╚════██║    ██║   
    ╚██████╗ ╚██████╔╝ ██████╔╝ ███████╗ ╚██████╔╝ ╚██████╔╝ ███████╗ ███████║    ██║   
     ╚═════╝  ╚═════╝   ╚════╝   ╚═════╝  ╚══▀▀═╝   ╚═════╝   ╚═════╝ ╚══════╝    ╚═╝   
    """)
    print("Welcome adventurer!")
    print("This is a mini text game where you choose what to do next.")

def draw_separator():
    print("=" * 60)

def print_rules():
    print("Rules:")
    print("1) Type the number of your choice and press Enter")
    print("2) Read carefully - some choices may end the game.")
    print("3) Have fun and don't panic if you make a mistake!")

def show_menu():
    print("Menu:")
    print("1) Start Game")
    print("2) Instructions")
    print("3) Quit")

def game_intro():
    print_title()
    draw_separator()
    print_rules()
    draw_separator()
    show_menu()
    draw_separator()

def print_quest_header(quest_name,reward):
    print("***** QUEST BOARD NOTICE *****")
    print(f"Quest: {quest_name}")
    print(f"Reward: {reward}")

def print_quest_details(location,danger_level):
    print(f"Location: {location}")
    print(f"Danger Level: {danger_level}")

    if danger_level.lower() == "low":
        print("Advice: EZZZ")
    elif danger_level.lower() == "medium":
        print("Advice: Stay alert. Travel in pairs")
    elif danger_level.lower() == "high":
        print("Advice: Risky mission. Prepare well and plan an escape route.")
    else:
        print("Unknown substaces and creatures. advice not to go anyway")

def show_quest_board(quest_name,reward,location,danger_level):
    print_quest_header(quest_name,reward)
    draw_separator()
    print_quest_details(location,danger_level)
    draw_separator()

def roll_dice(sides):
    roll = random.randint(1,sides)
    return roll

def calculate_damage(attack_roll):
    bonus_dmg = random.randint(1,5)
    final_dmg = attack_roll + bonus_dmg
    if attack_roll >= 18:
        final_dmg *= 2
    return final_dmg

def apply_damage(current_hp, damage):
    current_hp -= damage
    if current_hp < 0:
        current_hp = 0
    return current_hp

def calculate_reward(base_gold, danger_level):
    if danger_level.lower() == "low":
        pass
    elif danger_level.lower() == "medium":
        base_gold *= 1.5
    elif danger_level.lower() == "high":
        base_gold *= 2
    else:
        base_gold *= 4
    return base_gold

def get_battle_message(monster_name, monster_hp, gold_reward):
    if monster_hp == 0:
        print(f"You have defeated {monster_name}")
        print(f"Gold earned: {gold_reward}")
    else:
        print(f"{monster_name} is still alive!")
        print(f"Monster HP remaining: {monster_hp}")
    
def start_boss_fight(monster_name,monster_hp,danger_level,reward):

    monster_name = "Cave Slime King"
    monster_hp = 25
    danger_level = "medium"
    reward = 100
    
    print("=== BOSS FIGHT ===")
    print(f"Enemy: {monster_name}")
    print(f"Monster HP (start): {monster_hp}")
    turn = 1
    while monster_hp > 0:
        print(f"---Turn {turn}---")
        attack_roll = roll_dice(20)
        print(f"Attack roll: {attack_roll}")
        
        damage = calculate_damage(attack_roll)
        print(f"Damage dealt: {damage}")
        
        monster_hp = apply_damage(monster_hp, damage)
        print(f"Monster HP (after): {monster_hp}")
        turn += 1
        gold_reward = calculate_reward(reward, danger_level)

        get_battle_message(monster_name, monster_hp, gold_reward)

# Main code

# game_intro()

# show_quest_board("Rescue the Lost Owlbear", "120 gold", "Whispering Forest", "60")
# show_quest_board("Defeat the Cave Slime King", "Rare Gem","Dark Caverns", "High")

start_boss_fight("Cave Slime King",25,"medium",100)
