import streamlit as st

# Description of the Application
st.title('Hamilton Anxiety Scale (HAM-A) Calculator')
st.write('''
This application is designed to calculate the Hamilton Anxiety Scale (HAM-A), 
a widely used measure of anxiety. The scale consists of 14 items, each defined 
by a series of symptoms. Each item is rated on a scale of 0 (not present) to 
4 (severe), with a total score range of 0–56, where <17 indicates mild severity, 
18–24 mild to moderate severity and 25–30 moderate to severe.

Please note: This tool does not replace professional medical advice. 
If you're feeling anxious, please reach out to a healthcare professional.
''')

# Function to calculate the HAM-A score
def calculate_HAM_A(*args):
    return sum(args)

# Create inputs for each of the 14 items in the HAM-A scale
st.subheader('Please rate the severity of your symptoms')
items = [
    'Anxious mood', 'Tension', 'Fears', 'Insomnia', 'Intellectual (Cognitive)', 
    'Depressed mood', 'Somatic (Muscular)', 'Somatic (Sensory)', 
    'Cardiovascular symptoms', 'Respiratory symptoms', 
    'Gastrointestinal symptoms', 'Genitourinary symptoms', 
    'Autonomic symptoms', 'Behavior at interview'
]
scores = []
for item in items:
    scores.append(st.slider(item, 0, 4, 0))

# Calculate the HAM-A score
total_score = calculate_HAM_A(*scores)

# Display the HAM-A score and interpret it
st.subheader('Your Hamilton Anxiety Scale (HAM-A) Score is:')
st.write(total_score)

if total_score < 17:
    st.write('Your score suggests mild anxiety. However, this does not replace a professional diagnosis.')
elif 17 <= total_score <= 24:
    st.write('Your score suggests mild to moderate anxiety. Please consult with a healthcare professional.')
else:
    st.write('Your score suggests moderate to severe anxiety. It is important to consult with a healthcare professional immediately.')
