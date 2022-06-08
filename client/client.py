import requests
import pprint as pp

res = requests.post('http://localhost:8081/users', json={
    "username": "RistaTerorista",
    "ime": "Andreja",
    "prezime": "Ristic",
    "smer": "S",
    "predmeti": [
        {
            "ime": "RISO",
            "espb": 10
        }
    ]
})

pp.pprint(res.json())