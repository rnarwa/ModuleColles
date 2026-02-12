import os
import pickle

dico_labels = pickle.load(open(r'./Liste_exos.picl', 'rb'))

class PlancheSemaine:
    def __init__(self, number, name, planches):
        self.number = number
        self.name = name
        self.planches = planches

def gen_planches(dir_path):

    planches_semaine = {}

    for file in os.listdir(dir_path):
        
        if not('.tex' in file):
            continue
        print(file)
        semaine_name = ''
        for stuff in file.split(' '):
            if 'Planche' in stuff or 'Colle' in stuff:
                continue
            semaine_name += stuff.replace('.tex', '') + ' '
        semaine_number = file.split('-')[0]
        planches = {}
        planche_counter = 1

        with open(dir_path+'/' + file, 'r',encoding='utf-8') as read_file:
            line=next(read_file)
            while '\\end{document}' not in line:
                if '\\planche' in line:
                    liste_exo = []
                    cours_planche = ''
                    if '[' in line:
                        name = line.split('[')[1].strip('\n').strip(']')
                    else:
                        name = str(planche_counter)
                        planche_counter += 1

                    line = next(read_file)
                    while ('\\planche' not in line) and ('\\pageReponses' not in line)and ('\\end{document}' not in line):
                        if '\\cours' in line:
                            liste_exo.insert(0, 'Cours')
                            cours_planche = line
                        if '\\selectexo' in line:
                            liste_exo.append(line.split('{')[2].strip('\n').strip('}'))
                        line = next(read_file)
                    
                    for i, exo in enumerate(liste_exo):
                        if exo != 'Cours':
                            try:
                                liste_exo[i] = dico_labels[exo]
                            except:
                                pass
                    planches[name]=(liste_exo,cours_planche) 
                else:
                    line = next(read_file)

        planches_semaine[semaine_number + '-' + semaine_name] = PlancheSemaine(semaine_number, semaine_name, planches)

    pickle.dump(planches_semaine, open(f'./test.pickl', 'wb+'))
    return planches_semaine

def gen_eleves(csv_file_path):
    liste_eleves=[]
    file = open(csv_file_path, 'r', encoding='utf-8')
    for name in file:
        name.replace('\t', ' ').replace('\n','')
        print(name)
        liste_eleves.append(name)

    return liste_eleves
