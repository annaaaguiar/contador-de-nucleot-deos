import streamlit as st
import matplotlib.pyplot as plt

#processa o arquivo 
def processar_arquivo(uploaded_file):
    #le o arquivo
    dna_sequence = uploaded_file.read().decode("utf-8").strip().upper()
    return dna_sequence

#valida a seq
def validar_dna(seq):
    for letra in seq:
        if letra not in ["A", "T", "C", "G"]:
            return False
    return True

#aplicação Streamlit
def main():
    st.title("Contador de Nucleotídeos de DNA")

    #upload arquivo
    uploaded_file = st.file_uploader("Faça o upload de um arquivo de texto com a sequência de DNA", type=["txt"])

    # armazenena sequência de DNA
    dna_sequence = ""

    #se der upload, processa
    if uploaded_file is not None:
        dna_sequence = processar_arquivo(uploaded_file)
        st.write("Sequência de DNA do arquivo:")
        st.text(dna_sequence)  # Exibe a sequência do arquivo

    #sem upload
    else:
        dna_sequence = st.text_input("Ou digite uma sequência de DNA:").upper()

    #valida
    if dna_sequence:
        if validar_dna(dna_sequence):
            nucleotides_count = {
                "A": dna_sequence.count("A"),
                "T": dna_sequence.count("T"),
                "C": dna_sequence.count("C"),
                "G": dna_sequence.count("G")
            }

            #porcentagem
            st.write("### Porcentagem de cada nucleotídeo:")
            for nucleotide, count in nucleotides_count.items():
                percentage = (count / len(dna_sequence)) * 100
                st.write(f"{nucleotide}: {percentage:.2f}%")

            # GC content
            gc_content = (nucleotides_count["G"] + nucleotides_count["C"]) / len(dna_sequence) * 100
            st.write(f"### GC Content: {gc_content:.2f}%")

            # AT content
            at_content = (nucleotides_count["A"] + nucleotides_count["T"]) / len(dna_sequence) * 100
            st.write(f"### AT Content: {at_content:.2f}%")

            # grafico
            nucleotides = list(nucleotides_count.keys())
            counts = list(nucleotides_count.values())

            fig, ax = plt.subplots()
            ax.bar(nucleotides, counts, color=['blue', 'orange', 'green', 'red'])
            ax.set_title("Contagem de Nucleotídeos")
            ax.set_xlabel("Nucleotídeos")
            ax.set_ylabel("Quantidade")
            ax.grid(True)

            st.pyplot(fig)  

        else:
            st.error("Sua sequência contém caracteres inválidos! Apenas A, T, C e G são permitidos.")

if __name__ == "__main__":
    main()
