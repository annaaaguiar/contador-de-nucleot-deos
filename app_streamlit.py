import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter

def process_uploaded_file(uploaded_file):
    return uploaded_file.read().decode("utf-8").strip().upper()

def is_valid(dna_sequence):
    for nucleotide in dna_sequence:
        if nucleotide not in ["A", "T", "C", "G"]:
            return False
    return True

def write_nucleotides_percentage(nucleotides_count, dna_sequence_size):
    st.write("### Porcentagem de cada nucleotídeo:")
    
    for nucleotide, count in nucleotides_count.items():
        percentage = (count / dna_sequence_size) * 100
        st.write(f"{nucleotide}: {percentage:.2f}%")

def write_gc_content(nucleotides_count, dna_sequence_size):
    gc_content = (nucleotides_count["G"] + nucleotides_count["C"]) / dna_sequence_size * 100
    st.write(f"### GC Content: {gc_content:.2f}%")

def write_at_content(nucleotides_count, dna_sequence_size):
    at_content = (nucleotides_count["A"] + nucleotides_count["T"]) / dna_sequence_size * 100
    st.write(f"### AT Content: {at_content:.2f}%")

def plot_nucleotides_count_graph(nucleotides_count):
    nucleotides = list(nucleotides_count.keys())
    counts = list(nucleotides_count.values())

    fig, ax = plt.subplots()
    ax.bar(nucleotides, counts, color=['blue', 'orange', 'green', 'red'])
    ax.set_title("Contagem de Nucleotídeos")
    ax.set_xlabel("Nucleotídeos")
    ax.set_ylabel("Quantidade")
    ax.grid(True)

    st.pyplot(fig)

def main():
    st.title("Contador de Nucleotídeos de DNA")
    uploaded_file = st.file_uploader("Faça o upload de um arquivo de texto com a sequência de DNA", type=["txt"])
    dna_sequence = ""

    if uploaded_file is not None:
        dna_sequence = process_uploaded_file(uploaded_file)
        st.write("Sequência de DNA do arquivo:")
        st.text(dna_sequence)
    else:
        dna_sequence = st.text_input("Ou digite uma sequência de DNA:").upper()


    if not is_valid(dna_sequence):
        st.error("Sua sequência contém caracteres inválidos! Apenas A, T, C e G são permitidos.")
        return

    if not dna_sequence:
        return

    nucleotides_count = Counter(dna_sequence)
    dna_sequence_size = len(dna_sequence)

    write_nucleotides_percentage(nucleotides_count, dna_sequence_size)
    write_gc_content(nucleotides_count, dna_sequence_size)
    write_at_content(nucleotides_count, dna_sequence_size)
    plot_nucleotides_count_graph(nucleotides_count)

if __name__ == "__main__":
    main()
