import streamlit as st
import pandas as pd
import numpy as np
import random



st.title("🦸‍♀️ Superhero Generator 🦸‍♂️")

name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

favourite_colour = st.text_input("Enter your favourite colour:")

favourite_animal = st.text_input("Enter your favourite animal:")

lucky_number = st.number_input("Enter your lucky number:")

superpower = st.selectbox("Select your superpower:", [
    "Flying", "Invisibility", "Telepathy", "Time Travel",
    "Super Strength", "Telekinesis", "Shape Shifting", "Healing Factor",
    "Energy Projection", "Weather Control", "Mind Control", "Force Fields",
    "Teleportation", "Super Speed", "Elasticity", "X-Ray Vision",
    "Fire Control", "Ice Powers", "Electricity Manipulation", "Size Changing",
    "Animal Communication", "Probability Manipulation", "Gravity Control", "Duplication",
    "Portal Creation", "Matter Manipulation", "Reality Warping", "Energy Absorption",
    "Sonic Scream", "Phasing", "Technopathy", "Precognition",
    "Immortality", "Atomic Manipulation", "Dream Walking", "Memory Manipulation",
    "Light Control", "Shadow Control", "Plant Control", "Metal Manipulation",
    "Quantum Powers", "Time Stop", "Dimensional Travel", "Power Mimicry",
    "Regeneration", "Force Push/Pull", "Astral Projection", "Power Nullification"
])

st.markdown(f"""
### 🦸 Your Superhero Profile

**Superhero Name:** The {favourite_colour.title()} {favourite_animal.title()} of over {int(lucky_number)}  
**Superpower:** {superpower}
""")

# Add motto generator
def generate_motto():
    motto_templates = [
        f"With {superpower}, justice will prevail!",
        f"The {favourite_colour.lower()} light of hope shines eternal!",
        f"By the power of the {favourite_animal.lower()}, evil shall fall!",
        f"In darkness or light, {superpower} guides my fight!",
        f"Through {lucky_number} realms, my {superpower} brings peace!",
        f"Fear the wrath of the {favourite_colour.lower()} {favourite_animal.lower()}!",
        f"With great {superpower} comes great responsibility!",
        f"Neither villain nor foe can stop the {favourite_colour.lower()} glow!",
    ]
    return random.choice(motto_templates)

if st.button("Generate Superhero Motto! 🦸‍♂️"):
    motto = generate_motto()
    st.markdown(f"### Your Motto:\n\n_{motto}_")
