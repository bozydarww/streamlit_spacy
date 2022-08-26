# Core Pkgs
import streamlit as st 

# NLP Pkgs
import spacy_streamlit
import spacy
nlp = spacy.load("en_core_web_sm")

import os
#from PIL import Image

path = os.getcwd()
# Print the current working directory
# print("Current working directory: {0}".format(cwd))


def main():
    """A Simple NLP app with Spacy-Streamlit"""
    #nweh_logo = Image.open(os.path.join('nweh_logo_sm.jpg')) 
    #st.image(nweh_logo)
    st.title("PII QUEST **with** _spaCy_ **NLP**")
    st.markdown('**_(_ _pre-trained_ _CNN_ _model_ _with_ _English_ _language_ _)_**')
    menu = ["Named Entity Recognision","Tokenization"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Named Entity Recognision":
        st.subheader("Named Entity Recognision")
        raw_text = st.text_area("Sample Text","Ford Motor Company (commonly known as Ford) is an American multinational automobile manufacturer headquartered in Dearborn, Michigan, United States. It was founded by Henry Ford and incorporated on June 16, 1903. The company sells automobiles and commercial vehicles under the Ford brand, and luxury cars under its Lincoln luxury brand. Ford also owns Brazilian SUV manufacturer Troller, an 8% stake in Aston Martin of the United Kingdom and a 32% stake in Jiangling Motors.[5] It also has joint-ventures in China (Changan Ford), Taiwan (Ford Lio Ho), Thailand (AutoAlliance Thailand), Turkey (Ford Otosan), and Russia (Ford Sollers). The company is listed on the New York Stock Exchange and is controlled by the Ford family; they have minority ownership but the majority of the voting power.[6][4]Ford introduced methods for large-scale manufacturing of cars and large-scale management of an industrial workforce using elaborately engineered manufacturing sequences typified by moving assembly lines; by 1914, these methods were known around the world as Fordism. Ford's former UK subsidiaries Jaguar and Land Rover, acquired in 1989 and 2000 respectively, were sold to the Indian automaker Tata Motors in March 2008. Ford owned the Swedish automaker Volvo from 1999 to 2010.[7] In 2011, Ford discontinued the Mercury brand, under which it had marketed entry-level luxury cars in the United States, Canada, Mexico, and the Middle East since 1938.Ford is the second-largest U.S.-based automaker (behind General Motors) and the fifth-largest in the world (behind Toyota, Volkswagen, Hyundai and General Motors) based on 2015 vehicle production. At the end of 2010, Ford was the fifth largest automaker in Europe.[8] The company went public in 1956 but the Ford family, through special Class B shares, still retain 40 percent voting rights.[9][4] During the financial crisis at the beginning of the 21st century, it struggled financially to the point of collapse which was in large part prevented by President George W. Bush announcing his emergency financial rescue plan to help Ford Motors as well as Chrysler LLC and General Motors, making immediately available $13.4 billion to the automaker.[10] Ford Motors has since returned to profitability.[11] Ford was the eleventh-ranked overall American-based company in the 2018 Fortune 500 list, based on global revenues in 2017 of $156.7 billion.[12] In 2008, Ford produced 5.532 million automobiles[13] and employed about 213,000 employees at around 90 plants and facilities worldwide.")
        docx = nlp(raw_text)
        if st.button("Analyse"):
            spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)

    elif choice == "Tokenization":
        st.subheader("Tokenization")
        raw_text = st.text_area("Sample Text","Ford Motor Company (commonly known as Ford) is an American multinational automobile manufacturer headquartered in Dearborn, Michigan, United States. It was founded by Henry Ford and incorporated on June 16, 1903. The company sells automobiles and commercial vehicles under the Ford brand, and luxury cars under its Lincoln luxury brand. Ford also owns Brazilian SUV manufacturer Troller, an 8% stake in Aston Martin of the United Kingdom and a 32% stake in Jiangling Motors.[5] It also has joint-ventures in China (Changan Ford), Taiwan (Ford Lio Ho), Thailand (AutoAlliance Thailand), Turkey (Ford Otosan), and Russia (Ford Sollers). The company is listed on the New York Stock Exchange and is controlled by the Ford family; they have minority ownership but the majority of the voting power.[6][4]Ford introduced methods for large-scale manufacturing of cars and large-scale management of an industrial workforce using elaborately engineered manufacturing sequences typified by moving assembly lines; by 1914, these methods were known around the world as Fordism. Ford's former UK subsidiaries Jaguar and Land Rover, acquired in 1989 and 2000 respectively, were sold to the Indian automaker Tata Motors in March 2008. Ford owned the Swedish automaker Volvo from 1999 to 2010.[7] In 2011, Ford discontinued the Mercury brand, under which it had marketed entry-level luxury cars in the United States, Canada, Mexico, and the Middle East since 1938.Ford is the second-largest U.S.-based automaker (behind General Motors) and the fifth-largest in the world (behind Toyota, Volkswagen, Hyundai and General Motors) based on 2015 vehicle production. At the end of 2010, Ford was the fifth largest automaker in Europe.[8] The company went public in 1956 but the Ford family, through special Class B shares, still retain 40 percent voting rights.[9][4] During the financial crisis at the beginning of the 21st century, it struggled financially to the point of collapse which was in large part prevented by President George W. Bush announcing his emergency financial rescue plan to help Ford Motors as well as Chrysler LLC and General Motors, making immediately available $13.4 billion to the automaker.[10] Ford Motors has since returned to profitability.[11] Ford was the eleventh-ranked overall American-based company in the 2018 Fortune 500 list, based on global revenues in 2017 of $156.7 billion.[12] In 2008, Ford produced 5.532 million automobiles[13] and employed about 213,000 employees at around 90 plants and facilities worldwide.")
        docx = nlp(raw_text)
        if st.button("Analyse"):
            spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])

    


if __name__ == '__main__':
	main()
