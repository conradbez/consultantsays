# import streamlit as st
# from fastai.text import *
# learn = load_learner('text')


# st.markdown("## Consultant speak")
# st.text("""ML model trained on consultancy deliverables found with a google search""")
# # st.slider
# N_WORDS = st.slider('How many words would you like to predict?',value=40,min_value=1,max_value=200)
# N_SENTENCES = 2
# TEXT = st.text_input('Write text here to complete:',value='In todays world')
# st.write("\n".join(learn.predict(TEXT, N_WORDS, temperature=0.75) for _ in range(N_SENTENCES)))


from conditional_model import conditional_model
print(conditional_model(seed=1,sentences=['In todays world we can see a clear']))