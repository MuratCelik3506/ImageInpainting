import os
import streamlit as st
from PIL import Image

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

st.set_page_config(layout="wide")
st.markdown(
        """
       <style>
       [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 300px;
           max-width: 300px;
       }
       """,
        unsafe_allow_html=True,
    )   

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
    st.markdown('<a href="#references"  style="text-decoration:none; color:black" \
                >Refereneces</a>', unsafe_allow_html=True)
    
st.markdown("""<style>p{text-align: justify} li{text-align: justify} </style>""", unsafe_allow_html=True)
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

st.markdown(f'<h3>4.1 Experimental Details</h3>', unsafe_allow_html=True)

st.markdown(f'<h4>4.1.1 Models</h4>', unsafe_allow_html=True)
st.markdown(f'<h5>LaMa: Resolution-robust Large Mask Inpainting with Fourier Convolutions</h5>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("models/lama.txt")}</p>', unsafe_allow_html=True)
st.markdown(f'<h5>MAT: Mask-Aware Transformer for Large Hole Image Inpainting</h5>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("models/mat.txt")}</p>', unsafe_allow_html=True)
st.markdown(f'<h5>MISF: Multi-level Interactive Siamese Filtering for High-Fidelity Image Inpainting</h5>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("models/misf.txt")}</p>', unsafe_allow_html=True)

st.markdown(f'<h4>4.1.2 Masks</h4>', unsafe_allow_html=True)
st.markdown(f'<p><strong>Ratio Mask:</strong> By specifying 8 different ratios, random pixels were extracted from the picture with a \
            certain algorithm. For this algorithm, a random walk algorithm was used and a mask was prepared for each \
             image by determining the ratio of the masked area to all pixels. Ratios of 20,30,40,50,60,70,80 were used  \
            for the CelebAMask-HQ dataset, and 20,40,60 for the Places365 dataset.</p>', unsafe_allow_html=True)
image_ratio = Image.open('img/ratio.png')
st.image(image_ratio, caption='Ratio Masks')
st.markdown(f'<p><strong>Annotation Mask:</strong> The CelebAMask-HQ dataset has labeled face parts for each image. In this\
             study, the person\'s hair, the person\'s face, and the combination of certain facial parts of the person \
            (eye, mouth, nose, eyebrow) were selected.</p>', unsafe_allow_html=True)
image_face = Image.open('img/face.png')
st.image(image_face, caption='Face Annotation Masks')

st.markdown(f'<h4>4.1.3 Metrics</h4>', unsafe_allow_html=True)
st.markdown(f'<p><strong>L1 Loss Function</strong> is used to reduce the error, which is the total of all the absolute \
            differences between the true value and the predicted value.</p>', unsafe_allow_html=True)
st.markdown(f'<p><strong>L2 Loss Function</strong> is used to reduce the error, which is calculated as the square root \
            of the sum of every difference between the true value and the predicted value.</p>', unsafe_allow_html=True)
st.markdown(f'<p><strong>Structural Similarity Index (SSIM)</strong> is a method that determines the structural similarity of two images \
            with 3 components. These methods are Luminance, Contrast, Structural. <br> \
            The mean intensity of the signals determines the difference in luminance between the two images. \
            The contrast is determined by the standard deviation. The correlation between the two images establishes the structure. <br> \
            It takes a value between -1 and 1. 1 means most similar, -1 means most different. </p>', unsafe_allow_html=True)
st.markdown(f'<p><strong>Peak signal-to-noise ratio (PSNR)</strong> is a method that calculates the ratio between the peak power \
            of an image and the noise-distortion power that affects the representation quality. It uses the MSE value in the \
            denominator, so high PSNR means low error.  </p>', unsafe_allow_html=True)
st.markdown(f'<p><strong>Learned Perceptual Image Patch Similarity (LPIPS)</strong>is a metric used to measure the \
            perceptual similarity between images. It uses deep neural networks that have been trained on extensive \
            datasets to account for human vision and judgment. As LPIPS collects more complex visual cues and semantic \
            information about the appearance, texture, and shape of objects, it is more in line with how people perceive \
             objects.</p>', unsafe_allow_html=True)

st.markdown(f'{read_text("table/table_places.txt")}', unsafe_allow_html=True)
st.markdown(f"<p><br><br></p>", unsafe_allow_html=True)
st.markdown(f'{read_text("table/table_celeba.txt")}', unsafe_allow_html=True)
st.markdown(f'<h2>5. Conclusion</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("conclusion.txt")}</p>', unsafe_allow_html=True)


st.markdown(f'<h2>6. Vision and Future Work</h2>', unsafe_allow_html=True)
st.markdown(f'<p>{read_text("vision.txt")}</p>', unsafe_allow_html=True)



st.markdown(f'<h2>References</h2>', unsafe_allow_html=True)
st.markdown(f'<h3>Articles</h3>', unsafe_allow_html=True)
f = open("Reference/references_article.txt", "r")
texts = f.readlines()
f.close()
for text in texts:
    text = text.split("+")
    st.markdown(f"[{text[0]}]({text[1]})", unsafe_allow_html=True)

st.markdown(f'<h3>Datasets</h3>', unsafe_allow_html=True)
f = open("Reference/references_dataset.txt", "r")
texts = f.readlines()
f.close()
for text in texts:
    text = text.split("+")
    st.markdown(f"[{text[0]}]({text[1]})", unsafe_allow_html=True)