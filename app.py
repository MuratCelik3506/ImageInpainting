import os
import streamlit as st
import streamlit.components.v1 as components

def read_text(path, title_exist = False, return_title = False):
    f = open(path, "r")
    text = f.readlines()
    f.close()
    if return_title:
        return text[0]
    if title_exist:
        text = text[1:]
    text = " ".join(text)
    return text


with st.sidebar:
    st.markdown('<h3>Table of Contents</h3>', unsafe_allow_html=True)
    st.markdown('<a href="#abstract" style="text-decoration:none; color:black"           \
                >Abstract</a>', unsafe_allow_html=True)
    st.markdown('<a href="#1-introduction" style="text-decoration:none; color:black"           \
                >1. Introduction</a>', unsafe_allow_html=True)
    st.markdown('<a href="#2-related-works"  style="text-decoration:none; color:black"          \
                >2. Related Works</a>', unsafe_allow_html=True)
    st.markdown('<a href="#3-datasets"  style="text-decoration:none; color:black"               \
                >3. Datasets</a>', unsafe_allow_html=True)
    st.markdown('<a href="#4-experiments"  style="text-decoration:none; color:black"           \
                >4. Experiments</a>', unsafe_allow_html=True)
    st.markdown('<a href="#5-conclusion"  style="text-decoration:none; color:black"             \
                >5. Conclusion</a>', unsafe_allow_html=True)
    st.markdown('<a href="#6-vision-and-future-work"  style="text-decoration:none; color:black" \
                >6. Vision and Future Work</a>', unsafe_allow_html=True)
    

st.markdown(f'<h1 style="text-align: center;">AIChroma</h1>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<p style ="text-align: center";>Murat Çelik </br> \
                b21827263@cs.hacettepe.edu.tr </br>  \
                Department of Computer Engineering, </br>  \
                Hacettepe University </br> \
                Ankara,Turkey </p>', unsafe_allow_html=True)
with c2:
    st.markdown('<p style ="text-align: center";>Humeyra Uçar </br>  \
                b21827957@cs.hacettepe.edu.tr </br>  \
                Department of Computer Engineering, </br>  \
                Hacettepe University </br>  \
                Ankara,Turkey </p>', unsafe_allow_html=True)


st.markdown(f'<h2>Abstract</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("abstract.txt")}</p>', unsafe_allow_html=True)


st.markdown(f'<h2>Keywords</h2>', unsafe_allow_html=True)
st.markdown(f'<p>kw1, kw2, kw3</p>', unsafe_allow_html=True)


st.markdown(f'<h2>1. Introduction</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("introduction.txt")}</p>', unsafe_allow_html=True)


st.markdown(f'<h2>2. Related Works</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("introduction.txt")}</p>', unsafe_allow_html=True)

for i in range(1,len(os.listdir("related_work"))+1):
    st.markdown(f'<h3>2.{i} {read_text(f"related_work/2_{i}.txt",return_title=True)}</h3>', unsafe_allow_html=True)
    st.markdown(f'<p>{read_text(f"related_work/2_{i}.txt",title_exist=True)}</p>', unsafe_allow_html=True)


st.markdown(f'<h2>3. Datasets</h2>', unsafe_allow_html=True)
st.markdown("<ul>", unsafe_allow_html=True)
for dataset in ["celeba", "celebamask_hq", "dunhuang", "ffhq", "imagenet", "paris_sw", "places"]:
    st.markdown(f'<li><strong>{read_text(f"datasets/{dataset}.txt",return_title=True)}</strong>  \
                {read_text(f"datasets/{dataset}.txt",title_exist=True)}</li>', unsafe_allow_html=True)
st.markdown("</ul>", unsafe_allow_html=True)


st.markdown(f'<h2>4. Experiments</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("experiments.txt")}</p>', unsafe_allow_html=True)


st.markdown(f'<h2>5. Conclusion</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("conclusion.txt")}</p>', unsafe_allow_html=True)


st.markdown(f'<h2>6. Vision and Future Work</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("vision.txt")}</p>', unsafe_allow_html=True)