import streamlit as st

st.set_page_config(page_title="Treasure Island", page_icon="🏝️")

# ---------- ASCII ART (SAFE STRING) ----------
st.markdown(
    '''
<div style="overflow-x:auto; white-space:pre; font-family: monospace;">
<pre>
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
</pre>
</div>
''',
    unsafe_allow_html=True,
)

st.title("🏝️ Treasure Island")
st.write("Your mission is to find the treasure.")

# ---------- GAME STATE ----------
if "stage" not in st.session_state:
    st.session_state.stage = 1

# ---------- CALLBACKS ----------
def go_left():
    st.session_state.stage = 2

def go_right():
    st.session_state.stage = "hole"

def wait_boat():
    st.session_state.stage = 3

def swim():
    st.session_state.stage = "trout"

def door_red():
    st.session_state.stage = "fire"

def door_yellow():
    st.session_state.stage = "win"

def door_blue():
    st.session_state.stage = "beasts"

def restart():
    st.session_state.clear()

# ---------- STAGE 1 ----------
if st.session_state.stage == 1:
    st.write("You're at a crossroad. Where do you want to go?")
    col1, col2 = st.columns(2)
    col1.button("⬅️ Left", on_click=go_left)
    col2.button("➡️ Right", on_click=go_right)

# ---------- STAGE 2 ----------
elif st.session_state.stage == 2:
    st.write("You've come to a lake. There is an island in the middle.")
    col1, col2 = st.columns(2)
    col1.button("⏳ Wait for a boat", on_click=wait_boat)
    col2.button("🏊 Swim across", on_click=swim)

# ---------- STAGE 3 ----------
elif st.session_state.stage == 3:
    st.write("You arrive at the island unharmed.")
    st.write("There is a house with 3 doors.")
    col1, col2, col3 = st.columns(3)
    col1.button("🔴 Red", on_click=door_red)
    col2.button("🟡 Yellow", on_click=door_yellow)
    col3.button("🔵 Blue", on_click=door_blue)

# ---------- END STATES ----------
elif st.session_state.stage == "fire":
    st.error("🔥 It's a room full of fire. Game Over.")

elif st.session_state.stage == "beasts":
    st.error("🐺 You enter a room of beasts. Game Over.")

elif st.session_state.stage == "trout":
    st.error("🐟 You got attacked by an angry trout. Game Over.")

elif st.session_state.stage == "hole":
    st.error("🕳️ You fell into a hole. Game Over.")

elif st.session_state.stage == "win":
    st.success("💎 You found the treasure. YOU WIN!")

# ---------- RESTART ----------
st.button("🔄 Restart Game", on_click=restart)
