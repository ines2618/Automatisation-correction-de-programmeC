import subprocess
import sys
import re
import csv


#on appel ls et on stocke toute la sortie dans une liste
def stockefichier():
    resultat = subprocess.run("ls eleves_bis/", capture_output=True , text=True , shell=True).stdout
    list = resultat.split("\n")[:-1]
    return list




#prend la liste des fichiers et compile le programme
#cette fonction a egalement pour but de prendre en compte les differents warning
def compilation(nom_fichier):
    compile =  subprocess.run([f"gcc eleves_bis/{nom_fichier} -Wall -ansi -o {nom_fichier}" ],capture_output=True , text=True , shell=True)
    result = compile.stderr.split("\n")
    tuple_erreur = warning_erreur(result)
    
    return tuple_erreur
   

 

#prend une liste la split et stocke le nb d'erreur et le nb de warning dans des variables 
#on sait que l'elements à la pos 0 sera le nb erreur et pos 1 nb de warning si il y'en a 
#renvoie ces variables dans une liste
def warning_erreur(erreur):
    liste = erreur[len(erreur)-2]
    nb_erreur = 0
    nb_warning = 0
    res = liste.split(' ')

    if(len(res) == 6): #on est sur d'avoir des erreur et des warning
        nb_warning = int(res[0])
        nb_erreur =  int(res[3])
    
    if(len(res) == 3): #soit des erreurs soit des warnings
        if(res[1] == "warnings" or res[1] == "warning"):
            nb_warning = int(res[0])
            nb_erreur = 0

        if(res[1] == "error" or res[1] == "errors"):
            nb_erreur = int(res[0])
            nb_warning = 0
    
    return (nb_warning,nb_erreur)





#renverra 1 ou 0 selon que ca compile ou pas 
def compiled(tuple_stderr):
    if(tuple_stderr[1] == 0):
            return 1
    else:
        return 0

    



#genere l'executable et compte le nb de test reussi
def genere_executable(nom_fichier):
    liste_tuple = [(0,0),(1,0),(0,1),(1,1),(12,12),(12,-43),(-1,-52)]
    test_passed = 0
    
    for couple in liste_tuple:
        exec = subprocess.run([f"./{nom_fichier} {couple[0]} {couple[1]}" ],capture_output=True , text=True , shell=True)
        result = exec.stdout.split(' ')
        test_passed += test_reussi(only_integer(result[-1]))


    return test_passed

    




#prend une liste (resultat de l'execution du programme) et ne garde que les entiers à la fois positif ou negatif
def only_integer(liste):
    digit = []
    for elem in liste.split('\n'):
        try:
            digit.append(int(elem))
        except ValueError:
            pass
    
    return digit




#il faut gerer le cas ou la sortie est negatif
def test_reussi(digit):
    test = [0,1,1,2,24,-31,-53]
    nb_test = 0

    if(len(digit) > 0):
        for attendu in test:
            if(digit[-1] == attendu):
                return 1
    
    return 0



#split un nom de fichier et extrait les noms,prenoms 
def prenom_nom(nom_fichier):
    split1 = nom_fichier.split(".c")
    prenom_nom = split1[0].split("_")
    
    return prenom_nom




def note_compilation(compile,nb_warning):
    note_compile = 0
   
    if(compile == False):
        note_compile = 0
    else:
        note_compile = 3
    
    note_compile -= 0.5 * nb_warning
    
    if(note_compile < 0):
        return 0
    else:
        return float(note_compile)
    



def nb_test_reussi(result_execution):
    test_passed = 0
    test_passed += test_reussi(only_integer(result_execution[-1]))

    return test_passed



#fonction qui compte le nb de lignes contenant de la documentation dans chaque fichier .c
def compte_doc(nom_fichier):
    nb_doc = 0
    with  open(f"eleves_bis/{nom_fichier}","r") as file:
        for ligne in file:
            nb_doc += ligne.count('/*')
    
    return nb_doc




#qui depend du nombre de commentaire contenu dans le fichier
def note_qualite(nb_lignes_doc):
    note_qualite = 0
    
    if(nb_lignes_doc > 3):
        note_qualite = 2
    else:
        note_qualite += nb_lignes_doc * 2/3

    return note_qualite



def note_test(nb_test_passed):
    return nb_test_passed*5/7



def note_final(test_note,compilation_note,qualite_note):
    finale_note = test_note + compilation_note + qualite_note
    return str(round(finale_note,2))
    



#fonction qui crée une liste de liste contenant pour chaque fichier les informations
#liste_fichier : est la liste de tout les fichiers (obtenu via l'appel à ls)
def info(liste_fichier):
    liste_fichier_csv = []
    liste_info = []

    for nom_fichier in liste_fichier:
        first_last_name = prenom_nom(nom_fichier)

        lst_erreur = compilation(nom_fichier)
        
        nb_warn = lst_erreur[0]

        nb_test_passed = genere_executable(nom_fichier)
    
        nb_lignes_doc = compte_doc(nom_fichier)
        
        compileted = compiled(lst_erreur)
        
        note_compile = note_compilation(compileted,nb_warn)
        
        note_quality = note_qualite(compte_doc(nom_fichier))
        
        test_note = note_test(nb_test_passed)
        
        note_finale = note_final(test_note,note_compile,note_quality)

        liste_info = [first_last_name[0],first_last_name[1],compileted,nb_warn,nb_test_passed,nb_lignes_doc,note_compile,note_finale]
        liste_fichier_csv.append(liste_info)
        
    return liste_fichier_csv
      




        

# la liste contiendra dans l'ordre
# - prenom,nom,compil,nb_warnings,nb_test_reussi,nb_lignes_com,note_compil,note_final
def cree_fichier_csv(liste_fichier_csv):
    with open("resultat.csv", "w",newline= "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prénom','Nom','Compilation','Nombre Warning','Test Reussi','Nombre Documentation','Note Compilation','Note final'])
            for ligne in liste_fichier_csv:
                if isinstance(ligne, list):
                    writer.writerow(ligne)

    csvfile.close()
        
        
    

if __name__ == "__main__":
             
    liste = stockefichier()
    liste_fichier = info(liste)
    cree_fichier_csv(liste_fichier)
    print("terminé")
