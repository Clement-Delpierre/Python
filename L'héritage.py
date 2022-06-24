from abc import ABC, abstractmethod

class Fichier(ABC):
    def __init__(self, nom: str, taille: int):
        self.nom = nom
        self.taille = taille

    @abstractmethod
    def Afficher(self):
        pass

    def __str__(self) -> str:
        return f"Fichier {self.nom}"
        
class Image(Fichier):
    def Afficher(self):
        print(f"Image nommée {self.nom}")

class GIF(Image):
    def Afficher(self):
        super().Afficher()
        print(f"Cette image est au format GIF")

class PNG(Image):
    def Afficher(self):
        super().Afficher()
        print(f"Cette image est au format PNG")

class Utilisateur:
    def __init__(self, nom: str, motDePasse: str):
        self.nom = nom
        self.motDePasse = motDePasse

    def SInscrire(self):
        print(f"{self.nom} est inscrit(e).")

    def SeConnecter(self):
        print(f"{self.nom} est connecté(e).")

    def CreerFilDiscussion(self, date: str, contenu: str, titre: str ="") -> FilDiscussion:
        post = Post(date, self, contenu)
        return FilDiscussion(date, post, titre)

    def Repondre(self, fil: FilDiscussion, date: str, contenu: str, fichier: Fichier =None):
        if fichier:
            post = PostAvecFichier(date, self, contenu, fichier)
        else:
            post = Post(date, self, contenu)
        fil.AjouterPost(post)
        return post

    def __str__(self):
        return self.nom

class Moderateur(Utilisateur):
    def ModifierPost(self, post: Post, nouveauContenu: str):
        post.contenu = nouveauContenu

    def SupprimerPost(self, fil: FilDiscussion, post: Post):
        fil.posts.remove(post)

class Post:
    def __init__(self, date: str, utilisateur: Utilisateur, contenu: str):
        self.utilisateur = utilisateur
        self.datePublication = date
        self.contenu = contenu

    def Afficher(self):
        print(self.contenu)

    def __str__(self):
        return f"Ce poste a été publié par {self.utilisateur} à la date du {self.datePublication}"

class PostAvecFichier(Post):
    def __init__(self, date: str, utilisateur: Utilisateur, contenu: str, fichier: Fichier):
        self.utilisateur = utilisateur
        self.datePublication = date
        self.contenu = contenu
        self.fichierJoint = fichier
    
    def Afficher(self):
        super().Afficher()
        print("Piece jointe :")
        self.fichierJoint.Afficher()

class FilDiscussion:
    def __init__(self, date: str, post: Post, titre: str =""):
        self.titre = titre
        self.dateCreation = date
        self.posts = [post]

    def Afficher(self):
        print("-----Fil-----")
        print(f"titre : {self.titre}, date : {self.dateCreation}")
        print()
        for post in self.posts:
            post.Afficher()
            print()
        print("------------")            

    def AjouterPost(self, post: Post):
        self.posts.append(post)

    def __str__(self):
        return f"Ce fil de discussion a été créé le {self.dateCreation} et est intitulé {self.titre}, il contient {len(self.posts)} poste(s)."


# test fichier 
# document = Fichier("CV", 3) # l'instanciation doit échouer puisque la méthode est abstraite

# test image
image = Image("Ma belle maison", 3)
image.Afficher()
print(image)

# test post
post1 = Post("aujourd'hui", "Clément", "Demain dès l'aube...")
post1.Afficher()
print(post1)

# test post avec fichier
post2 = PostAvecFichier("03/02/22", "Alex", "Voici ci-joint ma dernière photo !", image)
post2.Afficher()
print(post2)

# test fil de discussion
fil1 = FilDiscussion("demain", post1, "Premier fil")
fil1.Afficher()
print(fil1)

fil1.AjouterPost(post2)
fil1.Afficher()
print(fil1)

# test utilisateur
clement = Utilisateur("Clément", "0000")
clement.SInscrire()
clement.SeConnecter()
monFil = clement.CreerFilDiscussion("06/06/06", "C'est mon fil !", "Mon fil")
monFil.Afficher()
monPost = clement.Repondre(monFil, "là", "N'importe", None)
monPost.Afficher()

# test modérateur
bob = Moderateur("Bob", "1234")
bob.ModifierPost(monPost, "Pas n'importe !")
monPost.Afficher()
bob.SupprimerPost(monFil, monPost)
monPost.Afficher()

# test GIF
gif = GIF("monGIF", 3)
gif.Afficher()

# test PNG
png = PNG("monPNG", 3)
png.Afficher()

print("**implémentation**")
print("**implémentation**")
print("**implémentation**")
print("**implémentation**")
print("**implémentation**")

user = Utilisateur("User", "bref")
modo = Moderateur("Modo", "bref")
date = "maintenant"
leFil = user.CreerFilDiscussion(date, "Test, test", "fil test")
modo.Repondre(leFil, date, "Test reçu !")
#msgHS = user.Repondre(leFil, date, "Message HS")
#repHS = modo.Repondre(leFil, date, "Votre message est HS")
leFil.Afficher()

modo.SupprimerPost(leFil, leFil.posts[-1])
modo.SupprimerPost(leFil, leFil.posts[-1])
#modo.SupprimerPost(leFil, msgHS)
#modo.SupprimerPost(leFil, repHS)
leFil.Afficher()

image = PNG("monImage", 3)
user.Repondre(leFil, date, "Voici...", image)
modo.Repondre(leFil, date, "Au top !")
leFil.Afficher()