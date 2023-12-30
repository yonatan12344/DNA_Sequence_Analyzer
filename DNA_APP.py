import streamlit as st
from Bio.Blast import NCBIWWW

st.header('DNA Sequence Analyzer')
uploaded_file = st.file_uploader("Give me your DNA sequence")


def GC_Content(uploaded_file):
    if uploaded_file is not None:
        # Read lines from the uploaded file
        lines = uploaded_file.readlines()[1:]  # Exclude the first line (header)
        DNA_String = ''.join(line.decode('utf-8').strip() for line in lines)

        DNA_Length = len(DNA_String)
        GC_Content = (DNA_String.count('C') + DNA_String.count('G')) / DNA_Length
        return GC_Content * 100
print('Hi')

def ATG_Count(uploaded_file):
    if uploaded_file is not None:
        # Reset file pointer to the beginning
        uploaded_file.seek(0)

        # Read lines from the uploaded file
        lines = uploaded_file.readlines()[1:]  # Exclude the first line (header)
        DNA_String = ''.join(line.decode('utf-8').strip() for line in lines)

        n = len(DNA_String)
        k = len("ATG")
        ATG_Count = 0

        # Iterate through the DNA string to find "ATG"
        for i in range(n - k + 1):
            if "ATG" in DNA_String[i:i + k]:
                ATG_Count += 1

        return ATG_Count

def Blast_Time(uploaded_file):
    blast_results = None
    if uploaded_file is not None:
        Blast_Button = st.button("NT BLAST, be sure to have fasta sequence")
        if Blast_Button:
            # Reset file pointer to the beginning
            uploaded_file.seek(0)

            sequence_data = uploaded_file.read().decode('utf-8')
            result_handle = NCBIWWW.qblast("blastn", "nt", sequence_data)
            blast_results = result_handle.read()
    return blast_results

if uploaded_file is not None:
    st.write("GC Content:", GC_Content(uploaded_file))
    st.write("Start Codon Count:", ATG_Count(uploaded_file))
    blast_results = Blast_Time(uploaded_file)
    st.write("BLAST Results:")
    st.text(blast_results if blast_results is not None else "No BLAST results yet")
