import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit tutrial")

st.write("DataFrame")

df = pd.DataFrame({
    "row1": [1, 2, 3, 4],
    "row2": [10, 20, 30, 40],
})

# st.dataframe(df.style.highlight_max(axis=0))    # dataframe(df, width=, height=)
st.table(df.style.highlight_max(axis=0))

#magiccommand

# """

# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption="sample", use_column_width=True)
    
option  = st.selectbox(
    'your favorite num',
    list(range(1,11)),
)

'your favorite num is ', option

hobbies = st.sidebar.text_input('your hobbies?')

'your hobbies is ', hobbies

condition = st.sidebar.slider('your condition?', 0, 100, 70)

'your condition is', condition

left_column, right_column = st.columns(2)

button = left_column.button('show letter')
if button:
    right_column.write("here is right column")
    
expander1 = st.expander('Question1')
expander1.write('Ansewer1')
expander1.write('Ansewer2')

expander2 = st.expander('Question2')
expander2.write('Ansewer1')
expander2.write('Ansewer2')

latest_iteration = st.empty()
bar = st.progress(10)

for i in range(100):
    latest_iteration.text(f'Iteration:{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)