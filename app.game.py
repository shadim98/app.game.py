import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️")

# ASCII Art
st.text(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
*******************************************************************************
''')

st.title("🏝️ Treasure Island")
st.write("Your mission is to find the treasure.")

# Initialize game state
if "stage" not in st.session_state:
    st.session_state.stage = 1

# -------- Stage 1 --------
if st.session_state.stage == 1:
    st.write("You're at a crossroad. Where do you want to go?")
    col1, col2 = st.columns(2)
    if col1.button("⬅️ Left"):
        st.session_state.stage = 2
    if col2.button("➡️ Right"):
        st.session_state.stage = "game_over_hole"

# -------- Stage 2 --------
elif st.session_state.stage == 2:
    st.write("You've come to a lake. There is an island in the middle.")
    col1, col2 = st.columns(2)
    if col1.button("⏳ Wait for a boat"):
        st.session_state.stage = 3
    if col2.button("🏊 Swim across"):
        st.session_state.stage = "game_over_trout"

# -------- Stage 3 --------
elif st.session_state.stage == 3:
    st.write("You arrive at the island unharmed.")
    st.write("There is a house with 3 doors.")
    col1, col2, col3 = st.columns(3)
    if col1.button("🔴 Red"):
        st.session_state.stage = "fire"
    if col2.button("🟡 Yellow"):
        st.session_state.stage = "win"
    if col3.button("🔵 Blue"):
        st.session_state.stage = "beasts"

# -------- End States --------
elif st.session_state.stage == "fire":
    st.error("🔥 It's a room full of fire. Game Over.")

elif st.session_state.stage == "beasts":
    st.error("🐺 You enter a room of beasts. Game Over.")

elif st.session_state.stage == "game_over_trout":
    st.error("🐟 You got attacked by an angry trout. Game Over.")

elif st.session_state.stage == "game_over_hole":
    st.error("🕳️ You fell into a hole. Game Over.")

elif st.session_state.stage == "win":
    st.success("💎 You found the treasure. YOU WIN!")

# Restart button
st.button("🔄 Restart Game", on_click=lambda: st.session_state.clear())
