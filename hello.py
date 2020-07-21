from flask import Flask, request, render_template, send_file
from flask_tex import render_to_pdf
from flask_tex import compile_source
from flask_tex import run_tex
from flask_tex import compile_source
#from flask_tex import TeX
#from pdflatex import PDFLaTeX
#from pylatex import Document, Section, Subsection, Command
#from latex import build_pdf


app = Flask(__name__)



@app.route("/")
def my_form():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def return_files_tut():
    
    date = request.form["date"]
    place = request.form["place"]
    stime = request.form["stime"]
    etime = request.form["etime"]
    m_id = request.form["m_id"]
    from_auth = request.form["from"]

    lst_attend = request.form["l_attd"]
    lst_excused = request.form["l_exd"]
    lst_enclosure = request.form["l_encl"]
    lst_decission = request.form["l_dcns"]

    ##Discussions:

    preamble_1 = request.form["1_prmbl"]
    dicussion_1 = request.form["1_discuss"]
    lst_decision_1 = request.form["1_1dcn"]
    lst_doc_1 = request.form["1_1docs"]

    preamble_2 = request.form["2_prmbl"]
    dicussion_2 = request.form["2_discuss"]
    lst_decision_2 = request.form["2_1dcn"]
    lst_doc_2 = request.form["2_1docs"]

    preamble_3 = request.form["3_prmbl"]
    dicussion_3 = request.form["3_discuss"]
    lst_decision_3 = request.form["3_1dcn"]
    lst_doc_3 = request.form["3_1docs"]

    


   
    
    # ntext = text.split("\n")
    # # print(ntext)
    # texdoc = []
    # with open("templates/texput.tex") as fin:
    #     for line in fin:
    #         texdoc.append(line.replace("width=.5\\textwidth", "width=.9\\textwidth"))

    # for i in range(len(texdoc)):

    #     if i == 6:
    #         texdoc.insert(i + 1, "\\begin{enumerate}\n")
    #         # print(texdoc[i])
    #         for j in range(len(ntext)):
    #             print(ntext[j])

    #             texdoc.insert(i + j + 2, "\\item " + ntext[j] + "\n")
    # texdoc.insert(-1, "\\end{enumerate}\n")

    # with open("templates/final.tex", "w") as fout:
    #     for i in range(len(texdoc)):
    #         fout.write(texdoc[i])

    #print(date,place,stime,etime,m_id,from_auth,preamble_1,preamble_2,dicussion_1,dicussion_2)

    pdf = render_to_pdf("texput.tex",date=date,place=place,stime=stime,etime=etime,m_id=m_id,from_auth=from_auth,preamble_1=preamble_1,preamble_2=preamble_2,preamble_3=preamble_3,dicussion_1=dicussion_1,dicussion_2=dicussion_2,dicussion_3=dicussion_3)
    #
    return pdf


if __name__ == "__main__":
    app.debug = True
    app.run()

