# APICalculadora
API para realização de cálculos matemáticos, com base em uma requisição POST com a propriedade expressão recebendo o calculo a se fazer.

Exemplo de uso:

POST JSON: http://seuendereco:8080/calcule
Header: application/json
Body:
{
  "expressao": "(5-2)+4*10/(45+2)"
}


Retorno:
{
    "expressao": {
        "expressao": "(5-2)+4*10/(45+2)"
    },
    "resultado": 3.851063829787234
}
  
