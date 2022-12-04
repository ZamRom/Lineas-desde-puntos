#!/usr/bin/env python3
#Author: Ariel Rodolfo Zamudio Romero
opi = input('¿Quiere volver a abrir la anterior grafica? [Si/No] ').lower()
if opi == "si" or opi == "s":
    exec(open("archivoPuntos.py").read())
else:
    AT = open("archivoPuntos.py", "w")
    print("¿Cual opcion quiere usar?\nA.- Forma Poligonal\nB.- Forma Estrella\nC.- Grafo completo")
    opm = input("Opcion: ").lower()
    A = ['a','1','forma poligonal','poligonal']
    B = ['b','2','forma estrella','estrella']
    C = ['c','3','forma grafo completo','grafo','grafo completo','completo']
    if opm not in A and opm not in B and opm not in C:
        print("Escoja una opcion valida")
        AT.close()
        exec(open("linesFromPoints.py").read())
    else:
        PLA1 = ["#!/usr/bin/env python3","import matplotlib.pyplot as plt","import numpy as np"]
        PLA2 = ["def f(x, m1,x1,y1):","\ty =m1*(x-x1)+y1", "\treturn y","Dx = 0.1","fig, ax=plt.subplots(figsize=(10,6))"]
        PLA = [PLA1, PLA2]
        for i in PLA:
            for e in i:
                AT.write("%s\n"%(e))
            AT.write("\n")
            
        PLA3 = ["ax.set_xlabel('X')","ax.set_ylabel('Y')","ax.set_title('Lines and points')","fig.set_facecolor('lightsteelblue')","plt.grid()","plt.legend()","plt.show()"]
            
        print("Si pone numeros demasiado grandes puede que el programa se vuelva lento o no funcione por completo\nLe recomendamos que use numeros con 5 digitos maximo si quiere que se execute rapidamente")
        LP = input("<<Favor de poner las coordenadas deseadas de modo: x1 y1, x2 y2>> ").split(",")
        X = []
        Y = []
        for x in range(len(LP)):
            x2 = list(map(float, LP[x].split()))
            LP.remove(LP[x])
            X.append(x2[0])
            Y.append(x2[1])
            LP.insert(x, x2)
        if opm in A:
            if len(LP) > 1:
                for i in range(len(LP)):
                    x_1, y_1 = LP[i-1][0],LP[i-1][1]
                    x_2, y_2 = LP[i][0], LP[i][1]
                    if LP[i][0] == LP[i-1][0]:
                        AT.write("ax.stem(%s, %s, bottom=%s, linefmt='C%s-')\n"%(x_1,y_2,y_1,i))
                    else:
                        if x_1 < x_2:
                            A, B = x_1, x_2
                        else:
                            A, B = x_2, x_1    
                        AT.write("x%s = np.arange(%s, %s+Dx, Dx)\n"%(i,A,B))
                        if (y_2-y_1) and (x_2-x_1):
                            m= (y_2-y_1)/(x_2-x_1)
                        else:
                            m = 0
                        xn,yn = x_2,y_2
                        AT.write("y%s = f(x%s,%s,%s,%s)\n"%(i,i,m,xn,yn))
                        AT.write('ax.plot(x%s,y%s)\n'%(i,i))
                        AT.write("\n")
        elif opm in B:
            pc = [(max(X)+min(X))/2,(max(Y)+min(Y))/2]
            if len(LP) > 1:
                for i in range(len(LP)):
                    if LP[i][0] == pc[0]:
                        AT.write("ax.stem(x%s, y%s, bottom=%s, linefmt='C%s-')\n"%(pc[0],LP[i][1],pc[1],i))
                    else:
                        if pc[0] < LP[i][0]:
                            A, B = pc[0], LP[i][0]
                        else:
                            A, B = LP[i][0], pc[0]    
                        AT.write("x%s = np.arange(%s, %s+Dx, Dx)\n"%(i,A,B))
                        if (LP[i][1]-pc[1]) and (LP[i][0]-pc[0]):
                            m = (LP[i][1]-pc[1])/(LP[i][0]-pc[0])
                        else:
                            m = 0
                        xn,yn = LP[i][0],LP[i][1]
                        AT.write("y%s = f(x%s,%s,%s,%s)\n"%(i,i,m,xn,yn))
                        AT.write('ax.plot(x%s,y%s)\n'%(i,i))
                        AT.write("\n")
            AT.write('ax.plot(%s,%s,marker="o",label="punto central")\n'%(pc[0],pc[1]))
        elif opm in C:
            LPT = LP.copy() 
            for e in LP:    
                i = 0
                for n in LPT:
                    if e != LPT[i-1]:
                        if e[0] == LPT[i-1][0]:
                            AT.write("ax.stem(%s, %s, bottom=%s, linefmt='C%s-')\n"%(LPT[i-1][0],e[1],LPT[i-1][1],i))
                            AT.write("\n")
                        else:
                            if LPT[i-1][0] < e[0]:
                                A, B = LPT[i-1][0], e[0]
                            else:
                                A, B = e[0], LPT[i-1][0]    
                            AT.write("x%s = np.arange(%s, %s+Dx, Dx)\n"%(i,A,B))
                            if (e[1]-LPT[i-1][1]) and (e[0]-LPT[i-1][0]):
                                m = (e[1]-LPT[i-1][1])/(e[0]-LPT[i-1][0])
                            else:
                                m = 0
                            xn,yn = e[0],e[1]
                            AT.write("y%s = f(x%s,%s,%s,%s)\n"%(i,i,m,xn,yn))
                            AT.write('ax.plot(x%s,y%s)\n'%(i,i))
                            AT.write("\n")
                    i += 1
                LPT.remove(e)
        


        for i in range(len(LP)):
            n,m = LP[i][0], LP[i][1]
            AT.write('ax.plot(%s,%s,marker="o",label="point %s")\n'%(n,m,i+1))
        AT.write("\n")

        for n in PLA3:
            AT.write("%s\n"%(n))
            
        AT.close()
        exec(open("archivoPuntos.py").read())
        
        
'''        
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.'''
