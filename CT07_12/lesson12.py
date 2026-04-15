# # Task 1
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
Advice = ""
def show_quest_board(quest_name,reward,location,danger_level):
    print_quest_header(quest_name,reward)
    draw_separator()
    print_quest_details(location,danger_level)
    draw_separator()
# Main code
game_intro()

show_quest_board("Rescue the Lost Owlbear", "120 gold", "Whispering Forest", "m44")
show_quest_board("Defeat the Cave Slime King", "Rare Gem","Dark Caverns", "High")

