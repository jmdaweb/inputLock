# Input Lock #

* Auteur : Jose Manuel Delicado
* Compatibilité NVDA: 2017.3 à 2019.1
* Télécharger [version stable][1]

## Introduction

Avez-vous des enfants ou des animaux domestiques à la maison? Avez-vous un
chat et il aime beaucoup grimper votre table et marcher sur votre clavier?
Déplacez-vous accidentellement la souris sur des parties aléatoires de
l'écran lorsque vous utilisez votre ordinateur portable? Ensuite, Input Lock
est pour vous! Vous pourrez laisser votre ordinateur seul et allumé sans
risque.

Une fois installé, vous pourrez verrouiller votre clavier, votre écran
tactile, si votre ordinateur portable en a un, un écran souris et un
afficheur braille.

## Utilisation

Ce module complémentaire ajoute deux gestes supplémentaires à NVDA. Par
défaut, ils ne sont pas attribués, vous devrez donc les configurer à partir
de la boîte de dialogue Gestes de commandes. Lisez le Guide de l'utilisateur
de NVDA pour plus d'informations.

Lorsque vous appuyez sur le geste Basculer le verrouillage d'entrée, NVDA
dira "Entrée verrouillée". Vos périphériques d'entrée seront bloqués jusqu'à
ce que vous appuyiez à nouveau sur le même geste. À ce moment, NVDA dira
"Entrée  déverrouillée" et tout fonctionnera comme d'habitude.

Si vous appuyez sur le geste Basculer le verrouillage de la souris, votre
souris sera verrouillée. Appuyez à nouveau sur cette commande pour la
déverrouiller. Lorsque la souris est verrouillée, vous pouvez utiliser les
gestes de NVDA pour la déplacer et cliquer avec les boutons gauche et droit,
mais vous ne pouvez pas déplacer la souris elle-même. Les clics de souris
peuvent également être désactivés à partir de la catégorie Input lock dans
la boîte de dialogue Paramètres de NVDA (NVDA 2018.2 et versions
ultérieures) ou dans la boîte de dialogue Paramètres du module
complémentaire pour les versions antérieures, disponibles dans le menu
Préférences. De plus, à partir de ces paramètres, vous pouvez contrôler si
la souris se verrouille au démarrage ou non de NVDA.

Remarque : lorsque les clics de souris sont bloqués, vous ne pouvez utiliser
aucun geste de NVDA pour travailler avec la souris.

## Limitations

Input Lock présente les limitations suivantes :

* Le raccourci clavier contrôle+alt+effacement peut être utilisé même
  lorsque le clavier est verrouillé.

## Journal des Changements

### Version 1.7

* Les indicateurs de compatibilité ont été mis à jour avec les versions
  récentes de NVDA.
* Traductions mises à jour.

### Version 1.6

* Désormais, les paramètres ne sont supprimés que lorsque le module
  complémentaire est désinstallé. La configuration n'est plus réinitialisée
  lors de la mise à niveau.
* Nouvelles traductions et mises à jour.

### Version 1.5

* Ajout de la compatibilité avec les dernières versions de NVDA.
* Nouvelles traductions.

### Version 1.4

* Les gestes pour le module complémentaire sont non affectés par défaut.

### Version 1.3

* Ajout d'un panneau de configuration dans la boîte de dialogue
  Paramètres. Pour les anciennes versions de NVDA, un élément de menu et une
  boîte de dialogue ont également été ajoutés.
* Ajout d'un paramètre pour verrouiller la souris au démarrage de NVDA.
* Ajout d'un paramètre pour bloquer également les clics de souris lorsque la
  souris est verrouillée.
* Correction de petits bogues, optimisations de code et réduction du nombre
  de chaînes dupliquées pour les traducteurs

### Version 1.2

* Maintenant, la souris peut également être verrouillée
* Nouvelle commande pour verrouiller et déverrouiller uniquement la souris

### Version 1.1

* Si un autre module complémentaire a déjà ajouté une fonction de capture à
  inputManager, il est restauré lorsque l'entrée est déverrouillée.

### Version 1.0

* Première version

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
