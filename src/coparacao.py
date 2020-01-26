out_ = open('comparacao.html','w')
out_.write("<div style='position: relative;float:center; margin:5vmax 5vmax 3vmax 3vmax;'><h1>BioInformatica - Comparando Genomas</h1>")

def gen_dict_combinations():
    cout = {}
    for i in ['A','T','C','G']:
        for j in ['A', 'T','C','G']:
            cout[i+j] = 0
    return cout

def execute(read, title, p='left'):
    in_ = open(read).read()
    cont  = gen_dict_combinations()    
    in_ = in_.replace('\n','')
    for i in range(len(in_)-1):
        par = in_[i] + in_[i+1]
        if par in cont.keys():
            cont[par] += 1 
    make_html(cont, title, p)

def  make_html(cont, title, p):
    i = 1
    out_.write("<div style='position: relative;float:" + p +"; '>")
    out_.write("<div style='position: relative; color: #333; '><h2>"+title+"</h2></div>")
    for k in cont:
        opacit = cont[k]/max(cont.values())
        html = "<div style='width: 100px; border: 2px solid #111; height: 100px; float:" + p + "; color: #fff; background-color: rgba(77,0,25," + str(opacit) + "); '>"+ k + "</div>"
        
        out_.write(html)
        if i%4 == 0:
            break_ = "<div style='clear:both'></div>" 
            out_.write(break_)
        i+=1
    out_.write("</div>")

execute(read='../res/bacteria.fasta', title='Bacteria')
execute(read='../res/human.fasta', title='Human', p='right')

out_.write("</div>")
out_.close()
