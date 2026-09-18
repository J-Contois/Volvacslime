# Documentation technique - Sandbox physique du Slime

**Projet :** Volvacslime, GTech 4, Bloc 1, Semaine 1 (Unreal Gameplay Architecture & Physics)
**Moteur :** Unreal Engine 5.8.2
**Auteur :** Contois Jonathan

---

## 1. Contexte et objectif du prototype

J'ai conçu une sandbox physique dans laquelle le joueur incarne un slime capable d'interagir avec des objets de l'environnement en les aspirant, en les posant ou en les projetant. Mon objectif cette semaine n'était pas de construire le jeu complet, mais de poser une architecture Gameplay Framework propre et un système d'interaction générique, que je pourrai réutiliser dans les semaines suivantes du projet pour le craft, les compétences et les biomes.

---

## 2. Ce que je n'ai pas eu le temps d'implémenter

J'ai passé une bonne partie de la semaine sur la détection et l'aspiration, ce qui ne m'a pas laissé le temps d'implémenter :

- le Souffle (Push) ;
- le fait de lâcher un objet dans le monde ;
- le fait de jeter ou lancer un objet dans le monde.

Le système d'aspiration fonctionne entièrement, tout comme la détection de cible.

---

## 3. Vue d'ensemble de l'architecture

```
BP_VolvacslimeCharacter
   └─ BPC_TargetDetectionComponent   (détecte la meilleure cible à proximité)
   └─ BPC_AspirationComponent        (gère l'aspiration)

BPI_Interactable  (interface commune)
   └─ BP_PhysicsObject_Base          (+ variantes : SmallRock, HeavyCrate, Fragile)

S_InteractableData (structure de données échangée entre systèmes)
```

### Comment mes systèmes communiquent entre eux

| Relation | Moyen utilisé | Pourquoi ce choix |
|---|---|---|
| Character vers ses propres Components | Appel direct de fonctions publiques | Le Character assemble simplement mes Components, il ne connaît pas leur logique interne |
| Component vers Component (Detection vers Aspiration) | `FindComponentByClass` au `BeginPlay`, puis un Event Dispatcher | Je découvre la dépendance au runtime plutôt que de la câbler en dur, et le lien reste à sens unique |
| Component vers un objet du monde | Blueprint Interface (`BPI_Interactable`) | Mon Component ne connaît jamais le type concret d'un objet. Je peux ajouter un nouvel objet sans jamais toucher au Component |

---

## 4. Mes classes et Components principaux

| Classe | Type | Rôle |
|---|---|---|
| `BP_VolvacslimeGameMode` | GameMode | Définit le Pawn et le PlayerController par défaut |
| `BP_VolvacslimePlayerController` | PlayerController | Ajoute le Mapping Context Enhanced Input au démarrage |
| `BP_VolvacslimeCharacter` | Character | Gère le mouvement et la caméra (SpringArm et Camera), assemble mes Components d'interaction, relaie les inputs |
| `BPC_TargetDetectionComponent` | Actor Component | Détecte et évalue la meilleure cible interactable à proximité, via une sphère de détection créée au runtime |
| `BPC_AspirationComponent` | Actor Component | Gère l'aspiration |
| `BPI_Interactable` | Blueprint Interface | Contrat commun entre mes Components et tout objet interactif du monde |
| `S_InteractableData` | Structure | Données transmises pour un objet interactif : nom, masse, volume, tag |
| `BP_PhysicsObject_Base` | Actor | Objet physique interactif de base, implémente `BPI_Interactable` |

**Composants du Character :** `CapsuleComponent` (racine), `SpringArmComponent`, `CameraComponent`, et un `SceneComponent` nommé `TransferPoint`. C'est un point d'ancrage positionnable qui représente la bouche du slime, taggé `"TransferPoint"`.

---

## 5. Fonctionnement de mon système d'interaction

### 5.1 Détection (`BPC_TargetDetectionComponent`)

Je crée une `SphereComponent` au runtime, avec `Add Component by Class`, dans le `BeginPlay` du Component lui-même plutôt que de la poser en dur sur le Character. Ça permet au Component de rester déplaçable sur n'importe quel Actor, sans dépendance.

Cette sphère est en `Query Only` et ne répond qu'au channel de collision `Aspirable` (détaillé au §6.2). Les overlaps alimentent un tableau `CandidateActors`, filtré par `Does Implement Interface (BPI_Interactable)`. Une fonction `EvaluateBestTarget`, appelée par un Timer toutes les 0.1 secondes plutôt que dans un `Tick`, calcule un score pour chaque candidat en combinant son alignement angulaire et sa proximité, puis retient le meilleur via `SetTarget`. Cette fonction déclenche `SetHighlighted` sur l'objet et diffuse un Event Dispatcher `OnTargetChanged`.

Ce Component ne connaît rien de l'aspiration : il répond uniquement à la question « quel est le meilleur candidat visible actuellement ? ».

### 5.2 Aspiration - Pull (`BPC_AspirationComponent`)

Je m'abonne à `OnTargetChanged` pour connaître la cible courante, sans effectuer ma propre recherche. Quand j'active l'input, `TryAcquirePullTarget` valide la cible via `CanBeAspirated` en comparant sa masse à ma force d'aspiration, puis désactive temporairement la réponse de collision de l'objet au channel `Pawn` (détaillé au §6.3) et réinitialise sa vélocité physique.

Le `Tick` du Component, actif uniquement pendant l'aspiration, applique une `AddForce` progressive vers `TransferPoint`, jusqu'à ce que l'objet atteigne un seuil de distance.

---

## 6. Systèmes physiques développés

### 6.1 Résumé des propriétés physiques utilisées

| Propriété | Où je la démontre |
|---|---|
| Forces continues | Aspiration, avec une `AddForce` progressive vers `TransferPoint` |
| Impulsions instantanées | Non démontrées cette semaine (fonctionnalités non terminées) |
| Masse | Filtre de gameplay via `CanBeAspirated` |
| Gravité | Chute naturelle des objets, empilements |
| Collisions | Blocage entre objets empilés, désactivation temporaire ciblée pendant l'aspiration |

### 6.2 Le channel de collision `Aspirable`

J'ai créé un Object Channel personnalisé nommé `Aspirable` plutôt que d'utiliser un preset générique du moteur comme `OverlapAllDynamic`. Il agit au niveau du solveur physique, avant toute exécution de Blueprint : seuls les objets déclarés `Aspirable` génèrent un overlap avec ma sphère de détection. Ça évite que des objets physiques non pertinents, comme des fragments Chaos ou d'autres Pawns, viennent polluer mon tableau de candidats.

Je n'ai sauvegardé aucun Profile dans les Project Settings. Chaque Component configure sa réponse directement en `Custom`, ce qui limite les couches de configuration à surveiller pour le petit nombre d'objets que j'ai cette semaine.

### 6.3 Gérer la collision pendant l'aspiration

Un objet en cours de traction physique continuerait de heurter ma capsule comme un solide normal si sa réponse au channel `Pawn` restait sur `Block`. Je la passe donc temporairement à `Ignore` pendant la traction active, puis je la restaure à `Block` dès que la cible change ou que l'aspiration s'arrête, en remettant aussi sa vélocité à zéro pour éviter une résolution de pénétration brutale par le solveur au moment de la restauration.

### 6.4 Mon choix pour `AddForce`

J'utilise volontairement une variante indépendante de la masse (`bAccelChange` à `true`) sur l'aspiration, pour garder un geste prévisible quel que soit l'objet manipulé. La masse reste une donnée de gameplay, utilisée comme seuil d'aspiration, plutôt qu'un facteur physique à ce stade. C'est un choix assumé de lisibilité plutôt que de réalisme brut.

---

## 7. Mes principaux choix techniques

- **Séparer Detection et Aspiration.** J'ai créé deux Components distincts plutôt qu'un seul, chacun avec une responsabilité unique. Le coût, un dispatcher et un binding au `BeginPlay`, me semble faible face au gain réel de modularité, puisque Detection pourrait être réutilisé un jour sur un Actor qui n'a pas besoin d'aspirer.
- **Créer la sphère de détection au runtime.** Plutôt que de la poser en dur sur le Character, j'évite qu'elle devienne un élément orphelin si je retire le Component de détection. En contrepartie, je ne peux pas régler son rayon visuellement dans le viewport de l'éditeur.
- **Utiliser un Timer plutôt qu'un Tick pour le scoring de cible.** La précision d'une frame n'apporte rien à la sélection d'une cible, donc réduire la fréquence de calcul est un gain de performance sans perte perceptible.
- **Utiliser `GetComponentLocation` plutôt que `GetActorLocation`** pour tout objet à physique simulée. Le `RootComponent` d'un Actor ne suit pas forcément le déplacement physique si le mesh simulé n'est pas lui-même la racine. Lire la position du Component physique directement m'évite ce piège.

---

## 8. Note sur l'assistance IA

J'ai utilisé l'IA pour résoudre certains problèmes de débogage rencontrés pendant le développement de mon prototype, ainsi que pour m'expliquer certaines configurations et propriétés à modifier afin d'obtenir un résultat précis, quand je ne savais pas où les trouver. Je m'en suis aussi beaucoup servi comme documentation, pour retrouver facilement les informations dont j'avais besoin. Enfin, je l'ai utilisée pour m'aider à rédiger ce document : elle m'a fourni une trame que j'ai ensuite remplie avec mon propre contenu.