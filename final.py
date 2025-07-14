import bystander

moral_values = {
    "man": {"saves": 0, "sacrificed": 0},
    "woman": {"saves": 0, "sacrificed": 0},
    "child": {"saves": 0, "sacrificed": 0},
    "elderly": {"saves": 0, "sacrificed": 0},
    "parent": {"saves": 0, "sacrificed": 0},
    "refugee": {"saves": 0, "sacrificed": 0},
    "politician": {"saves": 0, "sacrificed": 0},
    "athlete": {"saves": 0, "sacrificed": 0},
    "engineer": {"saves": 0, "sacrificed": 0},
    "criminal": {"saves": 0, "sacrificed": 0},
    "doctor": {"saves": 0, "sacrificed": 0},
    "teacher": {"saves": 0, "sacrificed": 0},
    "disabled": {"saves": 0, "sacrificed": 0},
    "pregnant": {"saves": 0, "sacrificed": 0},
    "homeless": {"saves": 0, "sacrificed": 0},
    "young": {"saves": 0, "sacrificed": 0}
}

leticia = bystander.Bystander(name="Letícia", traits=["woman", "elderly", "athlete", "engineer", "disabled"])
matheus = bystander.Bystander(name="Matheus", traits=["man", "refugee", "athlete", "engineer", "homeless", "young"])
print(leticia.status())
print(matheus.status())