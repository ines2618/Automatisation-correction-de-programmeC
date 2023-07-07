# Automatisation-correction-de-programmeC

**English Version**


The purpose of this project was to implement an automated solution to correct multiple C language programs submitted by fictional students and generate a CSV file containing the grades of each student.

The project was divided into two main parts: compilation and program execution.

In the first part, we obtained the list of file names using the "ls" command and stored the result in a list. Then, each program was compiled individually by capturing the compilation errors and warnings. A function was used to process the compilation results and extract the number of errors and warnings.

In the second part, we executed the compiled programs using predefined parameter combinations. The execution results were analyzed to count the number of successful tests.

After completing these two major steps, we counted the lines of documentation in each file by iterating through each line of the source code. The student grades were calculated using the specified formulas, taking into account the compilation results, the number of successful tests, and the number of lines of documentation.

Finally, to generate a clear and organized report, a CSV file was created. This file contained relevant information for each student, including their name, surname, compilation results, number of warnings, number of successful tests, number of lines of documentation, compilation grade, and final grade.

Thanks to this automated solution, teachers were able to efficiently and quickly correct students' programs while obtaining a detailed report with individual grades for each student, facilitating the grading process and performance evaluation.


-------------------------------------------------------------------------------------------------------------------------------------------------

**French version**

Le but de ce projet était de mettre en place une solution automatisée pour corriger plusieurs programmes en langage C soumis par des étudiants fictifs et générer un fichier CSV contenant les notes de chaque étudiant.

Le projet a été divisé en deux parties principales : la compilation et l'exécution des programmes.

Dans la première partie, nous avons obtenu la liste des noms de fichiers en utilisant la commande "ls" et en stockant le résultat dans une liste. Ensuite, nous avons compilé chaque programme individuellement, en récupérant les erreurs et les avertissements de compilation. Pour cela, nous avons utilisé une fonction pour traiter les résultats de la compilation et extraire le nombre d'erreurs et de warnings.

Dans la deuxième partie, nous avons exécuté les programmes compilés en utilisant différentes combinaisons de paramètres prédéfinis. Pour chaque exécution, nous avons vérifié la sortie standard (stdout) pour compter le nombre de tests réussis. Une fonction a été utilisée pour déterminer si un test a été validé ou non.

Une fois les deux grandes étapes réalisées, nous avons compté les lignes de documentation dans chaque fichier en parcourant chaque ligne du code source. En utilisant les formules spécifiées dans le sujet, nous avons calculé les notes en fonction des résultats de la compilation, du nombre de tests réussis et du nombre de lignes de documentation.

Enfin, pour créer le fichier CSV, nous avons créé une liste de listes contenant les informations nécessaires pour chaque fichier, telles que le nom, le prénom, les résultats de compilation, les avertissements, les tests réussis, les lignes de documentation, la note de compilation et la note finale. Cette liste a été passée à une fonction qui a généré le fichier CSV.

Il convient de noter qu'il peut y avoir quelques problèmes d'affichage, comme l'alignement des zéros dans la note de compilation, ainsi que le placement des exécutables dans le dossier principal lors de la compilation. Ces problèmes peuvent être corrigés en apportant des ajustements au code.
